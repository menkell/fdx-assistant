from flask import Flask, render_template, request
from markupsafe import Markup
import openai
import os
import time
import json
import markdown
import zipfile
from pathlib import Path

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
CONFIG_FILE = "assistant_config.json"
DOCS_FOLDER = "docs"

#laura change the assistant_id
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

    # Add PDFs from /docs
    for filename in os.listdir(DOCS_FOLDER):
        full_path = os.path.join(DOCS_FOLDER, filename)
        if filename.lower().endswith(".pdf"):
            files_to_upload.append(full_path)

    # Extract and include files from .zip
    for filename in os.listdir(DOCS_FOLDER):
        if filename.lower().endswith(".zip"):
            zip_path = os.path.join(DOCS_FOLDER, filename)
            extracted_files = extract_from_zip(zip_path)
            files_to_upload.extend(extracted_files)

    return files_to_upload

def create_or_load_assistant():
    if os.path.exists(CONFIG_FILE):
        print("🔁 Loading existing Assistant and thread...")
        return load_ids()

    print("🆕 Creating new Assistant with file search...")

    files_to_upload = get_all_files_to_upload()
    if not files_to_upload:
        raise Exception("No supported documents found in /docs.")

    # ✅ Create vector store
    vector_store = openai.vector_stores.create(name="FDX Knowledge Base")

    # ✅ Upload files using Path objects
    file_paths = [Path(path) for path in files_to_upload]
    openai.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store.id,
        files=file_paths
    )

    # ✅ Create Assistant
    assistant = openai.beta.assistants.create(
        name="FDX Tutorial Assistant",
        instructions="You are an expert on the Financial Data Exchange (FDX) API. "
    "Always prefer using the uploaded documents to answer questions. "
    "If you cannot find the answer in the documents, and you are confident, "
    "you may use your general knowledge of the topic to provide helpful guidance. "
    "Always indicate clearly when the answer is based on general knowledge rather than the provided documents."
,
        model="gpt-4-1106-preview",
        tools=[{"type": "file_search"}],
        tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}}
    )

    # ✅ Create thread and save everything
    thread = openai.beta.threads.create()
    save_ids(assistant.id, vector_store.id, thread.id)
    return assistant.id, vector_store.id, thread.id

# Setup
assistant_id, vector_store_id, thread_id = create_or_load_assistant()
assistant = openai.beta.assistants.retrieve(assistant_id)

@app.route("/", methods=["GET", "POST"])
def chat():
    messages = []

    if request.method == "POST":
        user_input = request.form["user_input"]

        # Add message to thread
        openai.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=user_input
        )

        # Run assistant
        run = openai.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant.id
        )

        # Wait for completion
        while True:
            run_status = openai.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
            if run_status.status == "completed":
                break
            time.sleep(0.5)

        # Get latest assistant messages
        response_msgs = openai.beta.threads.messages.list(thread_id=thread_id)

        for msg in reversed(response_msgs.data[:2]):
            role = msg.role
            parts = msg.content

            for part in parts:
                if part.type == "text":
                    content = part.text.value
                    annotations = part.text.annotations if hasattr(part.text, "annotations") else []

                    # Look for citation-style annotations
                    sources = []
                    for ann in annotations:
                        if ann.type == "file_citation":
                            file_id = ann.file_citation.file_id
                            file = openai.files.retrieve(file_id)
                            sources.append(file.filename)

                    # Render citations at bottom
                    if sources:
                        source_note = "\n\n📄 **Source(s)**: " + ", ".join(sources)
                        content += source_note

                    html_content = Markup(markdown.markdown(content))
                    messages.append((role, html_content))

    return render_template("chat.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)


