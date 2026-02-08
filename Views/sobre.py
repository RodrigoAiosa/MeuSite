import streamlit as st
import time
from utils import exibir_rodape

st.set_page_config(layout="wide", page_title="Portfolio | Rodrigo Aiosa")

# --- ESTILO CSS GLOBAL (INCLUINDO EFEITO FLIP) ---
st.markdown(
    """
    <style>
    .profile-pic {
        display: flex;
        justify-content: center;
        margin-top: -30px;
    }

    .profile-pic img {
        border-radius: 50%;
        width: 200px;
        height: 200px;
        object-fit: cover;
        border: 5px solid #00b4d8;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }

    .main-title {
        text-align: center;
        margin-top: 10px;
    }

    /* EFEITO FLIP CARD */
    .flip-card {
        background-color: transparent;
        width: 100%;
        height: 180px;
        perspective: 1000px;
        margin-bottom: 20px;
    }

    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.6s;
        transform-style: preserve-3d;
        cursor: pointer;
    }

    .flip-card:hover .flip-card-inner {
        transform: rotateY(180deg);
    }

    .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        -webkit-backface-visibility: hidden;
        backface-visibility: hidden;
        border-radius: 18px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 20px;
        border: 1px solid #1f2937;
    }

    .flip-card-front {
        background-color: #111827;
        color: white;
    }

    .flip-card-back {
        background-color: #00b4d8;
        color: #111827;
        transform: rotateY(180deg);
        font-weight: bold;
        font-size: 16px;
        line-height: 1.4;
    }

    .card-icon { font-size:28px; margin-bottom:5px; }
    .card-number { font-size:26px; font-weight:bold; color:#00b4d8; }
    .card-title { font-size:14px; color:#9ca3af; }

    /* TEXTO CENTRALIZADO */
    .centered-text {
        text-align: center;
        max-width: 900px;
        margin: 0 auto;
        font-size: 1.1em;
        color: #9ca3af;
    }

    /* SOCIAL ICONS */
    .social-icons {
        display: flex;
        justify-content: center;
        gap: 25px;
        margin-top: 20px;
    }
    .social-icons img {
        width: 42px;
        transition: transform 0.3s ease;
        border-radius: 8px;
    }
    .social-icons img:hover { 
        transform: scale(1.3) translateY(-5px); 
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- CABEÇALHO ---
st.markdown(
    '<div class="profile-pic">'
    '<img src="https://media.licdn.com/dms/image/v2/D5603AQH-2rDkpd-OxA/profile-displayphoto-scale_200_200/B56ZmxqxTBKMAY-/0/1759622405960?e=1772064000&v=beta&t=_6-zEhPhGUF9GQwDJ-7OZ0DtlWLD4AJBwI5kPsz-X6U">'
    '</div>',
    unsafe_allow_html=True
)

st.markdown('<h1 class="main-title">Rodrigo Aiosa</h1>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; font-size: 1.2em; color: #00b4d8; font-weight: bold;">Python | Excel | Power BI | ETL | SQL SERVER | Linguagem M | DAX</div>', unsafe_allow_html=True)

st.write("")

# --- CARDS COM CONTADOR ANIMADO E FLIP ---
st.markdown("### ⭐ Experiência e Resultados")

c1, c2, c3, c4 = st.columns(4)

# Placeholders para a animação
p1 = c1.empty()
p2 = c2.empty()
p3 = c3.empty()
p4 = c4.empty()

# Frases do verso (Habilidades destacadas)
back_texts = [
    "Expertise em automação de processos e análise preditiva.",
    "Soluções personalizadas para grandes players do mercado.",
    "Dashboards estratégicos focados em KPIs de alto nível.",
    "Parceria contínua baseada em confiança e resultados reais."
]

# Loop da animação de carregamento
for i in range(0, 101, 5):
    val_exp = int(20 * i / 100)
    val_emp = int(450 * i / 100)
    val_proj = int(500 * i / 100)
    val_rec = int(87 * i / 100)

    # Dados dos cards (Frente e Verso)
    cards_data = [
        (f"{val_exp}+", "Anos de experiência", "🏆", back_texts[0], p1),
        (f"{val_emp}+", "Empresas atendidas", "🏢", back_texts[1], p2),
        (f"{val_proj}+", "Projetos entregues", "📊", back_texts[2], p3),
        (f"{val_rec}%", "Recompra de clientes", "🤝", back_texts[3], p4)
    ]

    for val, title, icon, back, placeholder in cards_data:
        placeholder.markdown(f"""
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <div class="card-icon">{icon}</div>
                    <div class="card-number">{val}</div>
                    <div class="card-title">{title}</div>
                </div>
                <div class="flip-card-back">
                    {back}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    time.sleep(0.03)

st.markdown("---")

# --- EXPERIÊNCIA DE MERCADO ---
st.subheader("🤝 Experiência de Mercado")
st.write("Especialista em Análise de Dados e Business Intelligence, transformando dados brutos em decisões inteligentes.")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🔎 Análise Avançada e Automação")
    st.write("Desenvolvimento de scripts Python e modelos em Excel para otimização de tempo.")
    st.markdown("### 📊 Business Intelligence (BI)")
    st.write("Criação de ecossistemas de dados com Power BI, DAX e M.")
with col2:
    st.markdown("### 🗄️ Gerenciamento de Dados")
    st.write("Estruturação de bancos de dados SQL Server e fluxos de ETL eficientes.")
    st.markdown("### 🎯 Minha Abordagem")
    st.write("Foco total na dor do cliente e na geração de valor imediato.")

st.write("")

# --- SEÇÃO DE CLIENTES CENTRALIZADA ---
st.markdown(
    """
    <div class="centered-text">
        <p><strong>Clientes em Destaque:</strong></p>
        <p>Cimed, Unimed Seguros, Ouro Safra, Kraft Heinz, Loggi, Usina Santa Terezinha, Megavig, Lowell e BSS Blindagens.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.write("")

# Centralização da imagem de clientes
col_img1, col_img2, col_img3 = st.columns([1, 8, 1])
with col_img2:
    st.image("assets/clientes_atendidos.jpg", use_container_width=True)

st.markdown("---")

exibir_rodape()