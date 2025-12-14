import streamlit as st
import time

# Configuration de la page
st.set_page_config(
    page_title="Ada-Tech Group",
    page_icon="🌐",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Couleurs et styles
primary_color = "#00FFF7"
background_color = "#0D0D0D"
text_color = "#FFFFFF"
card_gradients = [
    "linear-gradient(135deg, #ff416c, #ff4b2b)",
    "linear-gradient(135deg, #1f4037, #99f2c8)",
    "linear-gradient(135deg, #654ea3, #eaafc8)",
    "linear-gradient(135deg, #f7971e, #ffd200)",
    "linear-gradient(135deg, #43cea2, #185a9d)",
]

# CSS avancé
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
    color: #0D0D0D;
    font-weight: bold;
    border-radius: 12px;
    padding: 12px 25px;
    box-shadow: 0 0 20px {primary_color};
    transition: all 0.3s ease;
}}
.stButton>button:hover {{
    transform: scale(1.05);
    box-shadow: 0 0 35px {primary_color}, 0 0 50px {primary_color};
}}
h1, h2, h3 {{
    color: {primary_color};
    text-shadow: 0 0 8px {primary_color}, 0 0 15px {primary_color};
}}
.service {{
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 25px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    color: #fff;
    transition: transform 0.4s ease, box-shadow 0.4s ease;
    background-size: 200% 200%;
    animation: gradientAnimation 4s ease infinite;
}}
.service:hover {{
    transform: scale(1.08);
    box-shadow: 0 0 30px rgba(255,255,255,0.4);
}}
@keyframes gradientAnimation {{
    0% {{ background-position: 0% 50%; }}
    50% {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
}}
.counter {{
    font-size: 38px;
    font-weight: bold;
    color: {primary_color};
    text-shadow: 0 0 10px {primary_color}, 0 0 20px {primary_color};
}}
</style>
""",
    unsafe_allow_html=True,
)

# Titre principal
st.title("✨ Bienvenue sur Ada-Tech Group ✨")
st.subheader("Découvrez nos services et solutions technologiques futuristes")

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
            "Génie Civil (à venir)",
        ]

        # Affichage des services avec animation
        for i, service in enumerate(services):
            gradient = card_gradients[i % len(card_gradients)]
            with st.container():
                st.markdown(
                    f"""
                    <div class="service" style="background-image:{gradient}">
                        {service}
                    </div>
                """,
                    unsafe_allow_html=True,
                )

                # Compteur numérique animé
                counter_placeholder = st.empty()
                for count in range(0, 101, 5):
                    counter_placeholder.markdown(
                        f'<div class="counter">{count}%</div>', unsafe_allow_html=True
                    )
                    time.sleep(0.03)
                counter_placeholder.empty()  # Supprime le compteur après animation
    else:
        st.error("Nom d'utilisateur ou mot de passe incorrect.")
