import streamlit as st
from utils import exibir_rodape, registrar_acesso
import urllib.parse
import time
from datetime import datetime

# --- REGISTRO DE ACESSO ---
registrar_acesso("Projetos Power BI")

# --- CONFIGURAÇÃO DE SESSÃO PARA RETENÇÃO ---
if "pbi_visualizacoes" not in st.session_state:
    st.session_state.pbi_visualizacoes = {}
if "tempo_gasto" not in st.session_state:
    st.session_state.tempo_gasto = 0
if "projetos_visualizados" not in st.session_state:
    st.session_state.projetos_visualizados = set()

# --- ESTILO ALTA RETENÇÃO (UX NEUROCIENTÍFICO) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700;14..32,800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

/* ========== BASE ========== */
* { margin: 0; padding: 0; box-sizing: border-box; }

[data-testid="stAppViewContainer"] {
    background: #0a0c12 !important;
    background-image: radial-gradient(circle at 25% 0%, rgba(0, 200, 255, 0.03) 0%, transparent 60%),
                      radial-gradient(circle at 75% 100%, rgba(100, 80, 255, 0.02) 0%, transparent 70%);
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"] { display: none !important; }

.block-container {
    max-width: 1400px !important;
    padding: 1rem 3rem 0 !important;
}

/* ========== TYPOGRAPHY ========== */
body, .main, [data-testid="stMarkdown"] {
    font-family: 'Inter', sans-serif !important;
    color: #e8edf5;
}

h1, h2, h3, .hero-title, .card-title {
    font-family: 'Space Grotesk', monospace !important;
    letter-spacing: -0.02em;
}

/* ========== ANIMAÇÃO DE ENTRADA PROGRESSIVA ========== */
@keyframes slideUp {
    from { opacity: 0; transform: translateY(40px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes scaleIn {
    from { opacity: 0; transform: scale(0.95); }
    to { opacity: 1; transform: scale(1); }
}

@keyframes shimmer {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}

@keyframes pulse-glow {
    0%, 100% { box-shadow: 0 0 0 0 rgba(0, 200, 255, 0); }
    50% { box-shadow: 0 0 0 8px rgba(0, 200, 255, 0.1); }
}

/* ========== HERO SECTION (PSYCHOLOGICAL HOOKS) ========== */
.hero-section {
    text-align: center;
    padding: 3rem 2rem 2rem;
    animation: slideUp 0.6s cubic-bezier(0.2, 0.9, 0.4, 1.1) forwards;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(0, 200, 255, 0.08);
    border: 1px solid rgba(0, 200, 255, 0.2);
    border-radius: 100px;
    padding: 0.4rem 1.2rem;
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.5px;
    color: #00ccff;
    margin-bottom: 1.5rem;
}

.hero-title {
    font-size: clamp(2.2rem, 5vw, 3.8rem);
    font-weight: 700;
    background: linear-gradient(135deg, #ffffff 0%, #94a3b8 50%, #00ccff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
}

.hero-subtitle {
    font-size: 1.1rem;
    color: #7e8aa2;
    max-width: 650px;
    margin: 0 auto 1.5rem;
    line-height: 1.6;
}

/* ========== PROGRESS TRACKER ========== */
.progress-tracker {
    background: rgba(15, 18, 25, 0.8);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 1rem 1.8rem;
    margin: 1rem auto 2rem;
    display: inline-flex;
    align-items: center;
    gap: 2rem;
    border: 1px solid rgba(255,255,255,0.05);
}

.progress-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    font-size: 0.85rem;
}

.progress-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #2a3649;
    transition: all 0.3s ease;
}

.progress-dot.active {
    background: #00ccff;
    box-shadow: 0 0 8px #00ccff;
}

.progress-dot.viewed {
    background: #10b981;
}

/* ========== SEARCH (RETENTION-OPTIMIZED) ========== */
.search-wrapper {
    max-width: 500px;
    margin: 0 auto 2rem;
    position: relative;
}

.search-wrapper input {
    width: 100%;
    background: rgba(20, 24, 35, 0.9) !important;
    border: 1px solid rgba(0, 200, 255, 0.15) !important;
    border-radius: 60px !important;
    padding: 1rem 1.5rem !important;
    color: white !important;
    font-size: 0.95rem !important;
    transition: all 0.3s ease !important;
}

.search-wrapper input:focus {
    border-color: #00ccff !important;
    box-shadow: 0 0 0 3px rgba(0, 200, 255, 0.15) !important;
    background: rgba(25, 30, 45, 0.95) !important;
}

.search-clear {
    position: absolute;
    right: 1.2rem;
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    color: #5a6680;
    cursor: pointer;
    font-size: 1rem;
}

/* ========== DASHBOARD CARDS (HIGH ENGAGEMENT) ========== */
.dashboard-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.dashboard-card {
    background: linear-gradient(145deg, rgba(25, 30, 45, 0.7) 0%, rgba(15, 18, 28, 0.9) 100%);
    border-radius: 24px;
    border: 1px solid rgba(255,255,255,0.05);
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.2, 0.9, 0.4, 1.1);
    cursor: pointer;
    position: relative;
    animation: scaleIn 0.5s ease-out forwards;
    opacity: 0;
}

.dashboard-card:hover {
    transform: translateY(-6px) scale(1.01);
    border-color: rgba(0, 200, 255, 0.3);
    box-shadow: 0 20px 40px -12px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(0, 200, 255, 0.1);
}

.card-header {
    padding: 1.25rem 1.5rem 0.75rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}

.card-icon {
    font-size: 2rem;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
}

.card-title {
    font-family: 'Space Grotesk', monospace;
    font-size: 1.1rem;
    font-weight: 600;
    color: #f0f4ff;
    flex: 1;
    line-height: 1.3;
}

.view-badge {
    font-size: 0.7rem;
    background: rgba(16, 185, 129, 0.15);
    color: #10b981;
    padding: 0.2rem 0.6rem;
    border-radius: 20px;
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
}

.card-content {
    padding: 1rem 1.5rem;
}

.card-description {
    font-size: 0.85rem;
    color: #9aa4bf;
    line-height: 1.55;
    margin-bottom: 1rem;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.card-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 0.75rem;
    padding-top: 0.75rem;
    border-top: 1px solid rgba(255,255,255,0.05);
}

.card-category {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #00ccff;
    font-weight: 600;
}

.card-actions {
    display: flex;
    gap: 0.75rem;
    opacity: 0.6;
    transition: opacity 0.3s ease;
}

.dashboard-card:hover .card-actions {
    opacity: 1;
}

.action-btn {
    background: none;
    border: none;
    color: #8a94b0;
    cursor: pointer;
    font-size: 0.9rem;
    padding: 0.25rem;
    transition: all 0.2s ease;
}

.action-btn:hover {
    color: #00ccff;
    transform: scale(1.1);
}

/* ========== EXPANDED VIEW (MICRO-INTERACTIONS) ========== */
.expanded-view {
    background: linear-gradient(145deg, rgba(20, 24, 38, 0.95) 0%, rgba(12, 15, 25, 0.98) 100%);
    border-radius: 28px;
    padding: 1.5rem;
    margin: 1rem 0 2rem;
    border: 1px solid rgba(0, 200, 255, 0.2);
    animation: slideUp 0.4s ease-out;
}

.expanded-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.25rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}

.expanded-title {
    font-family: 'Space Grotesk', monospace;
    font-size: 1.3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #fff, #00ccff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.close-expanded {
    background: rgba(255,255,255,0.05);
    border: none;
    border-radius: 50%;
    width: 32px;
    height: 32px;
    cursor: pointer;
    color: #8a94b0;
    transition: all 0.2s;
}

.close-expanded:hover {
    background: rgba(255,255,255,0.15);
    color: white;
}

.expanded-description {
    font-size: 0.95rem;
    line-height: 1.7;
    color: #b8c0d4;
    margin-bottom: 1.5rem;
}

.expanded-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
}

