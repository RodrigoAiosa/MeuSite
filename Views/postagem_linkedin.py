import streamlit as st
from utils import exibir_rodape, registrar_acesso

# -----------------------------
# REGISTRO DE ACESSO
# -----------------------------

st.set_page_config(layout="wide")

# -----------------------------
# CSS CORPORATIVO
# -----------------------------
st.markdown("""
<style>

/* Fundo geral */
.main {
    background-color: #0f172a;
}

/* Título principal */
.page-title {
    text-align: center;
    font-size: 2.8rem;
    font-weight: bold;
    margin-bottom: 10px;
    color: white;
}

/* Subtítulo */
.page-subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 40px;
}

/* Card de postagem */
.linkedin-card {
    background-color: #111827;
    padding: 25px;
    border-radius: 18px;
    border-left: 6px solid #00b4d8;
    margin-bottom: 30px;
    transition: all 0.3s ease;
}

.linkedin-card:hover {
    background-color: #1a2233;
    transform: translateY(-5px);
}

/* Título do card */
.post-title {
    font-size: 1.2rem;
    font-weight: bold;
    color: #00b4d8;
    margin-bottom: 15px;
}

/* Ajuste iframe */
iframe {
    width: 100% !important;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("<div class='page-title'>🚀 Insights & Estratégia no LinkedIn</div>", unsafe_allow_html=True)
st.markdown("<div class='page-subtitle'>Conteúdos sobre Dados, BI, Automação e Gestão Estratégica</div>", unsafe_allow_html=True)

st.write("")

# -----------------------------
# LISTA DE POSTAGENS
# -----------------------------
postagens = [
    {
        "titulo": "📊 A importância da precificação correta para MEIs",
        "embed": """
        <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:7427415116943597568?collapsed=1"
        height="497"
        frameborder="0"
        allowfullscreen=""
        title="Publicação incorporada">
        </iframe>
        """
    },
    # Adicione novas postagens aqui
]

# -----------------------------
# RENDERIZAÇÃO
# -----------------------------
for post in postagens:
    st.markdown(f"""
        <div class="linkedin-card">
            <div class="post-title">{post['titulo']}</div>
            {post['embed']}
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

exibir_rodape()
