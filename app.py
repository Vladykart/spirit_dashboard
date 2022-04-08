import streamlit as st
from multiapp import MultiApp
from apps import home, video # import your app modules here

app_title = 'Spirits'
st.set_page_config(page_title=app_title, page_icon=":eyeglasses:", layout="wide")
app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Video", video.app)

# The main app
app.run()