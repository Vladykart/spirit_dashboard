import pandas as pd


def prepare_date_columns(df):
    df['date'] = pd.to_datetime(
        df['date'], format='%Y%m%d')

    return df


def group_data(df, by=None):
    if by:
        return df.groupby(by=by)
    else:
        return df


def aggregate_data(df, method=None):
    df = df.agg(method)
    return df
