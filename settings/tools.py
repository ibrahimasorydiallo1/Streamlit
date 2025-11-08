import streamlit as st

def mise_en_page():
    st.set_page_config(
        page_title="Mon portfolio",
        page_icon="🌕",
        layout="wide",
        initial_sidebar_state="auto",
    )
    st.sidebar.title("💎 ISD")
    st.logo("assets\img\logo.png", size="large", link="https://isd.ydiallo.com/")