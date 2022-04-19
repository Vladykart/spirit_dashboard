import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from pivottablejs import pivot_ui
from settings import AGRID_OPTIONSS


if 'agrid_selected_theme' not in st.session_state:
    st.session_state.agrid_selected_theme = "dark"

if 'agrid_options' not in st.session_state:
    st.session_state.agrid_options = AGRID_OPTIONSS



def app():
    st.title('Settings')
    agrid_available_themes = ["streamlit", "light", "dark", "blue", "fresh", "material"]
    agrid_selected_theme = st.selectbox("Theme", agrid_available_themes, index=2)
    st.session_state.agrid_selected_theme = agrid_selected_theme
    if "agrid_selected_theme" not in st.session_state:
        st.session_state.agrid_selected_theme = agrid_selected_theme

    if 'agrid_options' not in st.session_state:
        st.session_state.agrid_options = AGRID_OPTIONSS
    st.write('Navigate to `Data Stats` page to visualize the data')