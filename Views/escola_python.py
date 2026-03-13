import streamlit as st
import json
from datetime import datetime, timedelta
import pandas as pd
from io import StringIO
import time

# --- CONFIGURAÇÃO DE PÁGINA ---
st.set_page_config(
    page_title="Python - Melhores Práticas Pro | Rodrigo Aiosa",
    page_icon="🐍",
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

# --- DESIGN LANDING PAGE ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, .main, [data-testid="stAppViewContainer"] {
    background-color: #0a0e27 !important;
}

[data-testid="stAppViewContainer"] {
    background-color: #0a0e27 !important;
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
    background: linear-gradient(135deg, #a78bfa 0%, #c4b5fd 50%, #ddd6fe 100%);
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
    border: 1px solid rgba(255,255,255,0.05);
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
    background: linear-gradient(90deg, #a78bfa, #c4b5fd);
    border-radius: 100px;
    transition: width 0.4s ease;
}

/* ── STAT CARDS ── */
.stat-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%);
    border: 1px solid rgba(255,255,255,0.05);
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
    border-color: rgba(167,139,250,0.2);
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
    border: 1px solid rgba(255,255,255,0.05);
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
    border: 1px solid rgba(255,255,255,0.05);
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
    background: linear-gradient(135deg, #a78bfa, #c4b5fd);
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

/* ── EXPANDERS ── */
.stExpander {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%) !important;
    border: 1px solid rgba(255,255,255,0.05) !important;
    border-radius: 14px !important;
    margin-bottom: 10px !important;
}

.stExpander [data-testid="stExpanderToggleButton"] {
    color: #e2e8f0 !important;
    font-weight: 600;
}

/* ── CODE BLOCKS ── */
.stCode {
    background-color: #0a0f1e !important;
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
    border-top: 1px solid rgba(255,255,255,0.05) !important;
    margin: 40px 0 !important;
}

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
    <h1 style="font-family:'Syne',sans-serif; font-size: 1.6rem; color: #a78bfa; margin: 0; font-weight:800; letter-spacing:-0.5px;">🐍 Python Pro</h1>
    <p style="color: #4a5568; font-size: 0.82rem; margin-top: 6px; letter-spacing:1px; text-transform:uppercase;">60 Melhores Práticas</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.sidebar.columns(2)
with col1:
    st.markdown(f"""
    <div style="background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%); border: 1px solid rgba(255,255,255,0.05); border-radius: 14px; padding: 16px; text-align: center;">
        <p style="font-family:'Syne',sans-serif; color: #a78bfa; font-weight: 800; font-size: 1.4rem; margin: 0;">⭐ {st.session_state.user_points}</p>
        <p style="color: #4a5568; font-size: 0.75rem; margin: 5px 0; text-transform:uppercase; letter-spacing:1px;">Pontos</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%); border: 1px solid rgba(255,255,255,0.05); border-radius: 14px; padding: 16px; text-align: center;">
        <p style="font-family:'Syne',sans-serif; color: #a78bfa; font-weight: 800; font-size: 1.4rem; margin: 0;">🔥 {st.session_state.daily_streak}</p>
        <p style="color: #4a5568; font-size: 0.75rem; margin: 5px 0; text-transform:uppercase; letter-spacing:1px;">Streak</p>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 Navegação")
menu = st.sidebar.radio(
    "Escolha uma seção:",
    ["📖 Todas as Práticas", "⭐ Meus Favoritos", "✅ Já Aprendi", "🏆 Progresso"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔍 Buscar")
search_query = st.sidebar.text_input("Buscar práticas:", placeholder="Digite aqui...", label_visibility="collapsed")
st.session_state.search_query = search_query.lower()
st.session_state.current_menu = menu

# ── HERO ──
st.markdown("""
<div class="hero-wrapper">
    <div class="hero-badge">🐍 Python Pro</div>
    <h1 class="hero-title">Melhores Práticas Python para <span class="accent">código que escala</span></h1>
    <p class="hero-subtitle">Padrões avançados, otimizações e design patterns. Transforme seu código Python em produção robusta.</p>
    <div class="hero-stats">
        <div class="hero-stat">
            <span class="hero-stat-number">60+</span>
            <span class="hero-stat-label">Práticas</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-number">6</span>
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
        {'🏆 Parabéns! Você completou todas as práticas!' if learned_count == total_practices else f'Continue! Faltam {total_practices - learned_count} práticas.'}
    </p>
</div>
""", unsafe_allow_html=True)

# --- STATS SECTION ---
st.markdown('<h2 class="section-header">📊 Números que Falam</h2>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""<div class="stat-card"><div class="stat-number">60+</div><div class="stat-label">Práticas Python</div><div class="stat-sublabel">Documentadas e Testadas</div></div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""<div class="stat-card"><div class="stat-number">6</div><div class="stat-label">Categorias</div><div class="stat-sublabel">De Conhecimento Essencial</div></div>""", unsafe_allow_html=True)

with col3:
    st.markdown("""<div class="stat-card"><div class="stat-number">3</div><div class="stat-label">Níveis</div><div class="stat-sublabel">Iniciante, Intermediário, Avançado</div></div>""", unsafe_allow_html=True)

# --- FILTROS ---
st.markdown('<h2 class="section-header">🔎 Filtrar Práticas</h2>', unsafe_allow_html=True)
st.markdown('<div class="filter-section">', unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1.5])
with col1:
    selected_category = st.selectbox("📂 Categoria", ["Todas", "Qualidade & Manutenção", "Performance & Elegância", "Elegância & Legibilidade", "Segurança & Manutenção", "Performance & Otimização", "Arquitetura & Avançado", "Concorrência & Performance", "Arquitetura & Design", "Qualidade & Testes", "Modernização & Legibilidade", "Elegância & Reutilização", "Elegância & Encapsulamento", "Elegância & Flexibilidade", "Programação Funcional"], key="category_filter")

