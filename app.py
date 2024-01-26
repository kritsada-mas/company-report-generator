import streamlit as st
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

# def create_workflow_step_options(label, key):
#     check = st.checkbox(label=label, key=key)
#     if check:
#         model_provider = st.selectbox("Model Provider", ["Bedrock", "OpenAI"])
#         if model_provider == "Bedrock":
#             model_options = [
#                 "anthropic.claude-v1",
#                 "anthropic.claude-v2",
#                 "anthropic.claude-instant-v1",
#             ]
#             use_multiprompt = st.toggle("Granular-prompt")
#             selected_model = st.selectbox("Model", model_options)
#             if use_multiprompt:
#                 c1, c2 = st.columns(2)
#                 with c1:
#                     p_human = st.text_input("p_human")
#                     p_task_context = st.text_input("p_task_context")
#                     p_tone_context = st.text_input("p_tone_context")
#                     p_data = st.text_input("p_data")
#                     p_task_description = st.text_input("p_task_description")
#                 with c2:
#                     p_example = st.text_input("p_example")
#                     p_conversation_history = st.text_input("p_conversation_history")
#                     p_thought_process = st.text_input("p_thought_process")
#                     p_formatting = st.text_input("p_formatting")
#                     p_assistant = st.text_input("p_assistant")
#                 return {
#                     "model_provider": model_provider,
#                     "model": selected_model,
#                     "use_multiprompt": use_multiprompt,
#                     "prompt": {
#                         "p_human": p_human,
#                         "p_task_context": p_task_context,
#                         "p_tone_context": p_tone_context,
#                         "p_data": p_data,
#                         "p_task_description": p_task_description,
#                         "p_example": p_example,
#                         "p_conversation_history": p_conversation_history,
#                         "p_thought_process": p_thought_process,
#                         "p_formatting": p_formatting,
#                         "p_assistant": p_assistant,
#                     },
#                 }
#             else:
#                 prompt = st.text_input("Prompt")
#                 return {
#                     "model_provider": model_provider,
#                     "model": selected_model,
#                     "use_multiprompt": use_multiprompt,
#                     "prompt": prompt,
#                 }
#     return None, None


def create_workflow():
    saved_config = {}  # Initialize saved configuration dictionary
    with st.expander("Customize Workflow (Optional)"):
        t1, t2, t3 = st.tabs(["Simple", "Advanced", "Fully Customize"])

        with t1:
            simple_in = st.checkbox(label="Introduction", key="simple_in")
            simple_bh = st.checkbox(label="Business Health", key="simple_bh")
            simple_au = st.checkbox(label="Audiences", key="simple_au")
            simple_co = st.checkbox(label="Competitors", key="simple_co")
            saved_config = {
                    "Introduction": simple_in,
                    "Business Health": simple_bh,
                    "Audiences": simple_au,
                    "Competitors": simple_co,
                }

        with t2:
            st.write("This feature is currently in development")
            # in_options = create_workflow_step_options(
            #     "Introduction", "advance_in"
            # )
            # bh_options = create_workflow_step_options(
            #     "Business Health", "advance_bh"
            # )
            # au_options = create_workflow_step_options(
            #     "Audiences", "advance_au"
            # )
            # co_options = create_workflow_step_options(
            #     "Competitors", "advance_co"
            # )
            # saved_config = {
            #     "Introduction": in_options,
            #     "Business Health": bh_options,
            #     "Audiences": au_options,
            #     "Competitors": co_options,
            # }

        with t3:
            st.write("This feature is currently in development")
            # save_t3 = st.button('Save Selection',key='custom_save')

        
    
def display_workflow(workflow):
    tt1, tt2 = st.tabs(["Current Workflow", "Backend workflow"])

    with tt1:
        st.write("Current Workflow Configuration:")
        st.write(workflow)
        
    


if __name__ == "__main__":
    init_page()
    user_input = get_user_input()
    workflow = create_workflow()
    display_workflow(workflow)
