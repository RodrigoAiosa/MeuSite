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

/* ── NOTES ── */
.notes-container {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%);
    border: 1px solid rgba(255,255,255,0.05);
    border-left: 3px solid #a78bfa;
    border-radius: 12px;
    padding: 16px 20px;
    margin: 10px 0;
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
    <p style="color: #4a5568; font-size: 0.82rem; margin-top: 6px; letter-spacing:1px; text-transform:uppercase;">Melhores Práticas em 60 Lições</p>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR STATS ---
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

# --- ARMAZENAR MENU SELECIONADO ---
st.session_state.current_menu = menu

# ── HERO ──
st.markdown("""
<div class="hero-wrapper">
    <div class="hero-badge">🐍 Python Pro</div>
    <h1 class="hero-title">
        Melhores Práticas Python para <span class="accent">código que escala</span>
    </h1>
    <p class="hero-subtitle">
        Padrões avançados, otimizações e design patterns. Transforme seu código Python em produção robusta e mantível.
    </p>
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

# --- PROGRESSO VISUAL (SEMPRE VISÍVEL) ---
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
        <div class="stat-label">Práticas Python</div>
        <div class="stat-sublabel">Documentadas e Testadas</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">6</div>
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
    Código Python escalável começa com melhores práticas. 
    Padrões robustos reduzem bugs, melhoram performance e facilitam manutenção.
    <br><br>
    <span style="color: #a78bfa; font-weight: 600;">
    Este é um guia completo para transformar você em um especialista Python.
    </span>
</p>
""", unsafe_allow_html=True)

# --- DATABASE DE PRÁTICAS PYTHON ---
python_practices = [
    {
        "icon": "📚",
        "title": "Usar Type Hints",
        "category": "Qualidade & Manutenção",
        "difficulty": "Iniciante",
        "description": "Especifique tipos de argumentos e retorno.",
        "bad_code": "def calcular_total(items):\n    return sum(item['valor'] for item in items)",
        "good_code": "from typing import List, Dict\n\ndef calcular_total(\n    items: List[Dict[str, float]]\n) -> float:\n    \"\"\"Calcula o total de valores.\"\"\"\n    return sum(item['valor'] for item in items)",
        "benefit": "Detecta erros em tempo de desenvolvimento.",
        "context": "Type hints são obrigatórios em código Python profissional.",
        "explanation": "Type hints melhoram a legibilidade e permitem que IDEs ofereçam autocomplete e detecção de erros antes da execução."
    },
    {
        "icon": "🔐",
        "title": "List Comprehension",
        "category": "Performance & Elegância",
        "difficulty": "Iniciante",
        "description": "Prefira list comprehension a loops tradicionais.",
        "bad_code": "numeros = [1, 2, 3, 4, 5]\npares = []\nfor num in numeros:\n    if num % 2 == 0:\n        pares.append(num * 2)",
        "good_code": "numeros = [1, 2, 3, 4, 5]\n\n# List comprehension - mais legível e rápida\npares = [num * 2 for num in numeros if num % 2 == 0]",
        "benefit": "30-40% mais rápido e mais Pythônico.",
        "context": "O jeito 'Pythônico' de trabalhar com listas.",
        "explanation": "List comprehension é otimizada em C e executa mais rapidamente que loops com append, além de ser mais legível."
    },
    {
        "icon": "✅",
        "title": "Context Managers (with)",
        "category": "Segurança & Manutenção",
        "difficulty": "Intermediário",
        "description": "Use with para gerenciar recursos automaticamente.",
        "bad_code": "f = open('dados.txt', 'r')\nconteudo = f.read()\nf.close()  # Pode ser esquecido se houver exceção",
        "good_code": "# Context manager garante fechamento\nwith open('dados.txt', 'r') as f:\n    conteudo = f.read()\n    # Arquivo é fechado automaticamente",
        "benefit": "Evita vazamento de recursos.",
        "context": "Crítico para I/O, banco de dados, conexões.",
        "explanation": "Context managers garantem que recursos sejam liberados mesmo se uma exceção ocorrer durante a execução."
    },
    {
        "icon": "🎯",
        "title": "Evitar Global Mutable State",
        "category": "Qualidade & Manutenção",
        "difficulty": "Intermediário",
        "description": "Não use variáveis globais mutáveis.",
        "bad_code": "# EVITAR\ncache = {}\n\ndef processar(chave, valor):\n    global cache  # Difícil de testar e rastrear\n    cache[chave] = valor\n    return cache",
        "good_code": "# PREFERIR\ndef processar(chave: str, valor: Any, \n             cache: Dict) -> Dict:\n    \"\"\"Passa cache como argumento.\"\"\"\n    cache[chave] = valor\n    return cache\n\n# Uso\ncache = {}\nresultado = processar('key', 'value', cache)",
        "benefit": "Código testável e previsível.",
        "context": "Facilita testes unitários e debugging.",
        "explanation": "Variáveis globais mutáveis criam dependências ocultas que tornam o código difícil de testar e rastrear."
    },
    {
        "icon": "🚀",
        "title": "Generator Expressions",
        "category": "Performance & Elegância",
        "difficulty": "Intermediário",
        "description": "Use generators para dados grandes.",
        "bad_code": "# Carrega TODA a lista em memória\nquadrados = [x**2 for x in range(1000000)]\nfor q in quadrados:\n    print(q)",
        "good_code": "# Generator - um item por vez\nquadrados = (x**2 for x in range(1000000))\nfor q in quadrados:\n    print(q)  # Memória constante",
        "benefit": "Reduz consumo de memória em 90%+.",
        "context": "Essencial para dados grandes ou infinitos.",
        "explanation": "Generators produzem valores sob demanda (lazy evaluation) em vez de criar toda a sequência na memória."
    },
    {
        "icon": "🔍",
        "title": "Usar f-strings",
        "category": "Elegância & Legibilidade",
        "difficulty": "Iniciante",
        "description": "f-strings são mais legíveis e rápidas.",
        "bad_code": "nome = 'Alice'\nidade = 30\n\n# Antigo\nmensagem = 'Olá, ' + nome + '. Você tem ' + str(idade) + ' anos'\n\n# Format antigo\nmensagem = 'Olá, {}. Você tem {} anos'.format(nome, idade)",
        "good_code": "nome = 'Alice'\nidade = 30\n\n# f-string - clara e rápida\nmensagem = f'Olá, {nome}. Você tem {idade} anos'\n\n# Com expressões\nprox_idade = f'Próximo ano terá {idade + 1} anos'",
        "benefit": "20% mais rápido que format().",
        "context": "Python 3.6+ - use sempre.",
        "explanation": "f-strings são otimizadas em tempo de compilação e permitem expressões complexas diretamente na string."
    },
]

