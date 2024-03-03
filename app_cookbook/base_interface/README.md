# Basic ChatBot UI
## The first chatbot experience

### Content

I simply implemented the basic interfaces.

- Submit prompt
- Regenerate
- Continue
- Delete

### Limit

I implemented components in seperate python files, and I expected that I can write independent tests for those functions. However, st.sessions_state is an obstacle when we write the tests. It would be better to use a custom dictionary instead of st.sessions_state.