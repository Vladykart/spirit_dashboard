import streamlit as st

# from data import get_data
from multiapp import MultiApp
from apps import session_settings
from apps import home
from apps import video
from apps import orders
from apps import clients
from data.get_data import get_unique_values_from_columns
import streamlit_authenticator as stauth
import extra_streamlit_components as stx


st.set_page_config(page_title="Spirit", layout="wide")


names = ["admin", "Rebecca Briggs"]
usernames = ["spirits", "rbriggs"]
passwords = ["spirits", "456"]

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    "some_cookie_name",
    "some_signature_key",
    cookie_expiry_days=30,
)

if authenticator:
    stx.bouncing_image(
        image_source="https://spiritsnetwork.com/assets/imgs/icons/logo.svg",
        animate=False,
        animation_time=1500,
        width=480,
        height=200,
    )

name, authentication_status, username = authenticator.login("Login", "main")

app = MultiApp()
if st.session_state["authentication_status"]:
    authenticator.logout("Logout", "sidebar")
    st.write("Welcome *%s*" % (st.session_state["name"]))
    st.title("Some content")
    if "events_action" not in st.session_state:
        st.session_state.events_action = get_unique_values_from_columns(
            "video", "eventAction"
        )
    # Add all your application here
    app.add_app("Settings", session_settings.app)
    app.add_app("Home", home.app)
    app.add_app("Video", video.app)
    app.add_app("Orders", orders.app)
    app.add_app("Clients", orders.app)

    # The main app
    app.run()
elif not st.session_state["authentication_status"]:
    st.error("Username/password is incorrect")

elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")
