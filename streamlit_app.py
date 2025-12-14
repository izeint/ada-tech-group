import streamlit as st
import time

# ================= CONFIG =================
st.set_page_config(
    page_title="Ada-Tech Group",
    page_icon="🌐",
    layout="wide",
)

BG = "#0A0A0A"
TEXT = "#EAEAEA"

# ================= CSS =================
st.markdown(f"""
<style>
body {{
    background-color: {BG};
    color: {TEXT};
}}

.header {{
    display: flex;
    align-items: center;
    padding: 20px 40px;
}}

.logo img {{
    height: 55px;
}}

.hero {{
    padding: 100px 40px;
    text-align: center;
}}

.hero h1 {{
    font-size: 4rem;
    color: white;
    text-shadow: 0 0 25px rgba(255,255,255,0.25);
}}

.hero p {{
    font-size: 1.4rem;
    opacity: 0.8;
}}

.cta {{
    margin-top: 30px;
    padding: 16px 38px;
    background: #1a1a1a;
    color: white;
    font-size: 18px;
    border-radius: 40px;
    display: inline-block;
    box-shadow: 0 0 20px rgba(255,255,255,0.1);
    transition: 0.4s;
}}

.cta:hover {{
    transform: scale(1.1);
    box-shadow: 0 0 40px rgba(255,255,255,0.25);
}}

.section {{
    padding: 80px 40px;
}}

.service-card {{
    background: #111;
    border-radius: 25px;
    overflow: hidden;
    transition: 0.4s;
}}

.service-card:hover {{
    transform: translateY(-15px);
    box-shadow: 0 0 30px rgba(255,255,255,0.2);
}}

.service-card img {{
    width: 100%;
    height: 220px;
    object-fit: cover;
    filter: grayscale(100%);
}}

.service-content {{
    padding: 25px;
    text-align: center;
}}

.footer {{
    text-align: center;
    padding: 40px;
    opacity: 0.6;
}}
</style>
""", unsafe_allow_html=True)

# ================= HEADER (LOGO) =================
st.markdown("""
<div class="header">
    <div class="logo">
    st.image("logo.png", width=180)

    </div>
</div>
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
st.markdown("<div class='section'><h2>Nos Services</h2></div>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

services = [
    ("Développement Web", "Sites modernes et performants.", "https://images.unsplash.com/photo-1521737604893-d14cc237f11d"),
    ("Développement Mobile", "Applications Android & iOS.", "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9"),
    ("Formation", "Formations tech professionnelles.", "https://images.unsplash.com/photo-1522202176988-66273c2fd55f"),
    ("Logistique", "Livraison et gestion de colis.", "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d"),
]

for col, (title, desc, img) in zip([col1, col2, col3, col4], services):
    with col:
        st.markdown(f"""
        <div class="service-card">
            <img src="{img}">
            <div class="service-content">
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.1)

# ================= FOOTER =================
st.markdown("""
<div class="footer">
© 2025 Ada-Tech Group • Tous droits réservés
</div>
""", unsafe_allow_html=True)
