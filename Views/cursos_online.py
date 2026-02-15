import streamlit as st
import os
import sys
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO REMOVIDO PARA NÃO SUJAR A PLANILHA ---
registrar_acesso("Cursos Online")

# 1. RESOLVENDO O CAMINHO DO MÓDULO UTILS
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    # Importação atualizada para incluir registrar_acesso
    from utils import exibir_rodape, registrar_acesso 
except ImportError:
    st.error("Erro: O arquivo 'utils.py' não foi encontrado na pasta raiz.")

# --- REGISTRO DE ACESSO ---
# Esta chamada envia os dados para a planilha via utils.py
registrar_acesso("Cursos Online")

# 2. CONFIGURAÇÃO VISUAL DA PÁGINA
st.title("🎓 Meus Cursos Online")
st.write("Aprimore suas habilidades com treinamentos práticos e focados no mercado.")
st.markdown("---")

# --- CURSO 1: FUNDAMENTO POWER BI ---
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    img_pbi = os.path.join("assets", "fundamentos_power_bi.png")
    # Atualizado para width='stretch' conforme as novas diretrizes do Streamlit
    st.image(img_pbi, width="stretch")

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

st.markdown("---")

# --- CURSO 2: SQL FUNDAMENTOS ---
col3, col4 = st.columns([1, 2], gap="large")

with col3:
    img_sql = os.path.join("assets", "SQL_Fundamentos.png")
    st.image(img_sql, width="stretch")

with col4:
    st.header("SQL Fundamentos")
    st.write(
        """
        Se dados são essenciais para decisões e SQL é a linguagem dos dados, 
        então dominar SQL é essencial para decisões inteligentes. No curso **Fundamentos SQL**, 
        you aprende desde o básico até consultas avançadas, com foco prático e direto ao ponto. 
        Ideal para quem quer entender, manipular e extrair valor real de bases de dados. 
        Lógica simples: quer analisar? Aprenda SQL.
        """
    )
    st.link_button("Saiba mais sobre o curso", "https://pay.kiwify.com.br/ivdojL8")

st.markdown("---")

# --- CURSO 3: EXCEL ESSENCIAL PARA NEGÓCIOS ---
col5, col6 = st.columns([1, 2], gap="large")

with col5:
    img_excel = os.path.join("assets", "excel_para_negocios.png")
    st.image(img_excel, width="stretch")

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

st.markdown("---")

# 3. EXIBIÇÃO DO RODAPÉ

exibir_rodape()
