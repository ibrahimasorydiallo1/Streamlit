import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Mes plots",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="auto",
)
st.header('Culture foot !⚽', divider="rainbow")
df_base = pd.read_csv("./assets/fichiers/past-data.csv")
df_infos = pd.DataFrame(df_base,)

liste_championnat = ["Premier League", "Bundesliga", "Serie A",
                     "Ligue 1", "LaLiga"
                     ]
championnat = st.selectbox("Quel championnat ?",
                           index=None,
                           options=liste_championnat,
                           )
if championnat:
    df_championnat = df_infos[(df_infos['Div'] == championnat) &              
                            (df_infos['Season'].str[-2:].astype(int).between(18, 23))
                            ].reset_index(drop=True)

    st.write(df_championnat)