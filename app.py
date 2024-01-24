# import streamlit as st
# from api_handler import create_new_report, get_existing_report

# st.set_page_config(page_title='AI Company Reports')

# hide_streamlit_style = "<style> footer { visibility: hidden; } </style>"
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# st.subheader('Company Report Generator', divider='rainbow')
# st.write('Harness the power of generative AI to create insightful company reports')

# # Form to create a new report
# create_report_form = st.form(key='create_report')
# input_url = create_report_form.text_input(label='Company Webpage URL', placeholder='', value='', disabled=False,
#                                           help='This can be any webpage that provides basic information about the company (e.g. https://fluxus.io).')
# create_report_submitted = create_report_form.form_submit_button(label='Create a New Report', disabled=False)

# # Expander for customizing workflow (optional)
# with st.expander("Customize Workflow (Optional)"):
#     workflow_form = st.form(key='workflow')
#     get_workflow = workflow_form.form_submit_button(label='Hit me')
#     create_workflow = workflow_form.form_submit_button(label='Hit me')

# if create_report_submitted:
#     with st.spinner('creating report...'):
#         create_new_report(create_report_form, input_url)

# # Form to query an existing report
# get_report_form = st.form(key='get_report')
# report_id = get_report_form.text_input(label='Report ID', placeholder='', value='', disabled=False,
#                                        help="All reports have a unique identifier assigned to them. This was provided to you in the response when creating a new report.")
# get_report_submitted = get_report_form.form_submit_button(label='Get an Existing Report', disabled=False)

# if get_report_submitted:
#     with st.spinner('retrieving report...'):
#         get_existing_report(get_report_form, report_id)


import streamlit as st

def create_workflow_step(index, default_values=None):
    st.subheader(f"Step {index}")
    name = st.text_input("Step Name", default_values.get("name", ""))
    step_type = st.selectbox("Step Type", ["scrape", "llm", "parallel"], index=index)
    # Add other input fields based on step_type and your requirements
    
    parameters = {}
    if st.checkbox("Add Parameters", key=f"add_parameters_{index}"):
        # Add input fields for parameters based on step_type and your requirements
        pass
    
    output = st.text_input("Output", default_values.get("output", ""))
    
    return {
        "index": str(index),
        "name": name,
        "type": step_type,
        "parameters": parameters,
        "output": output
    }

def create_workflow():
    workflow = {"body": {"workflow_name": "user_defined", "workflow": []}}
    st.title("Create Your Workflow")

    num_steps = st.number_input("Number of Steps", min_value=1, value=1)

    for i in range(1, num_steps + 1):
        workflow_step = create_workflow_step(i)
        workflow["body"]["workflow"].append(workflow_step)

    st.json(workflow)

if __name__ == "__main__":
    create_workflow()

