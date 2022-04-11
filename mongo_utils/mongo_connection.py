from settings import MONGO_CREDENTIALS as DGDB
from pymongo import MongoClient
import ssl
import asyncio
import motor.motor_asyncio


def compare_credentials(creds):
    cred = f"mongodb+srv://" \
           f"{creds.get('username')}:" \
           f"{creds.get('password')}@" \
           f"{creds.get('host')}/" \
           f"{creds.get('db')}?" \
           f"retryWrites=true&" \
           f"w=majority"
    return str(cred)


def _connect_mongo(creds):
    credentials = compare_credentials(creds)
    # Connect to MongoDB
    ssl._create_default_https_context = ssl._create_unverified_context
    try:
        # client = motor.motor_asyncio.AsyncIOMotorClient(creds, serverSelectionTimeoutMS=5000)
        # print(client.server_info())
        client = MongoClient(credentials)
        return client[creds.get('db')]
    except Exception:
        print("Unable to connect to the server.")


def get_mongodb_client():
    db = _connect_mongo(DGDB)
    return db


