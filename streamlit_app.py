PRIMARY = "#1E90FF"   # BLEU
SECONDARY = "#FFD700" # JAUNE
BG = "#0A0A0A"
TEXT = "#FFFFFF"

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
    background: {SECONDARY};
    color: {BG};
    font-size: 18px;
    border-radius: 40px;
    display: inline-block;
    box-shadow: 0 0 25px {SECONDARY};
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
    color: {PRIMARY};
}}

.footer {{
    text-align: center;
    padding: 40px;
    opacity: 0.6;
}}
</style>
""", unsafe_allow_html=True)