with col2:
    selected_difficulty = st.selectbox("📈 Nível de Dificuldade", ["Todas", "Iniciante", "Intermediário", "Avançado"], key="difficulty_filter")

st.markdown('</div>', unsafe_allow_html=True)

# --- DATABASE DE PRÁTICAS (60 itens) ---
python_practices = [
    # INICIANTE (20)
    {"icon": "📚", "title": "Usar Type Hints", "category": "Qualidade & Manutenção", "difficulty": "Iniciante", "description": "Especifique tipos de argumentos e retorno.", "bad_code": "def calcular_total(items):\n    return sum(item['valor'] for item in items)", "good_code": "from typing import List, Dict\n\ndef calcular_total(items: List[Dict[str, float]]) -> float:\n    return sum(item['valor'] for item in items)", "benefit": "Detecta erros em tempo de desenvolvimento.", "context": "Type hints são obrigatórios em código profissional.", "explanation": "Type hints melhoram legibilidade e oferecem autocomplete em IDEs."},
    {"icon": "🔐", "title": "List Comprehension", "category": "Performance & Elegância", "difficulty": "Iniciante", "description": "Prefira list comprehension a loops tradicionais.", "bad_code": "pares = []\nfor num in [1,2,3,4,5]:\n    if num % 2 == 0:\n        pares.append(num * 2)", "good_code": "pares = [num * 2 for num in [1,2,3,4,5] if num % 2 == 0]", "benefit": "30-40% mais rápido.", "context": "O jeito Pythônico.", "explanation": "Otimizada em C, executa mais rápido que loops com append."},
    {"icon": "🔍", "title": "Usar f-strings", "category": "Elegância & Legibilidade", "difficulty": "Iniciante", "description": "f-strings são mais legíveis e rápidas.", "bad_code": "nome = 'Alice'\nidade = 30\nmsg = 'Olá, ' + nome + '. Você tem ' + str(idade) + ' anos'", "good_code": "nome = 'Alice'\nidade = 30\nmsg = f'Olá, {nome}. Você tem {idade} anos'", "benefit": "20% mais rápido.", "context": "Python 3.6+", "explanation": "Otimizadas em tempo de compilação."},
    {"icon": "📋", "title": "Usar Docstrings", "category": "Qualidade & Manutenção", "difficulty": "Iniciante", "description": "Documente funções com docstrings.", "bad_code": "def calcular_idade(ano_nascimento):\n    return 2024 - ano_nascimento", "good_code": "def calcular_idade(ano_nascimento: int) -> int:\n    \"\"\"Calcula a idade de uma pessoa.\n    \n    Args:\n        ano_nascimento: Ano de nascimento\n    Returns:\n        Idade em anos\n    \"\"\"", "benefit": "Facilita manutenção.", "context": "PEP 257.", "explanation": "Acessíveis via help() e documentação automática."},
    {"icon": "✅", "title": "Usar Dicionários em vez de Variáveis", "category": "Elegância & Legibilidade", "difficulty": "Iniciante", "description": "Agrupe dados relacionados em dicionários.", "bad_code": "pessoa_nome = 'Alice'\npessoa_idade = 30\npessoa_email = 'alice@gmail.com'", "good_code": "pessoa = {\n    'nome': 'Alice',\n    'idade': 30,\n    'email': 'alice@gmail.com'\n}", "benefit": "Código organizado.", "context": "Estruturação de dados.", "explanation": "Agrupa dados logicamente, reduzindo variáveis."},
    {"icon": "🎯", "title": "Usar enumerate()", "category": "Elegância & Legibilidade", "difficulty": "Iniciante", "description": "Use enumerate para acessar índice e valor.", "bad_code": "for i in range(len(nomes)):\n    print(f'{i}: {nomes[i]}')", "good_code": "for i, nome in enumerate(nomes):\n    print(f'{i}: {nome}')", "benefit": "Mais legível.", "context": "Loop sobre sequências.", "explanation": "Otimizado e evita erros de indexação."},
    {"icon": "🔄", "title": "Usar zip()", "category": "Elegância & Legibilidade", "difficulty": "Iniciante", "description": "Use zip para combinar múltiplas iteráveis.", "bad_code": "for i in range(len(nomes)):\n    print(f'{nomes[i]} - {idades[i]}')", "good_code": "for nome, idade in zip(nomes, idades):\n    print(f'{nome} - {idade}')", "benefit": "Mais seguro.", "context": "Iteração múltipla.", "explanation": "Mais eficiente que indexação."},
    {"icon": "🛡️", "title": "Try/Except Específicos", "category": "Qualidade & Manutenção", "difficulty": "Iniciante", "description": "Capture exceções específicas.", "bad_code": "try:\n    valor = int('abc')\nexcept:\n    print('Erro')", "good_code": "try:\n    valor = int('abc')\nexcept ValueError:\n    print('Erro: valor inválido')", "benefit": "Precisão no tratamento.", "context": "Debugging.", "explanation": "Capturar específico evita silenciar bugs."},
    {"icon": "🔑", "title": "Usar dict.get()", "category": "Elegância & Legibilidade", "difficulty": "Iniciante", "description": "Use get() para acessar dicionários com segurança.", "bad_code": "if 'timeout' in config:\n    timeout = config['timeout']\nelse:\n    timeout = 30", "good_code": "timeout = config.get('timeout', 30)", "benefit": "Mais limpo.", "context": "Acesso seguro.", "explanation": "Retorna padrão se chave não existir."},
    {"icon": "📦", "title": "Usar setdefault()", "category": "Performance & Elegância", "difficulty": "Iniciante", "description": "setdefault() define e retorna valor.", "bad_code": "if 'python' not in categorias:\n    categorias['python'] = []\ncategorias['python'].append('best-practices')", "good_code": "categorias.setdefault('python', []).append('best-practices')", "benefit": "Uma linha.", "context": "Dicionários aninhados.", "explanation": "Combina verificação e atribuição."},
    {"icon": "⚡", "title": "Usar all() e any()", "category": "Elegância & Legibilidade", "difficulty": "Iniciante", "description": "Use all() para verificar se todos são verdadeiros.", "bad_code": "resultado = True\nfor item in lista:\n    if not item:\n        resultado = False", "good_code": "resultado = all(lista)\nqualquer = any(lista)", "benefit": "Mais legível.", "context": "Validações lógicas.", "explanation": "Implementadas em C, mais rápidas."},
    {"icon": "🔓", "title": "Context Managers (with)", "category": "Segurança & Manutenção", "difficulty": "Iniciante", "description": "Use with para gerenciar recursos.", "bad_code": "f = open('dados.txt', 'r')\nconteudo = f.read()\nf.close()", "good_code": "with open('dados.txt', 'r') as f:\n    conteudo = f.read()", "benefit": "Fechamento garantido.", "context": "I/O, BD.", "explanation": "Garante cleanup automático."},
    {"icon": "🎓", "title": "isinstance() vs type()", "category": "Qualidade & Manutenção", "difficulty": "Iniciante", "description": "isinstance() é melhor que type().", "bad_code": "if type(valor) == str:\n    print('É string')", "good_code": "if isinstance(valor, str):\n    print('É string')", "benefit": "Respeita herança.", "context": "Verificação de tipos.", "explanation": "Funciona com subclasses."},
    {"icon": "🔀", "title": "sorted() vs sort()", "category": "Elegância & Legibilidade", "difficulty": "Iniciante", "description": "sorted() retorna nova lista.", "bad_code": "numeros = [3, 1, 4]\nnumeros.sort()", "good_code": "numeros = [3, 1, 4]\nordenados = sorted(numeros)", "benefit": "Original intacto.", "context": "Manipulação.", "explanation": "Mais funcional, sem efeitos."},
    {"icon": "🔍", "title": "in vs count()", "category": "Performance & Elegância", "difficulty": "Iniciante", "description": "in é mais rápido que count() > 0.", "bad_code": "if lista.count(3) > 0:\n    print('Existe')", "good_code": "if 3 in lista:\n    print('Existe')", "benefit": "3x mais rápido.", "context": "Verificação.", "explanation": "Sem criar contador."},
    {"icon": "💾", "title": "defaultdict", "category": "Performance & Elegância", "difficulty": "Iniciante", "description": "defaultdict inicializa valores automaticamente.", "bad_code": "palavras = {}\nfor p in ['python', 'python']:\n    if p not in palavras:\n        palavras[p] = 0\n    palavras[p] += 1", "good_code": "from collections import defaultdict\npedras = defaultdict(int)\nfor p in ['python', 'python']:\n    pedras[p] += 1", "benefit": "Código limpo.", "context": "Contadores.", "explanation": "Cria valores padrão automaticamente."},
    {"icon": "🎪", "title": "String methods vs regex", "category": "Performance & Elegância", "difficulty": "Iniciante", "description": "String methods são mais simples que regex simples.", "bad_code": "import re\nif re.search(r'mundo', texto):\n    print('Encontrado')", "good_code": "if 'mundo' in texto:\n    print('Encontrado')", "benefit": "10x mais rápido.", "context": "Buscas simples.", "explanation": "Otimizadas em C."},
    {"icon": "🚀", "title": "Evitar Variáveis Globais", "category": "Qualidade & Manutenção", "difficulty": "Iniciante", "description": "Passe dados como argumentos.", "bad_code": "contador = 0\ndef incrementar():\n    global contador\n    contador += 1", "good_code": "def incrementar(contador: int) -> int:\n    return contador + 1", "benefit": "Testável.", "context": "Testes.", "explanation": "Evita dependências ocultas."},
    {"icon": "⚙️", "title": "Constants em UPPERCASE", "category": "Qualidade & Manutenção", "difficulty": "Iniciante", "description": "Constantes devem ser em UPPERCASE.", "bad_code": "max_retries = 5\ntimeout = 30", "good_code": "MAX_RETRIES = 5\nTIMEOUT = 30", "benefit": "Indica constantes.", "context": "PEP 8.", "explanation": "Sinaliza não modificação."},
    
    # INTERMEDIÁRIO (20)
    {"icon": "✅", "title": "Context Managers Customizados", "category": "Segurança & Manutenção", "difficulty": "Intermediário", "description": "Customize context managers.", "bad_code": "lock.acquire()\ntry:\n    processar()\nfinally:\n    lock.release()", "good_code": "class LockCtx:\n    def __enter__(self):\n        self.lock.acquire()\n    def __exit__(self, *args):\n        self.lock.release()\nwith LockCtx():\n    processar()", "benefit": "Reutilizável.", "context": "Locks, transações.", "explanation": "Implementa __enter__ e __exit__."},
    {"icon": "🎯", "title": "Evitar Global Mutable State", "category": "Qualidade & Manutenção", "difficulty": "Intermediário", "description": "Não use variáveis globais mutáveis.", "bad_code": "cache = {}\ndef processar(chave):\n    global cache\n    cache[chave] = valor", "good_code": "def processar(chave: str, cache: Dict) -> Dict:\n    cache[chave] = valor\n    return cache", "benefit": "Testável.", "context": "Testes unitários.", "explanation": "Passa estado como argumento."},
    {"icon": "🚀", "title": "Generator Expressions", "category": "Performance & Elegância", "difficulty": "Intermediário", "description": "Use generators para dados grandes.", "bad_code": "quadrados = [x**2 for x in range(1000000)]\nfor q in quadrados:\n    processar(q)", "good_code": "quadrados = (x**2 for x in range(1000000))\nfor q in quadrados:\n    processar(q)", "benefit": "90% menos memória.", "context": "Dados grandes.", "explanation": "Lazy evaluation sob demanda."},
    {"icon": "🔗", "title": "Usar Decorators", "category": "Elegância & Reutilização", "difficulty": "Intermediário", "description": "Decorators adicionam comportamento.", "bad_code": "def f1():\n    inicio = time.time()\n    resultado = calc()\n    print(time.time() - inicio)\n    return resultado", "good_code": "@timing\ndef f1():\n    return calc()\n\ndef timing(func):\n    def wrapper(*args):\n        inicio = time.time()\n        resultado = func(*args)\n        print(time.time() - inicio)\n        return resultado\n    return wrapper", "benefit": "Reutilização.", "context": "Logging, cache.", "explanation": "Encapsula lógica transversal."},
    {"icon": "⚡", "title": "Usar @property", "category": "Elegância & Encapsulamento", "difficulty": "Intermediário", "description": "@property cria getters Pythônicos.", "bad_code": "class Pessoa:\n    def get_nome(self):\n        return self._nome\n    def set_nome(self, valor):\n        self._nome = valor", "good_code": "class Pessoa:\n    @property\n    def nome(self):\n        return self._nome\n    @nome.setter\n    def nome(self, valor):\n        self._nome = valor", "benefit": "Sintaxe natural.", "context": "Encapsulamento.", "explanation": "Permite p.nome = 'valor' em vez de set_nome."},
    {"icon": "🔐", "title": "namedtuple para Estruturas", "category": "Elegância & Performance", "difficulty": "Intermediário", "description": "namedtuple é mais leve que classes.", "bad_code": "class Ponto:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y", "good_code": "from collections import namedtuple\nPonto = namedtuple('Ponto', ['x', 'y'])\np = Ponto(1, 2)", "benefit": "Menos código.", "context": "Estruturas imutáveis.", "explanation": "Classes otimizadas para dados."},
    {"icon": "🎪", "title": "Map, Filter, Reduce", "category": "Elegância & Programação Funcional", "difficulty": "Intermediário", "description": "Alternativa funcional a loops.", "bad_code": "quadrados = []\nfor n in [1,2,3]:\n    quadrados.append(n**2)", "good_code": "quadrados = list(map(lambda x: x**2, [1,2,3]))\n# Ou melhor:\nquadrados = [x**2 for x in [1,2,3]]", "benefit": "Estilo funcional.", "context": "Transformações.", "explanation": "List comprehension é geralmente melhor."},
    {"icon": "🔄", "title": "functools.lru_cache", "category": "Performance & Otimização", "difficulty": "Intermediário", "description": "Cache automático de resultados.", "bad_code": "def fibonacci(n):\n    if n < 2: return n\n    return fibonacci(n-1) + fibonacci(n-2)", "good_code": "from functools import lru_cache\n\n@lru_cache(maxsize=128)\ndef fibonacci(n):\n    if n < 2: return n\n    return fibonacci(n-1) + fibonacci(n-2)", "benefit": "1000x mais rápido.", "context": "Recursão.", "explanation": "Evita recalcular resultados."},
    {"icon": "📊", "title": "*args e **kwargs", "category": "Elegância & Flexibilidade", "difficulty": "Intermediário", "description": "*args e **kwargs para argumentos variáveis.", "bad_code": "def func(a, b, c=None, d=None):\n    print(a, b, c, d)", "good_code": "def func(a, b, *args, **kwargs):\n    print(a, b)\n    print(args)\n    print(kwargs)", "benefit": "Funções flexíveis.", "context": "APIs.", "explanation": "*args em tupla, **kwargs em dict."},
    {"icon": "🎯", "title": "isinstance com Múltiplos Tipos", "category": "Qualidade & Manutenção", "difficulty": "Intermediário", "description": "isinstance pode verificar múltiplos tipos.", "bad_code": "if type(v) == int or type(v) == float:\n    print('Número')", "good_code": "if isinstance(v, (int, float)):\n    print('Número')", "benefit": "Mais conciso.", "context": "Verificação.", "explanation": "Com tupla de tipos."},
    {"icon": "🔗", "title": "pathlib vs os.path", "category": "Modernização & Legibilidade", "difficulty": "Intermediário", "description": "pathlib é mais moderno.", "bad_code": "import os\narq = os.path.join('dados', 'arquivo.txt')\nif os.path.exists(arq):\n    conteudo = open(arq).read()", "good_code": "from pathlib import Path\narq = Path('dados') / 'arquivo.txt'\nif arq.exists():\n    conteudo = arq.read_text()", "benefit": "Orientado a objetos.", "context": "Caminhos.", "explanation": "Mais moderno e portável."},
    {"icon": "🎨", "title": "f-strings Avançadas", "category": "Elegância & Legibilidade", "difficulty": "Intermediário", "description": "f-strings com formatação.", "bad_code": "print(f'Preço: ${preco}')\nprint(f'Total: ${preco * quantidade}')", "good_code": "print(f'Preço: ${preco:.2f}')\nprint(f'Total: ${preco * quantidade:>10.2f}')", "benefit": "Precisão.", "context": "Exibição.", "explanation": "Especificadores de formato."},
    {"icon": "🔐", "title": "dataclasses", "category": "Modernização & Elegância", "difficulty": "Intermediário", "description": "dataclasses automatizam boilerplate.", "bad_code": "class Pessoa:\n    def __init__(self, nome, idade):\n        self.nome = nome\n        self.idade = idade", "good_code": "from dataclasses import dataclass\n\n@dataclass\nclass Pessoa:\n    nome: str\n    idade: int", "benefit": "Menos boilerplate.", "context": "Classes simples.", "explanation": "Cria __init__, __repr__, __eq__ automaticamente."},
    {"icon": "🎯", "title": "assertRaises em Testes", "category": "Qualidade & Testes", "difficulty": "Intermediário", "description": "Teste que funções levantam exceções.", "bad_code": "try:\n    dividir(10, 0)\nexcept ZeroDivisionError:\n    print('Correto')", "good_code": "import unittest\n\nclass TestDividir(unittest.TestCase):\n    def test_divisao(self):\n        with self.assertRaises(ZeroDivisionError):\n            dividir(10, 0)", "benefit": "Testes claros.", "context": "Testes unitários.", "explanation": "Formaliza teste de exceções."},
    {"icon": "🚀", "title": "Dict e Set Comprehensions", "category": "Elegância & Performance", "difficulty": "Intermediário", "description": "Dict e set comprehensions.", "bad_code": "quadrados_dict = {}\nfor n in [1,2,3]:\n    quadrados_dict[n] = n**2", "good_code": "numeros = [1,2,3]\nquadrados_dict = {n: n**2 for n in numeros}\nunicos = {x % 2 for x in numeros}", "benefit": "Conciso.", "context": "Transformação.", "explanation": "Mesma performance que list comprehensions."},
    {"icon": "⚙️", "title": "itertools para Combinações", "category": "Performance & Elegância", "difficulty": "Intermediário", "description": "itertools para permutações.", "bad_code": "combos = []\nfor i in range(len(itens)):\n    for j in range(i+1, len(itens)):\n        combos.append((itens[i], itens[j]))", "good_code": "from itertools import combinations\ncombos = list(combinations([1,2,3], 2))", "benefit": "Simples.", "context": "Combinações.", "explanation": "Implementado em C."},
    {"icon": "🔗", "title": "super() em Herança", "category": "Elegância & Manutenção", "difficulty": "Intermediário", "description": "super() chama método da classe pai.", "bad_code": "class Cachorro(Animal):\n    def falar(self):\n        Animal.falar(self)\n        print('Au!')", "good_code": "class Cachorro(Animal):\n    def falar(self):\n        super().falar()\n        print('Au!')", "benefit": "Funciona com MRO.", "context": "Herança múltipla.", "explanation": "Respeita Method Resolution Order."},
    {"icon": "🎨", "title": "Comprehension Aninhada", "category": "Elegância & Performance", "difficulty": "Intermediário", "description": "Comprehensions podem ser aninhadas.", "bad_code": "matriz = []\nfor i in range(3):\n    linha = []\n    for j in range(3):\n        linha.append(i * j)\n    matriz.append(linha)", "good_code": "matriz = [[i*j for j in range(3)] for i in range(3)]", "benefit": "Conciso.", "context": "Transformação.", "explanation": "Legível quando bem estruturada."},
    
    # AVANÇADO (20)
    {"icon": "🎯", "title": "Slots em Classes", "category": "Performance & Otimização", "difficulty": "Avançado", "description": "__slots__ reduz consumo de memória.", "bad_code": "class Ponto:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y", "good_code": "class Ponto:\n    __slots__ = ['x', 'y']\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y", "benefit": "50% menos memória.", "context": "Milhões de objetos.", "explanation": "Sem __dict__, menos overhead."},
    {"icon": "🔐", "title": "Metaclasses", "category": "Arquitetura & Avançado", "difficulty": "Avançado", "description": "Metaclasses controlam criação de classes.", "bad_code": "class Singleton:\n    _instance = None\n    def __new__(cls):\n        if cls._instance is None:\n            cls._instance = super().__new__(cls)\n        return cls._instance", "good_code": "class SingletonMeta(type):\n    _instances = {}\n    def __call__(cls, *args):\n        if cls not in cls._instances:\n            cls._instances[cls] = super().__call__(*args)\n        return cls._instances[cls]", "benefit": "Padrões reutilizáveis.", "context": "Framework patterns.", "explanation": "Classe de classes."},
    {"icon": "⚡", "title": "Typing Avançado (Protocol)", "category": "Qualidade & Manutenção", "difficulty": "Avançado", "description": "Protocol define interfaces.", "bad_code": "def processar(obj):\n    return obj.processar()", "good_code": "from typing import Protocol\n\nclass Processavel(Protocol):\n    def processar(self) -> str: ...\n\ndef processar(obj: Processavel) -> str:\n    return obj.processar()", "benefit": "Type checking.", "context": "Estrutural subtyping.", "explanation": "Structural subtyping sem herança."},
    {"icon": "🔗", "title": "ABC (Abstract Base Classes)", "category": "Arquitetura & Design", "difficulty": "Avançado", "description": "ABC define interfaces obrigatórias.", "bad_code": "class Database:\n    def conectar(self): pass", "good_code": "from abc import ABC, abstractmethod\n\nclass Database(ABC):\n    @abstractmethod\n    def conectar(self): pass", "benefit": "Força implementação.", "context": "Frameworks.", "explanation": "Torna métodos obrigatórios."},
    {"icon": "🎪", "title": "Async/Await", "category": "Concorrência & Performance", "difficulty": "Avançado", "description": "Programação assíncrona.", "bad_code": "for url in urls:\n    response = requests.get(url)  # Bloqueia", "good_code": "async def fetch(session, url):\n    async with session.get(url) as r:\n        return await r.text()\n\nasync def main():\n    async with aiohttp.ClientSession() as s:\n        tasks = [fetch(s, u) for u in urls]\n        results = await asyncio.gather(*tasks)", "benefit": "1000x mais rápido.", "context": "Web scraping.", "explanation": "I/O sem threads."},
    {"icon": "🔐", "title": "Descriptors", "category": "Elegância & Avançado", "difficulty": "Avançado", "description": "Descriptors controlam acesso a atributos.", "bad_code": "class Pessoa:\n    def __init__(self, idade):\n        if not (0 <= idade <= 150):\n            raise ValueError()\n        self.idade = idade", "good_code": "class ValidadorIdade:\n    def __get__(self, obj, objtype=None):\n        return obj._idade if obj else self\n    def __set__(self, obj, value):\n        if not (0 <= value <= 150):\n            raise ValueError()\n        obj._idade = value\n\nclass Pessoa:\n    idade = ValidadorIdade()", "benefit": "Validação automática.", "context": "ORM.", "explanation": "Intercepta acesso a atributos."},
    {"icon": "📊", "title": "__getattr__ Dinâmico", "category": "Elegância & Flexibilidade", "difficulty": "Avançado", "description": "__getattr__ para atributos dinâmicos.", "bad_code": "class Config:\n    def __init__(self, data):\n        self.data = data\n    def get(self, key, default=None):\n        return self.data.get(key, default)", "good_code": "class Config:\n    def __init__(self, data):\n        self.data = data\n    def __getattr__(self, key):\n        return self.data.get(key)\n\nconfig = Config({'debug': True})\nprint(config.debug)", "benefit": "API Pythônica.", "context": "ORMs.", "explanation": "Chamado quando atributo não existe."},
    {"icon": "🎪", "title": "Mixin Classes", "category": "Arquitetura & Reutilização", "difficulty": "Avançado", "description": "Mixins adicionam funcionalidade.", "bad_code": "class Cachorro:\n    def latir(self): return 'Au!'\n\nclass Gato:\n    def miar(self): return 'Miau!'", "good_code": "class ComFoto:\n    def tirar_foto(self): return 'Foto'\n\nclass Cachorro(ComFoto):\n    def latir(self): return 'Au!'\n\nclass Gato(ComFoto):\n    def miar(self): return 'Miau!'", "benefit": "Reutilização.", "context": "Design patterns.", "explanation": "Classes que fornecem métodos reutilizáveis."},
    {"icon": "⚙️", "title": "__call__ para Callables", "category": "Elegância & Padrões", "difficulty": "Avançado", "description": "__call__ torna objetos chamáveis.", "bad_code": "class Multiplicador:\n    def __init__(self, fator):\n        self.fator = fator\n    def multiplicar(self, valor):\n        return valor * self.fator", "good_code": "class Multiplicador:\n    def __init__(self, fator):\n        self.fator = fator\n    def __call__(self, valor):\n        return valor * self.fator\n\nmult3 = Multiplicador(3)\nresultado = mult3(5)", "benefit": "Sintaxe natural.", "context": "Decorators.", "explanation": "Permite usar objetos como funções."},
    {"icon": "🔗", "title": "Composition vs Herança", "category": "Arquitetura & Design", "difficulty": "Avançado", "description": "Composição é mais flexível.", "bad_code": "class Automovel(Veiculo): pass\nclass Bicicleta(Veiculo): pass", "good_code": "class Motor:\n    def ligar(self): pass\n\nclass Automovel:\n    def __init__(self):\n        self.motor = Motor()", "benefit": "Flexível.", "context": "Design.", "explanation": "Has-a é melhor que is-a."},
    {"icon": "🚀", "title": "Cython para Performance", "category": "Performance & Otimização", "difficulty": "Avançado", "description": "Cython compila Python para C.", "bad_code": "def contar_pares(nums):\n    return sum(1 for n in nums if n % 2 == 0)", "good_code": "# cdef int count_pairs(list nums):\n#     cdef int count = 0\n#     for n in nums:\n#         if n % 2 == 0:\n#             count += 1\n#     return count", "benefit": "100x mais rápido.", "context": "Loops críticos.", "explanation": "Compila para C com type hints."},
    {"icon": "📊", "title": "Profiling com cProfile", "category": "Performance & Debugging", "difficulty": "Avançado", "description": "Identifique gargalos.", "bad_code": "import time\ninicio = time.time()\nfuncao_lenta()\nprint(f'Tempo: {time.time() - inicio}')", "good_code": "import cProfile\nimport pstats\n\ncProfile.run('funcao_lenta()', 'stats')\np = pstats.Stats('stats')\np.sort_stats('cumulative').print_stats(10)", "benefit": "Identifica gargalo real.", "context": "Otimização.", "explanation": "Mostra chamadas e tempo."},
    {"icon": "🔐", "title": "Memory Profiling", "category": "Performance & Debugging", "difficulty": "Avançado", "description": "Identifique vazamentos.", "bad_code": "lista_grande = [x for x in range(1000000)]", "good_code": "# python -m memory_profiler script.py\n# @profile\n# def funcao():\n#     lista = [x for x in range(100000)]", "benefit": "Identifica vazamentos.", "context": "Otimização.", "explanation": "Memória por linha."},
    {"icon": "🎯", "title": "Logging vs Print", "category": "Qualidade & Produção", "difficulty": "Avançado", "description": "logging é melhor em produção.", "bad_code": "print('Começando...')\nprint(f'Dados: {dados}')", "good_code": "import logging\nlogger = logging.getLogger(__name__)\n\nlogger.info('Começando...')\nlogger.debug(f'Dados: {dados}')", "benefit": "Configurável.", "context": "Produção.", "explanation": "Níveis e handlers configuráveis."},
    {"icon": "🔗", "title": "Pytest vs unittest", "category": "Qualidade & Testes", "difficulty": "Avançado", "description": "pytest é mais poderoso.", "bad_code": "class TestFuncao(unittest.TestCase):\n    def test_resultado(self):\n        self.assertEqual(funcao(2, 3), 5)", "good_code": "def test_resultado():\n    assert funcao(2, 3) == 5\n\ndef test_erro():\n    with pytest.raises(ValueError):\n        funcao('a', 'b')", "benefit": "Sintaxe simples.", "context": "Testes.", "explanation": "Assertions e fixtures."},
    {"icon": "📦", "title": "mypy para Type Checking", "category": "Qualidade & Manutenção", "difficulty": "Avançado", "description": "mypy valida type hints.", "bad_code": "def somar(a: int, b: int) -> int:\n    return a + b\n\nresultado = somar('2', '3')", "good_code": "# mypy script.py\n# Detecta: Argument has incompatible type\nresultado = somar('2', '3')", "benefit": "Erros antes da execução.", "context": "CI/CD.", "explanation": "Validação estática."},
    {"icon": "🚀", "title": "Dependency Injection", "category": "Arquitetura & Manutenção", "difficulty": "Avançado", "description": "Injetar dependências.", "bad_code": "class Servico:\n    def __init__(self):\n        self.db = Database()\n    def processar(self):\n        self.db.query()", "good_code": "class Servico:\n    def __init__(self, db: Database):\n        self.db = db\n    def processar(self):\n        self.db.query()\n\ndb = Database()\nservico = Servico(db)", "benefit": "Testável.", "context": "Arquitetura.", "explanation": "Desacoplado e testável."},
    {"icon": "🎨", "title": "Context Managers __enter__/__exit__", "category": "Arquitetura & Elegância", "difficulty": "Avançado", "description": "Customize com __enter__ e __exit__.", "bad_code": "def processar(transacao):\n    transacao.begin()\n    try:\n        sql.execute()\n    finally:\n        transacao.commit()", "good_code": "class Transacao:\n    def __enter__(self):\n        self.begin()\n        return self\n    def __exit__(self, *args):\n        self.commit()\n\nwith Transacao() as t:\n    sql.execute()", "benefit": "Reutilizável.", "context": "Transações.", "explanation": "Cleanup garantido."},
    {"icon": "⚡", "title": "Lazy Properties", "category": "Performance & Elegância", "difficulty": "Avançado", "description": "Calcular atributos sob demanda.", "bad_code": "class Dados:\n    def __init__(self):\n        self.resultado = self.calcular_pesado()", "good_code": "class Dados:\n    @functools.cached_property\n    def resultado(self):\n        return self.calcular_pesado()", "benefit": "Calcula apenas se usado.", "context": "Performance.", "explanation": "Caching automático."},
]

