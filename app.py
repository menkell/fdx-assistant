from flask import Flask, render_template, request, session
from markupsafe import Markup
import openai
import os
import time
import json
import markdown
import zipfile
from pathlib import Path
from flask_session import Session
import logging
import hashlib
import shelve



CACHE_PATH = os.getenv("CACHE_PATH", "/var/cache/fdx/chat_cache.db")
#for suffix in ("", ".bak", ".dat", ".dir", ".db"):
#    try:
#       os.remove(CACHE_PATH + suffix)
#    except FileNotFoundError:
#        continue


# Setup logging
logging.basicConfig(level=logging.INFO)  # Limit global logging
app_logger = logging.getLogger("fdx-assistant")
app_logger.setLevel(logging.DEBUG)
logging.getLogger("openai").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

openai.api_key = os.getenv("OPENAI_API_KEY")
CONFIG_FILE = "assistant_config.json"
DOCS_FOLDER = "docs"
TOPICS = ["Brief history of Open Banking with timelines","Open Banking in North America", "What is CFPB 1033","What is the CFPB 1033 compliance timeline", "What is Financial Data Exchange (FDX)"]
TOPICS2 = ["What is screen scraping", "What are the challenges with screenscraping","What are the comparision between data sharing with Open Banking and Screen scraping", "Benefits of Financial Insitutions Adopting Open Banking", "Benefits of Third Party Providers adopting Open Banking", "Challenge Financial Insitutions face in adopting Open Banking", "Callenges Third Party Providers face in adopting Open Banking"]

def save_ids(assistant_id, vector_store_id, thread_id):
    with open(CONFIG_FILE, "w") as f:
        json.dump({
            "assistant_id": "asst_VvuAcybLhO6qjca7wzzwC1AN",
            "vector_store_id": vector_store_id,
            "thread_id": thread_id
        }, f)

def load_ids():
    with open(CONFIG_FILE, "r") as f:
        data = json.load(f)
    return data["assistant_id"], data["vector_store_id"], data["thread_id"]

def extract_from_zip(zip_path):
    extracted_files = []
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            if file_name.lower().endswith(('.pdf', '.txt', '.md')):
                zip_ref.extract(file_name, DOCS_FOLDER)
                extracted_path = os.path.join(DOCS_FOLDER, file_name)
                extracted_files.append(extracted_path)
    return extracted_files

def get_all_files_to_upload():
    files_to_upload = []
    for filename in os.listdir(DOCS_FOLDER):
        full_path = os.path.join(DOCS_FOLDER, filename)
        if filename.lower().endswith(".pdf"):
            files_to_upload.append(full_path)
    for filename in os.listdir(DOCS_FOLDER):
        if filename.lower().endswith(".zip"):
            zip_path = os.path.join(DOCS_FOLDER, filename)
            extracted_files = extract_from_zip(zip_path)
            files_to_upload.extend(extracted_files)
    return files_to_upload

def create_or_load_assistant():
    if os.path.exists(CONFIG_FILE):
        app_logger.debug("🔁 Loading existing Assistant and thread...")
        return load_ids()

    app_logger.debug("🆕 Creating new Assistant with file search...")
    files_to_upload = get_all_files_to_upload()
    if not files_to_upload:
        raise Exception("No supported documents found in /docs.")

    vector_store = openai.vector_stores.create(name="FDX Knowledge Base")
    file_paths = [Path(path) for path in files_to_upload]
    openai.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store.id,
        files=file_paths
    )

    assistant = openai.beta.assistants.create(
        name="FDX Tutorial Assistant",
        instructions="You are an expert on the Financial Data Exchange (FDX) API. "
            "Always prefer using the uploaded documents to answer questions. "
            "If you cannot find the answer in the documents, and you are confident, "
            "you may use your general knowledge of the topic to provide helpful guidance. "
            "Use bullet points. "
            "Keep answers short"
            "Always indicate clearly when the answer is based on general knowledge rather than the provided documents.",
        model="gpt-4-1106-preview",
        tools=[{"type": "file_search"}],
        tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}}
    )

    thread = openai.beta.threads.create()
    save_ids(assistant.id, vector_store.id, thread.id)
    return assistant.id, vector_store.id, thread.id

