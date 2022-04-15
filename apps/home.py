import streamlit as st

import pandas as pd
import numpy as np


def app():
    with st.container():
        st.image('https://spiritsnetwork.com/assets/imgs/icons/logo.svg', width=480)
        st.title('Spirits network')
        st.write('Navigate to `Data Stats` page to visualize the data')
