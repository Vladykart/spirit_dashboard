import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np


def app():
    st.title('Home')

    # select_rows = {'date': 1,
    #                'name': 1,
    #                'eventAction': 1,
    #                'hour': 1,
    #                'totalEvents': 1,
    #                'uniqueEvents': 1,
    #                'eventValue': 1,
    #                '_id': 0,
    #                }
    #
    # events_action = get_unique_values_from_columns('video', 'eventAction')
    # events_action_selector = st.multiselect(
    #     'Select event actions',
    #     events_action,
    #     help='choose station or stations',
    #     default='playing')
    # events_action_selector = [s for s in events_action_selector]
    # st.write("------------------------------")
    # st.markdown("### Sample Data")
    #
    # df = get_data_from_collection('video', {'eventAction': {"$in": events_action_selector}}, select_rows)
    #
    # t = pivot_ui(df)

    # with open(t.src) as t:
    #     components.html(t.read(), width=900, height=1000, scrolling=True)

    st.write('Navigate to `Data Stats` page to visualize the data')