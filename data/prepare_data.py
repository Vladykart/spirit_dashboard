from datetime import datetime
import pandas as pd


def group_data(df, by=None):
    if by:
        return df.groupby(by=by).sum()
    else:
        return df


def aggregate_data(df, method=None):
    df = df.agg(method)
    return df


def top_events(data, event):
    agg = {"totalEvents": "sum", "uniqueEvents": "sum", "eventValue": "sum"}
    # if type(start_date) == str:
    #     start_date = datetime.strptime(start_date, "%Y-%m-%d")
    # if type(end_date) == str:
    #     end_date = datetime.strptime(end_date, "%Y-%m-%d")
    df = data.copy()
    df["date"] = pd.to_datetime(df["date"])
    df = (
        df[df["eventAction"] == event]
        .groupby(by=["name", "date"])
        .agg(agg)
        .reset_index()
    )
    df = df.sort_values(by=["eventValue"], ascending=False).reset_index(drop=True)
    return df


def prepare_video_events_df_list(video_df) -> list:
    """
    return list of dataframes spited by unique eventAction
    """
    set_of_events_action_dfs = []
    for event_action in video_df["eventAction"].unique():
        set_of_events_action_dfs.append(
            video_df[video_df["eventAction"] == event_action]
        )
    return set_of_events_action_dfs


def prepare_video_events_df_dict(video_df) -> dict:
    """
    return dict of dataframes spited by unique eventAction
    """
    dict_of_events_action_dfs = {}
    for event_action in video_df["eventAction"].unique():
        dict_of_events_action_dfs[event_action] = video_df[
            video_df["eventAction"] == event_action
        ]
    return dict_of_events_action_dfs


def prepare_video_events_counted_dfs(video_df):
    dict_of_counted_events_dfs = {}
    for event_action in video_df["eventAction"].unique():
        dict_of_counted_events_dfs[event_action] = (
            video_df[video_df["eventAction"] == event_action]
            .groupby(by=["name"])["name"]
            .count()
        )
    return dict_of_counted_events_dfs


def prepare_seek_time_df(video_df_seeking, video_df_seeked):
    seek_time = pd.merge(
        video_df_seeking,
        video_df_seeked,
        on=["eventLabel", "name", "date", "hour", "minute", "customUserID"],
        how="inner",
        suffixes=("_seeking", "_seeked"),
    )
    seek_time["seek_time"] = abs(
        seek_time["eventValue_seeked"] - seek_time["eventValue_seeking"]
    )
    return seek_time[seek_time["seek_time"] > 0][
        ["date", "hour", "minute", "customUserID", "name", "seek_time"]
    ]


def prepare_date_columns(df):
    df["day"] = df["date"].dt.isocalendar().day
    df["week"] = df["date"].dt.isocalendar().week
    df["month"] = df["date"].dt.month
    df["year"] = df["date"].dt.year
    return df
