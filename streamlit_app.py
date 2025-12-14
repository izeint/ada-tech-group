import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Ada-Tech Group",
    page_icon="🌐",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Couleurs personnalisées
primary_color = "#00BFFF"  # accent bleu
background_color = "#1B263B"  # bleu nuit
text_color = "#F0F0F0"  # texte clair

# CSS pour le style
st.markdown(
    f"""
    <style>
        body {{
            background-color: {background_color};
            color: {text_color};
            font-family: 'Arial', sans-serif;
        }}
        .stButton>button {{
            background-color: {primary_color};
            color: {background_color};
            font-weight: bold;
        }}
        h1, h2, h3 {{
            color: {primary_color};
        }}
        .service {{
            background-color: #0D1B2A;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 15px;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Titre principal
st.title("Bienvenue sur Ada-Tech Group")
st.subheader("Découvrez nos services et solutions technologiques")

# Connexion simple
username = st.text_input("Nom d'utilisateur")
password = st.text_input("Mot de passe", type="password")

if st.button("Se connecter"):
    if username == "admin" and password == "1234":
        st.success(f"Connexion réussie ! Bienvenue {username} sur Ada-Tech Group.")

        st.write("### Nos Services :")
        services = [
            "Développement Web",
            "Développement Mobile",
            "Formation",
            "Logistique et Livraison de Colis",
            "Génie Civil (à venir)"
        ]

        for service in services:
            st.markdown(f'<div class="service">- {service}</div>', unsafe_allow_html=True)
    else:
        st.error("Nom d'utilisateur ou mot de passe incorrect.")
