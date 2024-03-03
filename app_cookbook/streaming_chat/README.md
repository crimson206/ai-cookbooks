# Basic ChatBot with streaming

## Display the response of your bot as streaming

### Content

OpenAI provides the guide for streaming the response. Visit their [page](https://platform.openai.com/docs/api-reference/streaming)

To stream the chatbot response, we must isolate the streaming container. Therefore, we use the st.empty() block to isolate the new outputs.

```python
display_chat_history()

prompt = st.chat_input("Enter your prompt")
if prompt:
    with st.empty():
        st.chat_message("user").write(prompt)
    with st.empty():
        start_stream_chat(prompt)
        bot_response = st.chat_message("assistant").write_stream(st.session_state.stream)
        close_stream_chat(bot_response)
```

display_chat_history() will display the previous chat history.
If a new prompt is submitted, we generate two new containers. Writing tests in them won't make any effects to the main container displaying the history.

According to OpenAI, we seem to implement the for loop for streaming in our app.

```python
from openai import OpenAI

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

To avoid this inconvenience, Streamlit implemented 'write_stream()' function.
Using this function, we can simply implement the streaming in our app like below.

```python
import streamlit as st
from openai import OpenAI

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)

st.write_stream(stream)
```

