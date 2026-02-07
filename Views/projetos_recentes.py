import streamlit as st

# --- ESTILO CSS PARA ALINHAMENTO À ESQUERDA E TAMANHO DE 200PX ---
st.markdown(
    """
    <style>
    .project-card {
        display: flex;
        flex-direction: column;
        align-items: flex-start; /* Alinha o conteúdo à esquerda */
        justify-content: flex-start;
        text-align: left;
        margin-bottom: 50px;
    }
    .project-image {
        border-radius: 12px;
        transition: transform 0.3s, box-shadow 0.3s;
        cursor: pointer;
        border: 2px solid rgba(0, 180, 216, 0.3);
        /* Tamanho fixo em 200px */
        width: 200px; 
        height: 200px;
        object-fit: cover;
    }
    .project-image:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 25px rgba(0, 180, 216, 0.5);
    }
    .project-title {
        color: #00b4d8;
        font-weight: bold;
        margin-bottom: 15px;
        margin-top: 10px;
        font-size: 1.2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🚀 Projetos Recentes")
st.write("Clique nos ícones para conferir as demonstrações completas no LinkedIn.")
st.markdown("---")

# --- PROJETO 1: DASHBOARD AUTOMATIZADO ---
st.markdown(
    """
    <div class="project-card">
        <h2 class="project-title">🏛️ O FIM DA ERA DO TRABALHO MANUAL: SEU DASHBOARD PRONTO EM UM CLIQUE</h2>
        <a href="https://www.linkedin.com/feed/update/urn:li:activity:7425547898580328449" target="_blank">
            <img src="https://media.licdn.com/dms/image/v2/D5605AQEZjyr3_u48-w/feedshare-thumbnail_720_1280/B56ZwzYaHOK4A4-/0/1770388562694?e=1771030800&v=beta&t=ylHtVPZgzEbyzEqvBv0v9-hHF0x4ZEpn-k8ktPDilXg" 
                 class="project-image" 
                 alt="Dashboard Automatizado">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- PROJETO 2: SISTEMAS DE AMORTIZAÇÃO ---
st.markdown(
    """
    <div class="project-card">
        <h2 class="project-title">📊 Análise Pro: Sistemas de Amortização</h2>
        <a href="https://www.linkedin.com/feed/update/urn:li:activity:7425612242248835073/" target="_blank">
            <img src="https://media.licdn.com/dms/image/v2/D5622AQF74taisme4XA/feedshare-shrink_480/B56Zw0S_FZHIAs-/0/1770403918426?e=1772064000&v=beta&t=eqFjQKekX8rYQATeRIhy2uruedxVjRL29Oo7Xt97Ogw" 
                 class="project-image" 
                 alt="Análise de Amortização">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- PROJETO 3: CIÊNCIA DE PROSPECÇÃO ---
st.markdown(
    """
    <div class="project-card">
        <h2 class="project-title">📍O fim das listas de leads obsoletas: A ciência por trás da prospecção de alta performance</h2>
        <a href="https://www.linkedin.com/feed/update/urn:li:activity:7425188593134026752" target="_blank">
            <img src="https://media.licdn.com/dms/image/v2/D5605AQEYmI4B2ByfGw/feedshare-thumbnail_720_1280/B56ZwuRowKK8A4-/0/1770302901551?e=1771030800&v=beta&t=DxCLIdRDCnXLMcadvJwW6zhWXMXZl6PoIm-PzzZM0fY" 
                 class="project-image" 
                 alt="Prospecção de Alta Performance">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- PROJETO 4: VISÃO COMPUTACIONAL ---
st.markdown(
    """
    <div class="project-card">
        <h2 class="project-title">🚗 Contagem de veículos em tempo real: um projeto prático de visão computacional com Python</h2>
        <a href="https://www.linkedin.com/feed/update/urn:li:activity:7422736985196371969" target="_blank">
            <img src="https://media.licdn.com/dms/image/v2/D5605AQHKj124qT0VeA/feedshare-thumbnail_720_1280/B56ZwLb66MIUA8-/0/1769718394777?e=1771030800&v=beta&t=Ytd5H0Ctowz9PYkim4wpahKxudojH9-kkiY5HLmd_2s" 
                 class="project-image" 
                 alt="Contagem de Veículos">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- PROJETO 5: JOGO IA ---
st.markdown(
    """
    <div class="project-card">
        <h2 class="project-title">💡Pedra; Papel; Tesoura com IA</h2>
        <a href="https://www.linkedin.com/feed/update/urn:li:activity:7422420309632303104" target="_blank">
            <img src="https://media.licdn.com/dms/image/v2/D5605AQEnOdzL023RyA/feedshare-thumbnail_720_1280/B56ZwG76crJoA4-/0/1769642895486?e=1771030800&v=beta&t=lA5YIEjUivMZFCCnFPOY6CG3Iinb6N6GFD0nXls-UzI" 
                 class="project-image" 
                 alt="Pedra Papel Tesoura IA">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- PROJETO 6: IA COMO PAI ---
st.markdown(
    """
    <div class="project-card">
        <h2 class="project-title">❤️ O dia em que a IA me ajudou como PAI</h2>
        <a href="https://www.linkedin.com/feed/update/urn:li:activity:7420842332155142144" target="_blank">
            <img src="https://media.licdn.com/dms/image/v2/D5605AQGGIbt2tD1Weg/feedshare-thumbnail_720_1280/B56ZvEub9nHAA4-/0/1768532066431?e=1771030800&v=beta&t=Cr22rY2M1p6TEYvf7fC36OJ-oaRFkCtBXEvcijBX450" 
                 class="project-image" 
                 alt="IA como Pai">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)