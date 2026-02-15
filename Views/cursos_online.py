import streamlit as st
import os
import sys

# 1. CONFIGURAÇÃO DA PÁGINA (Deve ser o primeiro comando Streamlit)
st.set_page_config(page_title="Cursos Online | Rodrigo Aiosa", page_icon="🎓", layout="wide")

# Resolvendo caminho do módulo utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from utils import exibir_rodape, registrar_acesso
except ImportError:
    st.error("Erro: O arquivo 'utils.py' não foi encontrado.")

# Registro de acesso
registrar_acesso("Página de Cursos")

# 2. ESTILIZAÇÃO CUSTOMIZADA (CSS) - O segredo do UX/UI
st.markdown("""
    <style>
    /* Estilização dos botões para maior conversão */
    div.stButton > button:first-child {
        background-color: #FF8C00;
        color: white;
        border-radius: 8px;
        padding: 0.6rem 2rem;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: #e67e00;
        transform: scale(1.05);
    }
    
    /* Títulos e Subtítulos */
    .main-title {
        font-size: 3rem !important;
        font-weight: 800;
        color: #1E3A8A;
        margin-bottom: 0;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #4B5563;
        margin-bottom: 2rem;
    }
    .highlight {
        color: #1E3A8A;
        font-weight: bold;
    }
    
    /* Card de Curso */
    .course-card {
        background-color: #F3F4F6;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #1E3A8A;
    }
    </style>
""", unsafe_allow_stdio=False)

# 3. HERO SECTION (Psicologia: Foco no Resultado)
st.markdown('<p class="main-title">Acelere sua Carreira com Dados</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Treinamentos práticos para quem não tem tempo a perder e busca o topo do mercado.</p>', unsafe_allow_html=True)

# 4. BOTÕES DE CONTATO RÁPIDO (Gatilho de Confiança)
col_c1, col_c2, _ = st.columns([1, 1, 2])
with col_c1:
    # Mensagem personalizada conforme solicitado
    msg_wa = "Olá Rodrigo! Vi seus cursos no site e gostaria de tirar algumas dúvidas sobre qual o melhor para meu momento profissional."
    link_wa = f"https://wa.me/5511977019335?text={msg_wa.replace(' ', '%20')}"
    st.link_button("💬 Falar com Especialista", link_wa, use_container_width=True)
with col_c2:
    st.link_button("📅 Agendar Reunião", "https://calendly.com/rodrigoaiosa", use_container_width=True)

st.write("") # Espaçador

# --- LISTAGEM DE CURSOS ---

def render_curso(titulo, descricao, imagem, link, preco_destaque=""):
    st.markdown(f"### {titulo}")
    col_img, col_txt = st.columns([1, 2], gap="large")
    
    with col_img:
        img_path = os.path.join("assets", imagem)
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        else:
            st.warning(f"Imagem {imagem} não encontrada.")
            
    with col_txt:
        st.markdown(f"""
        <div class="course-card">
            {descricao}
            <br><br>
            <span style="color: #1E3A8A; font-weight: bold; font-size: 1.1rem;">🚀 Invista no seu futuro hoje.</span>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.link_button(f"👉 Quero me inscrever no {titulo}", link)

# --- CURSO 1: POWER BI ---
render_curso(
    "Fundamento Power BI",
    "Transforme dados brutos em <b>dashboards estratégicos</b>. Aprenda a pensar como um analista e domine a ferramenta líder do mercado. Ideal para quem quer sair do 'acho' para o 'tenho certeza'.",
    "fundamentos_power_bi.png",
    "https://pay.kiwify.com.br/DFeDsQV"
)

st.divider()

# --- CURSO 2: SQL ---
render_curso(
    "SQL Fundamentos",
    "A linguagem universal dos dados. Pare de depender de planilhas lentas e aprenda a <b>extrair inteligência diretamente da fonte</b>. O curso vai do zero absoluto até consultas complexas de forma lógica.",
    "SQL_Fundamentos.png",
    "https://pay.kiwify.com.br/ivdojL8"
)

st.divider()

# --- CURSO 3: EXCEL ---
render_curso(
    "Excel Essencial Para Negócios",
    "Não é apenas sobre fórmulas, é sobre <b>solução de problemas</b>. Domine as funções que as empresas realmente usam e ganhe horas de produtividade no seu dia a dia profissional.",
    "excel_para_negocios.png",
    "https://pay.kiwify.com.br/EEb9ADQ"
)

# 5. RODAPÉ FINAL
st.write("")
exibir_rodape()
