import streamlit as st
import json


def init_page():
    st.set_page_config(page_title="AI Company Reports")
    hide_streamlit_style = "<style> footer { visibility: hidden; } </style>"
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.subheader("Company Report Generator", divider="rainbow")
    st.write("Harness the power of generative AI to create insightful company reports")

def company_url_text_input():
    return st.text_input(
        label="Company Webpage URL",
        placeholder="",
        value="",
        disabled=False,
        help="This can be any webpage that provides basic information about the company (e.g. https://fluxus.io).",
    )

def customize_workflow_expander():
    expander_state = {}
    with st.expander("Customize Workflow (Optional)"):
        t1, t2, t3 = st.tabs(["Simple", "Advanced", "Fully Customize"])

        with t1:
            expander_state = simple_workflow_tabs()
            
        with t2:
            expander_state = advanced_workflow_tabs()
            
        with t3:
            st.write("This feature is currently in development")
            
        display_workflow_tabs(expander_state)
        
        return expander_state

def simple_workflow_tabs():
    simple_in = st.checkbox(label="Introduction", key="simple_in")
    simple_bh = st.checkbox(label="Business Health", key="simple_bh")
    simple_au = st.checkbox(label="Audiences", key="simple_au")
    simple_co = st.checkbox(label="Competitors", key="simple_co")
    save_t1 = st.button("Save Selection", key="simple_save")
    if save_t1:
        expander_state = {
            "mode": "simple",
            "body": {
                "Introduction": simple_in,
                "Business Health": simple_bh,
                "Audiences": simple_au,
                "Competitors": simple_co,
            }
        }
        return expander_state
    else:
        return None
    
def advanced_workflow_tabs():
    advanced_in = advanced_workflow_step_options("Introduction", "advance_in")
    advanced_bh = advanced_workflow_step_options("Business Health", "advance_bh")
    advanced_au = advanced_workflow_step_options("Audiences", "advance_au")
    advanced_co = advanced_workflow_step_options("Competitors", "advance_co")
    save_t2 = st.button("Save Selection", key="advanced_save")
    if save_t2:
        expander_state = {
            "mode": "advanced",
            "body": {
                "Introduction": advanced_in,
                "Business Health": advanced_bh,
                "Audiences": advanced_au,
                "Competitors": advanced_co,
            }
        }
        return expander_state
    else:
        return None

def advanced_workflow_step_options(label, key):
    check = st.checkbox(label=label, key=key)
    if check:
        model_provider = st.selectbox("Model Provider", ["Bedrock", "OpenAI"])
        if model_provider == "Bedrock":
            model_options = [
                "anthropic.claude-v1",
                "anthropic.claude-v2",
                "anthropic.claude-instant-v1",
            ]
            use_multiprompt = st.toggle("Granular-prompt")
            selected_model = st.selectbox("Model", model_options)
            if use_multiprompt:
                c1, c2 = st.columns(2)
                with c1:
                    p_human = st.text_input("p_human")
                    p_task_context = st.text_input("p_task_context")
                    p_tone_context = st.text_input("p_tone_context")
                    p_data = st.text_input("p_data")
                    p_task_description = st.text_input("p_task_description")
                with c2:
                    p_example = st.text_input("p_example")
                    p_conversation_history = st.text_input("p_conversation_history")
                    p_thought_process = st.text_input("p_thought_process")
                    p_formatting = st.text_input("p_formatting")
                    p_assistant = st.text_input("p_assistant")
                return {
                    "model_provider": model_provider,
                    "model": selected_model,
                    "use_multiprompt": use_multiprompt,
                    "prompt": {
                        "p_human": p_human,
                        "p_task_context": p_task_context,
                        "p_tone_context": p_tone_context,
                        "p_data": p_data,
                        "p_task_description": p_task_description,
                        "p_example": p_example,
                        "p_conversation_history": p_conversation_history,
                        "p_thought_process": p_thought_process,
                        "p_formatting": p_formatting,
                        "p_assistant": p_assistant,
                    },
                }
            else:
                prompt = st.text_input("Prompt")
                return {
                    "model_provider": model_provider,
                    "model": selected_model,
                    "use_multiprompt": use_multiprompt,
                    "prompt": prompt,
                }
    return None, None

def display_workflow_tabs(expander_state):
    t1, t2, = st.tabs(["Current Workflow", "temp"])
    with t1:
        st.write("Current Workflow Configuration:")

        if expander_state["mode"] == "simple":
            st.write("Simple workflow")
            st.json(expander_state)
        elif expander_state["mode"] == "advanced":
            st.write("Advanced workflow")
            st.json(expander_state)
        else:
            st.write("Default workflow")
            
    with t2:
        pass

# def workflow_advanced_options(model_type, model_options, use_multiprompt):
#     selected_model = st.selectbox("Model", model_options)
#     if use_multiprompt:
#         c1, c2 = st.columns(2)
#         with c1:
#             p_human = st.text_input("p_human")
#             p_task_context = st.text_input("p_task_context")
#             p_tone_context = st.text_input("p_tone_context")
#             p_data = st.text_input("p_data")
#             p_task_description = st.text_input("p_task_description")
#         with c2:
#             p_example = st.text_input("p_example")
#             p_conversation_history = st.text_input("p_conversation_history")
#             p_thought_process = st.text_input("p_thought_process")
#             p_formatting = st.text_input("p_formatting")
#             p_assistant = st.text_input("p_assistant")
#     else:
#         prompt = st.text_input("Prompt")
#         return selected_model, prompt







    


if __name__ == "__main__":
    init_page()
    user_input = company_url_text_input()
    workflow = customize_workflow_expander()
