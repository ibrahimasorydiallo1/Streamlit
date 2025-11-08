import streamlit as st
from random import randint

st.set_page_config(page_title="Jeu du nombre mystère", page_icon="🎯", layout="centered")
st.title("🎯 Jeu du nombre mystère")

# Étape 1 : le joueur choisit un nombre
if "nombre_choisi" not in st.session_state:
    st.session_state.nombre_choisi = None
if "jeu_lance" not in st.session_state:
    st.session_state.jeu_lance = False
if "min" not in st.session_state:
    st.session_state.min = 1
if "max" not in st.session_state:
    st.session_state.max = 100
if "tentative" not in st.session_state:
    st.session_state.tentative = 1
if "nb_o" not in st.session_state:
    st.session_state.nb_o = randint(1, 100)
if "fini" not in st.session_state:
    st.session_state.fini = False

# ---------------------
# Étape 1 : Choisir le nombre
# ---------------------
if not st.session_state.jeu_lance:
    nbre_choisi = st.number_input("Choisis un nombre entre 1 et 100 :", 1, 100, key="choix_utilisateur")
    if st.button("✅ Valider mon nombre"):
        st.session_state.nombre_choisi = nbre_choisi
        st.session_state.jeu_lance = True
        st.toast("Ton nombre est enregistré, le jeu commence ! 🎮")
        st.rerun()
    st.stop()  # On arrête ici tant que le joueur n'a pas validé son choix

# ---------------------
# Étape 2 : L’ordinateur devine
# ---------------------
st.success(f"Ton nombre secret est bien enregistré ! 🤫")
st.write("Guide l’ordinateur pour qu’il devine ton nombre.")

if not st.session_state.fini:
    st.info(f"Tentative n°{st.session_state.tentative}")
    st.subheader(f"💭 L’ordinateur propose : **{st.session_state.nb_o}**")

    test = st.radio(
        "Ta réponse :",
        ["plus", "moins", "gagné"],
        horizontal=True,
        key=f"reponse_{st.session_state.tentative}"
    )

    if st.button("➡️ Valider ma réponse"):
        if test == "moins":
            st.session_state.max = st.session_state.nb_o - 1
            st.toast("C’est moins 👇")
        elif test == "plus":
            st.session_state.min = st.session_state.nb_o + 1
            st.toast("C’est plus 👆")
        elif test == "gagné":
            st.success(f"L’ordinateur a trouvé ton nombre {st.session_state.nombre_choisi} en {st.session_state.tentative} tentatives !")
            st.balloons()
            st.session_state.fini = True

        if not st.session_state.fini:
            st.session_state.tentative += 1
            if st.session_state.tentative > 7:
                st.error("L’ordinateur a perdu ! Tu as gagné 👏")
                st.session_state.fini = True
            else:
                st.session_state.nb_o = randint(st.session_state.min, st.session_state.max)
                st.rerun()

# Bouton pour recommencer une partie
if st.button("🔁 Rejouer"):
    st.session_state.clear()
    st.rerun()