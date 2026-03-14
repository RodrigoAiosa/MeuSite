import streamlit as st
import json
from datetime import datetime, timedelta
import pandas as pd
import sqlite3
from io import StringIO

# --- CONFIGURAÇÃO DE PÁGINA ---
st.set_page_config(
    page_title="SQL - Melhores Práticas Pro | Rodrigo Aiosa",
    page_icon="🗄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- INICIALIZAR SESSION STATE ---
if 'favorites' not in st.session_state:
    st.session_state.favorites = set()
if 'learned' not in st.session_state:
    st.session_state.learned = set()
if 'notes' not in st.session_state:
    st.session_state.notes = {}
if 'search_query' not in st.session_state:
    st.session_state.search_query = ""
if 'user_points' not in st.session_state:
    st.session_state.user_points = 0
if 'challenges_completed' not in st.session_state:
    st.session_state.challenges_completed = set()
if 'daily_streak' not in st.session_state:
    st.session_state.daily_streak = 1
if 'current_menu' not in st.session_state:
    st.session_state.current_menu = "📖 Todas as Práticas"
if 'page' not in st.session_state:
    st.session_state.page = 0
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = "Todas"
if 'selected_difficulty' not in st.session_state:
    st.session_state.selected_difficulty = "Todas"

# --- INICIALIZAR DATABASE EM MEMÓRIA ---
def init_database():
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    usuarios_df = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'nome': ['Alice Silva', 'Bob Santos', 'Carlos Oliveira', 'Diana Costa', 'Eduardo Pereira'],
        'email': ['alice@gmail.com', 'bob@gmail.com', 'carlos@hotmail.com', 'diana@gmail.com', 'edu@outlook.com'],
        'ativo': [True, True, False, True, True],
        'created_at': ['2023-01-15', '2023-02-20', '2023-03-10', '2023-04-05', '2023-05-12'],
        'categoria': ['Premium', 'Standard', 'Premium', 'Free', 'Standard']
    })
    usuarios_df.to_sql('usuarios', conn, index=False, if_exists='replace')
    vendas_df = pd.DataFrame({
        'id': [1, 2, 3, 4, 5, 6],
        'usuario_id': [1, 2, 1, 3, 2, 5],
        'valor': [150.00, 200.00, 75.50, 300.00, 120.00, 450.00],
        'status': ['pago', 'pago', 'pendente', 'pago', 'cancelado', 'pago'],
        'data': ['2024-01-10', '2024-01-15', '2024-02-01', '2024-02-10', '2024-02-15', '2024-03-01']
    })
    vendas_df.to_sql('vendas', conn, index=False, if_exists='replace')
    produtos_df = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'nome': ['Produto A', 'Produto B', 'Produto C', 'Produto D'],
        'categoria': ['Eletrônicos', 'Eletrônicos', 'Livros', 'Livros'],
        'preco': [99.99, 199.99, 29.99, 49.99]
    })
    produtos_df.to_sql('produtos', conn, index=False, if_exists='replace')
    return conn

def execute_query(query):
    try:
        query = query.strip()
        if not query:
            return None, "❌ Escreva uma query SQL primeiro!"
        conn = init_database()
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df, f"✅ Query executada com sucesso! {len(df)} registros retornados."
    except sqlite3.OperationalError as e:
        return None, f"❌ Erro SQL: {str(e)}"
    except Exception as e:
        return None, f"❌ Erro: {str(e)}"

# ── DESIGN (Python Pro palette) ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, .main, [data-testid="stAppViewContainer"] {
    background-color: #0a0e27 !important;
}

[data-testid="stAppViewContainer"] {
    background-image:
        radial-gradient(ellipse 80% 50% at 50% -10%, rgba(139,92,246,0.12) 0%, transparent 60%),
        radial-gradient(ellipse 40% 30% at 80% 60%, rgba(59,130,246,0.08) 0%, transparent 50%);
}

[data-testid="stHeader"] { background: transparent !important; }

