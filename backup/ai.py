import openai
import os
import time

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
# Or hardcode it like: openai.api_key = "your-api-key-here"

# --- Create the assistant (only do this once and save the ID if you want to reuse later)
assistant = openai.beta.assistants.create(
    name="FDX Tutorial Assistant",
    instructions=(
        "You are an expert in the Financial Data Exchange (FDX) API and specifications. "
        "Help students understand the concepts of FDX, including data structures, authentication, endpoints, and best practices. "
        "Explain clearly and provide examples."
    ),
    model="gpt-4-1106-preview",
)
print(f"✅ Assistant created: {assistant.id}")

# --- Create a conversation thread
thread = openai.beta.threads.create()

# --- Chat loop
print("\n👋 Welcome to the FDX Assistant! Type 'exit' to end the session.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("👋 Goodbye!")
        break

    # Send user message
    openai.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_input
    )

    # Run the assistant
    run = openai.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id
    )

    # Poll for completion
    while True:
        run_status = openai.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run_status.status == "completed":
            break
        time.sleep(0.5)

    # Fetch and print the assistant's reply
    messages = openai.beta.threads.messages.list(thread_id=thread.id)
    last_msg = messages.data[0]
    print("\n🤖 Assistant:", last_msg.content[0].text.value, "\n")

