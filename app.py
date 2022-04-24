import streamlit as st

from data import get_data
from multiapp import MultiApp
from apps import session_settings
from apps import home
from apps import video
from apps import orders
from apps import clients
from data.get_data import get_unique_values_from_columns

st.set_page_config(page_title="Spirit", layout="wide")

app = MultiApp()

if 'events_action' not in st.session_state:
    st.session_state.events_action = get_data.get_unique_values_from_columns('video', 'eventAction')


# Add all your application here

app.add_app("Home", home.app)
app.add_app("Video", video.app)
app.add_app("Orders", orders.app)
app.add_app("Clients", orders.app)
app.add_app('Settings', session_settings.app)

# The main app
app.run()
