import streamlit as st
import os
import sys

# 1. RESOLVENDO O CAMINHO DO MÓDULO UTILS
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
    # Atualizado com a imagem da caverna PBI
    img_pbi = os.path.join("assets", "image_9dcf03.jpg")
    st.image(img_pbi, use_container_width=True)

with col2:
    st.header("Fundamento Power BI")
    st.write(
        """
        Se entender dados é essencial e o Power BI é a ferramenta ideal para isso, 
        então dominar o Power BI é fundamental. No treinamento **Fundamento Power BI**, 
        você aprende do zero a criar análises visuais, importar, transformar e relacionar 
        dados de forma lógica e estratégica. Se você busca decisões mais inteligentes, 
        esse é o primeiro passo.
        """
    )
    st.link_button("Saiba mais sobre o curso", "https://pay.kiwify.com.br/DFeDsQV")
    
    # WhatsApp Personalizado para PBI
    pbi_msg = "Olá Rodrigo! Gostaria de tirar dúvidas sobre o curso de Power BI."
    pbi_url = f"https://wa.me/5511977019335?text={pbi_msg.replace(' ', '%20')}"
    st.link_button("💬 Dúvidas no WhatsApp", pbi_url)

# --- CURSO 2: SQL FUNDAMENTOS ---
col3, col4 = st.columns([1, 2], gap="large")

with col3:
    # Atualizado com a imagem da caverna SQL
    img_sql = os.path.join("assets", "image_9dcf21.jpg")
    st.image(img_sql, use_container_width=True)

with col4:
    st.header("SQL Fundamentos")
    st.write(
        """
        Se dados são essenciais para decisões e SQL é a linguagem dos dados, 
        então dominar SQL é essencial para decisões inteligentes. No curso **Fundamentos SQL**, 
        você aprende desde o básico até consultas avançadas, com foco prático e direto ao ponto. 
        Ideal para quem quer entender, manipular e extrair valor real de bases de dados. 
        Lógica simples: quer analisar? Aprenda SQL.
        """
    )
    st.link_button("Saiba mais sobre o curso", "https://pay.kiwify.com.br/ivdojL8")

    # WhatsApp Personalizado para SQL
    sql_msg = "Olá Rodrigo! Quero saber mais sobre o treinamento de SQL Fundamentos."
    sql_url = f"https://wa.me/5511977019335?text={sql_msg.replace(' ', '%20')}"
    st.link_button("💬 Dúvidas no WhatsApp", sql_url)

# --- CURSO 3: EXCEL ESSENCIAL PARA NEGÓCIOS ---
col5, col6 = st.columns([1, 2], gap="large")

with col5:
    # Atualizado com a imagem da caverna Excel
    img_excel = os.path.join("assets", "image_9dcf3a.jpg")
    st.image(img_excel, use_container_width=True)

with col6:
    st.header("Excel Essencial Para Negócios")
    st.write(
        """
        Todo profissional que domina Excel se destaca no mercado. 
        Meu treinamento ensina **Excel de forma prática e aplicada**, única no mercado. 
        Logo, quem faz meu treinamento conquista vantagem real e imediata na carreira.
        """
    )
    st.link_button("Saiba mais sobre o curso", "https://pay.kiwify.com.br/EEb9ADQ")

    # WhatsApp Personalizado para Excel
    exc_msg = "Olá Rodrigo! Tenho interesse no Excel Essencial para Negócios."
    exc_url = f"https://wa.me/5511977019335?text={exc_msg.replace(' ', '%20')}"
    st.link_button("💬 Dúvidas no WhatsApp", exc_url)

exibir_rodape()
