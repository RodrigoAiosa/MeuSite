import streamlit as st
import sys
from io import StringIO
from datetime import datetime
import json

st.set_page_config(
    page_title="Python - Melhores Práticas Pro",
    page_icon="🐍",
    layout="wide"
)

# --- INICIALIZAR SESSION STATE ---
if 'python_favorites' not in st.session_state:
    st.session_state.python_favorites = set()
if 'python_learned' not in st.session_state:
    st.session_state.python_learned = set()
if 'python_points' not in st.session_state:
    st.session_state.python_points = 0
if 'python_level' not in st.session_state:
    st.session_state.python_level = 1
if 'python_xp' not in st.session_state:
    st.session_state.python_xp = 0
if 'python_badges' not in st.session_state:
    st.session_state.python_badges = set()
if 'python_challenges_completed' not in st.session_state:
    st.session_state.python_challenges_completed = set()
if 'python_streak' not in st.session_state:
    st.session_state.python_streak = 0
if 'python_last_session' not in st.session_state:
    st.session_state.python_last_session = None

MASTERY_LEVELS = {
    1: {"title": "🥉 Python Padawan", "icon": "🥉", "xp_required": 0, "color": "#CD7F32", "theme": "bronze"},
    2: {"title": "🥈 Code Ninja", "icon": "🥈", "xp_required": 250, "color": "#C0C0C0", "theme": "silver"},
    3: {"title": "🥇 Python Master", "icon": "🥇", "xp_required": 750, "color": "#FFD700", "theme": "gold"},
    4: {"title": "💎 Arquiteto Python", "icon": "💎", "xp_required": 1500, "color": "#00D9FF", "color_rgb": "rgb(0, 217, 255)", "theme": "diamond"},
    5: {"title": "🏆 Pythonista Elite", "icon": "🏆", "xp_required": 2500, "color": "#FF1493", "theme": "legendary"},
}

BADGES = {
    "first_steps": {"icon": "👣", "title": "Primeiros Passos", "description": "Completou a 1ª prática", "condition": lambda p: p >= 1},
    "ten_practices": {"icon": "🔟", "title": "Persistência", "description": "Completou 10 práticas", "condition": lambda p: p >= 10},
    "twenty_practices": {"icon": "2️⃣0️⃣", "title": "Veterano", "description": "Completou 20 práticas", "condition": lambda p: p >= 20},
    "beginner_master": {"icon": "📚", "title": "Mestre Iniciante", "description": "Completou todas as práticas Iniciante", "condition": lambda p: p >= 20},
    "code_ninja": {"icon": "🥷", "title": "Código Ninja", "description": "Completou 5 práticas Intermediário", "condition": lambda p: p >= 5},
    "advanced_warrior": {"icon": "⚔️", "title": "Guerreiro Avançado", "description": "Completou 5 práticas Avançado", "condition": lambda p: p >= 5},
    "speed_demon": {"icon": "⚡", "title": "Demônio da Velocidade", "description": "Executou 50 scripts no editor", "condition": lambda p: p >= 50},
    "favorite_collector": {"icon": "⭐", "title": "Colecionador", "description": "Favoritou 10 práticas", "condition": lambda p: p >= 10},
    "perfect_streak": {"icon": "🔥", "title": "Em Chamas", "description": "7 dias seguidos aprendendo", "condition": lambda p: p >= 7},
    "code_master": {"icon": "👑", "title": "Rei do Código", "description": "1000+ pontos conquistados", "condition": lambda p: p >= 1000},
}

CHALLENGES = [
    {"id": "challenge_1", "title": "Mestre de List Comprehension", "difficulty": "Intermediário", "xp_reward": 100, "description": "Complete 3 práticas sobre List Comprehension", "target": 3, "type": "practices", "practice_filter": "List Comprehension"},
    {"id": "challenge_2", "title": "Decorador Profissional", "difficulty": "Avançado", "xp_reward": 150, "description": "Complete 2 práticas sobre Decorators", "target": 2, "type": "practices", "practice_filter": "Decorators"},
    {"id": "challenge_3", "title": "Editor Speedrunner", "difficulty": "Iniciante", "xp_reward": 50, "description": "Execute 20 scripts no editor interativo", "target": 20, "type": "editor_runs"},
    {"id": "challenge_4", "title": "Colecionador de Estrelas", "difficulty": "Iniciante", "xp_reward": 75, "description": "Favoritou 5 práticas", "target": 5, "type": "favorites"},
    {"id": "challenge_5", "title": "Generador de Poder", "difficulty": "Avançado", "xp_reward": 200, "description": "Complete todas as práticas sobre Generators", "target": 3, "type": "practices", "practice_filter": "Generator"},
]

# ── DESIGN (mesma paleta SQL Pro) ──
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
.stat-card:hover {
    transform: translateY(-4px);
    border-color: rgba(167,139,250,0.4);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}
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

