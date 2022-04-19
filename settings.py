from dotenv import load_dotenv
import pathlib
import os
import streamlit as st

ROOT_DIR = pathlib.Path.cwd().parent
LOCAL_DATA_PATH = ROOT_DIR.joinpath("data")

load_dotenv()


AGRID_OPTIONSS = {
    "fit_columns_on_grid_load": True,
    "allow_unsafe_jscode": True,
    "enable_enterprise_modules": True,
    "height": 500,
    "rows": 40
}
st.session_state.agrid_options = AGRID_OPTIONSS

MONGO_CREDENTIALS = {
    "username": os.environ.get("MONGO_USERNAME"),
    "password": os.environ.get("MONGO_PASSWORD"),
    "host": "spirit-test.qhagm.mongodb.net",
    "db": "spirit-test"
}

BC_CREDENTIALS = {
    "access_token": os.environ.get("ACCESS_TOKEN"),
    "client_name": os.environ.get("CLIENT_NAME"),
    "api_path": os.environ.get("API_PATH"),
    "client_id": os.environ.get("CLIENT_ID"),
    "client_secret": os.environ.get("CLIENT_SECRET"),
    "store_hash": os.environ.get("STORE_HASH")
}

GAPI = {
    'key': os.environ.get("GAPI_KEY"),
    'unique_id': os.environ.get("UNIQUE_ID"),
    'key_file_location': ROOT_DIR.joinpath('GApi', 'spirit-api-339912-56d447179352.json')
}