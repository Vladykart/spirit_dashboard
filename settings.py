from dotenv import load_dotenv
import pathlib
import os

ROOT_DIR = pathlib.Path.cwd().parent
LOCAL_DATA_PATH = ROOT_DIR.joinpath("data")

load_dotenv()

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

print(BC_CREDENTIALS)