/* ── LEVEL / BADGES / CHALLENGES ── */
.level-bronze { border-color: #CD7F32; color: #CD7F32; box-shadow: 0 0 20px rgba(205,127,50,0.3); }
.level-silver { border-color: #C0C0C0; color: #C0C0C0; box-shadow: 0 0 20px rgba(192,192,192,0.3); }
.level-gold { border-color: #FFD700; color: #FFD700; box-shadow: 0 0 20px rgba(255,215,0,0.3); }
.level-diamond { border-color: #00D9FF; color: #00D9FF; box-shadow: 0 0 20px rgba(0,217,255,0.5); }
.level-legendary { border-color: #FF1493; color: #FF1493; box-shadow: 0 0 20px rgba(255,20,147,0.5); animation: pulse 2s infinite; }

@keyframes pulse {
    0% { box-shadow: 0 0 20px rgba(255,20,147,0.5); }
    50% { box-shadow: 0 0 40px rgba(255,20,147,0.8); }
    100% { box-shadow: 0 0 20px rgba(255,20,147,0.5); }
}

.badge-container { display: flex; flex-wrap: wrap; gap: 10px; margin: 15px 0; }

.badge {
    background: linear-gradient(145deg, rgba(255,255,255,0.05) 0%, rgba(0,0,0,0.3) 100%);
    border: 1px solid rgba(167,139,250,0.2);
    border-radius: 10px;
    padding: 10px 15px;
    text-align: center;
    font-size: 2rem;
    cursor: pointer;
    transition: all 0.3s ease;
}
.badge:hover { transform: scale(1.1); border-color: #a78bfa; box-shadow: 0 0 15px rgba(167,139,250,0.3); }
.badge-locked { opacity: 0.3; }

.challenge-box {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%);
    border: 1px solid rgba(167,139,250,0.2);
    border-radius: 12px;
    padding: 15px;
    margin: 10px 0;
}
.challenge-completed { border-color: #22c55e; background: linear-gradient(145deg, rgba(34,197,94,0.1) 0%, rgba(0,0,0,0.2) 100%); }

.streak-fire { font-size: 2rem; animation: bounce 1s infinite; }
@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

.output-box {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%);
    border: 1px solid rgba(167,139,250,0.2);
    border-radius: 12px;
    padding: 15px;
    margin-top: 15px;
    font-family: 'Courier New', monospace;
    color: #a78bfa;
    white-space: pre-wrap;
    word-wrap: break-word;
}
.error-box {
    background: linear-gradient(145deg, rgba(239,68,68,0.1) 0%, rgba(239,68,68,0.05) 100%);
    border: 1px solid rgba(239,68,68,0.3);
    border-radius: 12px;
    padding: 15px;
    margin-top: 15px;
    font-family: 'Courier New', monospace;
    color: #ff6b6b;
    white-space: pre-wrap;
    word-wrap: break-word;
}
.success-box {
    background: linear-gradient(145deg, rgba(34,197,94,0.1) 0%, rgba(34,197,94,0.05) 100%);
    border: 1px solid rgba(34,197,94,0.3);
    border-radius: 12px;
    padding: 15px;
    margin-top: 15px;
    font-family: 'Courier New', monospace;
    color: #22c55e;
    white-space: pre-wrap;
    word-wrap: break-word;
}
.achievement-pop { animation: slideIn 0.5s ease-out; }
@keyframes slideIn {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* ── INPUTS ── */
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
}
hr {
    border: none !important;
    border-top: 1px solid rgba(167,139,250,0.1) !important;
    margin: 40px 0 !important;
}
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0a0e27; }
::-webkit-scrollbar-thumb { background: rgba(167,139,250,0.2); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(167,139,250,0.4); }
</style>
""", unsafe_allow_html=True)

# ── HERO (idêntico ao SQL Pro, adaptado para Python) ──
st.markdown("""
<div class="hero-wrapper">
    <h1 class="hero-title">
        Melhores Práticas Python para <span class="accent">código que escala</span>
    </h1>
    <p class="hero-subtitle">
        Estratégias avançadas para código limpo, performático e manutenível.
        Transforme seus projetos em referências de qualidade.
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

# --- FUNÇÕES AUXILIARES ---
def get_current_level(xp):
    for level in sorted(MASTERY_LEVELS.keys(), reverse=True):
        if xp >= MASTERY_LEVELS[level]["xp_required"]:
            return level
    return 1

def get_xp_for_next_level(current_level):
    if current_level >= 5:
        return MASTERY_LEVELS[5]["xp_required"] + 1000
    return MASTERY_LEVELS[current_level + 1]["xp_required"]

def get_xp_progress(xp, current_level):
    current_level_xp = MASTERY_LEVELS[current_level]["xp_required"]
    next_level_xp = get_xp_for_next_level(current_level)
    progress = ((xp - current_level_xp) / (next_level_xp - current_level_xp)) * 100
    return min(100, max(0, progress))

def check_badges(learned_count, favorites_count, editor_runs, points):
    new_badges = set()
    if learned_count >= 1: new_badges.add("first_steps")
    if learned_count >= 10: new_badges.add("ten_practices")
    if learned_count >= 20: new_badges.add("twenty_practices")
    if favorites_count >= 10: new_badges.add("favorite_collector")
    if points >= 1000: new_badges.add("code_master")
    return new_badges

def get_level_color_class(level):
    colors = {1: "level-bronze", 2: "level-silver", 3: "level-gold", 4: "level-diamond", 5: "level-legendary"}
    return colors.get(level, "level-bronze")

# --- HEADER PONTOS + STREAK ---
col1, col2, col3 = st.columns([2, 3, 2])
with col1:
    st.markdown(f'<h1 style="text-align: center; color: #a78bfa; font-family: Syne, sans-serif;">🐍 Python Pro</h1>', unsafe_allow_html=True)
with col2:
    st.markdown('<h3 style="text-align: center; color: #7c3aed;">Jornada de Maestria</h3>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<h1 style="text-align: center; font-size: 2rem;">⭐ {st.session_state.python_points} pontos</h1>', unsafe_allow_html=True)

current_level = get_current_level(st.session_state.python_xp)
current_xp = st.session_state.python_xp
level_info = MASTERY_LEVELS[current_level]
xp_progress = get_xp_progress(current_xp, current_level)
next_level_xp = get_xp_for_next_level(current_level)
current_level_xp = MASTERY_LEVELS[current_level]["xp_required"]

if st.session_state.python_streak > 0:
    st.markdown(f'<p style="text-align: center; font-size: 1.3rem;"><span class="streak-fire">🔥</span> {st.session_state.python_streak} dias em sequência!</p>', unsafe_allow_html=True)

# --- TABS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📚 Práticas", "✏️ Editor", "🎯 Desafios", "🏆 Badges", "📊 Perfil"])

# ============================================================================
# TAB 1: PRÁTICAS
# ============================================================================
with tab1:
    st.markdown('<h3 class="section-header">🔎 Filtrar Práticas</h3>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        selected_difficulty = st.selectbox("📈 Nível de Dificuldade", ["Todas", "Iniciante", "Intermediário", "Avançado"], key="python_difficulty")
    with col2:
        search = st.text_input("🔍 Buscar prática", key="python_search")

    python_practices = [
        {"icon": "📚", "title": "Usar Type Hints", "category": "Qualidade & Manutenção", "difficulty": "Iniciante", "description": "Especifique tipos de argumentos e retorno.", "bad_code": "def calcular_total(items):\n    return sum(item['valor'] for item in items)", "good_code": "from typing import List, Dict\n\ndef calcular_total(items: List[Dict[str, float]]) -> float:\n    return sum(item['valor'] for item in items)", "benefit": "Detecta erros em tempo de desenvolvimento.", "explanation": "Type hints melhoram legibilidade e oferecem autocomplete."},
        {"icon": "🔐", "title": "List Comprehension", "category": "Performance & Elegância", "difficulty": "Iniciante", "description": "Prefira list comprehension a loops tradicionais.", "bad_code": "pares = []\nfor num in [1,2,3,4,5]:\n    if num % 2 == 0:\n        pares.append(num * 2)", "good_code": "pares = [num * 2 for num in [1,2,3,4,5] if num % 2 == 0]", "benefit": "30-40% mais rápido.", "explanation": "Otimizada em C, executa mais rápido."},
        {"icon": "🔍", "title": "Usar f-strings", "category": "Elegância & Legibilidade", "difficulty": "Iniciante", "description": "f-strings são mais legíveis e rápidas.", "bad_code": "nome = 'Alice'\nidade = 30\nmsg = 'Olá, ' + nome + '. Você tem ' + str(idade) + ' anos'", "good_code": "nome = 'Alice'\nidade = 30\nmsg = f'Olá, {nome}. Você tem {idade} anos'", "benefit": "20% mais rápido.", "explanation": "Otimizadas em tempo de compilação."},
        {"icon": "📋", "title": "Usar Docstrings", "category": "Qualidade & Manutenção", "difficulty": "Iniciante", "description": "Documente funções com docstrings.", "bad_code": "def calcular_idade(ano_nascimento):\n    return 2024 - ano_nascimento", "good_code": "def calcular_idade(ano_nascimento: int) -> int:\n    \"\"\"Calcula a idade de uma pessoa.\n    \n    Args:\n        ano_nascimento: Ano de nascimento\n    Returns:\n        Idade em anos\n    \"\"\"", "benefit": "Facilita manutenção.", "explanation": "Acessíveis via help()."},
        {"icon": "✅", "title": "Usar Dicionários", "category": "Elegância & Legibilidade", "difficulty": "Iniciante", "description": "Agrupe dados relacionados.", "bad_code": "pessoa_nome = 'Alice'\npessoa_idade = 30", "good_code": "pessoa = {'nome': 'Alice', 'idade': 30}", "benefit": "Código organizado.", "explanation": "Agrupa dados logicamente."},
        {"icon": "🎯", "title": "Usar enumerate()", "category": "Elegância & Legibilidade", "difficulty": "Iniciante", "description": "Acesse índice e valor simultaneamente.", "bad_code": "for i in range(len(nomes)):\n    print(f'{i}: {nomes[i]}')", "good_code": "for i, nome in enumerate(nomes):\n    print(f'{i}: {nome}')", "benefit": "Mais legível.", "explanation": "Evita erros de indexação."},
        {"icon": "🔄", "title": "Usar zip()", "category": "Elegância & Legibilidade", "difficulty": "Iniciante", "description": "Combine múltiplas iteráveis.", "bad_code": "for i in range(len(nomes)):\n    print(f'{nomes[i]} - {idades[i]}')", "good_code": "for nome, idade in zip(nomes, idades):\n    print(f'{nome} - {idade}')", "benefit": "Mais seguro.", "explanation": "Mais eficiente que indexação."},
        {"icon": "🛡️", "title": "Try/Except Específicos", "category": "Qualidade & Manutenção", "difficulty": "Iniciante", "description": "Capture exceções específicas.", "bad_code": "try:\n    valor = int('abc')\nexcept:\n    print('Erro')", "good_code": "try:\n    valor = int('abc')\nexcept ValueError:\n    print('Erro: valor inválido')", "benefit": "Precisão.", "explanation": "Capturar específico evita silenciar bugs."},
        {"icon": "🔑", "title": "Usar dict.get()", "category": "Elegância & Legibilidade", "difficulty": "Iniciante", "description": "Acesse dicionários com segurança.", "bad_code": "if 'timeout' in config:\n    timeout = config['timeout']\nelse:\n    timeout = 30", "good_code": "timeout = config.get('timeout', 30)", "benefit": "Mais limpo.", "explanation": "Retorna padrão se chave não existir."},
        {"icon": "⚡", "title": "Usar all() e any()", "category": "Elegância & Legibilidade", "difficulty": "Iniciante", "description": "Verifique condições lógicas.", "bad_code": "resultado = True\nfor item in lista:\n    if not item:\n        resultado = False", "good_code": "resultado = all(lista)\nqualquer = any(lista)", "benefit": "Mais legível.", "explanation": "Implementadas em C."},
        {"icon": "🔓", "title": "Context Managers (with)", "category": "Segurança & Manutenção", "difficulty": "Iniciante", "description": "Gerencie recursos automaticamente.", "bad_code": "f = open('dados.txt')\nconteudo = f.read()\nf.close()", "good_code": "with open('dados.txt') as f:\n    conteudo = f.read()", "benefit": "Fechamento garantido.", "explanation": "Garante cleanup automático."},
        {"icon": "🎓", "title": "isinstance() vs type()", "category": "Qualidade & Manutenção", "difficulty": "Iniciante", "description": "Verifique tipos corretamente.", "bad_code": "if type(valor) == str:\n    print('É string')", "good_code": "if isinstance(valor, str):\n    print('É string')", "benefit": "Respeita herança.", "explanation": "Funciona com subclasses."},
        {"icon": "🔀", "title": "sorted() vs sort()", "category": "Elegância & Legibilidade", "difficulty": "Iniciante", "description": "Escolha a versão correta.", "bad_code": "numeros = [3, 1, 4]\nnumeros.sort()", "good_code": "numeros = [3, 1, 4]\nordenados = sorted(numeros)", "benefit": "Original intacto.", "explanation": "Mais funcional."},
        {"icon": "💾", "title": "defaultdict", "category": "Performance & Elegância", "difficulty": "Iniciante", "description": "Inicialize automaticamente.", "bad_code": "palavras = {}\nfor p in lista:\n    if p not in palavras:\n        palavras[p] = 0\n    palavras[p] += 1", "good_code": "from collections import defaultdict\npedras = defaultdict(int)\nfor p in lista:\n    pedras[p] += 1", "benefit": "Código limpo.", "explanation": "Cria valores padrão."},
        {"icon": "🚀", "title": "Evitar Variáveis Globais", "category": "Qualidade & Manutenção", "difficulty": "Iniciante", "description": "Passe dados como argumentos.", "bad_code": "contador = 0\ndef incrementar():\n    global contador\n    contador += 1", "good_code": "def incrementar(contador: int) -> int:\n    return contador + 1", "benefit": "Testável.", "explanation": "Evita dependências ocultas."},
        {"icon": "⚙️", "title": "Constants em UPPERCASE", "category": "Qualidade & Manutenção", "difficulty": "Iniciante", "description": "Nomeie constantes corretamente.", "bad_code": "max_retries = 5\ntimeout = 30", "good_code": "MAX_RETRIES = 5\nTIMEOUT = 30", "benefit": "Indica constantes.", "explanation": "Sinaliza não modificação."},
        {"icon": "🎪", "title": "String methods vs regex", "category": "Performance & Elegância", "difficulty": "Iniciante", "description": "Use método simples quando possível.", "bad_code": "import re\nif re.search(r'mundo', texto):\n    print('Encontrado')", "good_code": "if 'mundo' in texto:\n    print('Encontrado')", "benefit": "10x mais rápido.", "explanation": "Otimizadas em C."},
        {"icon": "📦", "title": "setdefault()", "category": "Performance & Elegância", "difficulty": "Iniciante", "description": "Define e retorna simultaneamente.", "bad_code": "if 'python' not in cat:\n    cat['python'] = []\ncat['python'].append('item')", "good_code": "cat.setdefault('python', []).append('item')", "benefit": "Uma linha.", "explanation": "Combina verificação e atribuição."},
        {"icon": "🔍", "title": "in vs count()", "category": "Performance & Elegância", "difficulty": "Iniciante", "description": "Use in para verificar existência.", "bad_code": "if lista.count(3) > 0:\n    print('Existe')", "good_code": "if 3 in lista:\n    print('Existe')", "benefit": "3x mais rápido.", "explanation": "Sem criar contador."},
        {"icon": "🔗", "title": "Usar Decorators", "category": "Elegância & Reutilização", "difficulty": "Intermediário", "description": "Reutilize lógica comum.", "bad_code": "def f1():\n    inicio = time.time()\n    resultado = calc()\n    print(time.time() - inicio)\n    return resultado", "good_code": "@timing\ndef f1():\n    return calc()\n\ndef timing(func):\n    def wrapper(*args):\n        inicio = time.time()\n        resultado = func(*args)\n        print(time.time() - inicio)\n        return resultado\n    return wrapper", "benefit": "Reutilização.", "explanation": "Encapsula lógica transversal."},
        {"icon": "⚡", "title": "Usar @property", "category": "Elegância & Encapsulamento", "difficulty": "Intermediário", "description": "Crie getters/setters Pythônicos.", "bad_code": "class Pessoa:\n    def get_nome(self):\n        return self._nome", "good_code": "class Pessoa:\n    @property\n    def nome(self):\n        return self._nome", "benefit": "Sintaxe natural.", "explanation": "Permite p.nome = 'valor'."},
        {"icon": "🚀", "title": "Generator Expressions", "category": "Performance & Elegância", "difficulty": "Intermediário", "description": "Economize memória com generators.", "bad_code": "quadrados = [x**2 for x in range(1000000)]\nfor q in quadrados:\n    processar(q)", "good_code": "quadrados = (x**2 for x in range(1000000))\nfor q in quadrados:\n    processar(q)", "benefit": "90% menos memória.", "explanation": "Lazy evaluation."},
        {"icon": "🔐", "title": "namedtuple", "category": "Elegância & Performance", "difficulty": "Intermediário", "description": "Estruturas leves e imutáveis.", "bad_code": "class Ponto:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y", "good_code": "from collections import namedtuple\nPonto = namedtuple('Ponto', ['x', 'y'])\np = Ponto(1, 2)", "benefit": "Menos código.", "explanation": "Classes otimizadas."},
        {"icon": "🔄", "title": "functools.lru_cache", "category": "Performance & Otimização", "difficulty": "Intermediário", "description": "Cache automático de resultados.", "bad_code": "def fibonacci(n):\n    if n < 2: return n\n    return fibonacci(n-1) + fibonacci(n-2)", "good_code": "from functools import lru_cache\n\n@lru_cache(maxsize=128)\ndef fibonacci(n):\n    if n < 2: return n\n    return fibonacci(n-1) + fibonacci(n-2)", "benefit": "1000x mais rápido.", "explanation": "Evita recalcular."},
        {"icon": "📊", "title": "*args e **kwargs", "category": "Elegância & Flexibilidade", "difficulty": "Intermediário", "description": "Argumentos variáveis.", "bad_code": "def func(a, b, c=None, d=None):\n    print(a, b, c, d)", "good_code": "def func(a, b, *args, **kwargs):\n    print(a, b)\n    print(args)\n    print(kwargs)", "benefit": "Flexível.", "explanation": "*args em tupla, **kwargs em dict."},
        {"icon": "🎯", "title": "isinstance com Múltiplos Tipos", "category": "Qualidade & Manutenção", "difficulty": "Intermediário", "description": "Verifique múltiplos tipos.", "bad_code": "if type(v) == int or type(v) == float:\n    print('Número')", "good_code": "if isinstance(v, (int, float)):\n    print('Número')", "benefit": "Conciso.", "explanation": "Com tupla de tipos."},
        {"icon": "🔗", "title": "pathlib vs os.path", "category": "Modernização & Legibilidade", "difficulty": "Intermediário", "description": "pathlib é mais moderno.", "bad_code": "import os\narq = os.path.join('dados', 'arquivo.txt')\nif os.path.exists(arq):\n    conteudo = open(arq).read()", "good_code": "from pathlib import Path\narq = Path('dados') / 'arquivo.txt'\nif arq.exists():\n    conteudo = arq.read_text()", "benefit": "OOP.", "explanation": "Mais moderno."},
        {"icon": "🎨", "title": "f-strings Avançadas", "category": "Elegância & Legibilidade", "difficulty": "Intermediário", "description": "Formatação de strings.", "bad_code": "print(f'Preço: ${preco}')\nprint(f'Total: ${preco * quantidade}')", "good_code": "print(f'Preço: ${preco:.2f}')\nprint(f'Total: ${preco * quantidade:>10.2f}')", "benefit": "Precisão.", "explanation": "Especificadores de formato."},
        {"icon": "🔐", "title": "dataclasses", "category": "Modernização & Elegância", "difficulty": "Intermediário", "description": "Automatize classes de dados.", "bad_code": "class Pessoa:\n    def __init__(self, nome, idade):\n        self.nome = nome\n        self.idade = idade", "good_code": "from dataclasses import dataclass\n\n@dataclass\nclass Pessoa:\n    nome: str\n    idade: int", "benefit": "Menos boilerplate.", "explanation": "Cria __init__, __repr__ automaticamente."},
        {"icon": "🚀", "title": "Dict Comprehension", "category": "Elegância & Performance", "difficulty": "Intermediário", "description": "Crie dicionários com elegância.", "bad_code": "quadrados_dict = {}\nfor n in [1,2,3]:\n    quadrados_dict[n] = n**2", "good_code": "quadrados_dict = {n: n**2 for n in [1,2,3]}", "benefit": "Conciso.", "explanation": "Mesma performance."},
        {"icon": "⚙️", "title": "itertools", "category": "Performance & Elegância", "difficulty": "Intermediário", "description": "Combinações e permutações.", "bad_code": "combos = []\nfor i in range(len(itens)):\n    for j in range(i+1, len(itens)):\n        combos.append((itens[i], itens[j]))", "good_code": "from itertools import combinations\ncombos = list(combinations([1,2,3], 2))", "benefit": "Simples.", "explanation": "Implementado em C."},
        {"icon": "🔗", "title": "super() em Herança", "category": "Elegância & Manutenção", "difficulty": "Intermediário", "description": "Chame método da classe pai.", "bad_code": "class Cachorro(Animal):\n    def falar(self):\n        Animal.falar(self)\n        print('Au!')", "good_code": "class Cachorro(Animal):\n    def falar(self):\n        super().falar()\n        print('Au!')", "benefit": "MRO.", "explanation": "Method Resolution Order."},
        {"icon": "🎪", "title": "Map e Filter", "category": "Programação Funcional", "difficulty": "Intermediário", "description": "Estilo funcional.", "bad_code": "quadrados = []\nfor n in [1,2,3]:\n    quadrados.append(n**2)", "good_code": "quadrados = list(map(lambda x: x**2, [1,2,3]))\n# Ou melhor:\nquadrados = [x**2 for x in [1,2,3]]", "benefit": "Funcional.", "explanation": "List comprehension é melhor."},
        {"icon": "✅", "title": "assertRaises", "category": "Qualidade & Testes", "difficulty": "Intermediário", "description": "Teste exceções corretamente.", "bad_code": "try:\n    dividir(10, 0)\nexcept ZeroDivisionError:\n    print('OK')", "good_code": "import unittest\n\nclass TestDividir(unittest.TestCase):\n    def test_divisao(self):\n        with self.assertRaises(ZeroDivisionError):\n            dividir(10, 0)", "benefit": "Claro.", "explanation": "Formaliza teste."},
        {"icon": "📦", "title": "Set Comprehension", "category": "Elegância & Performance", "difficulty": "Intermediário", "description": "Crie conjuntos com elegância.", "bad_code": "unicos = set()\nfor x in numeros:\n    unicos.add(x % 2)", "good_code": "unicos = {x % 2 for x in numeros}", "benefit": "Conciso.", "explanation": "Mesma performance."},
        {"icon": "🌟", "title": "Avoid Global Mutable", "category": "Qualidade & Manutenção", "difficulty": "Intermediário", "description": "Não use globais mutáveis.", "bad_code": "cache = {}\ndef processar(chave):\n    global cache\n    cache[chave] = valor", "good_code": "def processar(chave: str, cache: dict) -> dict:\n    cache[chave] = valor\n    return cache", "benefit": "Testável.", "explanation": "Passa estado como argumento."},
        {"icon": "⚡", "title": "Comprehension Aninhada", "category": "Elegância & Performance", "difficulty": "Intermediário", "description": "Aninhamento elegante.", "bad_code": "matriz = []\nfor i in range(3):\n    linha = []\n    for j in range(3):\n        linha.append(i * j)\n    matriz.append(linha)", "good_code": "matriz = [[i*j for j in range(3)] for i in range(3)]", "benefit": "Conciso.", "explanation": "Legível quando bem estruturada."},
        {"icon": "🎯", "title": "__slots__", "category": "Performance & Otimização", "difficulty": "Avançado", "description": "Reduz consumo de memória.", "bad_code": "class Ponto:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y", "good_code": "class Ponto:\n    __slots__ = ['x', 'y']\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y", "benefit": "50% menos memória.", "explanation": "Sem __dict__."},
        {"icon": "🔐", "title": "Metaclasses", "category": "Arquitetura & Avançado", "difficulty": "Avançado", "description": "Controlam criação de classes.", "bad_code": "class Singleton:\n    _instance = None\n    def __new__(cls):\n        if cls._instance is None:\n            cls._instance = super().__new__(cls)\n        return cls._instance", "good_code": "class SingletonMeta(type):\n    _instances = {}\n    def __call__(cls, *args):\n        if cls not in cls._instances:\n            cls._instances[cls] = super().__call__(*args)\n        return cls._instances[cls]", "benefit": "Padrões.", "explanation": "Classe de classes."},
        {"icon": "⚡", "title": "Protocol (Typing)", "category": "Qualidade & Manutenção", "difficulty": "Avançado", "description": "Interfaces sem herança.", "bad_code": "def processar(obj):\n    return obj.processar()", "good_code": "from typing import Protocol\n\nclass Processavel(Protocol):\n    def processar(self) -> str: ...\n\ndef processar(obj: Processavel) -> str:\n    return obj.processar()", "benefit": "Type checking.", "explanation": "Structural subtyping."},
        {"icon": "🔗", "title": "ABC", "category": "Arquitetura & Design", "difficulty": "Avançado", "description": "Interfaces obrigatórias.", "bad_code": "class Database:\n    def conectar(self): pass", "good_code": "from abc import ABC, abstractmethod\n\nclass Database(ABC):\n    @abstractmethod\n    def conectar(self): pass", "benefit": "Força implementação.", "explanation": "Torna métodos obrigatórios."},
        {"icon": "🎪", "title": "Async/Await", "category": "Concorrência & Performance", "difficulty": "Avançado", "description": "Programação assíncrona.", "bad_code": "for url in urls:\n    response = requests.get(url)", "good_code": "async def fetch(session, url):\n    async with session.get(url) as r:\n        return await r.text()\n\nasync def main():\n    tasks = [fetch(s, u) for u in urls]\n    await asyncio.gather(*tasks)", "benefit": "1000x mais rápido.", "explanation": "I/O sem threads."},
        {"icon": "🔐", "title": "Descriptors", "category": "Elegância & Avançado", "difficulty": "Avançado", "description": "Controlam acesso a atributos.", "bad_code": "class Pessoa:\n    def __init__(self, idade):\n        if not (0 <= idade <= 150):\n            raise ValueError()\n        self.idade = idade", "good_code": "class ValidadorIdade:\n    def __get__(self, obj, objtype=None):\n        return obj._idade if obj else self\n    def __set__(self, obj, value):\n        if not (0 <= value <= 150):\n            raise ValueError()\n        obj._idade = value", "benefit": "Validação.", "explanation": "Intercepta acesso."},
        {"icon": "📊", "title": "__getattr__", "category": "Elegância & Flexibilidade", "difficulty": "Avançado", "description": "Atributos dinâmicos.", "bad_code": "class Config:\n    def __init__(self, data):\n        self.data = data\n    def get(self, key):\n        return self.data.get(key)", "good_code": "class Config:\n    def __init__(self, data):\n        self.data = data\n    def __getattr__(self, key):\n        return self.data.get(key)", "benefit": "API Pythônica.", "explanation": "Chamado quando não existe."},
        {"icon": "🎪", "title": "Mixin Classes", "category": "Arquitetura & Reutilização", "difficulty": "Avançado", "description": "Reutilize funcionalidade.", "bad_code": "class Cachorro:\n    def latir(self): return 'Au!'\n\nclass Gato:\n    def miar(self): return 'Miau!'", "good_code": "class ComFoto:\n    def tirar_foto(self): return 'Foto'\n\nclass Cachorro(ComFoto):\n    def latir(self): return 'Au!'", "benefit": "Reutilização.", "explanation": "Métodos reutilizáveis."},
        {"icon": "⚙️", "title": "__call__", "category": "Elegância & Padrões", "difficulty": "Avançado", "description": "Objetos chamáveis.", "bad_code": "class Mult:\n    def __init__(self, fator):\n        self.fator = fator\n    def multiplicar(self, valor):\n        return valor * self.fator", "good_code": "class Mult:\n    def __init__(self, fator):\n        self.fator = fator\n    def __call__(self, valor):\n        return valor * self.fator\n\nmult3 = Mult(3)\nmult3(5)", "benefit": "Natural.", "explanation": "Usar como funções."},
        {"icon": "🔗", "title": "Composition vs Herança", "category": "Arquitetura & Design", "difficulty": "Avançado", "description": "Composição é mais flexível.", "bad_code": "class Automovel(Veiculo): pass", "good_code": "class Automovel:\n    def __init__(self):\n        self.motor = Motor()\n        self.pneus = Pneus()", "benefit": "Flexível.", "explanation": "Has-a vs is-a."},
        {"icon": "🚀", "title": "Cython", "category": "Performance & Otimização", "difficulty": "Avançado", "description": "Compila para C.", "bad_code": "def contar_pares(nums):\n    return sum(1 for n in nums if n % 2 == 0)", "good_code": "# cdef int contar_pares(list nums):\n#     cdef int count = 0\n#     for n in nums:\n#         if n % 2 == 0:\n#             count += 1\n#     return count", "benefit": "100x mais rápido.", "explanation": "Com type hints."},
        {"icon": "📊", "title": "cProfile", "category": "Performance & Debugging", "difficulty": "Avançado", "description": "Identifique gargalos.", "bad_code": "import time\ninicio = time.time()\nfuncao_lenta()\nprint(time.time() - inicio)", "good_code": "import cProfile\nimport pstats\n\ncProfile.run('funcao_lenta()', 'stats')\np = pstats.Stats('stats')\np.print_stats(10)", "benefit": "Gargalo real.", "explanation": "Chamadas e tempo."},
        {"icon": "🔐", "title": "Memory Profiler", "category": "Performance & Debugging", "difficulty": "Avançado", "description": "Identifique vazamentos.", "bad_code": "lista = [x for x in range(1000000)]", "good_code": "# @profile\n# def funcao():\n#     lista = [x for x in range(100000)]\n\n# python -m memory_profiler script.py", "benefit": "Vazamentos.", "explanation": "Memória por linha."},
        {"icon": "🎯", "title": "Logging", "category": "Qualidade & Produção", "difficulty": "Avançado", "description": "logging vs print.", "bad_code": "print('Começando...')\nprint(f'Dados: {dados}')", "good_code": "import logging\nlogger = logging.getLogger(__name__)\n\nlogger.info('Começando...')\nlogger.debug(f'Dados: {dados}')", "benefit": "Configurável.", "explanation": "Níveis e handlers."},
        {"icon": "🔗", "title": "Pytest", "category": "Qualidade & Testes", "difficulty": "Avançado", "description": "pytest é melhor.", "bad_code": "class Test(unittest.TestCase):\n    def test_resultado(self):\n        self.assertEqual(funcao(2, 3), 5)", "good_code": "def test_resultado():\n    assert funcao(2, 3) == 5\n\ndef test_erro():\n    with pytest.raises(ValueError):\n        funcao('a', 'b')", "benefit": "Simples.", "explanation": "Assertions e fixtures."},
        {"icon": "📦", "title": "mypy", "category": "Qualidade & Manutenção", "difficulty": "Avançado", "description": "Type checking estático.", "bad_code": "def somar(a: int, b: int) -> int:\n    return a + b\n\nsomar('2', '3')", "good_code": "# mypy script.py\n# Detecta: Argument has incompatible type\n# somar('2', '3')", "benefit": "Antes da execução.", "explanation": "Validação estática."},
        {"icon": "🚀", "title": "Dependency Injection", "category": "Arquitetura & Manutenção", "difficulty": "Avançado", "description": "Injetar dependências.", "bad_code": "class Servico:\n    def __init__(self):\n        self.db = Database()", "good_code": "class Servico:\n    def __init__(self, db):\n        self.db = db\n\ndb = Database()\nservico = Servico(db)", "benefit": "Testável.", "explanation": "Desacoplado."},
        {"icon": "🎨", "title": "__enter__/__exit__", "category": "Arquitetura & Elegância", "difficulty": "Avançado", "description": "Context managers customizados.", "bad_code": "transacao.begin()\ntry:\n    sql.execute()\nfinally:\n    transacao.commit()", "good_code": "class Transacao:\n    def __enter__(self):\n        self.begin()\n        return self\n    def __exit__(self, *args):\n        self.commit()\n\nwith Transacao() as t:\n    sql.execute()", "benefit": "Reutilizável.", "explanation": "Cleanup garantido."},
        {"icon": "⚡", "title": "cached_property", "category": "Performance & Elegância", "difficulty": "Avançado", "description": "Propriedades com cache.", "bad_code": "class Dados:\n    def __init__(self):\n        self.resultado = self.calcular_pesado()", "good_code": "class Dados:\n    @functools.cached_property\n    def resultado(self):\n        return self.calcular_pesado()", "benefit": "Sob demanda.", "explanation": "Caching automático."},
    ]

    filtered = python_practices
    if selected_difficulty != "Todas":
        filtered = [p for p in filtered if p["difficulty"] == selected_difficulty]
    if search:
        filtered = [p for p in filtered if search.lower() in p["title"].lower()]

    st.markdown('<h3 class="section-header">📖 Melhores Práticas</h3>', unsafe_allow_html=True)
    st.markdown(f'**Mostrando {len(filtered)} de {len(python_practices)} práticas**')

    for idx, p in enumerate(filtered):
        is_learned = idx in st.session_state.python_learned
        is_favorite = idx in st.session_state.python_favorites

        with st.expander(f"{p['icon']} {p['title']} — {p['difficulty']}" + (" ✅" if is_learned else "") + (" ⭐" if is_favorite else ""), expanded=False):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**Descrição:** {p['description']}")
                st.markdown(f"**Benefício:** {p['benefit']}")
                st.markdown(f"**Categoria:** `{p['category']}`")
            with col2:
                if is_favorite:
                    if st.button("★ Favoritado", key=f"fav_{idx}"):
                        st.session_state.python_favorites.discard(idx)
                        st.session_state.python_points -= 5
                        st.session_state.python_xp -= 5
                        st.rerun()
                elif st.button("⭐ Favoritar", key=f"fav_{idx}"):
                    st.session_state.python_favorites.add(idx)
                    st.session_state.python_points += 5
                    st.session_state.python_xp += 5
                    st.rerun()
                if is_learned:
                    st.button("✅ Aprendida", key=f"learn_{idx}", disabled=True)
                elif st.button("✅ Aprendida", key=f"learn_{idx}"):
                    st.session_state.python_learned.add(idx)
                    st.session_state.python_points += 25
                    st.session_state.python_xp += 25
                    st.session_state.python_level = get_current_level(st.session_state.python_xp)
                    st.rerun()

            st.markdown("**❌ Evitar:**")
            st.code(p["bad_code"], language="python")
            st.markdown("**✅ Preferir:**")
            st.code(p["good_code"], language="python")
            st.markdown(f"**Explicação:** {p['explanation']}")

# ============================================================================
# TAB 2: EDITOR
# ============================================================================
with tab2:
    st.markdown('<h3 class="section-header">✏️ Editor Python Interativo</h3>', unsafe_allow_html=True)
    st.markdown("**📚 Templates Rápidos:**")

    templates = {
        "Hello World": "print('Hello, World!')",
        "Soma": "a = 5\nb = 3\nprint(f'Soma: {a + b}')",
        "List": "numeros = [1, 2, 3, 4, 5]\nfor n in numeros:\n    print(n * 2)",
        "Dict": "pessoa = {'nome': 'Alice', 'idade': 30}\nprint(pessoa)",
        "Função": "def saudar(nome):\n    return f'Olá, {nome}!'\n\nprint(saudar('Python'))",
        "Loop": "for i in range(5):\n    print(f'Número: {i}')",
        "Compreensão": "pares = [n for n in range(10) if n % 2 == 0]\nprint(pares)",
        "Classe": "class Pessoa:\n    def __init__(self, nome):\n        self.nome = nome\n\np = Pessoa('Alice')\nprint(p.nome)",
        "Try/Except": "try:\n    resultado = 10 / 2\n    print(resultado)\nexcept ZeroDivisionError:\n    print('Erro!')",
    }

    selected_template = st.selectbox("Escolha um template:", ["Vazio"] + list(templates.keys()), key="template_selector")
    template_code = templates.get(selected_template, "")

    st.markdown("**Seu Código:**")
    code_input = st.text_area("Digite seu código Python aqui", value=template_code, height=250, key="code_editor", placeholder="# Digite seu código aqui\nprint('Hello, World!')")

    col1, col2, col3 = st.columns([2, 2, 2])
    with col1:
        run_button = st.button("▶️ RUN", use_container_width=True)

    if 'editor_runs' not in st.session_state:
        st.session_state.editor_runs = 0

    if run_button and code_input.strip():
        st.markdown("**Resultado:**")
        st.session_state.editor_runs += 1
        st.session_state.python_xp += 5
        st.session_state.python_points += 5
        try:
            output_buffer = StringIO()
            old_stdout = sys.stdout
            sys.stdout = output_buffer
            exec(code_input)
            sys.stdout = old_stdout
            output = output_buffer.getvalue()
            if output:
                st.markdown(f'<div class="success-box achievement-pop">{output}</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="success-box">✅ Código executado com sucesso (sem output)</div>', unsafe_allow_html=True)
        except Exception as e:
            sys.stdout = old_stdout
            st.markdown(f'<div class="error-box">❌ {type(e).__name__}: {str(e)}</div>', unsafe_allow_html=True)
    elif run_button and not code_input.strip():
        st.markdown('<div class="error-box">❌ Digite um código antes de executar!</div>', unsafe_allow_html=True)

    st.divider()
    st.markdown("""
    ### 💡 Dicas para o Editor
    - **Templates:** Use os botões acima para inserir exemplos rápidos
    - **Print:** Use `print()` para ver resultados
    - **Erros:** Os erros serão exibidos em vermelho
    - **XP:** Ganhe +5 XP cada vez que executa um script
    """)

# ============================================================================
# TAB 3: DESAFIOS
# ============================================================================
with tab3:
    st.markdown('<h3 class="section-header">🎯 Desafios Semanais</h3>', unsafe_allow_html=True)
    st.markdown("Complete desafios para ganhar XP e subir de nível!")

    for challenge in CHALLENGES:
        is_completed = challenge["id"] in st.session_state.python_challenges_completed
        col1, col2 = st.columns([4, 1])
        with col1:
            status = "✅ Completo" if is_completed else f"🎯 {challenge['difficulty']}"
            st.markdown(f"""
            <div class="challenge-box {'challenge-completed' if is_completed else ''}">
                <h4>{challenge['title']} {status}</h4>
                <p>{challenge['description']}</p>
                <p><strong>Recompensa:</strong> +{challenge['xp_reward']} XP</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if not is_completed:
                if st.button(f"Marcar ✓", key=f"challenge_{challenge['id']}"):
                    st.session_state.python_challenges_completed.add(challenge["id"])
                    st.session_state.python_xp += challenge["xp_reward"]
                    st.session_state.python_points += challenge["xp_reward"]
                    st.session_state.python_level = get_current_level(st.session_state.python_xp)
                    st.rerun()

# ============================================================================
# TAB 4: BADGES
# ============================================================================
with tab4:
    st.markdown('<h3 class="section-header">🏆 Suas Conquistas</h3>', unsafe_allow_html=True)

    learned_count = len(st.session_state.python_learned)
    favorites_count = len(st.session_state.python_favorites)
    current_badges = check_badges(learned_count, favorites_count, st.session_state.editor_runs, st.session_state.python_points)
    st.session_state.python_badges = current_badges

    st.markdown(f"""
    ### 📊 Estatísticas
    - **Práticas Aprendidas:** {learned_count}/60
    - **Práticas Favoritadas:** {favorites_count}
    - **Scripts Executados:** {st.session_state.editor_runs}
    - **Pontos Totais:** {st.session_state.python_points}
    - **XP Total:** {st.session_state.python_xp}
    """)

    unlocked = [(bid, bi) for bid, bi in BADGES.items() if bid in st.session_state.python_badges]
    locked = [(bid, bi) for bid, bi in BADGES.items() if bid not in st.session_state.python_badges]

    st.markdown("### 🎖️ Badges Desbloqueados")
    if unlocked:
        cols = st.columns(5)
        for idx, (badge_id, badge_info) in enumerate(unlocked):
            with cols[idx % 5]:
                st.markdown(f'<div class="badge">{badge_info["icon"]}<br><small><b>{badge_info["title"]}</b></small></div>', unsafe_allow_html=True)

    st.markdown("### 🔒 Badges Bloqueados")
    if locked:
        cols = st.columns(5)
        for idx, (badge_id, badge_info) in enumerate(locked):
            with cols[idx % 5]:
                st.markdown(f'<div class="badge badge-locked">{badge_info["icon"]}<br><small>{badge_info["title"]}</small><br><tiny style="font-size: 0.7rem;">{badge_info["description"]}</tiny></div>', unsafe_allow_html=True)

# ============================================================================
# TAB 5: PERFIL
# ============================================================================
with tab5:
    st.markdown('<h3 class="section-header">📊 Seu Perfil</h3>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        ### 🏆 Estatísticas Gerais
        - **Nível Atual:** {current_level}/{len(MASTERY_LEVELS)}
        - **Título:** {MASTERY_LEVELS[current_level]['title']}
        - **XP Total:** {st.session_state.python_xp}
        - **Pontos:** {st.session_state.python_points}
        - **Streak:** 🔥 {st.session_state.python_streak} dias
        """)
    with col2:
        learned_count = len(st.session_state.python_learned)
        st.markdown(f"""
        ### 📚 Progresso no Aprendizado
        - **Práticas Completadas:** {learned_count}/60
        - **Taxa de Conclusão:** {(learned_count/60)*100:.1f}%
        - **Favoritas:** {len(st.session_state.python_favorites)}
        - **Scripts Testados:** {st.session_state.editor_runs}
        - **Badges:** {len(st.session_state.python_badges)}/{len(BADGES)}
        """)

    st.divider()
    st.markdown("### 🎯 Próximas Metas")
    if current_level < 5:
        next_level_xp = get_xp_for_next_level(current_level)
        xp_needed = next_level_xp - st.session_state.python_xp
        next_title = MASTERY_LEVELS[current_level + 1]["title"]
        st.markdown(f"""
        ⬆️ **Próximo Nível:** {next_title}

        Você precisa de **{xp_needed} XP** para chegar ao próximo nível!
        """)
    else:
        st.markdown("🏆 **Você é uma Pythonista Elite! Parabéns!**")

    st.divider()
    st.markdown("""
    ### 💪 Dicas para Evoluir Rápido
    1. **Complete Desafios:** +100-200 XP cada
    2. **Teste no Editor:** +5 XP por execução
    3. **Favoritize Práticas:** +5 XP cada
    4. **Marque Aprendidas:** +25 XP cada
    5. **Mantenha Streak:** Use a plataforma todos os dias!

    **Meta:** Chegue ao nível Lendário (🏆) em 30 dias!
    """)
