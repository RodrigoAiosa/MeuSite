import streamlit as st
import time
import sys
import os

# --- CORREÇÃO DINÂMICA DE CAMINHO ---
# Adiciona a raiz do projeto ao PATH para que o Python encontre o 'utils.py'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    # Agora o import funcionará tanto localmente quanto no Streamlit Cloud
    from utils import registrar_acesso_db, exibir_rodape
except ImportError:
    st.error("Erro técnico: O sistema não conseguiu carregar as dependências de banco de dados.")

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(layout="wide", page_title="Portfolio | Rodrigo Aiosa")

# 2. REGISTRO DE ACESSO NO POSTGRESQL (Aiven)
# O nome do banco de dados deve ser 'defaultdb' conforme seu console Aiven
registrar_acesso_db("Sobre Mim")

# --- ESTILO CSS CUSTOMIZADO ---
st.markdown(
    """
    <style>
    /* Container da Foto com Borda Animada */
    .profile-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: -30px;
    }
    .profile-pic-border {
        position: relative;
        width: 210px;
        height: 210px;
        background: #151515;
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 50%;
        overflow: hidden;
    }
    .profile-pic-border::before {
        content: '';
        position: absolute;
        width: 150%;
        height: 150%;
        background: conic-gradient(transparent, #00b4d8, #00b4d8, transparent 40%);
        animation: rotate-border 4s linear infinite;
    }
    .profile-pic-border img {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        object-fit: cover;
        z-index: 1;
        background-color: #151515;
    }
    @keyframes rotate-border {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    .main-title { text-align: center; margin-top: 10px; }
    
    /* Estilo dos Cards de Experiência */
    .exp-card {
        background-color: #111827;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #00b4d8;
        transition: transform 0.3s ease;
    }
    .exp-card:hover {
        transform: translateY(-5px);
        background-color: #1f2937;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- CABEÇALHO ---
st.markdown(
    """
    <div class="profile-container">
        <div class="profile-pic-border">
            <img src="https://media.licdn.com/dms/image/v2/D5603AQFTfyqJswUYwg/profile-displayphoto-scale_200_200/B56ZxDaPuZK4AY-/0/1770657482765?e=1772064000&v=beta&t=1PXFrPJTt5w46Y7NUTgqCQ3H2jjMmkE1QwFi-lwwwko">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="main-title">Rodrigo Aiosa</h1>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; color: #00b4d8; font-weight: bold;">Python | Excel | Power BI | ETL | SQL SERVER</div>', unsafe_allow_html=True)

st.write("---")

# --- CONTEÚDO DE EXPERIÊNCIA ---
st.subheader("🤝 Experiência de Mercado")
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="exp-card">
            <h3 style="color: white;">🔎 Análise e Automação</h3>
            <p style="color: #9ca3af;">Otimização de processos corporativos com Python e modelos avançados de Excel.</p>
        </div>
        """, unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="exp-card">
            <h3 style="color: white;">📊 Business Intelligence</h3>
            <p style="color: #9ca3af;">Dashboards estratégicos utilizando Power BI, Linguagem M e DAX para tomada de decisão.</p>
        </div>
        """, unsafe_allow_html=True
    )

st.write("")
# Exibição da imagem de clientes utilizando o caminho correto no seu repositório
st.image("assets/clientes_atendidos.jpg", use_container_width=True)

# --- RODAPÉ E ATUALIZAÇÃO DE DURAÇÃO ---
# Esta função encerra a página atualizando o tempo de permanência no banco
exibir_rodape()
