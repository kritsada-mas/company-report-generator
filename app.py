import streamlit as st
import components.authenticate as authenticate
from components.constants import REMOVE_AUTHENTICATION

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.write("# Welcome to Fluxus AI/ML! 👋")

if REMOVE_AUTHENTICATION:
    st.write("Hi")
else:
    # Check authentication when user lands on the home page.
    authenticate.set_st_state_vars()

    # Add login/logout buttons
    if st.session_state["authenticated"]:
        st.write("Hi")
        authenticate.button_logout()
    else:
        st.write("Please login")
        authenticate.button_login()



# import streamlit as st
# import json
# # from api_handler import create_new_report, get_existing_report

# def init_page():
#     st.set_page_config(page_title="AI Company Reports")
#     hide_streamlit_style = "<style> footer { visibility: hidden; } </style>"
#     st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#     st.subheader("Company Report Generator", divider="rainbow")
#     st.write("Harness the power of generative AI to create insightful company reports")

# def get_user_input():
#     return st.text_input(
#         label="Company Webpage URL",
#         placeholder="",
#         value="",
#         disabled=False,
#         help="This can be any webpage that provides basic information about the company (e.g. https://fluxus.io).",
#     )

# def create_workflow():
#     saved_config = {}  # Initialize saved configuration dictionary
#     with st.expander("Customize Workflow (Optional)"):
#         t1, t2, t3 = st.tabs(["Simple", "Advanced", "Fully Customize"])

#         with t1:
#             simple_in = st.checkbox(label="Introduction", key="simple_in", value=True)
#             simple_bh = st.checkbox(label="Business Health", key="simple_bh", value=True)
#             simple_au = st.checkbox(label="Audiences", key="simple_au", value=True)
#             simple_co = st.checkbox(label="Competitors", key="simple_co", value=True)
#             saved_config = {
#                     "Introduction": simple_in,
#                     "Business Health": simple_bh,
#                     "Audiences": simple_au,
#                     "Competitors": simple_co,
#                 }

#         with t2:
#             st.write("Advanced workflow is currently in development")

#         with t3:
#             st.write("Fully customize workflow is currently in development")
            
#     return saved_config
    
    
# def map_workflow(workflow):
#     with open("default_workflow.json", "r") as f:
#         default_workflow = json.load(f)
        
#     parallel_step = default_workflow["body"]["workflow"][3]
    
#     # Check if all workflow options are False, indicating no branch should be included
#     if not any(workflow.values()):
#         default_workflow["body"]["workflow"] = default_workflow["body"]["workflow"][:3]  # Remove the parallel step
#     else:
#         # Remove branches based on user-selected workflow
#         if not workflow["Introduction"]:
#             parallel_step["branches"] = [branch for branch in parallel_step["branches"] if branch["branch_name"] != "introduction"]
#         if not workflow["Business Health"]:
#             parallel_step["branches"] = [branch for branch in parallel_step["branches"] if branch["branch_name"] != "business_health"]
#         if not workflow["Audiences"]:
#             parallel_step["branches"] = [branch for branch in parallel_step["branches"] if branch["branch_name"] != "audience"]
#         if not workflow["Competitors"]:
#             parallel_step["branches"] = [branch for branch in parallel_step["branches"] if branch["branch_name"] != "competitors"]
    
#     return default_workflow


# def display_workflow(workflow):
#     t1,t2 = st.tabs(["User Selection", "Backend Workflow"])
#     with t1:
#         st.write("Current Workflow Configuration:")
#         st.write(workflow)
        
#     with t2:
#         backend_workflow = map_workflow(workflow)
#         st.write("Backend Workflow:")
#         st.write(backend_workflow)

# if __name__ == "__main__":
#     init_page()
#     user_input = get_user_input()
#     workflow = create_workflow()
    
#     c1,c2 = st.columns(2)
#     with c1:
#         create_report = st.button(label = 'Create a New Report', disabled = False)
#         # if create_report_submitted: 
#             # with st.spinner('creating report...'): create_new_report(create_report_form, input_url)
#     with c2:
#         display_workflow(workflow)