# Filtrar práticas
filtered_practices = python_practices
if selected_category != "Todas":
    filtered_practices = [p for p in filtered_practices if p["category"] == selected_category]
if selected_difficulty != "Todas":
    filtered_practices = [p for p in filtered_practices if p["difficulty"] == selected_difficulty]
if st.session_state.search_query:
    filtered_practices = [p for p in filtered_practices if st.session_state.search_query in p["title"].lower()]

# --- PRÁTICAS LISTADAS ---
st.markdown('<h2 class="section-header">📖 Melhores Práticas Python</h2>', unsafe_allow_html=True)
st.markdown(f'<p style="color: #4a5568; margin-bottom: 20px;">Mostrando {len(filtered_practices)} de {len(python_practices)} práticas</p>', unsafe_allow_html=True)

for idx, practice in enumerate(filtered_practices):
    with st.expander(f"{practice['icon']} {practice['title']} — {practice['difficulty']}", expanded=False):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"**📝 Descrição:** {practice['description']}")
            st.markdown(f"**📂 Categoria:** `{practice['category']}`")
            st.markdown(f"**⚡ Benefício:** {practice['benefit']}")
            st.markdown(f"**💡 Contexto:** {practice['context']}")
            
        with col2:
            if st.button(f"⭐ Favoritar", key=f"fav_{idx}_{practice['title']}"):
                st.session_state.favorites.add(idx)
                st.session_state.user_points += 5
                st.rerun()
            if st.button(f"✅ Aprendida", key=f"learn_{idx}_{practice['title']}"):
                st.session_state.learned.add(idx)
                st.session_state.user_points += 10
                st.rerun()
        
        st.markdown("**❌ Evitar (Bad Practice):**")
        st.code(practice["bad_code"], language="python")
        
        st.markdown("**✅ Preferir (Good Practice):**")
        st.code(practice["good_code"], language="python")
        
        st.markdown(f"**📚 Explicação:** {practice['explanation']}")

st.divider()

# --- FOOTER ---
st.markdown("""
<div style="text-align: center; padding: 40px 0; border-top: 1px solid rgba(255,255,255,0.04); color: #2d3748;">
    <p style="margin-bottom: 10px; font-size: 0.92rem;">
        <span style="font-family:'Syne',sans-serif; color: #a78bfa; font-weight: 700;">Python - Melhores Práticas</span> 
        &nbsp;•&nbsp; Inspirado em Rodrigo Aiosa
    </p>
    <p style="font-size: 0.82rem; font-weight:300;">
        Transforme seu código Python em produção robusta e escalável
    </p>
</div>
<div style="height: 60px;"></div>
""", unsafe_allow_html=True)
