import streamlit as st
import components.authenticate as authenticate
import components.workflow as workflow
from components.constants import IGNORE_AUTHORIZATION_GROUP, REMOVE_AUTHENTICATION
from components.api_handler import upload_workflow, create_new_report, get_existing_report


# Page configuration
st.set_page_config(page_title="Company Report Generator", page_icon="📈")
hide_streamlit_style = "<style> footer { visibility: hidden; } </style>"
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# st.subheader("Company Report Generator", divider="rainbow")
st.subheader("Company Report Generator")

if REMOVE_AUTHENTICATION:
    authorized = True
else:
    # Check authentication when user lands on the home page.
    authenticate.set_st_state_vars()
    authorized = st.session_state["authenticated"]

    # Add login/logout buttons
    if authorized:
        st.write("Hi")
        authenticate.button_logout()
    else:
        st.write("Please login?")
        authenticate.button_login()

if (
    (authorized)
    # and 
    # (("demo" in st.session_state["user_cognito_groups"]) or IGNORE_AUTHORIZATION_GROUP)
    ):
    st.write("Harness the power of generative AI to create insightful company reports")
    
    
    with st.sidebar:
        workflow_name = "default"
        
        with st.expander("Customize Report (Optional)"):
            t1, t2 = st.tabs(["Report Generation", "Report Template"])
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
                
                if st.button("Confirm Selection"):
                    workflow_body, workflow_name = workflow.map_workflow(saved_config)
                    with st.spinner('Uploading workflow...'): upload_workflow(workflow_body)
            with t2:
                st.write("Report Template is currently in development")
        with st.expander("History"):
            st.write("History is currently in development")
    
    
    create_report_form = st.form(key = 'create_report')
    workflow_name = workflow_name
    st.write(workflow_name)
    input_url = create_report_form.text_input(label = 'Company Webpage URL', placeholder = '', value = '', disabled = False, help = 'This can be any webpage that provides basic information about the company (e.g. https://fluxus.io).')
    create_report_submitted = create_report_form.form_submit_button(label = 'Create a New Report', disabled = False)
    if create_report_submitted: 
        with st.spinner('creating report...'): create_new_report(workflow_name, create_report_form, input_url)
    

else:
    if authorized:
        st.write("You do not have access. Please contact the administrator.")
    else:
        st.write("Please login!")