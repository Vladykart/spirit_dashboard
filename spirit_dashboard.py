import streamlit as st
import pandas as pd
import numpy as np

# -- Set page config
app_title = 'Stations map'
st.set_page_config(page_title=app_title, page_icon=":eyeglasses:", layout="wide")

st.title('Uber pickups in NYC')

# -- Default detector list
page_list = ['first', 'second', 'third']
# -- Choose page
page = st.sidebar.selectbox('Page', page_list)