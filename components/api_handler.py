import logging
import streamlit as st
import requests
from components.constants import (
    GENERATE_WORKFLOW_ENDPOINT,
    GENERATE_COMPANY_REPORT_ENDPOINT,
    GET_PROGRESS_ENDPOINT,
    API_KEY,
)


def upload_workflow(workflow_body):
    headers = {"content-type": "application/json"}
    data = workflow_body
    try:
        response = requests.post(GENERATE_WORKFLOW_ENDPOINT, headers=headers, json=data)
        response_json = response.json()
        if response_json["statusCode"] != 200:
            st.error(response_json["body"]["message"])
        else:
            st.success("Workflow map generated and saved successfully!")
    except Exception as e:
        logging.error(str(e))


def create_new_report(workflow_name, form_obj, company_webpage_url):
    # client-side validation
    if len(company_webpage_url) == 0:
        form_obj.error("Please input a company webpage url.")
    elif not company_webpage_url.startswith("https://"):
        form_obj.error(
            "Please specify HTTPS protocol for this url (e.g. https://fluxus.io)."
        )
    else:
        if not workflow_name:
            workflow_name = "default"
            
        # send HTTP POST request to API endpoint
        headers = {"content-type": "application/json"}
        data = {"input_url": company_webpage_url, "workflow_name": workflow_name}

        try:
            response = requests.post(
                GENERATE_COMPANY_REPORT_ENDPOINT, headers=headers, json=data
            )
            response_json = response.json()
            
            form_obj.info(
                "Our AI agent is in the process of generating your report, this could take up to 3 minutes to complete. Please fill the form below using the following report ID to get the result:"
            )
            form_obj.info(f"workflow name = {workflow_name}")
            form_obj.code(response_json["transactionID"])
        except Exception as e:
            logging.error(str(e))
            form_obj.error(
                "An unexpected error occurred, please try again. If this error persists, send an email to 'info@fluxus.io'."
            )


def get_existing_report(form_obj, report_id):
    # client-side validation
    if len(report_id) == 0:
        form_obj.error("Please input a report ID.")
    else:
        # send HTTP GET request to API endpoint
        headers = {"content-type": "application/json"}
        try:
            response = requests.get(
                f"{GET_PROGRESS_ENDPOINT}{report_id}", headers=headers
            )
            response_json = response.json()
            # message = response_json["message"]
            # check for errors
            if response_json["transactionStatus"] == "Inprogress":
                form_obj.info(
                    "Our AI agent is still in the process of generating your report. Please be patient, and retry in one minute."
                )
            elif response_json["transactionStatus"] in "Fail":
                form_obj.error(
                    "The company report failed to generate. Please try re-creating the report using the form above. If this error persists, please contact 'info@fluxus.io'."
                )
            else:
                # display report on screen
                report = response_json["report"]
                form_obj.success("Please find your report in JSON format below:")
                form_obj.divider()
                form_obj.json(report)
                form_obj.divider()
        except Exception as e:
            logging.error(str(e))
            form_obj.error(
                "An unexpected error occurred, please try again. If this error persists, send an email to 'info@fluxus.io'."
            )
