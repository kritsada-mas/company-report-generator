import streamlit as st
import components.authenticate as authenticate
from components.constants import REMOVE_AUTHENTICATION

st.set_page_config(
    page_title="Home",
    page_icon="images/logo.jpg",
)

st.write("# Welcome to Fluxus AI/ML!")

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

if st.session_state["authenticated"]:
    # Additional content on the home page
    st.write("Explore the latest advancements in AI/ML and unlock the potential of Fluxus technologies.")

    blank_row = st.columns(3)
    row1 = st.columns(3)
    

    for col in blank_row:
        col.container(height=60,border=False)
        
    tile1 = row1[0].container(height=90)
    tile1.page_link("pages/1_company_report_generator.py", label="Company Report\n\nGenerator", use_container_width=True)
    
    tile2 = row1[1].container(height=90)
    tile2.page_link("pages/2_server_log_generator.py", label="Server Log\n\nGenerator", use_container_width=True)
    
    tile3 = row1[2].container(height=90)
    tile3.page_link("pages/3_temp.py", label="Document PII\n\nDetector", use_container_width=True)

