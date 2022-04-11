import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
import numpy as np
from data.get_data import get_unique_values_from_columns, get_data_from_collection
from data.prepare_data import prepare_date_columns
from apps.ui_elements.agrid.agrid_video import get_table, set_ggrid_options

if 'events_action' not in st.session_state:
    st.session_state.events_action = get_unique_values_from_columns('video', 'eventAction')


def app():
    st.title('Video')
    st.sidebar.subheader("St-AgGrid example options")
    events_action_selector = st.multiselect(
        'Select event actions',
        st.session_state.events_action,
        help='choose event action',
        default='playing')



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

    st.markdown("### Sample Data")

    df = get_data_from_collection('video', {'eventAction': {"$in": events_action_selector}}, select_rows)
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
    st.write(gridOptions)
    st.write(grid_response['data'])