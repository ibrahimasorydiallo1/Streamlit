import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Mes plots",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="auto",
)
st.sidebar.title("💎 ISD")
st.subheader('Culture foot !⚽', divider="rainbow")
df_base = pd.read_csv("./assets/fichiers/past-data.csv")

df_infos = pd.DataFrame(df_base,)

liste_championnat = ["Premier League", "Bundesliga", "Serie A",
                     "Ligue 1", "LaLiga"
                     ]
championnat = st.sidebar.selectbox("Quel championnat ?",
                           index=None,
                           options=liste_championnat,
                           )
if championnat:
    df_championnat = df_infos[(df_infos['Div'] == championnat) &              
                              (df_infos['Season'].str[-2:].astype(int).between(18, 23))
                            ].reset_index(drop=True)
    
    df_championnat = df_championnat.drop(columns=['Referee','HTHG', 'HTAG', 'AS', 'HS']
                                         ).iloc[:, :-8]
    # st.write(df_championnat)
    # Regarder le nombre de buts marqués par an dans le championnat (graphe et tableau)
    
    # for i in (18, 24):
    goals_stats = df_infos[(df_infos['Div'] == championnat) &              
                            (df_infos['Season'].str[-2:].astype(int).between(17, 18))
                            ].reset_index(drop=True)
    st.write(goals_stats)