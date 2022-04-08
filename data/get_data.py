from mongo_utils.mongo_connection import get_mongodb_client
import pandas as pd
import streamlit as st


# Connect to MongoDB
client = get_mongodb_client()


def get_data_from_collection(collection, query=None, column_filter=None):
    # Make a query to the specific DB and Collection
    if query is None:
        query = {}
    if filter is None:
        column_filter = {}

    cursor = client[collection].find(query, column_filter)
    # Expand the cursor and construct the DataFrame
    df = pd.DataFrame(list(cursor))
    return df


def get_unique_values_from_columns(collection, column_name):
    values = []
    for testy in client[collection].find().distinct(column_name):
        values.append(testy)
    return values

