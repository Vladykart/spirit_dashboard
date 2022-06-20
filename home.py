import streamlit as st
import streamlit_authenticator as stauth
import extra_streamlit_components as stx
from settings import AGRID_OPTIONSS

st.set_page_config(page_title="Spirit", layout="wide")
if 'agrid_selected_theme' not in st.session_state:
    st.session_state.agrid_selected_theme = "dark"

if 'agrid_options' not in st.session_state:
    st.session_state.agrid_options = AGRID_OPTIONSS

agrid_available_themes = ["streamlit", "light", "dark", "blue", "fresh", "material"]
agrid_selected_theme = st.selectbox("Theme", agrid_available_themes, index=2)
st.session_state.agrid_selected_theme = agrid_selected_theme
if "agrid_selected_theme" not in st.session_state:
    st.session_state.agrid_selected_theme = agrid_selected_theme

if 'agrid_options' not in st.session_state:
    st.session_state.agrid_options = AGRID_OPTIONSS


st.write('To view Video usage from Google Analysis, click The [Video](https://share.streamlit.io/vladykart/spirit_dashboard/home.py) button on the sidebar menu on the '
         'left ')

