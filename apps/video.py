import datetime

import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
import numpy as np
from data.get_data import get_unique_values_from_columns, get_data_from_collection
from data.prepare_data import prepare_date_columns, group_data, aggregate_data
from apps.ui_elements.agrid.agrid_video import get_table, set_ggrid_options

st.session_state.events_action = 'playing'
if 'events_action' in st.session_state:
    st.session_state.events_action = get_unique_values_from_columns('video', 'eventAction')


def app():
    st.title('Video')
    st.sidebar.subheader("St-AgGrid example options")




    select_rows = {'date':1,
                   'name':1,
                   'eventAction':1,
                   'hour':1,
                   'totalEvents':1,
                   'uniqueEvents':1,
                   'eventValue':1,
                   '_id': 0,
                   }
    with st.container():
        st.write("This is inside the container")

        with st.form(key='my_form'):
            events_action_selector = st.multiselect(
                'Select event actions',
                st.session_state.events_action,
                help='choose event action',
                default='playing')
            col1, col2, col3 = st.columns(3)
            with col1:
                date_from_input = st.date_input("Select from date",
                                                min_value=datetime.datetime(2022, 1, 1),
                                                value=datetime.datetime(2022, 1, 1))
                date_from_input = datetime.datetime.combine(date_from_input, datetime.time.min)


            with col2:
                date_to_input = st.date_input("Select to date",
                                              max_value=datetime.datetime(2022,3,1),
                                              value=datetime.datetime(2022,3,1))
                date_to_input = datetime.datetime.combine(date_to_input, datetime.time.min)


            with col3:
                time_frame = st.selectbox(
                    "Select weekly or monthly downloads", ("weekly", "monthly", "daily"))

            st.form_submit_button()


    st.markdown("### Sample Data")
    query = {'eventAction': {"$in": events_action_selector},
             "date": {
                 "$gte": date_from_input,
                 "$lt": date_to_input
                }
             }
    agg = {
        'date': 'first',
        # 'name': 'first',
        'totalEvents': 'sum',
        'uniqueEvents': 'sum',
        'eventValue': 'sum'}
    df = get_data_from_collection('video', query, select_rows)
    if time_frame == 'weekly':
        df = df.groupby(['eventAction', df['date'].dt.isocalendar().week, 'name']).agg(agg)

    elif time_frame == 'daily':
        df = df.groupby(['eventAction', df['date'].dt.day, 'name']).sum(agg)

    else:
        df = df.groupby(['eventAction', df['date'].dt.month, 'name']).sum(agg)
    df = df.reset_index()
    # df = prepare_date_columns(df)
    gb = set_ggrid_options(df)

    gridOptions = gb.build()

    with st.form('example form') as f:
        st.spinner("Displaying results...")
        st.header('Example Form')
        grid_response = get_table(df, gridOptions)
        # Infer basic colDefs from dataframe types
        st.form_submit_button()
    # st.markdown(grid_response['data'].to_html(), unsafe_allow_html=True)
    # st.write(gridOptions)
    st.write(grid_response['data'])