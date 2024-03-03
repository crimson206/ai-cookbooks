# setting.py
from client import CustomClient
import streamlit as st

def set_client():
    base_url = st.text_input("Base URL", value='null', help="1. OpenAI API : insert 'OpenAI'. \n2. No Endpoint : insert 'null'. \n3. OpenAI Proxy : insert your custom endpoint.")
    api_key = st.text_input("API Key(if proxy, any value.)", value="API Key", type="password")
    model_name = st.text_input("Model Name", value='gpt-4')

    if base_url == "OpenAI":
        base_url = "https://api.openai.com/v1/"

    st.session_state["client"] = CustomClient(
        api_key=api_key,
        base_url=base_url,
    )

    st.session_state["model_name"] = model_name

def set_initial_chat():
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]