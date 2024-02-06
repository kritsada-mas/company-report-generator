import streamlit as st
import components.authenticate as authenticate
from components.constants import REMOVE_AUTHENTICATION

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

