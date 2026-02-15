import streamlit as st
import os
import sys
from utils import exibir_rodape, registrar_acesso

# 1. RESOLVENDO O CAMINHO DO MÓDULO UTILS
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from utils import exibir_rodape, registrar_acesso 
except ImportError:
    st.error("Erro: O arquivo 'utils.py' não foi encontrado na pasta raiz.")

# --- REGISTRO DE ACESSO ---
registrar_acesso("Cursos Online - Galeria Caverna")

# 2. CONFIGURAÇÃO VISUAL DA PÁGINA
st.set_page_config(page_title="Meus Cursos - Rodrigo Aiosa", layout="wide")

st.title("🎓 Meus Cursos Online")
st.write("Aprimore suas habilidades com treinamentos práticos e saia da 'caverna' da obscuridade de dados.")

# --- SEÇÃO DE CONTATO RÁPIDO ---
col_cat1, col_cat2 = st.columns(2)
with col_cat1:
    # Link do WhatsApp com mensagem personalizada conforme solicitado
    whatsapp_url = "https://wa.me/5511977019335?text=Olá%20Rodrigo!%20Gostaria%20de%20saber%20mais%20sobre%20seus%20treinamentos%20de%20dados."
    st.link_button("💬 Falar com Rodrigo no WhatsApp", whatsapp_url)
with col_cat2:
    # Link do Calendário conforme solicitado
    st.link_button("📅 Agendar Reunião / Consultoria", "https://calendly.com/rodrigoaiosa")

st.write("") # Espaçador

# --- CURSO 1: FUNDAMENTO POWER BI ---
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    # Usando a nova imagem da caverna (ajuste o nome do arquivo se necessário)
    img_pbi = os.path.join("assets", "image_9dcf03.jpg") 
    st.image(img_pbi, use_container_width=True)

with col2:
    st.header("Fundamento Power BI")
    st.subheader("Venha para a luz dos dados!")
    st.write(
        """
        Se entender dados é essencial e o Power BI é a ferramenta ideal para isso, 
        então dominar o Power BI é fundamental. No treinamento **Fundamento Power BI**, 
        você aprende do zero a criar análises visuais, importar, transformar e relacionar 
        dados de forma lógica e estratégica. Se você busca decisões mais inteligentes, 
        esse é o primeiro passo.
        """
    )
    # Link específico para compra/saiba mais
    st.link_button("Quero sair da caverna com Power BI", "https://pay.kiwify.com.br/DFeDsQV")

# --- CURSO 2: SQL FUNDAMENTOS ---
col3, col4 = st.columns([1, 2], gap="large")

with col3:
    # Usando a nova imagem do conhecimento com SQL
    img_sql = os.path.join("assets", "image_9dcf21.jpg")
    st.image(img_sql, use_container_width=True)

with col4:
    st.header("SQL Fundamentos")
    st.subheader("Do silêncio da ignorância ao poder do SQL")
    st.write(
        """
        Se dados são essenciais para decisões e SQL é a linguagem dos dados, 
        então dominar SQL é essencial para decisões inteligentes. No curso **Fundamentos SQL**, 
        você aprende desde o básico até consultas avançadas, com foco prático e direto ao ponto. 
        Ideal para quem quer entender, manipular e extrair valor real de bases de dados. 
        Lógica simples: quer analisar? Aprenda SQL.
        """
    )
    st.link_button("Dominar o SQL agora", "https://pay.kiwify.com.br/ivdojL8")

# --- CURSO 3: EXCEL ESSENCIAL PARA NEGÓCIOS ---
col5, col6 = st.columns([1, 2], gap="large")

with col5:
    # Usando a nova imagem do Excel além das sombras
    img_excel = os.path.join("assets", "image_9dcf3a.jpg")
    st.image(img_excel, use_container_width=True)

with col6:
    st.header("Excel Essencial Para Negócios")
    st.subheader("Veja além das sombras!")
    st.write(
        """
        Todo profissional que domina Excel se destaca no mercado. 
        Meu treinamento ensina **Excel de forma prática e aplicada**, única no mercado. 
        Logo, quem faz meu treinamento conquista vantagem real e imediata na carreira.
        """
    )
    st.link_button("Ver a luz com Excel", "https://pay.kiwify.com.br/EEb9ADQ")

# Rodapé padrão
exibir_rodape()
