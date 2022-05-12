import datetime

import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
import numpy as np
from data.get_data import get_unique_values_from_columns, get_data_from_collection
from data.prepare_data import prepare_date_columns, group_data, aggregate_data
from apps.ui_elements.agrid.agrid_video import get_table, set_ggrid_options


def app():
    st.title('Orders')
    st.sidebar.subheader("St-AgGrid example options")

    select_rows = {'order_id': 1,
                   'name': 1,
                   'sku': 1,
                   'quantity': 1,
                   'date_created': 1,
                   '_id': 0
                   }
    query = {}
    df = get_data_from_collection('orders', query, select_rows)
    df['date_created'] = pd.to_datetime(df.date_created)
    df['day'] = df.date_created.dt.day
    df['month'] = df.date_created.dt.month
    df['year'] = df.date_created.dt.year
    df['weekday'] = df.date_created.dt.weekday
    df['hour'] = df.date_created.dt.hour
    df['minute'] = df.date_created.dt.minute

    namespace = df['name'].unique()
    with st.container():
        st.write("This is inside the container")

        with st.form(key='orders_form'):
            events_action_selector = st.multiselect(
                'Select event actions',
                namespace,
                help='choose event action',
                default=namespace)
    #         col1, col2, col3 = st.columns(3)
    #         with col1:
    #             date_from_input = st.date_input("Select from date",
    #                                             min_value=datetime.datetime(2022, 1, 1),
    #                                             value=datetime.datetime(2022, 1, 1))
    #             date_from_input = datetime.datetime.combine(date_from_input, datetime.time.min)
    #
    #         with col2:
    #             date_to_input = st.date_input("Select to date",
    #                                           max_value=datetime.datetime(2022,3,1),
    #                                           value=datetime.datetime(2022,3,1))
    #             date_to_input = datetime.datetime.combine(date_to_input, datetime.time.min)
    #
    #         with col3:
    #             time_frame = st.selectbox(
    #                 "Select weekly or monthly downloads", ("weekly", "monthly", "daily"))
    #
    #             st.form_submit_button()
    df_g = df.groupby(['year', 'month', 'sku'])[['quantity']].sum({'quantity': 'sum'}).reset_index()
    df = df.reset_index()
    # df = prepare_date_columns(df)
    gb = set_ggrid_options(df_g)

    gridOptions = gb.build()
    grid_response = get_table(df, gridOptions)
    st.write(grid_response['data'])


