import streamlit as st
import components.authenticate as authenticate
from components.constants import REMOVE_AUTHENTICATION

def switch_page(page_name: str):
    from streamlit import _RerunData, _RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")
    
    page_name = standardize_name(page_name)

    pages = get_pages("app.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise _RerunException(
                _RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")```

st.set_page_config(
    page_title="Home",
    page_icon="images/logo.jpg",
)

st.write("# Welcome to Fluxus AI/ML! 👋")

if REMOVE_AUTHENTICATION:
    st.write("Hello there! Explore Fluxus AI/ML.")
else:
    # Check authentication when the user lands on the home page.
    authenticate.set_st_state_vars()

    # Add login/logout buttons
    if st.session_state["authenticated"]:
        st.write("Welcome back! Ready to dive into Fluxus AI/ML?")
        authenticate.button_logout()
    else:
        st.write("Unlock the full experience by logging in.")
        authenticate.button_login()

# Additional content on the home page
st.write("Explore the latest advancements in AI/ML and unlock the potential of Fluxus technologies.")

if st.button("Company Report Generator"):
    switch_page("Company Report Generator")