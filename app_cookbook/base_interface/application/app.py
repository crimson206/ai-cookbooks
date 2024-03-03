# app.py
#from shared import st
import streamlit as st
from setting import set_client, set_initial_chat
from functions import continue_st, regenerate, delete, chat

def display_chat():
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

def write_app():
    st.title('Basic ChatBot UI')
    st.header('The first chatbot experience.')
    st.write("""This app is an implementation example of basic chatbot interfaces, regenerate, continue, and delete.
             \nEndpoint is not necessary to test the functionalities. With the default setting, test the buttons with prompts. 
             """)

with st.sidebar:
    write_app()
    set_client()
    set_initial_chat()

display_chat()

col1, col2, col3, col4 = st.columns(spec=[0.20, 0.20, 0.20, 0.4])
with col1:
    st.button("Regenerate", on_click=regenerate, use_container_width=True)
with col2:
    st.button("Continue", on_click=continue_st, use_container_width=True)
with col3:
    st.button("Delete", on_click=delete, use_container_width=True)

st.chat_input("Enter your prompt", key="prompt", on_submit=chat)
