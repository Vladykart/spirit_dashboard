import datetime

import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
import numpy as np
from data.get_data import get_unique_values_from_columns, get_data_from_collection
from data.prepare_data import prepare_date_columns, group_data, aggregate_data
from apps.ui_elements.agrid.agrid_video import get_table, set_ggrid_options


def app():
    st.title('Clients')
    st.sidebar.subheader("St-AgGrid example options")

    query = {}
    df = get_data_from_collection('clients', query)
    df = df.reset_index()
    # df = prepare_date_columns(df)
    gb = set_ggrid_options(df)

    gridOptions = gb.build()
    grid_response = get_table(df, gridOptions)