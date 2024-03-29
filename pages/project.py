import streamlit as st

st.set_page_config(
    page_title="Mes projets",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="auto",
)
st.header('Mes projets:', divider="rainbow")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Portfolio**")
with col2:
    st.link_button("Voir mon site internet", 
                "https://isd.ydiallo.com/", 
                type="primary", 
                use_container_width=False
                )



