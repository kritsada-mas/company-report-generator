import streamlit as st

def workflow_checkbox(column, label, key):
    return column.checkbox(label=label, key=key)

def workflow_advanced_options(model_type, model_options, use_multiprompt):
    selected_model = st.selectbox("Model", model_options)
    if use_multiprompt:
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
    else:
        prompt = st.text_input("Prompt")
        return selected_model, prompt

def create_workflow_step_options(label, key):
    check = st.checkbox(label=label, key=key)
    if check:
        model_provider = st.selectbox("Model Provider", ["Bedrock", "OpenAI"])
        if model_provider == "Bedrock":
            model_options = ["anthropic.claude-v1", "anthropic.claude-v2", "anthropic.claude-instant-v1"]
            use_multiprompt = st.toggle("Granular-prompt")
            return model_provider, workflow_advanced_options(model_provider, model_options, use_multiprompt)
        else:
            return model_provider, None
    return None, None

def create_workflow():
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
        t1, t2, t3 = st.tabs(["Simple", "Advanced", "Fully Customize"])

        with t1:
            c1, c2, c3, c4 = st.columns(4)
            workflow_checkbox(c1, "Introduction", "simple_in")
            workflow_checkbox(c2, "Business Health", "simple_bh")
            workflow_checkbox(c3, "Audiences", "simple_au")
            workflow_checkbox(c4, "Competitors", "simple_co")
            save_t1 = st.button('Save Selection')

        with t2:
            in_model_provider, in_options = create_workflow_step_options("Introduction", "advance_in")
            bh_model_provider, bh_options = create_workflow_step_options("Business health", "advance_bh")

        # Continue for other tabs if needed

if __name__ == "__main__":
    create_workflow()
