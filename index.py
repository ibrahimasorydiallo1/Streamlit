import streamlit as st

st.set_page_config(
    page_title="Mon portfolio",
    page_icon="🌕",
    layout="wide",
    initial_sidebar_state="auto",
)
# st.sidebar.image("assets/img/profile_photo.jpg")
st.header('Projet portfolio *by streamlit*', divider="rainbow")
st.subheader("Ibrahima Sory DIALLO", divider="rainbow")

st.write("# Qui suis-je ? 🤔")
col_img1, col_img2, col_img3 = st.columns(3)
with col_img2:
    st.image("assets/img/profile_photo.jpg", 
            caption="My photo", 
            width=250,
            )
st.markdown(
    """
    Je m'appelle **Ibrahima Sory DIALLO**, je suis étudiant en 2ème année de bachelor informatique 
    à l'ESGI de Lyon et alternant chez **APICIL**. Je suis développeur *Snowflake et streamlit*. 
    J'ai obtenu diverses certifications comme: ***[MuleSoft Developer Level 1, AWS Cloud Quest: Cloud Practitioner]*** \n
    Pendant cette alternance chez APICIL j'ai acquis beaucoup de compétences
    Cette magnifique expérience dans la data où j'ai eu la chance de faire.
    Dynamique, proactif, rigoureux et relationnel , j'ai l'ambition de réussir chez APICIL qui est
    une entreprise qui ne cesse d'évoluer, une entreprise sociétale, sociale et solidaire.
    Pour l'année scolaire 2024-2025, j'ai pour objectif principal la réussite en école et en entreprise.
    """
)

st.write("## Découvrons ensemble Streamlit! 👋")
st.markdown(
    """
    Streamlit est un framework open-source qui sert à créer des interfaces ou applications
    dédiées à des projets en Machine Learning et en Data Science.

    Dans le passé, une visualisation bien réalisée ou un petit PowerPoint suffisaient pour présenter un projet de data science. 
    Mais avec l’avènement des outils de création de tableaux de bord comme RShiny et Dash, un bon data scientist doit désormais avoir 
    une certaine connaissance des frameworks web pour s'en sortir.

    Les frameworks web, cependant, sont difficiles à apprendre. Je me perds encore parmi tout ce HTML, CSS et Javascript, 
    avec toutes les tentatives et erreurs nécessaires pour faire quelque chose qui semble pourtant simple.

    Sans parler des nombreuses façons de faire la même chose, ce qui rend les choses encore plus confuses pour nous, 
    les spécialistes en data science, pour qui le développement web est une compétence secondaire.

    C’est là que Streamlit entre en jeu et tient sa promesse : créer des applications web uniquement avec Python.

    ### Cela vous intéresse?
    - Explorons la [documentation](https://docs.streamlit.io)
    - Obtenez des réponses à vos questions [community
        forums](https://discuss.streamlit.io)
"""
)

with st.sidebar:
    st.page_link("pages/Projets et certifications.py",
                  label="Mes projets",
                  icon="📅"
                  )

