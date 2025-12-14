import streamlit as st
from PIL import Image

# Charger le logo
logo = Image.open("3182dbc4-7c69-4245-8bd0-88799d82302d.png")
st.image(logo, width=300)  # Ajuste la taille si nécessaire

# Titre et sous-titre
st.title("Bienvenue sur Ada-Tech Group")
st.subheader("Notre technologie, votre expérience numérique idyllique")

# Liste des services
services = [
    "Développement web",
    "Applications mobiles",
    "Formation",
    "Logistique de livraison de colis",
    "Génie civil (bientôt disponible)"
]

st.write("Voici nos services :")
for service in services:
    st.write(f"- {service}")
