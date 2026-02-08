import streamlit as st

# --- ESTILO CSS PARA CARDS E BOTÃO CENTRALIZADO ---
st.markdown(
    """
    <style>
    .train-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 180, 216, 0.2);
        border-radius: 20px;
        padding: 35px;
        height: 320px;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin-bottom: 25px;
    }

    .train-card:hover {
        transform: scale(1.05);
        background: rgba(0, 180, 216, 0.08);
        border-color: #00b4d8;
        box-shadow: 0 15px 40px rgba(0, 180, 216, 0.2);
    }

    .train-icon { font-size: 55px; margin-bottom: 15px; }
    
    .train-title { 
        color: #00b4d8; 
        font-size: 1.4rem; 
        font-weight: bold; 
        margin-bottom: 15px;
    }

    .train-text { 
        color: #9ca3af; 
        font-size: 1.1rem; 
        line-height: 1.5;
    }

    /* Centralização do Botão WhatsApp */
    .cta-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin-top: 50px;
        padding-bottom: 50px;
    }

    .btn-whatsapp {
        background-color: #25d366;
        color: white !important;
        padding: 18px 45px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        font-size: 1.2rem;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(37, 211, 102, 0.3);
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .btn-whatsapp:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(37, 211, 102, 0.5);
        background-color: #20ba5a;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- CABEÇALHO ---
st.markdown("<h1 style='text-align: center; font-size: 3.2rem;'>Treinamento Corporativo Personalizado 🎓</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af; font-size: 1.3rem; max-width: 900px; margin: auto;'>Capacite seus colaboradores com treinamentos práticos e voltados para resultados reais.</p>", unsafe_allow_html=True)
st.write("")
st.write("")

# --- GRID DE BENEFÍCIOS ---
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.markdown("""
        <div class="train-card">
            <div class="train-icon">🚀</div>
            <div class="train-title">Aumente a Produtividade</div>
            <div class="train-text">Otimize o tempo da equipe com automações que eliminam tarefas repetitivas e manuais.</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="train-card">
            <div class="train-icon">🎯</div>
            <div class="train-title">Reduza Erros Operacionais</div>
            <div class="train-text">Garanta a integridade dos dados e processos através de metodologias de conferência eficientes.</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="train-card">
            <div class="train-icon">🛠️</div>
            <div class="train-title">100% Aplicável</div>
            <div class="train-text">Treinamentos focados nos problemas reais da sua empresa para aplicação imediata.</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="train-card">
            <div class="train-icon">📊</div>
            <div class="train-title">Acompanhamento de Evolução</div>
            <div class="train-text">Métricas claras de desempenho para medir o crescimento técnico da sua equipe.</div>
        </div>
    """, unsafe_allow_html=True)

# --- CONFIGURAÇÃO DA MENSAGEM DO WHATSAPP ---
telefone = "5511977019335"
mensagem = (
    "Olá,\n\n"
    "Vejo que deseja maiores informações sobre nosso treinamento, por gentileza, enviar os seguintes dados:\n\n"
    "CNPJ:\n"
    "Razão Social:\n"
    "e-mail:\n\n"
    "Entrarei em contato em seguida."
)

# Encode da mensagem para URL
import urllib.parse
mensagem_url = urllib.parse.quote(mensagem)
link_whatsapp = f"https://wa.me/{telefone}?text={mensagem_url}"

# --- BOTÃO CENTRALIZADO ---
st.markdown(f"""
    <div class="cta-container">
        <a href="{link_whatsapp}" target="_blank" class="btn-whatsapp">
            💬 Fale conosco via WhatsApp
        </a>
    </div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #6b7280; font-size: 1rem;'>Rodrigo Aiosa © 2026 | Especialista em BI & Treinamentos</p>", unsafe_allow_html=True)