assistant_id, vector_store_id, thread_id = create_or_load_assistant()
assistant = openai.beta.assistants.retrieve(assistant_id)

# Cache utilities
def get_cache_key(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def get_cached_response(prompt):
    key = get_cache_key(prompt)
    with shelve.open(CACHE_PATH) as cache:
        return cache.get(key)

def store_response(prompt, html_blocks):
    key = get_cache_key(prompt)
    with shelve.open(CACHE_PATH) as cache:
        cache[key] = html_blocks

@app.route("/", methods=["GET", "POST"])
def chat():
    if "completed_topics" not in session:
        session["completed_topics"] = []

    messages = []

    if request.method == "POST":
        user_input = request.form["user_input"]
        app_logger.debug(f"🟡 Received user input: {user_input}")

         # ✅ Check if cached response exists
        cached = get_cached_response(user_input)
        if cached:
            app_logger.debug("✅ Cache hit. Returning cached response.")
            messages.extend(cached)
            for topic in TOPICS + TOPICS2:
                if topic.lower() in user_input.lower() and topic not in session["completed_topics"]:
                    session["completed_topics"].append(topic)
        else:
            # Wait for previous run to complete
            while True:
                runs = openai.beta.threads.runs.list(thread_id=thread_id).data
                if not runs:
                    app_logger.debug("🟢 No previous runs found, safe to continue.")
                    break

                run_status = runs[0].status
                run_created = runs[0].created_at
                app_logger.debug(f"⏳ Waiting for run to complete... status: {run_status}")

                if run_status == "completed":
                    break

                if time.time() - run_created > 300:
                    app_logger.debug("⚠️ Run is older than 5 minutes. Skipping wait.")
                    break

                time.sleep(0.5)

            app_logger.debug("✉️ Sending message to assistant...")
            openai.beta.threads.messages.create(
                thread_id=thread_id,
                role="user",
                content=user_input
            )

            app_logger.debug("⚙️ Running assistant...")
            run = openai.beta.threads.runs.create(
                thread_id=thread_id,
                assistant_id=assistant.id
            )

            while True:
                run_status = openai.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
                app_logger.debug(f"⏳ Run status: {run_status.status}")

                if run_status.status == "failed":
                    error_info = getattr(run_status, "last_error", None)
                    if error_info:
                        app_logger.error(f"❌ Assistant run failed. Error: {error_info}")
                    else:
                        app_logger.error("❌ Assistant run failed. No error message available.")
                    break

                if run_status.status == "completed":
                    break

                time.sleep(0.5)

            response_msgs = openai.beta.threads.messages.list(thread_id=thread_id)

            new_html_blocks = []

            for msg in reversed(response_msgs.data[:2]):
                role = msg.role
                parts = msg.content

                for part in parts:
                    app_logger.debug(f"📬 Message part type: {part.type}")
                    if part.type == "text":
                        content = part.text.value
                        app_logger.debug(f"📥 Assistant reply: {content}")
                        annotations = part.text.annotations if hasattr(part.text, "annotations") else []
                        sources = []
                        for ann in annotations:
                            if ann.type == "file_citation":
                                file_id = ann.file_citation.file_id
                                file = openai.files.retrieve(file_id)
                                sources.append(file.filename)
                        if sources:
                            content += "\n\n📄 **Source(s)**: " + ", ".join(sources)
                        html_content = Markup(markdown.markdown(content))
                        new_html_blocks.append((role, html_content))
                        
            messages.extend(new_html_blocks)

            # ✅ Store the response in cache
            store_response(user_input, new_html_blocks)

            for topic in TOPICS + TOPICS2:
                if topic.lower() in user_input.lower() and topic not in session["completed_topics"]:
                    session["completed_topics"].append(topic)

    return render_template("chat.html", messages=messages, completed_topics=session["completed_topics"], topics=TOPICS, topics2=TOPICS2)

if __name__ == "__main__":
    app.run(debug=True, port=5050, use_reloader=False)
