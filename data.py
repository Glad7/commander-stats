from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
import streamlit as st

@st.cache_resource
def get_worksheet():
    creds_dict = json.loads(st.secrets["gspread"]["gcp_service_account"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(
        creds_dict,
        ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    )
    gc = gspread.authorize(creds)
    sh = gc.open("Commander_Games")
    print(sh)
    return sh.worksheet("Games")