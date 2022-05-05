import pandas as pd
from datetime import datetime


def prepare_date_columns(df):
    df['date'] = pd.to_datetime(
        df['date'], format='%Y%m%d')

    return df


def group_data(df, by=None):
    if by:
        return df.groupby(by=by).sum()
    else:
        return df


def aggregate_data(df, method=None):
    df = df.agg(method)
    return df


def top_events(data, event, start_date, end_date, top_n = 10):
    agg = {"totalEvents": "sum", "uniqueEvents": "sum", "eventValue": "sum"}
    if type(start_date) == str:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    if type(end_date) == str:
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    df = data.copy()
    df["date"] = pd.to_datetime(df["date"])
    df = df[df["eventAction"] == event].groupby(["name", "date"]).agg(agg).reset_index()
    df = df.sort_values(by=["eventValue"], ascending=False).reset_index(drop=True)
    return df.iloc[:top_n, :]


