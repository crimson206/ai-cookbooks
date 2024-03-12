import streamlit as st
#from shared import st
from openai import OpenAI

class CustomClient(OpenAI):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

    def generate(self, mock_response=None, *arg, **kwarg):
        if mock_response:
            return mock_response
        if self.base_url.path == "null/":
            if "response_count" not in st.session_state.keys():
                st.session_state["response_count"] = 1
            else:
                st.session_state["response_count"] += 1

            return f"Endpoint is not given. A constant message. Count:{st.session_state.response_count}."

        return self.chat.completions.create(*arg, **kwarg).choices[0].message.content

    def response(self):
        response = self.generate(
            model=st.session_state.model_name,
            messages=st.session_state.messages
        )
        return response