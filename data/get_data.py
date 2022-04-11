from bson import SON

from mongo_utils.mongo_connection import get_mongodb_client
import pandas as pd
import streamlit as st
import asyncio



# Connect to MongoDB

client = get_mongodb_client()


def get_data_from_collection(collection, query=None, column_filter=None):
    # pipeline = [
    #
    #     {"$unwind": "$name"},
    #     {"$group": {"_id": "$name", "count": {"$sum": 1}}},
    #     {"$sort": SON([("count", -1), ("_id", -1)])}
    # ]
    # pipeline = [
    #
    #     {"$unwind": "$name"},
    #     {"$group": {"_id": "$name", "count": {"$sum": 1}}},
    #     {"$sort": SON([("count", -1), ("_id", -1)])}
    # ]
    # Make a query to the specific DB and Collection
    if query is None:
        query = {}
    if filter is None:
        column_filter = {}

    # cursor = client[collection].aggregate(pipeline)
    cursor = client[collection].find(query, column_filter)
    # Expand the cursor and construct the DataFrame
    df = pd.DataFrame(list(cursor))
    return df


def get_unique_values_from_columns(collection, column_name):
    values = []
    for testy in client[collection].find().distinct(column_name):
        values.append(testy)
    return values




