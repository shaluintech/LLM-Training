import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Page Configuration
st.set_page_config(page_title="Groq Chat", page_icon="💬")

# Default system prompt
system_prompt = os.getenv(
    "SYSTEM_PROMPT",
    "You are a helpful assistant."
)

# Create Groq Client
def get_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return None
    return Groq(api_key=api_key)

client = get_client()

# Sidebar
st.sidebar.title("Settings")

model = st.sidebar.selectbox(
    "Model",
    [
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
    ],
)

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Check API Key
if client is None:
    st.error(
        "No GROQ_API_KEY found.\n\n"
        "Create a .env file with:\n"
        "GROQ_API_KEY=your_api_key"
    )
    st.stop()

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat Input
user_text = st.chat_input("Type your message and press Enter")

if user_text:

    # Display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_text,
        }
    )

    with st.chat_message("user"):
        st.write(user_text)

    # Assistant Response
    with st.chat_message("assistant"):

        messages_to_send = [
            {
                "role": "system",
                "content": system_prompt,
            }
        ]

        messages_to_send.extend(st.session_state.messages)

        stream = client.chat.completions.create(
            model=model,
            messages=messages_to_send,
            temperature=0.4,
            stream=True,
        )

        def token_generator():
            for chunk in stream:
                if chunk.choices:
                    delta = chunk.choices[0].delta
                    if delta.content:
                        yield delta.content

        reply = st.write_stream(token_generator())

    # Save assistant reply
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply,
        }
    )