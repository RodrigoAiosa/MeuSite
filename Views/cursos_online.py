import streamlit as st
import os
import sys

# 1. RESOLVENDO O CAMINHO DO MÓDULO UTILS ANTES DO IMPORT
# Isso garante que ele ache o utils.py na raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from utils import exibir_rodape, registrar_acesso
except ImportError:
    st.error("Erro: O arquivo 'utils.py' não foi encontrado na pasta raiz.")

# --- REGISTRO DE ACESSO ---
# Chamando a função conforme solicitado para registrar a entrada na página
registrar_acesso("Cursos Online")

# 2. CONFIGURAÇÃO VISUAL DA PÁGINA (UI/UX)
st.markdown("""
    <style>
    h1, h2 { color: #1E3A8A !important; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("🎓 Meus Cursos Online")
st.write("Aprimore suas habilidades com treinamentos práticos e focados no mercado.")

# Botões de Conversão Rápida
col_c1, col_c2, _ = st.columns([1, 1, 2])
with col_c1:
    msg_wa_geral = "Olá Rodrigo! Vi seus cursos e gostaria de tirar algumas dúvidas."
    link_wa_geral = f"https://wa.me/5511977019335?text={msg_wa_geral.replace(' ', '%20')}"
    st.link_button("💬 WhatsApp", link_wa_geral)
with col_c2:
    st.link_button("📅 Reunião", "https://calendly.com/rodrigoaiosa")

st.divider()

# --- CURSO 1: FUNDAMENTO POWER BI ---
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    img_pbi = os.path.join("assets", "fundamentos_power_bi.png")
    st.image(img_pbi, use_container_width=True)

with col2:
    st.header("Fundamento Power BI")
    st.write(
        """
        Domine o Power BI do zero. Aprenda a criar análises visuais estratégicas, 
        importar e transformar dados de forma lógica. Se você busca decisões mais 
        inteligentes e dashboards de impacto, esse é o seu primeiro passo.
        """
    )
    
    # Mensagem personalizada WhatsApp
    msg_pbi = "Olá Rodrigo! Tenho interesse no curso de Power BI. Pode me ajudar?"
    link_pbi = f"https://wa.me/5511977019335?text={msg_pbi.replace(' ', '%20')}"
    
    c1, c2 = st.columns(2)
    with c1:
        st.link_button("🚀 Comprar Agora", "https://pay.kiwify.com.br/DFeDsQV")
    with c2:
        st.link_button("💬 Dúvidas", link_pbi)

st.divider()

# --- CURSO 2: SQL FUNDAMENTOS ---
col3, col4 = st.columns([1, 2], gap="large")

with col3:
    img_sql = os.path.join("assets", "SQL_Fundamentos.png")
    st.image(img_sql, use_container_width=True)

with col4:
    st.header("SQL Fundamentos")
    st.write(
        """
        Aprenda a linguagem dos dados. Do básico ao avançado, com foco prático 
        para manipular e extrair valor real de grandes bases de dados. 
        Ideal para quem quer autonomia na análise.
        """
    )
    
    # Mensagem personalizada WhatsApp
    msg_sql = "Olá Rodrigo! Quero saber mais sobre o curso de SQL."
    link_sql = f"https://wa.me/5511977019335?text={msg_sql.replace(' ', '%20')}"

    c1, c2 = st.columns(2)
    with c1:
        st.link_button("🚀 Comprar Agora", "https://pay.kiwify.com.br/ivdojL8")
    with c2:
        st.link_button("💬 Dúvidas", link_sql)

st.divider()

# --- CURSO 3: EXCEL ESSENCIAL PARA NEGÓCIOS ---
col5, col6 = st.columns([1, 2], gap="large")

with col5:
    img_excel = os.path.join("assets", "excel_para_negocios.png")
    st.image(img_excel, use_container_width=True)

with col6:
    st.header("Excel Essencial Para Negócios")
    st.write(
        """
        Excel de forma prática e aplicada. Domine as ferramentas que o mercado 
        realmente exige e conquiste uma vantagem imediata na sua rotina profissional.
        """
    )
    
    # Mensagem personalizada WhatsApp
    msg_excel = "Olá Rodrigo! Tenho interesse no curso de Excel para Negócios."
    link_excel = f"https://wa.me/5511977019335?text={msg_excel.replace(' ', '%20')}"

    c1, c2 = st.columns(2)
    with c1:
        st.link_button("🚀 Comprar Agora", "https://pay.kiwify.com.br/EEb9ADQ")
    with c2:
        st.link_button("💬 Dúvidas", link_excel)

st.divider()

# 3. EXIBIÇÃO DO RODAPÉ
exibir_rodape()
