import streamlit as st
from api_handler import create_new_report, get_existing_report
import json


def init_page():
    st.set_page_config(page_title="AI Company Reports")
    hide_streamlit_style = "<style> footer { visibility: hidden; } </style>"
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.subheader("Company Report Generator", divider="rainbow")
    st.write("Harness the power of generative AI to create insightful company reports")

def get_user_input():
    return st.text_input(
        label="Company Webpage URL",
        placeholder="",
        value="",
        disabled=False,
        help="This can be any webpage that provides basic information about the company (e.g. https://fluxus.io).",
    )

def create_workflow():
    saved_config = {}  # Initialize saved configuration dictionary
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
            
    return saved_config
    
    
def map_workflow(workflow):
    with open("default_workflow.json", "r") as f:
        default_workflow = json.load(f)
    
    # Remove branches based on user-selected workflow
    if not workflow["Introduction"]:
        default_workflow["body"]["workflow"] = [step for step in default_workflow["body"]["workflow"] if step["name"] != "llm_generate_introduction"]
    if not workflow["Business Health"]:
        default_workflow["body"]["workflow"] = [step for step in default_workflow["body"]["workflow"] if step["name"] != "llm_generate_business_health"]
    if not workflow["Audiences"]:
        default_workflow["body"]["workflow"] = [step for step in default_workflow["body"]["workflow"] if step["name"] != "llm_generate_audience"]
    if not workflow["Competitors"]:
        default_workflow["body"]["workflow"] = [step for step in default_workflow["body"]["workflow"] if step["name"] != "llm_generate_competitors"]
    
    return default_workflow

def display_workflow(workflow):
    t1,t2 = st.tabs(["User Selection", "Backend Workflow"])
    with t1:
        st.write("Current Workflow Configuration:")
        st.write(workflow)
        
    with t2:
        backend_workflow = map_workflow(workflow)
        st.write("Backend Workflow:")
        st.write(backend_workflow)

if __name__ == "__main__":
    init_page()
    user_input = get_user_input()
    workflow = create_workflow()
    
    c1,c2 = st.columns(2)
    with c1:
        create_report = st.button(label = 'Create a New Report', disabled = False)
        # if create_report_submitted: 
            # with st.spinner('creating report...'): create_new_report(create_report_form, input_url)
    with c2:
        display_workflow(workflow)
