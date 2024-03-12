# Instruction

Just copy and phast of the [streamlit example](https://docs.streamlit.io/library/advanced-features/multipage-apps/custom-navigation)

```python
menu() # function shows menu in the sidebar
# menu() wraps authenticated_menu() and unauthenticated_menu()

menu_with_redirect() # is a wrapper of menu(). It runs menu only if any role is defined in st.session-state

authenticated_menu() # show all the links of sub pages of available roles.
# According to the authorization level, disabled is applied.

unauthenticated_menu() # shows only user.py sub-page.

```