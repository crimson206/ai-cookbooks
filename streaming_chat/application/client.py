from openai import OpenAI

class CustomClient(OpenAI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def stream_chat(self, *args, **kwargs):
        kwargs['stream'] = True
        return self.chat.completions.create(*args, **kwargs)
