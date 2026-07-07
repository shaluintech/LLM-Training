import os
import streamlit as st
from dotenv import load_dotenv
from groq import groq
load_dotenv()
st.set_page_config(page_title="Groq Chat",page_icon="💬")
def get_client():
    if not os.getenv("GROQ_API_KEY"):
        return none
    return groq.Client(api_key=os.getenv("GROQ_API_KEY"))
client = get_client()
st.sidebar.title("Settings")
model = st.sidebar.selectbox("model",["llama3-8b-8192","llama3-70b-8192"])
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []

if client is None:
    st.error(
        "No GROQ_API_KEY found. Create a .env file with GROQ_API_KEY=your_key_here, "
        "then restart the app."
    )
    st.stop()  # st.stop() halts the script here - nothing below runs.


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    # Draw each stored message inside a chat bubble matching its role.
    with st.chat_message(message["role"]):
        st.write(message["content"])
user_text = st.chat_input("Type your message and press Enter")

if user_text:
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.write(user_text)

    with st.chat_message("assistant"):
    
        messages_to_send = [{"role": "system", "content": system_prompt}]
        messages_to_send.extend(st.session_state.messages)
        stream = client.chat.completions.create(
            model=model,
            messages=messages_to_send,
            temperature=0.4,
            stream=True,
        )
        reply = streamlit.choices[o].message.content.


        def token_generator():
            for chunk in stream:
                piece = chunk.choices[0].delta.content
                if piece:
                    yield piece

    st.session_state.messages.append({"role": "assistant", "content": reply})