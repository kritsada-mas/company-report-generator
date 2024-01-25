import streamlit as st
from api_handler import create_new_report, get_existing_report

st.set_page_config(page_title='AI Company Reports')

hide_streamlit_style = "<style> footer { visibility: hidden; } </style>"
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.subheader('Company Report Generator', divider='rainbow')
st.write('Harness the power of generative AI to create insightful company reports')
st.text_input(label='Company Webpage URL',
              placeholder='',
              value='',
              disabled=False,
              help='This can be any webpage that provides basic information about the company (e.g. https://fluxus.io).')

with st.expander("Customize Workflow (Optional)"):
    t1, t2 , t3 = st.tabs(["Simple", "Advanced", "Fully Customize"])
    with t1:
        c1, c2, c3, c4 = st.columns(4)
        
        with c1:
            st.checkbox(label="Introduction", key="simple_in")
        with c2:
            st.checkbox(label="Business Health", key="simple_bh")
        with c3:
            st.checkbox(label="Audiences", key="simple_au")
        with c4:
            st.checkbox(label="Competitors", key="simple_co")
            
        save_t1 = st.button('Save Selection')

    with t2:
        check_in = st.checkbox(label="Introduction", key="advance_in")
        if check_in:
            model_provider = st.selectbox("Model Provider", ["Bedrock", "OpenAI"])
            if model_provider == "Bedrock":
                model =  st.selectbox("Model", ["anthropic.claude-v1", "anthropic.claude-v2","anthropic.claude-instant-v1"])
                multiprompt = st.toggle("Granular-prompt")
                if not multiprompt:
                    prompt = st.text_input("Prompt")
                else:
                    p_human = st.text_input("p_human")
                    p_task_context = st.text_input("p_task_context")
                    p_tone_context = st.text_input("p_tone_context")
                    p_data = st.text_input("p_data")
                    p_task_description = st.text_input("p_task_description")
                    p_example = st.text_input("p_example")
                    p_conversation_history = st.text_input("p_conversation_history")
                    p_thought_process = st.text_input("p_thought_process")
                    p_formatting = st.text_input("p_formatting")
                    p_assistant = st.text_input("p_assistant")
        check_bh = st.checkbox(label="Business health", key="advance_bh")
        if check_bh:
            model_provider = st.selectbox("Model Provider", ["Bedrock", "OpenAI"])
            if model_provider == "Bedrock":
                model =  st.selectbox("Model", ["anthropic.claude-v1", "anthropic.claude-v2","anthropic.claude-instant-v1"])
                multiprompt = st.toggle("Granular-prompt")
                if not multiprompt:
                    prompt = st.text_input("Prompt")
                else:
                    p_human = st.text_input("p_human")
                    p_task_context = st.text_input("p_task_context")
                    p_tone_context = st.text_input("p_tone_context")
                    p_data = st.text_input("p_data")
                    p_task_description = st.text_input("p_task_description")
                    p_example = st.text_input("p_example")
                    p_conversation_history = st.text_input("p_conversation_history")
                    p_thought_process = st.text_input("p_thought_process")
                    p_formatting = st.text_input("p_formatting")
                    p_assistant = st.text_input("p_assistant")

        



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



