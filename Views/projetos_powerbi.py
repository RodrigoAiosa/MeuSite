import streamlit as st
from utils import exibir_rodape, registrar_acesso
import urllib.parse

# --- REGISTRO DE ACESSO ---
registrar_acesso("Projetos Power BI")

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Rodrigo Aiosa | BI & Estratégia", layout="wide")

# --- CSS DE ALTO IMPACTO (FIXO NO MARKDOWN) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    /* Grid de Projetos Simétrico */
    [data-testid="column"] { padding: 0 16px !important; }
    .flip-card { width: 100%; height: 400px; perspective: 1000px; margin-bottom: 32px; }
    .flip-card-inner { position: relative; width: 100%; height: 100%; transition: transform 0.6s; transform-style: preserve-3d; border-radius: 20px; }
    .flip-card:hover .flip-card-inner { transform: rotateY(180deg); }
    .flip-card-front, .flip-card-back { position: absolute; width: 100%; height: 100%; backface-visibility: hidden; border-radius: 20px; display: flex; flex-direction: column; justify-content: center; align-items: center; padding: 30px; }
    .flip-card-front { background: #111827; border: 1px solid rgba(255,255,255,0.1); }
    .flip-card-back { background: #1e293b; transform: rotateY(180deg); border: 2px solid #00b4d8; }
    
    /* Botões e Estilos Auxiliares */
    .btn-pbi { background:#00b4d8; color:#111 !important; padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:800; font-size:0.75rem; text-transform:uppercase; }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
""", unsafe_allow_html=True)

# --- SEÇÃO PSICOLÓGICA (ISOLADA PARA NÃO VAZAR CÓDIGO) ---
# Aqui usamos st.write com o HTML direto para evitar que o Streamlit tente "ler" o conteúdo
# A mensagem de WhatsApp agora inclui o link do calendário como solicitado [cite: 2026-02-14]
st.markdown(f"""
<div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); padding: 60px 40px; border-radius: 30px; border: 2px solid #00b4d8; margin-bottom: 50px; text-align: center; box-shadow: 0 25px 50px -12px rgba(0, 180, 216, 0.4);">
    <div style="color: #00b4d8; font-weight: 700; letter-spacing: 2px; margin-bottom: 10px; text-transform: uppercase;">Estratégia & Performance</div>
    <h1 style="font-size: 3rem; font-weight: 900; color: white; line-height: 1.1; margin-bottom: 25px;">Dados sem inteligência são apenas custos.<br>Eu entrego clareza para lucrar.</h1>
    
    <div style="display: flex; gap: 25px; margin: 40px 0; text-align: left; flex-wrap: wrap;">
        <div style="flex: 1; min-width: 280px; padding: 30px; border-radius: 20px; background: rgba(255,255,255,0.03); border-left: 5px solid #ef4444;">
            <h4 style="color:#ef4444; margin-bottom:10px; font-weight:800;">❌ O Custo da Intuição</h4>
            <p style="color:#cbd5e1; font-size:0.95rem; line-height:1.5;">Decisões baseadas no "achismo" geram desperdício financeiro e cegueira sobre a saúde real do seu negócio.</p>
        </div>
        <div style="flex: 1; min-width: 280px; padding: 30px; border-radius: 20px; background: rgba(34, 197, 94, 0.05); border-left: 5px solid #22c55e;">
            <h4 style="color:#22c55e; margin-bottom:10px; font-weight:800;">✅ A Precisão do BI</h4>
            <p style="color:#cbd5e1; font-size:0.95rem; line-height:1.5;">Dashboards estratégicos transformam números em lucro, revelando gargalos que seus olhos não conseguem ver.</p>
        </div>
    </div>
    
    <p style="color:white; font-style:italic; margin-bottom:30px; font-size: 1.1rem;">Se a sua empresa gera dados e você não os usa para decidir, você está deixando dinheiro na mesa.</p>
    <a href="https://api.whatsapp.com/send?phone=5511977019335&text=Olá Rodrigo! 👋 Quero transformar os dados da minha empresa em lucro. Vamos agendar um diagnóstico?" 
       target="_blank" 
       style="background: #00b4d8; color: #111827 !important; padding: 20px 45px; border-radius: 15px; font-weight: 900; font-size: 1.1rem; text-decoration: none; display: inline-block; text-transform: uppercase; box-shadow: 0 10px 20px rgba(0, 180, 216, 0.3);">
       Agendar Diagnóstico Gratuito
    </a>
</div>
""", unsafe_allow_html=True)

# --- DADOS DOS PROJETOS ---
pbi_projects = [
    {"title": "💳 Relatório STONE", "icon": "🏛️", "url": "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Monitoramento de KPIs de faturamento B2B e análise de margem regional."},
    {"title": "📊 Vendas vs Realizado", "icon": "📈", "url": "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Controle absoluto de metas comerciais e performance de equipe em tempo real."},
    {"title": "🏝️ Financeiro Beocean", "icon": "🏖️", "url": "https://app.powerbi.com/view?r=eyJrIjoiY2VkZmU1MDMtNTgwZS00NTJmLWFhOTktYzM0YzMwZDE3OTE4IiwidCI6IjdjNTYzNjMxLTcyZGMtNDY1Ny05MTRkLWIyM2M5ZTI5OGVlMSJ9", "desc": "Gestão hoteleira premium: controle total de fluxo de caixa e lucratividade."},
    {"title": "📦 Controle BNZ", "icon": "📦", "url": "https://app.powerbi.com/view?r=eyJrIjoiODE4YmZkNDItNWQ0OC00YmUyLThiZTktOTlmN2E0NWM3NTljIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Inteligência em suprimentos e redução de perdas em estoque operacional."},
    {"title": "🎯 Dashboard OEE", "icon": "🎯", "url": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Eficiência industrial: monitoramento de disponibilidade e qualidade produtiva."},
    {"title": "👥 Dashboard de RH", "icon": "👥", "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "People Analytics focado em redução de turnover e custos de folha de pagamento."},
    {"title": "🚀 Gestão de Negócios", "icon": "🚀", "url": "https://app.powerbi.com/view?r=eyJrIjoiYzNhNDFkNzEtZmVkNy00ODZkLTgyZDYtMWIzMDQ3YWU2ZjFiIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Visão estratégica 360º para suporte imediato à tomada de decisão do CEO."}
]

# --- RENDERIZAÇÃO DA GRADE ---
with st.container():
    for i in range(0, len(pbi_projects), 3):
        cols = st.columns(3) 
        for j in range(3):
            idx = i + j
            if idx < len(pbi_projects):
                p = pbi_projects[idx]
                wa_msg = f"Olá Rodrigo! 👋\n\nGostaria de falar sobre o projeto: *{p['title']}*"
                wa_link = f"https://api.whatsapp.com/send?phone=5511977019335&text={urllib.parse.quote(wa_msg)}"
                
                with cols[j]:
                    st.markdown(f"""
                    <div class="flip-card">
                        <div class="flip-card-inner">
                            <div class="flip-card-front">
                                <div style="font-size:50px; margin-bottom:15px;">{p['icon']}</div>
                                <div style="font-size:1.3rem; font-weight:700; color:white; text-align:center;">{p['title']}</div>
                                <div style="font-size:0.7rem; color:#00b4d8; margin-top:10px;">VER DETALHES ↻</div>
                            </div>
                            <div class="flip-card-back">
                                <p style="font-size:0.85rem; color:#cbd5e1; margin-bottom:20px; text-align:center;">{p['desc']}</p>
                                <a href="{p['url']}" target="_blank" class="btn-pbi">ABRIR DASHBOARD</a>
                                <div style="margin-top:20px;">
                                    <a href="{wa_link}" target="_blank" style="color:#25d366; font-size:1.5rem;"><i class="fab fa-whatsapp"></i></a>
                                </div>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

exibir_rodape()
