import streamlit as st
import time

# ================= CONFIG =================
st.set_page_config(
    page_title="Ada-Tech Group",
    page_icon="🚀",
    layout="wide",
)

PRIMARY = "#00FFF7"
BG = "#0A0A0A"
TEXT = "#FFFFFF"

# ================= CSS =================
st.markdown(f"""
<style>
body {{
    background-color: {BG};
    color: {TEXT};
}}

.hero {{
    padding: 120px 40px;
    text-align: center;
}}

.hero h1 {{
    font-size: 4rem;
    color: {PRIMARY};
    text-shadow: 0 0 30px {PRIMARY};
}}

.hero p {{
    font-size: 1.4rem;
    opacity: 0.85;
}}

.cta {{
    margin-top: 30px;
    padding: 16px 38px;
    background: {PRIMARY};
    color: #000;
    font-size: 18px;
    border-radius: 40px;
    display: inline-block;
    box-shadow: 0 0 25px {PRIMARY};
    transition: 0.4s;
}}

.cta:hover {{
    transform: scale(1.1);
    box-shadow: 0 0 60px {PRIMARY};
}}

.section {{
    padding: 80px 40px;
}}

.service-card {{
    background: linear-gradient(135deg, #1a1a1a, #111);
    border-radius: 25px;
    padding: 40px;
    text-align: center;
    transition: 0.4s;
    height: 100%;
}}

.service-card:hover {{
    transform: translateY(-15px);
    box-shadow: 0 0 40px rgba(0,255,247,0.35);
}}

.service-card h3 {{
    color: {PRIMARY};
}}

.footer {{
    text-align: center;
    padding: 40px;
    opacity: 0.6;
}}
</style>
""", unsafe_allow_html=True)

# ================= HERO =================
st.markdown("""
<div class="hero">
    <h1>Ada-Tech Group</h1>
    <p>Vos solutions technologiques sur mesure</p>
    <div class="cta">Découvrir nos services</div>
</div>
""", unsafe_allow_html=True)

# ================= SERVICES =================
st.markdown("<div class='section'><h2>🚀 Nos Services</h2></div>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

services = [
    ("🌐", "Développement Web", "Sites modernes, performants et sécurisés."),
    ("📱", "Développement Mobile", "Applications Android & iOS sur mesure."),
    ("🎓", "Formation", "Formations pratiques en technologies modernes."),
    ("🚚", "Logistique", "Solutions digitales pour la livraison de colis."),
]

for col, (icon, title, desc) in zip([col1, col2, col3, col4], services):
    with col:
        st.markdown(f"""
        <div class="service-card">
            <h1>{icon}</h1>
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.1)

# ================= VISION =================
st.markdown("""
<div class="section">
    <h2>💡 Notre Vision</h2>
    <p>
        Ada-Tech Group accompagne les entreprises et particuliers
        dans leur transformation digitale grâce à des solutions
        innovantes, fiables et adaptées à leurs besoins.
    </p>
</div>
""", unsafe_allow_html=True)

# ================= CONTACT =================
st.markdown("""
<div class="section">
    <h2>📩 Contactez-nous</h2>
    <p>Prêt à transformer votre business ? Parlons-en.</p>
</div>
""", unsafe_allow_html=True)

st.button("📞 Nous contacter")

# ================= FOOTER =================
st.markdown("""
<div class="footer">
© 2025 Ada-Tech Group • Tous droits réservés
</div>
""", unsafe_allow_html=True)
