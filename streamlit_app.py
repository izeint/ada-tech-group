import streamlit as st

# Titre du site
st.title("Bienvenue sur Ada-Tech Group")
st.subheader("Découvrez nos services et solutions technologiques")

# Connexion simple
username = st.text_input("Nom d'utilisateur")
password = st.text_input("Mot de passe", type="password")

if st.button("Se connecter"):
    if username == "admin" and password == "1234":
        st.success(f"Connexion réussie ! Bienvenue {username} sur Ada-Tech Group.")
        st.write("Voici nos services :")
        st.write("- Développement web")
        st.write("- Applications mobiles")
        st.write("- Data Science et Analyse")
        st.write("- Maintenance et support")
    else:
        st.error("Nom d'utilisateur ou mot de passe incorrect.")
