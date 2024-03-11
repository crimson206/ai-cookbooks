import streamlit as st
#from shared import st

def regenerate():
    st.session_state.messages = st.session_state.messages[:-1]
    msg = st.session_state.client.response()
    st.session_state.messages.append({"role": "assistant", "content": msg})

def continue_st():
    st.session_state.messages.append({"role": "user", "content": "[user pressed a continue button.]"})
    msg = st.session_state.client.response()
    st.session_state.messages = st.session_state.messages[:-1]
    st.session_state.messages.append({"role": "assistant", "content": msg})

def delete():
    if len(st.session_state.messages) == 1:
        return
    st.session_state.messages = st.session_state.messages[:-1]

def chat():
    """
    It adds user prompt and bot response to session_state.messages.
    It uses session_state.prompt as user prompt. Therefore, the value must be set.
    Example:
        st.chat_input("Say something", key="prompt", on_submit=chat)
    """
    prompt = st.session_state.prompt
    st.session_state.messages.append({"role": "user", "content": prompt})
    msg = st.session_state.client.response()
    st.session_state.messages.append({"role": "assistant", "content": msg})