.main h1, .main h2, .main h3, .main h4,
.main p, .main a, .main li,
[data-testid="stAppViewContainer"] div:not([data-testid="stSidebar"]) {
    font-family: 'DM Sans', sans-serif !important;
}

.material-symbols-rounded,
.material-icons,
[data-testid*="Collapse"] span,
[data-testid*="collapse"] span {
    font-family: 'Material Symbols Rounded', 'Material Icons' !important;
}

[data-testid="stMarkdownContainer"] { width: 100% !important; }
.block-container {
    max-width: 100% !important;
    padding-left: 4rem !important;
    padding-right: 4rem !important;
}

/* ── HERO ── */
.hero-wrapper {
    text-align: center;
    padding: 80px 20px 50px;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.hero-badge {
    display: inline-block;
    font-family: 'Syne', sans-serif !important;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #a78bfa;
    border: 1px solid rgba(167,139,250,0.35);
    background: rgba(167,139,250,0.07);
    padding: 6px 18px;
    border-radius: 100px;
    margin-bottom: 28px;
}

.hero-title {
    font-family: 'Syne', sans-serif !important;
    font-size: clamp(2.4rem, 5vw, 4rem);
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -1.5px;
    color: #f0f4ff;
    margin: 0 auto 20px;
    max-width: 760px;
    text-align: center;
}

.hero-title .accent {
    background: linear-gradient(135deg, #a78bfa 0%, #7c3aed 50%, #c4b5fd 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-subtitle {
    font-size: 1.05rem;
    font-weight: 300;
    color: #7b8ba8;
    max-width: 560px;
    margin: 0 auto 48px;
    line-height: 1.7;
    text-align: center;
}

.hero-stats {
    display: flex;
    justify-content: center;
    gap: 48px;
    flex-wrap: wrap;
    margin-bottom: 60px;
}

.hero-stat { text-align: center; }

.hero-stat-number {
    font-family: 'Syne', sans-serif !important;
    font-size: 2rem;
    font-weight: 800;
    color: #a78bfa;
    display: block;
    line-height: 1;
}

.hero-stat-label {
    font-size: 0.78rem;
    color: #4a5568;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 6px;
    display: block;
}

.hero-divider {
    width: 100%;
    max-width: 900px;
    margin: 0 auto 60px;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(167,139,250,0.3), transparent);
}

/* ── SECTION HEADERS ── */
.section-header {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.5rem;
    font-weight: 800;
    color: #f0f4ff;
    margin: 50px 0 28px;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba(167,139,250,0.2);
    letter-spacing: -0.5px;
    position: relative;
}

.section-header::after {
    content: '';
    position: absolute;
    bottom: -1px;
    left: 0;
    width: 48px;
    height: 2px;
    background: #a78bfa;
}

/* ── PROGRESS BAR ── */
.progress-container {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%);
    border: 1px solid rgba(167,139,250,0.2);
    border-radius: 20px;
    padding: 28px 32px;
    margin: 0 0 40px;
}

.progress-bar {
    width: 100%;
    height: 8px;
    background: rgba(255,255,255,0.05);
    border-radius: 100px;
    overflow: hidden;
    margin: 12px 0;
}

.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #a78bfa, #7c3aed);
    border-radius: 100px;
    transition: width 0.4s ease;
}

/* ── STAT CARDS ── */
.stat-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%);
    border: 1px solid rgba(167,139,250,0.2);
    border-radius: 20px;
    padding: 36px 28px;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

.stat-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(167,139,250,0.5), transparent);
    opacity: 0;
    transition: opacity 0.35s ease;
}

.stat-card:hover {
    transform: translateY(-4px);
    border-color: rgba(167,139,250,0.4);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4), 0 0 0 1px rgba(167,139,250,0.1);
}

.stat-card:hover::before { opacity: 1; }

.stat-number {
    font-family: 'Syne', sans-serif !important;
    font-size: 2.6rem;
    font-weight: 800;
    color: #a78bfa;
    margin-bottom: 10px;
    line-height: 1;
}

