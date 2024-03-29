import streamlit as st

st.set_page_config(
    page_title="Mes projets",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="auto",
)
st.header('Mes projets:', divider="rainbow")

col1, col2 = st.columns(2)

with col1:
    st.write("Portfolio sur internet")
with col2:
    st.link_button("Voir mon site internet", 
                "https://isd.ydiallo.com/", 
                type="secondary", 
                use_container_width=False
                )