.primary-btn {
    background: linear-gradient(135deg, #00ccff, #0099cc);
    border: none;
    border-radius: 40px;
    padding: 0.8rem 2rem;
    color: white;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}

.primary-btn:hover {
    transform: scale(1.02);
    box-shadow: 0 8px 20px rgba(0, 200, 255, 0.3);
}

.secondary-btn {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(0, 200, 255, 0.3);
    border-radius: 40px;
    padding: 0.8rem 1.5rem;
    color: #00ccff;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
}

/* ========== ENGAGEMENT FOOTER ========== */
.engagement-footer {
    margin-top: 3rem;
    padding: 2rem;
    text-align: center;
    background: linear-gradient(180deg, transparent, rgba(0, 200, 255, 0.03));
    border-radius: 40px;
}

.cta-buttons {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-top: 1.5rem;
    flex-wrap: wrap;
}

.pulse-btn {
    animation: pulse-glow 2s infinite;
}

/* ========== TOAST NOTIFICATION ========== */
.toast-notification {
    position: fixed;
    bottom: 24px;
    right: 24px;
    background: #1e293b;
    border-left: 3px solid #00ccff;
    padding: 0.75rem 1.25rem;
    border-radius: 12px;
    font-size: 0.85rem;
    z-index: 1000;
    animation: slideUp 0.3s ease-out;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
}

/* ========== SCROLLBAR ========== */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #0a0c12; }
::-webkit-scrollbar-thumb { background: #00ccff40; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# --- DADOS COM CATEGORIAS PARA MELHOR RETENÇÃO ---
pbi_projects = [
    {"title": "Dashboard Transporte", "icon": "🚚", "category": "logística", "url": "https://app.powerbi.com/view?r=eyJrIjoiNjY5NThlNjctZWY1Ny00YjA0LTk0MjEtNzhiNjgzZjdjZjA2IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9", "desc": "Otimização logística completa com KPIs de performance operacional, redução de lead time e análise preditiva de gargalos."},
    {"title": "Dashboard ANATEL", "icon": "📞", "category": "regulatório", "url": "https://app.powerbi.com/view?r=eyJrIjoiZjgwNmViZjMtYTQ3OS00ZjljLWFiZjktOTNlNzJhYWQ2MzZkIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9", "desc": "Monitoramento estratégico de reclamações regulatórias com identificação de tendências e prevenção de sanções."},
    {"title": "Dashboard OEE Industrial", "icon": "🏭", "category": "industrial", "url": "https://app.powerbi.com/view?r=eyJrIjoiM2YxN2NhZmQtMTg4My00YTgwLWJhOGQtZmRkNGZkNTM1ZDM0IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9", "desc": "Eficiência industrial em tempo real: disponibilidade, performance e qualidade. Redução de perdas e aumento de produtividade."},
    {"title": "Portal Transparência", "icon": "🏛️", "category": "governança", "url": "https://app.powerbi.com/view?r=eyJrIjoiYTM2ZWFlM2QtOTc2NC00NDQ2LTg2ZTctOGY5Nzc4YTk2YWM1IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9", "desc": "Controle social e transparência pública com análise granular de receitas, despesas e indicadores municipais."},
    {"title": "DRE Estratégico", "icon": "💰", "category": "financeiro", "url": "https://app.powerbi.com/view?r=eyJrIjoiOWE0ZmU3ZTMtYzAyYi00NDE1LTg3YWItYjcxZTE2ZWI2OWRjIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9", "desc": "Análise financeira completa com DRE, margens de contribuição e projeções estratégicas de rentabilidade."},
    {"title": "Monitoramento Bradesco", "icon": "🏦", "category": "rh", "url": "https://app.powerbi.com/view?r=eyJrIjoiMjQxN2Q4NGYtNWRmNy00NWVjLWE4YmQtNWMyNWYwNGYyZDUzIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9", "desc": "Gestão estratégica de recrutamento com análise de vagas por perfil, região e tendências de mercado."},
    {"title": "Relatório STONE", "icon": "💳", "category": "financeiro", "url": "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Faturamento B2B com margem de contribuição, ticket médio e análise regional detalhada."},
    {"title": "Vendas Meta vs Real", "icon": "🎯", "category": "vendas", "url": "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Acompanhamento preditivo de metas com análise de gap e recomendações automáticas para correção de rota."},
    {"title": "Controle de Pedidos", "icon": "📦", "category": "logística", "url": "https://app.powerbi.com/view?r=eyJrIjoiZDZlNzViNzMtODllZS00OTVlLWI4MWQtNzBhZmU5ZTkxY2E0IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9", "desc": "Gestão de inventário inteligente com alertas de ruptura e otimização de giro de estoque."},
    {"title": "People Analytics RH", "icon": "👥", "category": "rh", "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Análise de performance de equipes, turnover e planejamento sucessório com dashboards preditivos."},
    {"title": "Gestão Borelli", "icon": "🚀", "category": "industrial", "url": "https://app.powerbi.com/view?r=eyJrIjoiZTY5YmEzZmQtZDVhMS00N2QyLWJhY2QtMDNhMWFmMDRjMjNmIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9", "desc": "Eficiência fabril com análise de desperdícios, capacidade ociosa e otimização de recursos."},
    {"title": "Beocean Resort", "icon": "🏖️", "category": "financeiro", "url": "https://app.powerbi.com/view?r=eyJrIjoiY2VkZmU1MDMtNTgwZS00NTJmLWFhOTktYzM0YzMwZDE3OTE4IiwidCI6IjdjNTYzNjMxLTcyZGMtNDY1Ny05MTRkLWIyM2M5ZTI5OGVlMSJ9", "desc": "Painel financeiro hoteleiro com análise de fluxo de caixa, receitas por categoria e otimização de tarifas."}
]

# --- FUNÇÕES AUXILIARES DE RETENÇÃO ---
def registrar_visualizacao(project_title):
    hoje = datetime.now().strftime("%Y-%m-%d")
    if project_title not in st.session_state.pbi_visualizacoes:
        st.session_state.pbi_visualizacoes[project_title] = []
    st.session_state.pbi_visualizacoes[project_title].append(hoje)
    st.session_state.projetos_visualizados.add(project_title)

def total_visualizacoes():
    return sum(len(v) for v in st.session_state.pbi_visualizacoes.values())

def projetos_unicos_vistos():
    return len(st.session_state.projetos_visualizados)

# --- HERO COM GAMIFICAÇÃO ---
st.markdown(f"""
<div class="hero-section">
    <div class="hero-badge">
        <span>⚡</span> +20 anos transformando dados em decisões
    </div>
    <h1 class="hero-title">Inteligência que gera<br>resultados reais</h1>
    <p class="hero-subtitle">
        Cada dashboard é uma ferramenta estratégica desenvolvida para acelerar sua tomada de decisão
    </p>
    <div class="progress-tracker">
        <div class="progress-item">
            <div class="progress-dot {'active' if projetos_unicos_vistos() > 0 else ''} {'viewed' if projetos_unicos_vistos() > 0 else ''}"></div>
            <span>{projetos_unicos_vistos()} projetos vistos</span>
        </div>
        <div class="progress-item">
            <div class="progress-dot {'active' if total_visualizacoes() > 0 else ''}"></div>
            <span>{total_visualizacoes()} visualizações</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- CATEGORIAS RÁPIDAS (FOMO E SCARCITY) ---
st.markdown("""
<div style="display: flex; justify-content: center; gap: 0.75rem; flex-wrap: wrap; margin: 1rem 0 2rem;">
    <span style="background: rgba(0,200,255,0.1); padding: 0.3rem 1rem; border-radius: 40px; font-size: 0.75rem; cursor: pointer;" onclick="filterCategory('todos')">📊 Todos</span>
    <span style="background: rgba(0,200,255,0.1); padding: 0.3rem 1rem; border-radius: 40px; font-size: 0.75rem; cursor: pointer;" onclick="filterCategory('financeiro')">💰 Financeiro</span>
    <span style="background: rgba(0,200,255,0.1); padding: 0.3rem 1rem; border-radius: 40px; font-size: 0.75rem; cursor: pointer;" onclick="filterCategory('vendas')">🎯 Vendas</span>
    <span style="background: rgba(0,200,255,0.1); padding: 0.3rem 1rem; border-radius: 40px; font-size: 0.75rem; cursor: pointer;" onclick="filterCategory('rh')">👥 RH</span>
    <span style="background: rgba(0,200,255,0.1); padding: 0.3rem 1rem; border-radius: 40px; font-size: 0.75rem; cursor: pointer;" onclick="filterCategory('industrial')">🏭 Industrial</span>
</div>
""", unsafe_allow_html=True)

# --- SEARCH COM JS PARA MAIOR INTERATIVIDADE ---
search_query = st.text_input(
    "🔍 Pesquisar dashboard...",
    placeholder="Ex: financeiro, vendas, logística...",
    label_visibility="collapsed"
)

# --- ESTADO PARA EXPANSÃO DE CARD ---
if "expanded_card" not in st.session_state:
    st.session_state.expanded_card = None

# --- FILTRO ---
filtered = [p for p in pbi_projects 
            if not search_query or 
            search_query.lower() in p["title"].lower() or 
            search_query.lower() in p["desc"].lower() or
            search_query.lower() in p["category"].lower()]

# --- RENDERIZAÇÃO COM SISTEMA DE RETENÇÃO ---
st.markdown('<div class="dashboard-grid">', unsafe_allow_html=True)

cols = st.columns(2)
for idx, project in enumerate(filtered):
    col = cols[idx % 2]
    with col:
        visto = project["title"] in st.session_state.projetos_visualizados
        
        card_html = f"""
        <div class="dashboard-card" data-project="{project['title']}" data-category="{project['category']}" style="animation-delay: {idx * 0.05}s;">
            <div class="card-header">
                <div class="card-icon">{project['icon']}</div>
                <div class="card-title">{project['title']}</div>
                {'<div class="view-badge">✓ Visto</div>' if visto else ''}
            </div>
            <div class="card-content">
                <div class="card-description">{project['desc'][:120]}...</div>
                <div class="card-meta">
                    <span class="card-category">{project['category'].upper()}</span>
                    <div class="card-actions">
                        <button class="action-btn" onclick="expandProject('{project['title']}')">🔍 Detalhes</button>
                        <button class="action-btn" onclick="shareProject('{project['title']}')">📤 Compartilhar</button>
                    </div>
                </div>
            </div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
        
        # Botão de ação direta (acesso rápido)
        col1, col2 = st.columns([3, 1])
        with col1:
            if st.button(f"📊 Abrir {project['title'].split()[0]}", key=f"open_{idx}", use_container_width=True):
                registrar_visualizacao(project["title"])
                st.markdown(f'<div class="toast-notification">✅ Visualização registrada! Continue explorando...</div>', unsafe_allow_html=True)
                st.markdown(f'<meta http-equiv="refresh" content="0; url={project["url"]}">', unsafe_allow_html=True)
        with col2:
            if st.button(f"💬", key=f"share_{idx}", help="Compartilhar via WhatsApp"):
                msg = f"Olá! Vi o dashboard {project['title']} e gostaria de saber mais.\n\n{project['desc'][:100]}..."
                wa_link = f"https://wa.me/?text={urllib.parse.quote(msg)}"
                st.markdown(f'<meta http-equiv="refresh" content="0; url={wa_link}">', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- EXPANDED VIEW (quando clica em detalhes) ---
if st.session_state.expanded_card:
    projeto_exp = next((p for p in pbi_projects if p["title"] == st.session_state.expanded_card), None)
    if projeto_exp:
        st.markdown(f"""
        <div class="expanded-view">
            <div class="expanded-header">
                <div class="expanded-title">{projeto_exp['icon']} {projeto_exp['title']}</div>
                <button class="close-expanded" onclick="closeExpanded()">✕</button>
            </div>
            <div class="expanded-description">
                {projeto_exp['desc']}
                <br><br>
                <strong>Categoria:</strong> {projeto_exp['category'].upper()}
            </div>
            <div class="expanded-actions">
                <a href="{projeto_exp['url']}" target="_blank" class="primary-btn">🚀 Abrir Dashboard Agora</a>
                <button class="secondary-btn" onclick="copyLink('{projeto_exp['url']}')">📋 Copiar Link</button>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER COM CTAS DE RETENÇÃO ---
st.markdown(f"""
<div class="engagement-footer">
    <h3 style="font-family: 'Space Grotesk'; margin-bottom: 0.5rem;">⚡ Você já explorou {projetos_unicos_vistos()} de {len(pbi_projects)} dashboards</h3>
    <p style="color: #7e8aa2; margin-bottom: 1rem;">A inteligência de negócio mais premiada do mercado</p>
    <div class="cta-buttons">
        <a href="#" class="primary-btn pulse-btn" onclick="scrollToTop()">📈 Continuar Explorando</a>
        <a href="#" class="secondary-btn" onclick="contactExpert()">💬 Falar com Especialista</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- JAVASCRIPT PARA MICRO-INTERAÇÕES ---
st.markdown("""
<script>
// Filtro por categoria
function filterCategory(cat) {
    const cards = document.querySelectorAll('.dashboard-card');
    cards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (cat === 'todos' || category === cat) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

// Expandir projeto
function expandProject(title) {
    // Isso seria integrado com Streamlit via Streamlit.setComponentValue
    console.log('Expandindo:', title);
}

// Fechar expandido
function closeExpanded() {
    // Reset do estado expandido
    console.log('Fechando expandido');
}

// Copiar link
function copyLink(url) {
    navigator.clipboard.writeText(url);
    alert('Link copiado! Compartilhe com sua equipe.');
}

// Scroll para topo
function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Contatar especialista
function contactExpert() {
    window.open('https://wa.me/5548999999999?text=Olá!%20Gostaria%20de%20saber%20mais%20sobre%20os%20dashboards...', '_blank');
}

// Compartilhar projeto
function shareProject(title) {
    console.log('Compartilhando:', title);
}
</script>
""", unsafe_allow_html=True)

# --- SPAÇO FINAL ---
st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)
exibir_rodape()
