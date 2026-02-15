import streamlit as st
import os
import sys

# 1. AJUSTE DE CAMINHO PARA ENCONTRAR O UTILS NA RAIZ
# Define o diretório base do projeto (um nível acima de /Views)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

try:
    from utils import exibir_rodape, registrar_acesso 
except ImportError:
    st.error("Erro: O arquivo 'utils.py' não foi encontrado na pasta raiz.")

# --- REGISTRO DE ACESSO ---
registrar_acesso("Cursos Online - Galeria Caverna")

# 2. CONFIGURAÇÃO DA PÁGINA
st.title("🎓 Meus Cursos Online")
st.write("Saia da caverna e domine o mundo dos dados com treinamentos práticos.")

# --- BOTÕES DE CONTATO (Conforme solicitado) ---
col_ct1, col_ct2 = st.columns(2)
with col_ct1:
    # WhatsApp com mensagem personalizada
    zap_msg = "Olá Rodrigo! Gostaria de saber mais sobre os seus treinamentos de SQL, Power BI e Excel."
    zap_url = f"https://wa.me/5511977019335?text={zap_msg.replace(' ', '%20')}"
    st.link_button("💬 Falar com Rodrigo no WhatsApp", zap_url)

with col_ct2:
    # Link do Calendário
    st.link_button("📅 Agendar Reunião / Consultoria", "https://calendly.com/rodrigoaiosa")

st.write("") # Espaçador visual

# FUNÇÃO PARA LOCALIZAR IMAGEM COM SEGURANÇA
def get_image_path(filename):
    # Procura na pasta assets que está na raiz do projeto
    path = os.path.join(BASE_DIR, "assets", filename)
    if not os.path.exists(path):
        # Fallback caso a estrutura seja diferente
        path = os.path.join(os.path.dirname(__file__), "assets", filename)
    return path

# --- CURSO 1: POWER BI ---
col1, col2 = st.columns([1, 2], gap="large")
with col1:
    img_pbi = get_image_path("image_9dcf03.jpg")
    try:
        st.image(img_pbi, use_container_width=True)
    except:
        st.warning(f"Imagem {img_pbi} não encontrada.")

with col2:
    st.header("Fundamento Power BI")
    st.subheader("Venha para a luz dos dados!")
    st.write("Aprenda do zero a criar análises visuais e estratégicas. O primeiro passo para decisões inteligentes.")
    st.link_button("Saiba mais sobre Power BI", "https://pay.kiwify.com.br/DFeDsQV")

st.write("") # Espaçador visual

# --- CURSO 2: SQL ---
col3, col4 = st.columns([1, 2], gap="large")
with col3:
    img_sql = get_image_path("image_9dcf21.jpg")
    try:
        st.image(img_sql, use_container_width=True)
    except:
        st.warning(f"Imagem {img_sql} não encontrada.")

with col4:
    st.header("SQL Fundamentos")
    st.subheader("Conhecimento com SQL")
    st.write("Saia da ignorância e domine a linguagem essencial dos dados. Quer analisar? Aprenda SQL.")
    st.link_button("Saiba mais sobre SQL", "https://pay.kiwify.com.br/ivdojL8")

st.write("") # Espaçador visual

# --- CURSO 3: EXCEL ---
col5, col6 = st.columns([1, 2], gap="large")
with col5:
    img_excel = get_image_path("image_9dcf3a.jpg")
    try:
        st.image(img_excel, use_container_width=True)
    except:
        st.warning(f"Imagem {img_excel} não encontrada.")

with col6:
    st.header("Excel Essencial Para Negócios")
    st.subheader("Veja além das sombras!")
    st.write("Treinamento prático e aplicado. Conquiste vantagem real e imediata na sua carreira.")
    st.link_button("Saiba mais sobre Excel", "https://pay.kiwify.com.br/EEb9ADQ")

# Rodapé
exibir_rodape()
