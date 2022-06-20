import streamlit as st
import streamlit_authenticator as stauth
import extra_streamlit_components as stx
from settings import AGRID_OPTIONSS

st.set_page_config(page_title="Spirit", layout="wide")

st.markdown("# Home")
st.sidebar.markdown("# Home")

st.write(
    "To view Video usage from Google Analysis, click The [Video]("
    "https://share.streamlit.io/vladykart/spirit_dashboard/home.py/video) button on the sidebar menu on "
    "the "
    "left "
)

st.write(
    "To view Orders usage from BIGCOMMERCE, click The [Orders]("
    "https://share.streamlit.io/vladykart/spirit_dashboard/home.py/orders) button on the sidebar "
    "menu on "
    "the "
    "left "
)

st.write(
    "To view Clients usage from BIGCOMMERCE, click The [Products]("
    "https://share.streamlit.io/vladykart/spirit_dashboard/home.py/clients) button on the sidebar "
    "menu on "
    "the "
    "left "
)
