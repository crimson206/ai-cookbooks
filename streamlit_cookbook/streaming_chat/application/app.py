import streamlit as st
from setting import set_client, set_initial_chat
from chat import start_stream_chat, close_stream_chat
from openai import OpenAI

# https://5c76-172-83-13-4.ngrok-free.app'

with st.sidebar:
    st.title('Basic ChatBot with streaming.')
    st.header('Display the response of your bot as streaming.')
    st.write("""
        For implementation and for information, visit [my GitHub repository](https://github.com/crimson206/streamlit_blog/tree/main/app_cookbook/streaming_chat)\n
        If you need a cheap endpoint, visit my [OpenAI Proxy Shortcut](https://github.com/crimson206/openai_proxy_shortcut) repository

    """)
    set_client()
    set_initial_chat()

def display_chat_history():
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
 
display_chat_history()

prompt = st.chat_input("Enter your prompt")
if prompt:
    with st.empty():
        st.chat_message("user").write(prompt)
    with st.empty():
        start_stream_chat(prompt)
        bot_response = st.chat_message("assistant").write_stream(st.session_state.stream)
        close_stream_chat(bot_response)