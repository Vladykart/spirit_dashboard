import datetime
import pandas as pd
import streamlit as st
from data.prepare_data import top_events
from apps.ui_elements.agrid.agrid_video import get_table, set_ggrid_options
from apps.ui_elements.visualisations.charts import get_chart
from data.get_data import get_data_from_collection


def app():

    st.title("Video")
    st.sidebar.subheader("St-AgGrid example options")

    select_rows = {
        "date": 1,
        "name": 1,
        "eventAction": 1,
        "hour": 1,
        "totalEvents": 1,
        "uniqueEvents": 1,
        "eventValue": 1,
        "_id": 0,
    }
    with st.container():
        with st.form(key="my_form"):
            events_action_selector = st.multiselect(
                "Select event actions",
                st.session_state.events_action,
                help="choose event action",
                default=["playing", "seeked"],
            )
            col1, col2, col3 = st.columns(3)
            with col1:
                date_from_input = st.date_input(
                    "Select from date",
                    min_value=datetime.datetime(2022, 1, 1),
                    value=datetime.datetime(2022, 1, 1),
                )
                date_from_input = datetime.datetime.combine(
                    date_from_input, datetime.time.min
                )

            with col2:
                date_to_input = st.date_input(
                    "Select to date",
                    max_value=datetime.datetime(2022, 3, 1),
                    value=datetime.datetime(2022, 3, 1),
                )
                date_to_input = datetime.datetime.combine(
                    date_to_input, datetime.time.min
                )

            with col3:
                time_frame = st.selectbox(
                    "Select agg period", ("weekly", "monthly", "daily")
                )

            st.form_submit_button()

    st.markdown("### Sample Data")
    query = {
        "eventAction": {"$in": events_action_selector},
        "date": {"$gte": date_from_input, "$lt": date_to_input},
    }

    agg = {"totalEvents": "sum", "uniqueEvents": "sum", "eventValue": "sum"}

    df = get_data_from_collection("video", query, select_rows)

    df["day"] = df["date"].dt.isocalendar().day
    df["week"] = df["date"].dt.isocalendar().week
    df["month"] = df["date"].dt.month
    grid_df = df.copy()
    # tops_df = top_events(df, events_action_selector, date_from_input, date_to_input)
    if time_frame == "weekly":
        grid_df = grid_df.groupby(["eventAction", "week", "name"]).agg(agg)

    elif time_frame == "daily":
        grid_df = grid_df.groupby(["eventAction", "day", "name"]).sum(agg)

    else:
        grid_df = grid_df.groupby(["eventAction", "month", "name"]).sum(agg)

    grid_df = grid_df.reset_index()
    # df = prepare_date_columns(df)
    gb = set_ggrid_options(grid_df)

    gridOptions = gb.build()

    with st.container():
        with st.container() as f:
            st.spinner("Displaying results...")
            st.header("Example Form")
            grid_response = get_table(df, gridOptions)

            # Infer basic colDefs from dataframe types
        for e in events_action_selector:
            data = (
                top_events(df[df['eventAction'] == e], e, date_from_input, date_to_input)
                .sort_values(["eventValue"], ascending=False)
                .reset_index(drop=True)
            )
            total = (
                data.groupby("name")
                .sum()
                .reset_index()
                .sort_values(["eventValue"], ascending=False)
                .reset_index(drop=True)
            )
            namespace = total["name"].unique()

            with st.expander(e) as f:
                col1, col2 = st.columns([21, 9])

                with col1:
                    st.subheader(f"Top {e} events")
                    df_to_wiz = total.iloc[:11, :]
                    st.write(df_to_wiz)
                with col2:
                    names = st.multiselect(
                        "Choose name to visualize", df_to_wiz["name"].unique(), df_to_wiz["name"].unique()[:11]
                    )
                    source = df[(df['eventAction'] == e) & (df.name.isin(names))].sort_values(
                        ["eventValue"], ascending=False
                    )

                    chart = get_chart(source, e, "date", "eventValue")
                st.altair_chart(chart, use_container_width=True)