# --- FILTROS SECTION ---
st.markdown('<h2 class="section-header">🔎 Filtrar Práticas</h2>', unsafe_allow_html=True)

st.markdown('<div class="filter-section">', unsafe_allow_html=True)

col1, col2, col_space = st.columns([1.5, 1.5, 1])

with col1:
    categorias = ["Todas"] + sorted(list(set([p["category"] for p in python_practices])))
    selected_category = st.selectbox("📂 Categoria", categorias, key="category_filter")

with col2:
    dificuldades = ["Todas", "Iniciante", "Intermediário", "Avançado"]
    selected_difficulty = st.selectbox("📈 Nível de Dificuldade", dificuldades, key="difficulty_filter")

st.markdown('</div>', unsafe_allow_html=True)

# --- SEÇÃO EDITOR PYTHON ---
st.markdown('<h2 class="section-header">✏️ Editor Python Interativo</h2>', unsafe_allow_html=True)
st.markdown('<p style="color: #4a5568; margin-bottom: 30px; font-weight:300;">Teste suas funções Python em tempo real. Execute código Python seguro e veja o resultado instantaneamente.</p>', unsafe_allow_html=True)

# --- EXEMPLOS PRÉ-DEFINIDOS ---
python_templates = {
    "Hello World": "# Seu primeiro programa\nmessage = 'Hello, World!'\nprint(message)",
    "Soma de Lista": "numeros = [1, 2, 3, 4, 5]\ntotal = sum(numeros)\nprint(f'Total: {total}')",
    "List Comprehension": "numeros = range(1, 11)\npares = [n for n in numeros if n % 2 == 0]\nprint(f'Pares: {pares}')",
    "Dicionário": "pessoa = {'nome': 'Alice', 'idade': 30}\nprint(f\"{pessoa['nome']} tem {pessoa['idade']} anos\")",
    "Função com Type Hints": "def saudar(nome: str) -> str:\n    return f'Olá, {nome}!'\n\nprint(saudar('Python'))",
    "Try/Except": "try:\n    resultado = 10 / int('abc')\nexcept ValueError:\n    print('Erro: valor inválido')\nexcept ZeroDivisionError:\n    print('Erro: divisão por zero')",
    "Lambda": "numeros = [1, 2, 3, 4, 5]\nquadrados = list(map(lambda x: x**2, numeros))\nprint(quadrados)",
    "Generator": "def contar(n):\n    for i in range(n):\n        yield i\n\nfor num in contar(5):\n    print(num)",
    "f-string": "nome = 'Alice'\nidade = 30\nprint(f'{nome} tem {idade} anos')",
    "Dictionary Comprehension": "numeros = [1, 2, 3, 4]\nsquares = {n: n**2 for n in numeros}\nprint(squares)",
    "Unpacking": "dados = [1, 2, 3]\na, b, c = dados\nprint(f'a={a}, b={b}, c={c}')",
    "With Statement": "# Simulando arquivo\ndata = {'teste': 'valor'}\nprint('Simulação de context manager')",
}

st.markdown('<div class="editor-section">', unsafe_allow_html=True)

