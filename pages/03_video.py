import datetime
import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
import numpy as np
from data.get_data import get_unique_values_from_columns, get_data_from_collection
from data.prepare_data import prepare_date_columns, group_data, aggregate_data
from apps.ui_elements.visualisations.charts import get_chart
from data.prepare_data import top_events
from apps.ui_elements.agrid.agrid_video import get_table, set_ggrid_options
from settings import AGRID_OPTIONSS

st.markdown("# Video")
st.sidebar.markdown("# Video")

if 'agrid_selected_theme' not in st.session_state:
    st.session_state.agrid_selected_theme = "dark"

if 'agrid_options' not in st.session_state:
    st.session_state.agrid_options = AGRID_OPTIONSS

agrid_available_themes = ["streamlit", "light", "dark", "blue", "fresh", "material"]
agrid_selected_theme = st.selectbox("Theme", agrid_available_themes, index=2)
st.session_state.agrid_selected_theme = agrid_selected_theme
if "agrid_selected_theme" not in st.session_state:
    st.session_state.agrid_selected_theme = agrid_selected_theme

if 'agrid_options' not in st.session_state:
    st.session_state.agrid_options = AGRID_OPTIONSS


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
if "events_action" not in st.session_state:
    st.session_state.events_action = get_unique_values_from_columns(
        "video", "eventAction"
    )

with st.container():
    st.write("This is inside the container")

    with st.form(key="my_form"):
        events_action_selector = st.multiselect(
            "Select event actions",
            st.session_state.events_action,
            help="choose event action",
            default="playing",
        )
        col1, col2, col3 = st.columns(3)
        with col1:
            date_from_input = st.date_input(
                "Select from date",
                min_value=datetime.datetime(2021, 1, 1),
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
                "Select weekly or monthly downloads", ("weekly", "monthly", "daily")
            )

            st.form_submit_button("Submit")

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
if time_frame == "weekly":
    grid_df = df.groupby(["eventAction", "week", "name"]).agg(agg)

elif time_frame == "daily":
    grid_df = df.groupby(["eventAction", "day", "name"]).agg(agg)

else:
    grid_df = df.groupby(["eventAction", "month", "name"]).agg(agg)

df = df.reset_index()
# df = prepare_date_columns(df)
gb = set_ggrid_options(df)

gridOptions = gb.build()

with st.container():
    with st.container() as f:
        st.spinner("Displaying results...")
        st.header("Example Form")
        grid_response = get_table(df, gridOptions)

        # Infer basic colDefs from dataframe types
    for e in events_action_selector:
        data = (
            top_events(
                df[df["eventAction"] == e], e, date_from_input, date_to_input
            )
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
            df_to_wiz = total.iloc[:11, :]
            st.session_state.names = df_to_wiz["name"].unique()[:11]
            if st.checkbox(f"Choose {e} name to visualize", False):
                st.session_state.names = st.multiselect(
                    "Choose name to visualize",
                    total["name"].unique(),
                    df_to_wiz["name"].unique()[:11],
                )

            st.subheader(f"Top {e} events")

            st.write(df_to_wiz)
            dff = df.copy()
            agg = {
                   'uniqueEvents': 'sum',
                   'totalEvents': 'sum',
                   'eventValue': 'sum'}
            dff['date'] = pd.to_datetime(dff['date'].astype(str) + ' ' + dff['hour'].astype(str),
                                         format='%Y-%M-%d %H')
            gdf = dff[(dff["eventAction"] == e)].groupby(['date', 'eventAction', 'name']).agg(agg).reset_index()


            source = gdf[
                (gdf["eventAction"] == e) & (gdf['name'].isin(st.session_state.names))
            ].sort_values(["eventValue"], ascending=False)


            # source = source.groupby(['date', 'hour', 'eventAction']).agg(agg)
            chart = get_chart(source, e, "date", "uniqueEvents")
            st.altair_chart(chart, use_container_width=True)