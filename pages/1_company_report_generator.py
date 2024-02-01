import streamlit as st
import time
import numpy as np
import components.authenticate as authenticate



# Page configuration
st.set_page_config(page_title="Company Report Generator", page_icon="📈")
hide_streamlit_style = "<style> footer { visibility: hidden; } </style>"
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# st.subheader("Company Report Generator", divider="rainbow")
st.subheader("Company Report Generator")

# Check authentication
authenticate.set_st_state_vars()

# Add login/logout buttons
if st.session_state["authenticated"]:
    authenticate.button_logout()
else:
    authenticate.button_login()

if (st.session_state["authenticated"] and "demo" in st.session_state["user_cognito_groups"]):
    st.write("Harness the power of generative AI to create insightful company reports")
    st.text_input(
        label="Company Webpage URL",
        placeholder="",
        value="",
        disabled=False,
        help="This can be any webpage that provides basic information about the company (e.g. https://fluxus.io).",
    )
    
    with st.sidebar:
        with st.expander("Customize Workflow (Optional)"):
            t1, t2, t3 = st.tabs(["Simple", "Advanced", "Fully Customize"])
            with t1:
                simple_in = st.checkbox(label="Introduction", key="simple_in", value=True)
                simple_bh = st.checkbox(label="Business Health", key="simple_bh", value=True)
                simple_au = st.checkbox(label="Audiences", key="simple_au", value=True)
                simple_co = st.checkbox(label="Competitors", key="simple_co", value=True)
                saved_config = {
                        "Introduction": simple_in,
                        "Business Health": simple_bh,
                        "Audiences": simple_au,
                        "Competitors": simple_co,
                    }
            with t2:
                st.write("Advanced workflow is currently in development")
            with t3:
                st.write("Fully customize workflow is currently in development")
        with st.expander("History"):
            st.write("History is currently in development")

else:
    if st.session_state["authenticated"]:
        st.write("You do not have access. Please contact the administrator.")
    else:
        st.write("Please login!")