import streamlit as st
import time

# ================= CONFIG =================
st.set_page_config(
    page_title="Ada-Tech Group",
    page_icon="🌐",
    layout="wide",
)

PRIMARY = "#1E90FF"   # Bleu
SECONDARY = "#FFD700" # Jaune
BG = "#0A0A0A"
TEXT = "#FFFFFF"

# ================= CSS =================
st.markdown("""
<style>
body {{
    background-color: {bg};
    color: {text};
}}

.hero {{
    padding: 120px 40px;
    text-align: center;
}}

.hero h1 {{
    font-size: 4rem;
    color: {primary};
    text-shadow: 0 0 30px {primary};
}}

.hero p {{
    font-size: 1.4rem;
    opacity: 0.85;
}}

.cta {{
    margin-top: 30px;
    padding: 16px 38px;
    background: {secondary};
    color: {bg};
    font-size: 18px;
    border-radius: 40px;
    display: inline-block;
    box-shadow: 0 0 25px {secondary};
    transition: 0.4s;
    cursor: pointer;
}}

.cta:hover {{
    transform: scale(1.1);
    box-shadow: 0 0 60px {primary};
}}

.section {{
    padding: 80px 40px;
}}

.service-card {{
    background: linear-gradient(135deg, #0f1c2e, #0a2540);
    border-radius: 25px;
    overflow: hidden;
    transition: 0.4s;
    height: 100%;
}}

.service-card:hover {{
    transform: translateY(-15px);
    box-shadow: 0 0 40px rgba(255,215,0,0.5);
}}

.service-card img {{
    width: 100%;
    height: 220px;
    object-fit: cover;
}}

.service-content {{
    padding: 25px;
    text-align: center;
}}

.service-content h3 {{
    color: {primary};
}}

.footer {{
    text-align: center;
    padding: 40px;
    opacity: 0.6;
}}
</style>
""".format(bg=BG, text=TEXT, primary=PRIMARY, secondary=SECONDARY), unsafe_allow_html=True)

# ================= HERO =================
st.markdown("""
<div class="hero">
    <h1>Ada-Tech Group</h1>
    <p>Vos solutions technologiques sur mesure</p>
    <div class="cta">Découvrir nos services</div>
</div>
""", unsafe_allow_html=True)

# ================= SERVICES =================
st.markdown("<div class='section'><h2>🔵 Nos Services</h2></div>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

services = [
    ("Développement Web", "Sites modernes, sécurisés et performants.", "https://images.unsplash.com/photo-1521737604893-d14cc237f11d"),
    ("Développement Mobile", "Applications Android & iOS sur mesure.", "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9"),
    ("Formation", "Formations pratiques en technologies modernes.", "https://images.unsplash.com/photo-1522202176988-66273c2fd55f"),
    ("Logistique de livraison", "Solutions digitales pour la gestion et livraison de colis.", "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d"),
]

for col, (title, desc, img) in zip([col1, col2, col3, col4], services):
    with col:
        st.markdown(f"""
        <div class="service-card">
            <img src="{img}" />
            <div class="service-content">
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.1)

# ================= VISION =================
st.markdown("""
<div class="section">
    <h2>💡 Notre Vision</h2>
    <p>
        Ada-Tech Group accompagne les entreprises et particuliers
        dans leur transformation digitale à travers des solutions
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