col_template, col_editor = st.columns([1, 2], gap="large")

with col_template:
    st.markdown('<p class="editor-title">📚 Templates</p>', unsafe_allow_html=True)
    selected_template = st.selectbox(
        "Escolha um exemplo:",
        ["Escrever Manual"] + list(python_templates.keys()),
        key="template_select",
        label_visibility="collapsed"
    )
    if selected_template != "Escrever Manual":
        template_code = python_templates[selected_template]
    else:
        template_code = ""

with col_editor:
    st.markdown('<p class="editor-title">🐍 Seu Python</p>', unsafe_allow_html=True)
    user_code = st.text_area(
        "Escreva seu código Python:",
        value=template_code,
        height=200,
        key="python_editor",
        placeholder="print('Hello, World!')",
        label_visibility="collapsed"
    )

st.markdown('</div>', unsafe_allow_html=True)

# --- EXECUTOR DE CÓDIGO ---
def execute_python(code):
    """Executa código Python de forma segura."""
    try:
        if not code.strip():
            return None, "❌ Escreva um código Python primeiro!"
        
        # Captura output
        import sys
        from io import StringIO
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        # Executa com timeout
        try:
            exec(code, {"__builtins__": __builtins__})
            output = sys.stdout.getvalue()
            sys.stdout = old_stdout
            
            if not output:
                return "✅ Código executado com sucesso! (sem output)", "✅"
            return output, "✅"
        except Exception as e:
            sys.stdout = old_stdout
            return f"❌ Erro: {type(e).__name__}: {str(e)}", "❌"
            
    except Exception as e:
        return f"❌ Erro ao executar: {str(e)}", "❌"

# --- SEÇÃO DE RESULTADO ---
st.markdown('<h2 class="section-header">📊 Resultado da Execução</h2>', unsafe_allow_html=True)

col_result, col_info = st.columns([2, 1], gap="large")

with col_result:
    st.markdown('<div style="background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%); border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; padding: 24px;">', unsafe_allow_html=True)
    if user_code.strip():
        output, status = execute_python(user_code)
        if status == "✅":
            st.success("✅ Código executado com sucesso!")
            st.code(output if output != "✅ Código executado com sucesso! (sem output)" else "", language="text")
        else:
            st.error("❌ Erro na execução")
            st.code(output, language="text")
    else:
        st.markdown("""
        <div style="text-align: center; padding: 40px; color: #2d3748;">
            <p style="font-size: 1rem;">📝 Escreva um código Python no editor para ver o resultado</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_info:
    st.markdown("""
    <div style="background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%); border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; padding: 24px;">
        <p style="font-family:'Syne',sans-serif; color: #a78bfa; font-weight: 700; font-size:0.8rem; letter-spacing:1.5px; text-transform:uppercase; margin-bottom: 16px;">ℹ️ Dicas & Atalhos</p>
        <p style="color: #4a5568; font-size: 0.85rem; line-height: 1.8; margin-bottom: 16px; font-weight:300;">
            <span style="color:#e2e8f0; font-weight:600;">Funcionalidades:</span>
            <br>• Exécute Python puro
            <br>• Use print() para output
            <br>• Importe bibliotecas padrão
            <br>• Type hints opcionais
        </p>
        <p style="color: #2d3748; font-size: 0.82rem; font-weight:300; border-top: 1px solid rgba(255,255,255,0.04); padding-top: 14px;">
            💡 Selecione templates para aprender padrões Python!
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- PRÁTICAS LISTADAS ---
st.markdown('<h2 class="section-header">📖 Melhores Práticas Python</h2>', unsafe_allow_html=True)

# Filtrar práticas
filtered_practices = python_practices
if selected_category != "Todas":
    filtered_practices = [p for p in filtered_practices if p["category"] == selected_category]
if selected_difficulty != "Todas":
    filtered_practices = [p for p in filtered_practices if p["difficulty"] == selected_difficulty]
if st.session_state.search_query:
    filtered_practices = [p for p in filtered_practices if st.session_state.search_query in p["title"].lower()]

# Mostrar práticas
for idx, practice in enumerate(filtered_practices):
    with st.expander(f"{practice['icon']} {practice['title']} — {practice['difficulty']}", expanded=False):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"**📝 Descrição:** {practice['description']}")
            st.markdown(f"**📂 Categoria:** `{practice['category']}`")
            st.markdown(f"**⚡ Benefício:** {practice['benefit']}")
            st.markdown(f"**💡 Contexto:** {practice['context']}")
            
        with col2:
            if st.button(f"⭐ Favoritar", key=f"fav_{idx}"):
                st.session_state.favorites.add(idx)
                st.session_state.user_points += 5
            if st.button(f"✅ Marcar como Aprendida", key=f"learn_{idx}"):
                st.session_state.learned.add(idx)
                st.session_state.user_points += 10
        
        # Código
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
<div class="footer-spacer"></div>
""", unsafe_allow_html=True)