.stat-label {
    font-family: 'Syne', sans-serif !important;
    font-size: 0.75rem;
    font-weight: 700;
    color: #e2e8f0;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.stat-sublabel {
    font-size: 0.82rem;
    color: #4a5568;
    margin-top: 8px;
    font-weight: 300;
}

/* ── FILTER / EDITOR SECTIONS ── */
.filter-section,
.editor-section {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%);
    border: 1px solid rgba(167,139,250,0.2);
    border-radius: 20px;
    padding: 30px 32px;
    margin: 20px 0 32px;
}

.editor-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 0.9rem;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #a78bfa;
    margin-bottom: 14px;
}

/* ── METRIC BOX ── */
.metric-box {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%);
    border: 1px solid rgba(167,139,250,0.2);
    border-radius: 16px;
    padding: 22px;
    text-align: center;
}

.metric-value {
    font-family: 'Syne', sans-serif !important;
    font-size: 2.2rem;
    font-weight: 800;
    color: #a78bfa;
}

.metric-label {
    color: #7b8ba8;
    font-weight: 400;
    margin-top: 8px;
    font-size: 0.88rem;
}

/* ── BADGES ── */
.points-badge {
    background: linear-gradient(135deg, #a78bfa, #7c3aed);
    color: #0a0e27;
    padding: 7px 16px;
    border-radius: 100px;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700;
    font-size: 0.82rem;
    display: inline-block;
    margin: 4px;
    letter-spacing: 0.5px;
}

.streak-badge {
    background: linear-gradient(135deg, #ef4444, #dc2626);
    color: white;
    padding: 7px 16px;
    border-radius: 100px;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700;
    font-size: 0.82rem;
    display: inline-block;
    margin: 4px;
    letter-spacing: 0.5px;
}

.badge {
    display: inline-block;
    background: rgba(167,139,250,0.12);
    color: #a78bfa;
    border: 1px solid rgba(167,139,250,0.25);
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 0.78rem;
    font-weight: 600;
    margin: 3px;
}

/* ── NOTES ── */
.notes-container {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%);
    border: 1px solid rgba(167,139,250,0.2);
    border-left: 3px solid #a78bfa;
    border-radius: 12px;
    padding: 16px 20px;
    margin: 10px 0;
}

/* ── EXPANDERS ── */
.stExpander {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%) !important;
    border: 1px solid rgba(167,139,250,0.2) !important;
    border-radius: 14px !important;
    margin-bottom: 10px !important;
}

.stExpander [data-testid="stExpanderToggleButton"] {
    color: #e2e8f0 !important;
    font-weight: 600;
}

/* ── CODE BLOCKS ── */
.stCode {
    background-color: #1a1a2e !important;
    border: 1px solid rgba(167,139,250,0.15) !important;
    border-radius: 10px !important;
}

