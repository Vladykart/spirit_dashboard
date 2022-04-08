import streamlit as st
import streamlit.components.v1 as components
from st_aggrid import AgGrid
import pandas as pd
import numpy as np
from pivottablejs import pivot_ui

from data.get_data import get_unique_values_from_columns, get_data_from_collection


def app():
    st.title('Video')
    select_rows = {'date':1,
                   'name':1,
                   'eventAction':1,
                   'hour':1,
                   'totalEvents':1,
                   'uniqueEvents':1,
                   'eventValue':1,
                   '_id': 0,
                   }

    date_from_input = st.date_input("Select from date")
    date_to_input = st.date_input("Select to date")
    events_action = get_unique_values_from_columns('video', 'eventAction')
    events_action_selector = st.multiselect(
        'Select event actions',
        events_action,
        help='choose station or stations',
        default='playing')
    events_action_selector = [s for s in events_action_selector]
    st.write("------------------------------")
    st.markdown("### Sample Data")

    df = get_data_from_collection('video', {'eventAction': {"$in": events_action_selector}}, select_rows)
    # st.write(df)
    AgGrid(df, theme='dark')


    st.write('Navigate to `Data Stats` page to visualize the data')