import streamlit as st

ENV = st.secrets['env']
API_BASE_URL = st.secrets['api_base_url']
API_KEY = st.secrets['api_key']
GENERATE_WORKFLOW_ENDPOINT = f'{API_BASE_URL}/create-workflow'
GENERATE_COMPANY_REPORT_ENDPOINT = f'{API_BASE_URL}/generate-company-report'
GET_PROGRESS_ENDPOINT = f'{API_BASE_URL}/get-report?transactionID='
LOCAL_HOST = True
IGNORE_AUTHORIZATION_GROUP = True
REMOVE_AUTHENTICATION = False