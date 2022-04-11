import streamlit as st
from multiapp import MultiApp
from apps import home, video, session_settings  # import your app modules here


st.set_page_config(page_title="Spirit", layout="wide")

app = MultiApp()
init_session_settings = session_settings.app
# Add all your application here

app.add_app("Home", home.app)
app.add_app("Video", video.app)
app.add_app('Settings', init_session_settings)

# The main app
app.run()
