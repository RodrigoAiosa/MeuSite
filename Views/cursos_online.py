import streamlit as st
import os
import sys
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---
registrar_acesso("Cursos Online")

# 1. RESOLVENDO O CAMINHO DO MÓDULO UTILS
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from utils import exibir_rodape, registrar_acesso
except ImportError:
    st.error("Erro: O arquivo 'utils.py' não foi encontrado na pasta raiz.")

# ---------------- ESTILO PREMIUM ----------------
st.markdown("""
<style>

/* HERO */
.hero {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    padding: 60px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
}

/* SECTION TITLE */
.section-title {
    font-size: 32px;
    font-weight: 700;
    margin-top: 40px;
    margin-bottom: 20px;
}

/* FEATURE CARDS */
.feature-card {
    background: #111827;
    padding: 25px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.08);
    min-height: 140px;

    opacity: 0;
    transform: translateY(20px);
    animation: fadeUp 0.7s ease forwards;
}

/* Delay para efeito em sequência */
.card1 { animation-delay: 0.1s; }
.card2 { animation-delay: 0.3s; }
.card3 { animation-delay: 0.5s; }

@keyframes fadeUp {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Glow hover */
.feature-card:hover {
    transform: translateY(-6px);
    border: 1px solid rgba(59,130,246,0.6);
    box-shadow: 0 0 18px rgba(59,130,246,0.35);
}

/* TEXT */
.feature-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 10px;
}

.feature-text {
    color: #cbd5e1;
}

/* BOTÕES */
.stLinkButton a {
    background-color: #2563eb !important;
    color: white !important;
    padding: 14px 26px !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
<h1>Habilidades que transformam profissionais comuns em profissionais indispensáveis</h1>
<p>Power BI • SQL • Excel aplicados ao mundo real dos negócios</p>
</div>
""", unsafe_allow_html=T