code { color: #c4b5fd !important; background: transparent !important; }

/* ── INPUTS & SELECTS ── */
.stSelectbox > div > div {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(167,139,250,0.2) !important;
    color: #e2e8f0 !important;
    border-radius: 12px !important;
}

.stTextArea > div > div {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(167,139,250,0.2) !important;
    color: #e2e8f0 !important;
    border-radius: 12px !important;
}

div[data-testid="stTextInput"] input {
    background-color: rgba(255,255,255,0.03) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(167,139,250,0.25) !important;
    border-radius: 14px !important;
    padding: 14px 22px !important;
    font-size: 0.95rem !important;
    font-family: 'DM Sans', sans-serif !important;
}

div[data-testid="stTextInput"] input::placeholder { color: #2d3748 !important; }
div[data-testid="stTextInput"] input:focus {
    box-shadow: 0 0 0 3px rgba(167,139,250,0.15) !important;
    border-color: rgba(167,139,250,0.6) !important;
}

/* ── STATUS MESSAGES ── */
.stInfo {
    background: rgba(167,139,250,0.07) !important;
    border: 1px solid rgba(167,139,250,0.25) !important;
    border-radius: 12px !important;
}

.stSuccess {
    background: rgba(34,197,94,0.07) !important;
    border: 1px solid rgba(34,197,94,0.3) !important;
    border-radius: 12px !important;
}

.stError {
    background: rgba(239,68,68,0.07) !important;
    border: 1px solid rgba(239,68,68,0.3) !important;
    border-radius: 12px !important;
}

/* ── DIVIDER ── */
hr {
    border: none !important;
    border-top: 1px solid rgba(167,139,250,0.1) !important;
    margin: 40px 0 !important;
}

/* ── LINKS ── */
a { color: #a78bfa !important; transition: all 0.3s ease; }
a:hover { filter: brightness(1.2); }

.footer-spacer { height: 60px; }

::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0a0e27; }
::-webkit-scrollbar-thumb { background: rgba(167,139,250,0.2); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(167,139,250,0.4); }

</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.markdown("""
<div style="text-align: center; padding: 20px 0; border-bottom: 1px solid rgba(167,139,250,0.2);">
    <h1 style="font-family:'Syne',sans-serif; font-size: 1.6rem; color: #a78bfa; margin: 0; font-weight:800; letter-spacing:-0.5px;">🗄️ SQL Pro</h1>
    <p style="color: #4a5568; font-size: 0.82rem; margin-top: 6px; letter-spacing:1px; text-transform:uppercase;">Domine SQL em 60 práticas</p>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR STATS ---
col1, col2 = st.sidebar.columns(2)
with col1:
    st.markdown(f"""
    <div style="background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%); border: 1px solid rgba(167,139,250,0.2); border-radius: 14px; padding: 16px; text-align: center;">
        <p style="font-family:'Syne',sans-serif; color: #a78bfa; font-weight: 800; font-size: 1.4rem; margin: 0;">⭐ {st.session_state.user_points}</p>
        <p style="color: #4a5568; font-size: 0.75rem; margin: 5px 0; text-transform:uppercase; letter-spacing:1px;">Pontos</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%); border: 1px solid rgba(167,139,250,0.2); border-radius: 14px; padding: 16px; text-align: center;">
        <p style="font-family:'Syne',sans-serif; color: #a78bfa; font-weight: 800; font-size: 1.4rem; margin: 0;">🔥 {st.session_state.daily_streak}</p>
        <p style="color: #4a5568; font-size: 0.75rem; margin: 5px 0; text-transform:uppercase; letter-spacing:1px;">Streak</p>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR MENU ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 Navegação")

menu = st.sidebar.radio(
    "Escolha uma seção:",
    ["📖 Todas as Práticas", "⭐ Meus Favoritos", "✅ Já Aprendi", "🏆 Progresso", "🎯 Desafios"],
    label_visibility="collapsed"
)

# --- SEARCH FUNCTIONALITY ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔍 Buscar")
search_query = st.sidebar.text_input(
    "Buscar práticas:",
    placeholder="Digite aqui...",
    label_visibility="collapsed"
)
st.session_state.search_query = search_query.lower()
st.session_state.current_menu = menu

# ── HERO ──
st.markdown("""
<div class="hero-wrapper">
    <div class="hero-badge">🗄️ SQL Pro</div>
    <h1 class="hero-title">
        Melhores Práticas SQL para <span class="accent">queries que escalam</span>
    </h1>
    <p class="hero-subtitle">
        Estratégias avançadas para queries eficientes, escaláveis e precisas. Transforme dados em vantagem competitiva.
    </p>
    <div class="hero-stats">
        <div class="hero-stat">
            <span class="hero-stat-number">60+</span>
            <span class="hero-stat-label">Práticas</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-number">5</span>
            <span class="hero-stat-label">Categorias</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-number">3</span>
            <span class="hero-stat-label">Níveis</span>
        </div>
    </div>
    <div class="hero-divider"></div>
</div>
""", unsafe_allow_html=True)

# --- PROGRESSO VISUAL ---
total_practices = 60
learned_count = len(st.session_state.learned)
progress_percent = (learned_count / total_practices) * 100

st.markdown(f"""
<div class="progress-container">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
        <p style="font-family:'Syne',sans-serif; color: #e2e8f0; font-weight: 700; font-size:0.85rem; letter-spacing:1.5px; text-transform:uppercase; margin: 0;">🎓 Seu Progresso</p>
        <p style="font-family:'Syne',sans-serif; color: #a78bfa; font-weight: 800; font-size:1.1rem; margin: 0;">{learned_count}/{total_practices}</p>
    </div>
    <div class="progress-bar">
        <div class="progress-fill" style="width: {progress_percent}%"></div>
    </div>
    <p style="color: #4a5568; font-size: 0.82rem; margin: 10px 0 0; font-weight:300;">
        {'🏆 Parabéns! Você completou todas as práticas!' if learned_count == total_practices else f'Continue! Faltam {total_practices - learned_count} práticas para completar o guia.'}
    </p>
</div>
""", unsafe_allow_html=True)

# --- STATS SECTION ---
st.markdown('<h2 class="section-header">📊 Números que Falam</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">60+</div>
        <div class="stat-label">Práticas SQL</div>
        <div class="stat-sublabel">Documentadas e Testadas</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">5</div>
        <div class="stat-label">Categorias</div>
        <div class="stat-sublabel">De Conhecimento Essencial</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">3</div>
        <div class="stat-label">Níveis</div>
        <div class="stat-sublabel">Iniciante, Intermediário, Avançado</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<p style="text-align: center; color: #4a5568; margin: 40px 0; font-size: 1rem; line-height: 1.8; max-width:660px; margin-left:auto; margin-right:auto;">
    Queries eficientes são a base de dashboards que escalam.
    Boas práticas em SQL reduzem tempo de processamento e amplificam a precisão das análises.
    <br><br>
    <span style="color: #a78bfa; font-weight: 600;">
    Este é um guia completo para transformar você em um especialista SQL.
    </span>
</p>
""", unsafe_allow_html=True)

# --- DATABASE DE PRÁTICAS SQL ---
sql_practices = [
    {
        "icon": "🔍",
        "title": "Evitar SELECT *",
        "category": "Performance",
        "difficulty": "Iniciante",
        "description": "Selecione apenas as colunas necessárias.",
        "bad_query": "SELECT * FROM vendas WHERE ano = 2024;",
        "good_query": "SELECT\n    id,\n    produto,\n    valor,\n    data_venda\nFROM vendas\nWHERE ano = 2024;",
        "benefit": "Reduz bandwidth de rede, acelera processamento.",
        "context": "Impacto exponencial em sistemas com muitos dados.",
        "explanation": "Especificar colunas reduz o volume de dados trafegado pela rede e melhora o índice utilizado pelo banco de dados."
    },
    {
        "icon": "✅",
        "title": "Tratar NULL Explicitamente",
        "category": "Lógica & Precisão",
        "difficulty": "Iniciante",
        "description": "NULL não é zero nem string vazia.",
        "bad_query": "SELECT SUM(comissao) FROM vendas WHERE status = 'concluida';",
        "good_query": "SELECT\n    SUM(COALESCE(comissao, 0)) AS total_comissao\nFROM vendas\nWHERE status = 'concluida'\n    AND comissao IS NOT NULL;",
        "benefit": "Evita resultados inesperados.",
        "context": "Crítico em cálculos financeiros.",
        "explanation": "COALESCE substitui NULLs por um valor padrão, evitando que a soma resulte em NULL quando há valores nulos na coluna."
    },
    {
        "icon": "🔐",
        "title": "Prepared Statements",
        "category": "Segurança & Manutenção",
        "difficulty": "Iniciante",
        "description": "Parameterize queries contra SQL Injection.",
        "bad_query": "query = f\"SELECT * FROM usuarios WHERE email = '{user_email}'\"",
        "good_query": "query = (\n    \"SELECT *\"\n    \"FROM usuarios\"\n    \"WHERE email = %s\"\n)\ncursor.execute(query, (user_email,))",
        "benefit": "Impede ataques de segurança.",
        "context": "Obrigatório em produção.",
        "explanation": "Usar placeholders (%) em vez de concatenação protege contra SQL Injection, pois os parâmetros são tratados como dados, não como código SQL."
    },
    {
        "icon": "📋",
        "title": "Documentar Queries",
        "category": "Segurança & Manutenção",
        "difficulty": "Iniciante",
        "description": "Comente queries complexas.",
        "bad_query": "SELECT u.id, COUNT(DISTINCT v.id) FROM usuarios u LEFT JOIN vendas v ON u.id = v.usuario_id GROUP BY u.id;",
        "good_query": "-- Query: Contagem de vendas por usuário\n-- Propósito: Dashboard de Engagement\nSELECT\n    u.id,\n    u.nome,\n    COUNT(DISTINCT v.id) AS total_vendas\nFROM usuarios u\nLEFT JOIN vendas v\n    ON u.id = v.usuario_id\nGROUP BY u.id, u.nome;",
        "benefit": "Fácil handoff e manutenção.",
        "context": "Um comentário economiza horas.",
        "explanation": "Comentários explicam o objetivo da query e facilitam manutenção futura, especialmente em equipes com múltiplos desenvolvedores."
    },
    {
        "icon": "🎓",
        "title": "Usar LIMIT em Development",
        "category": "Performance",
        "difficulty": "Iniciante",
        "description": "Sempre limitar resultados em queries de teste.",
        "bad_query": "SELECT * FROM usuarios;",
        "good_query": "SELECT *\nFROM usuarios\nLIMIT 100;",
        "benefit": "Evita lentidão ao testar em prod.",
        "context": "Development vs Production.",
        "explanation": "LIMIT reduz o tempo de execução durante testes e evita carregar dados desnecessários em memória, protegendo também a produção de queries descontroladas."
    },
]

# --- FILTROS SECTION ---
st.markdown('<h2 class="section-header">🔎 Filtrar Práticas</h2>', unsafe_allow_html=True)

st.markdown('<div class="filter-section">', unsafe_allow_html=True)

col1, col2, col_space = st.columns([1.5, 1.5, 1])

with col1:
    categorias = ["Todas"] + sorted(list(set([p["category"] for p in sql_practices])))
    selected_category = st.selectbox("📂 Categoria", categorias, key="category_filter")

with col2:
    dificuldades = ["Todas", "Iniciante", "Intermediário", "Avançado"]
    selected_difficulty = st.selectbox("📈 Nível de Dificuldade", dificuldades, key="difficulty_filter")

st.markdown('</div>', unsafe_allow_html=True)

# --- EDITOR SQL ---
st.markdown('<h2 class="section-header">✏️ Editor SQL Interativo</h2>', unsafe_allow_html=True)
st.markdown('<p style="color: #4a5568; margin-bottom: 30px; font-weight:300;">Teste suas queries SQL em tempo real. O banco contém as tabelas: <span style="color:#a78bfa;">usuarios</span>, <span style="color:#a78bfa;">vendas</span> e <span style="color:#a78bfa;">produtos</span>.</p>', unsafe_allow_html=True)

sql_templates = {
    "SELECT Básico": "SELECT * FROM produtos LIMIT 10;",
    "WHERE Filtro": "SELECT id, nome, categoria FROM produtos WHERE categoria = 'Livros';",
    "COUNT Agregação": "SELECT COUNT(*) AS total_produtos FROM produtos;",
    "GROUP BY": "SELECT categoria, COUNT(*) AS total FROM produtos GROUP BY categoria;",
    "JOIN Tabelas": "SELECT u.nome, v.valor FROM usuarios u INNER JOIN vendas v ON u.id = v.usuario_id LIMIT 5;",
    "ORDER BY": "SELECT id, nome FROM usuarios ORDER BY nome ASC;",
    "SUM com Agregação": "SELECT usuario_id, SUM(valor) AS total_valor FROM vendas GROUP BY usuario_id;",
    "LEFT JOIN": "SELECT u.id, u.nome, COUNT(v.id) AS total_vendas FROM usuarios u LEFT JOIN vendas v ON u.id = v.usuario_id GROUP BY u.id, u.nome;",
    "DISTINCT": "SELECT DISTINCT categoria FROM produtos ORDER BY categoria;",
    "BETWEEN": "SELECT * FROM vendas WHERE valor BETWEEN 100 AND 300;",
    "IN Clause": "SELECT * FROM usuarios WHERE id IN (1, 2, 3, 4, 5);",
    "LIKE Pattern": "SELECT * FROM usuarios WHERE nome LIKE '%Silva%';",
}

st.markdown('<div class="editor-section">', unsafe_allow_html=True)

col_template, col_editor = st.columns([1, 2], gap="large")

with col_template:
    st.markdown('<p class="editor-title">📚 Templates</p>', unsafe_allow_html=True)
    selected_template = st.selectbox(
        "Escolha um exemplo:",
        ["Escrever Manual"] + list(sql_templates.keys()),
        key="template_select",
        label_visibility="collapsed"
    )
    template_query = sql_templates[selected_template] if selected_template != "Escrever Manual" else ""

with col_editor:
    st.markdown('<p class="editor-title">📝 Seu SQL</p>', unsafe_allow_html=True)
    user_query = st.text_area(
        "Escreva sua query SQL:",
        value=template_query,
        height=150,
        key="sql_editor",
        placeholder="SELECT * FROM produtos;",
        label_visibility="collapsed"
    )

st.markdown('</div>', unsafe_allow_html=True)

# --- RESULTADO ---
st.markdown('<h2 class="section-header">📊 Resultado da Query</h2>', unsafe_allow_html=True)

col_result, col_info = st.columns([2, 1], gap="large")

with col_result:
    st.markdown('<div style="background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%); border: 1px solid rgba(167,139,250,0.2); border-radius: 16px; padding: 24px;">', unsafe_allow_html=True)
    if user_query.strip():
        result_df, message = execute_query(user_query)
        if "✅" in message:
            st.success(message)
            if result_df is not None and len(result_df) > 0:
                st.dataframe(result_df, use_container_width=True)
            else:
                st.info("Query executada, mas nenhum resultado foi retornado.")
        else:
            st.error(message)
    else:
        st.markdown("""
        <div style="text-align: center; padding: 40px; color: #2d3748;">
            <p style="font-size: 1rem;">📝 Escreva uma query SQL no editor para ver o resultado</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_info:
    st.markdown("""
    <div style="background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%); border: 1px solid rgba(167,139,250,0.2); border-radius: 16px; padding: 24px;">
        <p style="font-family:'Syne',sans-serif; color: #a78bfa; font-weight: 700; font-size:0.8rem; letter-spacing:1.5px; text-transform:uppercase; margin-bottom: 16px;">ℹ️ Tabelas & Dicas</p>
        <p style="color: #4a5568; font-size: 0.85rem; line-height: 1.8; margin-bottom: 16px; font-weight:300;">
            <span style="color:#e2e8f0; font-weight:600;">usuarios:</span> id, nome, email, ativo, created_at, categoria
            <br><br>
            <span style="color:#e2e8f0; font-weight:600;">vendas:</span> id, usuario_id, valor, status, data
            <br><br>
            <span style="color:#e2e8f0; font-weight:600;">produtos:</span> id, nome, categoria, preco
        </p>
        <p style="color: #2d3748; font-size: 0.82rem; font-weight:300; border-top: 1px solid rgba(167,139,250,0.1); padding-top: 14px;">
            💡 Teste SELECT, WHERE, JOIN, GROUP BY, LIMIT e mais!
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- FOOTER ---
st.markdown("""
<div style="text-align: center; padding: 40px 0; border-top: 1px solid rgba(167,139,250,0.1); color: #2d3748;">
    <p style="margin-bottom: 10px; font-size: 0.92rem;">
        <span style="font-family:'Syne',sans-serif; color: #a78bfa; font-weight: 700;">SQL - Melhores Práticas</span>
        &nbsp;•&nbsp; Criado por Rodrigo Aiosa
    </p>
    <p style="font-size: 0.82rem; font-weight:300;">
        Transforme seus dados em vantagem competitiva com SQL estratégico
    </p>
</div>
<div class="footer-spacer"></div>
""", unsafe_allow_html=True)
