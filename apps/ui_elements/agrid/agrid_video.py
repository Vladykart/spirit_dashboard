import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, DataReturnMode, GridUpdateMode
from settings import AGRID_OPTIONSS
import pandas as pd
import numpy as np
from data.get_data import get_unique_values_from_columns, get_data_from_collection
from data.prepare_data import prepare_date_columns


def set_ggrid_options(df):
    # grid_options = {
    #     "columnDefs": [
    # {'field': 'name', "rowGroup": True, 'hide': True}], 'groupDisplayType': 'groupRows',}


    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(editable=True, groupable=True, value=True, enableRowGroup=True, aggFunc='sum')
    gb.configure_side_bar()
    gb.configure_grid_options(enableRangeSelection=True, domLayout='normal', )
    # gb.configure_column("group")
    # gb.configure_column("totalEvents", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], precision=2,
    #                     aggFunc='sum')
    # gb.configure_column("uniqueEvents", type=["numericColumn", "numberColumnnumberColumnFilter", "customNumericFormat"], precision=1,
    #                     aggFunc='count')
    gb.configure_column("date", type=["dateColumn"],
                        rowGroup=False, hide=False, precision=0)
    #
    gb.configure_column("name", type=["TextColumn"],
                        rowGroup=False, hide=False, precision=4)

    # gb.configure_columns(grid_options)

    return gb


def get_table(df, gridOptions):
    selected_theme = st.session_state.agrid_selected_theme
    agrid_table = AgGrid(
        df,
        theme=selected_theme,
        gridOptions=gridOptions,
        fit_columns_on_grid_load=st.session_state.agrid_options.get('fit_columns_on_grid_load'),
        allow_unsafe_jscode=st.session_state.agrid_options.get('allow_unsafe_jscode'),
        enable_enterprise_modules=st.session_state.agrid_options.get('enable_enterprise_modules'),
        height=st.session_state.agrid_options.get('height'),
        rows=st.session_state.agrid_options.get('rows'),
        data_return_mode=DataReturnMode.FILTERED_AND_SORTED
    )
    return agrid_table
