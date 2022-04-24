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
                   'product_id': 1,
                   'variant_id': 1,
                   'order_address_id': 1,
                   'name': 1,
                   'name_customer': 1,
                   'name_merchant': 1,
                   'sku': 1,
                   'upc': 1,
                   'type': 1,
                   'base_price': 1,
                   'price_ex_tax': 1,
                   'price_inc_tax': 1,
                   'price_tax': 1,
                   'base_total': 1,
                   'total_ex_tax': 1,
                   'total_inc_tax': 1,
                   'total_tax': 1,
                   'weight': 1,
                   'width': 1,
                   'height': 1,
                   'depth': 1,
                   'quantity': 1,
                   'base_cost_price': 1,
                   'cost_price_inc_tax': 1,
                   'cost_price_ex_tax': 1,
                   'cost_price_tax': 1,
                   'is_refunded': 1,
                   'quantity_refunded': 1,
                   'refund_amount': 1,
                   'return_id': 1,
                   'wrapping_name': 1,
                   'base_wrapping_cost': 1,
                   'wrapping_cost_ex_tax': 1,
                   'wrapping_cost_inc_tax': 1,
                   'wrapping_cost_tax': 1,
                   'wrapping_message': 1,
                   'quantity_shipped': 1,
                   'event_name': 1,
                   'event_date': 1,
                   'fixed_shipping_cost': 1,
                   'ebay_item_id': 1,
                   'ebay_transaction_id': 1,
                   'option_set_id': 1,
                   'parent_order_product_id': 1,
                   }
    query = {}
    df = get_data_from_collection('orders', query, select_rows)
    df = df.reset_index()
    # df = prepare_date_columns(df)
    gb = set_ggrid_options(df)

    gridOptions = gb.build()
    grid_response = get_table(df, gridOptions)


