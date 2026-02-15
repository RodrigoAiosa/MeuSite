import streamlit as st
import os
import sys

# 1. RESOLVENDO O CAMINHO DO MÓDULO UTILS E ASSETS (CAMINHO ABSOLUTO)
# Pega o diretório onde este arquivo (cursos_online.py) está
current_dir = os.path.dirname(os.path.abspath(__file__))
# Sobe um nível para chegar na raiz do projeto
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
# Define o caminho da pasta assets
assets_dir = os.path.join(root_dir, "assets")

if root_dir not in sys.path:
    sys.path.append(root_dir)

try:
    from utils import exibir_rodape, registrar_acesso 
except ImportError:
    st.error("Erro: O arquivo 'utils.py' não foi encontrado na pasta raiz.")

# --- REGISTRO DE ACESSO ---
registrar_acesso("Cursos Online")

# 2. CONFIGURAÇÃO VISUAL DA PÁGINA
st.title("🎓 Meus Cursos Online")
st.write("Aprimore suas habilidades com treinamentos práticos e focados no mercado.")

# --- CURSO 1: FUNDAMENTO POWER BI ---
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    img_pbi_path = os.path.join(assets_dir, "image_9dcf03.jpg")
    if os.path.exists(img_pbi_path):
        st.image(img_pbi_path, use_container_width=True)
    else:
        st.error(f"Arquivo não encontrado: {img_pbi_path}")

with col2:
    st.header("Fundamento Power BI")
    st.write(
        """
        Se entender dados é essencial e o Power BI é a ferramenta ideal para isso, 
        então dominar o Power BI é fundamental. No treinamento **Fundamento Power BI**, 
        você aprende do zero a criar análises visuais, importar, transformar e relacionar 
        dados de forma lógica e estratégica.
        """
    )
    st.link_button("Saiba mais sobre o curso", "https://pay.kiwify.com.br/DFeDsQV")
    
    # WhatsApp Personalizado PBI
    url_pbi = "https://wa.me/5511977019335?text=Olá%20Rodrigo!%20Quero%20sair%20da%20caverna%20com%20o%20Power%20BI."
    st.link_button("💬 Dúvidas no WhatsApp", url_pbi)

st.write("") # Espaçador simples

# --- CURSO 2: SQL FUNDAMENTOS ---
col3, col4 = st.columns([1, 2], gap="large")

with col3:
    img_sql_path = os.path.join(assets_dir, "image_9dcf21.jpg")
    if os.path.exists(img_sql_path):
        st.image(img_sql_path, use_container_width=True)
    else:
        st.error(f"Arquivo não encontrado: {img_sql_path}")

with col4:
    st.header("SQL Fundamentos")
    st.write(
        """
        Se dados são essenciais para decisões e SQL é a linguagem dos dados, 
        então dominar SQL é essencial para decisões inteligentes. No curso **Fundamentos SQL**, 
        you aprende desde o básico até consultas avançadas.
        """
    )
    st.link_button("Saiba mais sobre o curso", "https://pay.kiwify.com.br/ivdojL8")
    
    # WhatsApp Personalizado SQL
    url_sql = "https://wa.me/5511977019335?text=Olá%20Rodrigo!%20Quero%20dominar%20o%20SQL%20e%20sair%20da%20caverna."
    st.link_button("💬 Dúvidas no WhatsApp", url_sql)

st.write("") # Espaçador simples

# --- CURSO 3: EXCEL ESSENCIAL PARA NEGÓCIOS ---
col5, col6 = st.columns([1, 2], gap="large")

with col5:
    img_excel_path = os.path.join(assets_dir, "image_9dcf3a.jpg")
    if os.path.exists(img_excel_path):
        st.image(img_excel_path, use_container_width=True)
    else:
        st.error(f"Arquivo não encontrado: {img_excel_path}")

with col6:
    st.header("Excel Essencial Para Negócios")
    st.write(
        """
        Todo profissional que domina Excel se destaca no mercado. 
        Meu treinamento ensina **Excel de forma prática e aplicada**, única no mercado.
        """
    )
    st.link_button("Saiba mais sobre o curso", "https://pay.kiwify.com.br/EEb9ADQ")
    
    # WhatsApp Personalizado Excel
    url_exc = "https://wa.me/5511977019335?text=Olá%20Rodrigo!%20Quero%20ver%20além%20das%20sombras%20com%20o%20Excel."
    st.link_button("💬 Dúvidas no WhatsApp", url_exc)

exibir_rodape()
