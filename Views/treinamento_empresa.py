import streamlit as st
import urllib.parse
from utils import exibir_rodape, registrar_acesso  # Importação atualizada

# --- REGISTRO DE ACESSO ---
# Registra que o usuário está visualizando a página de Treinamento Corporativo
registrar_acesso("Treinamento Corporativo")

# --- ESTILO CSS (TEXTOS MAIORES E EFEITOS) ---
st.markdown(
    """
    <style>
    /* Manifesto de Aristóteles */
    .manifesto-container {
        max-width: 900px;
        margin: auto;
        text-align: justify;
        background: rgba(0, 180, 216, 0.05);
        padding: 40px;
        border-radius: 20px;
        border: 1px dashed rgba(0, 180, 216, 0.3);
        margin-bottom: 50px;
    }

    .manifesto-title {
        text-align: center;
        color: #00b4d8;
        font-size: 2.2rem;
        margin-bottom: 25px;
        font-weight: bold;
    }

    .manifesto-text {
        font-size: 1.25rem;
        color: #e5e7eb;
        line-height: 1.8;
        margin-bottom: 20px;
    }

    /* Cards de Treinamento */
    .train-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 180, 216, 0.2);
        border-radius: 20px;
        padding: 35px;
        height: 380px;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin-bottom: 30px;
    }

    .train-card:hover {
        transform: scale(1.05);
        background: rgba(0, 180, 216, 0.08);
        border-color: #00b4d8;
        box-shadow: 0 15px 40px rgba(0, 180, 216, 0.2);
    }

    .train-icon { font-size: 65px; margin-bottom: 20px; }
    
    .train-title { 
        color: #00b4d8; 
        font-size: 1.7rem; 
        font-weight: bold; 
        margin-bottom: 15px;
    }

    .train-text { 
        color: #9ca3af; 
        font-size: 1.2rem; 
        line-height: 1.5;
    }

    /* Botão WhatsApp Centralizado */
    .cta-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin-top: 50px;
        padding-bottom: 60px;
    }

    .btn-whatsapp {
        background-color: #25d366;
        color: white !important;
        padding: 22px 55px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        font-size: 1.4rem;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(37, 211, 102, 0.3);
        display: flex;
        align-items: center;
        gap: 12px;
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
st.markdown("<h1 style='text-align: center; font-size: 3.8rem;'>Treinamento Corporativo Personalizado 🎓</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af; font-size: 1.5rem; max-width: 900px; margin: auto;'>Capacite seus colaboradores com treinamentos práticos e voltados para resultados reais.</p>", unsafe_allow_html=True)
st.write("")
st.write("")

# --- MANIFESTO PERSUASIVO (ARISTÓTELES) ---
st.markdown(
    """
    <div class="manifesto-container">
        <h2 class="manifesto-title">A Diferença entre Operar Dados e Gerar Lucro</h2>
        <p class="manifesto-text">
             Com anos de experiência transformando estruturas de dados complexas em decisões estratégicas para grandes players do mercado, meu compromisso não é apenas ensinar ferramentas, mas transmitir a mentalidade de excelência em Business Intelligence que validei na prática.
        </p>
        <p class="manifesto-text">
             Imagine a frustração de uma equipe talentosa presa em planilhas lentas, corrigindo erros manuais que nunca deveriam ter existido, enquanto a concorrência avança com decisões baseadas em dados em tempo real. O custo do "jeito que sempre fizemos" é o esgotamento do seu time e a perda de oportunidades invisíveis.
        </p>
        <p class="manifesto-text">
             Números não mentem: empresas que investem em alfabetização de dados aumentam sua produtividade em até 25% e reduzem custos operacionais drasticamente. Meu treinamento conecta seus relatórios diretamente ao banco de dados com performance otimizada, garantindo que sua equipe foque em análise, e não em digitação.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- GRID DE BENEFÍCIOS ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="train-card">
            <div class="train-icon">🚀</div>
            <div class="train-title">Aumente a Produtividade</div>
            <div class="train-text">Otimize o tempo da equipe com automações que eliminam tarefas repetitivas e manuais.</div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="train-card">
            <div class="train-icon">🛠️</div>
            <div class="train-title">100% Aplicável</div>
            <div class="train-text">Treinamentos focados nos problemas reais da sua empresa para aplicação imediata.</div>
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
    st.markdown("""
        <div class="train-card">
            <div class="train-icon">📊</div>
            <div class="train-title">Acompanhamento de Evolução</div>
            <div class="train-text">Métricas claras de desempenho para medir o crescimento técnico da sua equipe.</div>
        </div>
    """, unsafe_allow_html=True)

# --- CONFIGURAÇÃO DO WHATSAPP ---
telefone = "5511977019335"
mensagem = (
    "Olá,\n\n"
    "Vejo que deseja maiores informações sobre nosso treinamento, por gentileza, enviar os seguintes dados:\n\n"
    "CNPJ:\n"
    "Razão Social:\n"
    "e-mail:\n\n"
    "Entrarei em contato em seguida."
)
mensagem_url = urllib.parse.quote(mensagem)
link_whatsapp = f"https://wa.me/{telefone}?text={mensagem_url}"

# --- BOTÃO FINAL CENTRALIZADO ---
st.markdown(f"""
    <div class="cta-container">
        <a href="{link_whatsapp}" target="_blank" class="btn-whatsapp">
            💬 Fale conosco via WhatsApp
        </a>
    </div>
""", unsafe_allow_html=True)

exibir_rodape()