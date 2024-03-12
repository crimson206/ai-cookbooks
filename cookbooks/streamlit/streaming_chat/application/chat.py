import streamlit as st

def start_stream_chat(prompt):
    """
    generate 'stream' key of session_state
    """
    st.session_state.messages.append({"role":"user", "content":prompt})
    stream = st.session_state.client.stream_chat(
        model=st.session_state.model_name,
        messages=st.session_state.messages
    )
    st.session_state.stream = stream
    #return stream

def close_stream_chat(bot_response):
    st.session_state.messages.append({"role":"assistant", "content":bot_response})