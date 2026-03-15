import streamlit as st
import streamlit.components.v1 as components
import sys
from io import StringIO

st.set_page_config(
    page_title="Escola Excel — Atalhos & Fórmulas",
    page_icon="📗",
    layout="wide"
)

# ── SESSION STATE ──────────────────────────────────────────────────────────────
if 'excel_favorites' not in st.session_state:
    st.session_state.excel_favorites = set()
if 'excel_learned' not in st.session_state:
    st.session_state.excel_learned = set()
if 'excel_points' not in st.session_state:
    st.session_state.excel_points = 0
if 'excel_xp' not in st.session_state:
    st.session_state.excel_xp = 0
if 'excel_badges' not in st.session_state:
    st.session_state.excel_badges = set()
if 'excel_challenges_completed' not in st.session_state:
    st.session_state.excel_challenges_completed = set()
if 'excel_quiz_score' not in st.session_state:
    st.session_state.excel_quiz_score = 0
if 'excel_quiz_total' not in st.session_state:
    st.session_state.excel_quiz_total = 0

# ── NÍVEIS ─────────────────────────────────────────────────────────────────────
MASTERY_LEVELS = {
    1: {"title": "🥉 Excel Padawan",       "xp_required": 0,    "theme": "bronze"},
    2: {"title": "🥈 Planilha Ninja",       "xp_required": 250,  "theme": "silver"},
    3: {"title": "🥇 Excel Master",         "xp_required": 750,  "theme": "gold"},
    4: {"title": "💎 Arquiteto de Dados",   "xp_required": 1500, "theme": "diamond"},
    5: {"title": "🏆 Especialista Elite",   "xp_required": 2500, "theme": "legendary"},
}

BADGES = {
    "first_steps":      {"icon": "👣", "title": "Primeiros Passos",     "description": "Aprendeu a 1ª prática"},
    "ten_practices":    {"icon": "🔟", "title": "Persistência",          "description": "Aprendeu 10 práticas"},
    "twenty_practices": {"icon": "🎖️", "title": "Veterano",             "description": "Aprendeu 20 práticas"},
    "favorite_col":     {"icon": "⭐", "title": "Colecionador",          "description": "Favoritou 10 práticas"},
    "quiz_ace":         {"icon": "🎯", "title": "Ás do Quiz",            "description": "Acertou 10 questões"},
    "code_master":      {"icon": "👑", "title": "Rei das Planilhas",      "description": "1000+ pontos"},
    "shortcut_king":    {"icon": "⚡", "title": "Rei dos Atalhos",       "description": "Aprendeu 15 atalhos"},
    "formula_wizard":   {"icon": "🧙", "title": "Mago das Fórmulas",     "description": "Aprendeu 15 fórmulas"},
}

CHALLENGES = [
    {"id": "ch1", "title": "Mestre de Atalhos",    "difficulty": "Iniciante",   "xp_reward": 75,  "description": "Aprenda 10 atalhos de teclado"},
    {"id": "ch2", "title": "Fórmulas Essenciais",  "difficulty": "Iniciante",   "xp_reward": 100, "description": "Aprenda SOMA, MÉDIA, SE e PROCV"},
    {"id": "ch3", "title": "Power User",            "difficulty": "Avançado",    "xp_reward": 200, "description": "Aprenda 5 práticas de nível avançado"},
    {"id": "ch4", "title": "Colecionador de Stars", "difficulty": "Iniciante",   "xp_reward": 50,  "description": "Favorite 5 práticas"},
    {"id": "ch5", "title": "Quiz Ace",              "difficulty": "Intermediário","xp_reward": 150, "description": "Acerte 10 questões no quiz"},
]

# ── CSS (mesmo design do escola_python) ───────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, .main, [data-testid="stAppViewContainer"] {
    background-color: #060912 !important;
}

[data-testid="stAppViewContainer"] {
    background-image:
        radial-gradient(ellipse 80% 50% at 50% -10%, rgba(33,115,70,0.13) 0%, transparent 60%),
        radial-gradient(ellipse 40% 30% at 80% 60%, rgba(16,124,65,0.07) 0%, transparent 50%);
}

[data-testid="stHeader"] { background: transparent !important; }

.main h1,.main h2,.main h3,.main h4,
.main p,.main a,.main li,
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
    color: #21a366;
    border: 1px solid rgba(33,163,102,0.35);
    background: rgba(33,163,102,0.07);
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
    background: linear-gradient(135deg, #21a366 0%, #3dbb7e 50%, #85d4aa 100%);
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
    color: #21a366;
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
    background: linear-gradient(90deg, transparent, rgba(33,163,102,0.3), transparent);
}

/* ── SECTION HEADERS ── */
.section-header {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.5rem;
    font-weight: 800;
    color: #f0f4ff;
    margin: 50px 0 28px;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba(33,163,102,0.2);
    letter-spacing: -0.5px;
    position: relative;
}

.section-header::after {
    content: '';
    position: absolute;
    bottom: -1px; left: 0;
    width: 48px; height: 2px;
    background: #21a366;
}

/* ── STAT CARDS ── */
.stat-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%);
    border: 1px solid rgba(33,163,102,0.2);
    border-radius: 20px;
    padding: 36px 28px;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}
.stat-card:hover {
    transform: translateY(-4px);
    border-color: rgba(33,163,102,0.4);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}
.stat-number {
    font-family: 'Syne', sans-serif !important;
    font-size: 2.6rem;
    font-weight: 800;
    color: #21a366;
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

/* ── LEVEL/BADGE CLASSES ── */
.level-bronze  { border-color: #CD7F32; color: #CD7F32; box-shadow: 0 0 20px rgba(205,127,50,0.3); }
.level-silver  { border-color: #C0C0C0; color: #C0C0C0; box-shadow: 0 0 20px rgba(192,192,192,0.3); }
.level-gold    { border-color: #FFD700; color: #FFD700; box-shadow: 0 0 20px rgba(255,215,0,0.3); }
.level-diamond { border-color: #00D9FF; color: #00D9FF; box-shadow: 0 0 20px rgba(0,217,255,0.5); }
.level-legendary { border-color: #FF1493; color: #FF1493; box-shadow: 0 0 20px rgba(255,20,147,0.5);
    animation: pulse 2s infinite; }

@keyframes pulse {
    0%,100% { box-shadow: 0 0 20px rgba(255,20,147,0.5); }
    50%      { box-shadow: 0 0 40px rgba(255,20,147,0.8); }
}

.badge {
    background: linear-gradient(145deg, rgba(255,255,255,0.05) 0%, rgba(0,0,0,0.3) 100%);
    border: 1px solid rgba(33,163,102,0.2);
    border-radius: 10px;
    padding: 10px 15px;
    text-align: center;
    font-size: 2rem;
    cursor: pointer;
    transition: all 0.3s ease;
}
.badge:hover { transform: scale(1.1); border-color: #21a366; box-shadow: 0 0 15px rgba(33,163,102,0.3); }
.badge-locked { opacity: 0.3; }

.challenge-box {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%);
    border: 1px solid rgba(33,163,102,0.2);
    border-radius: 12px;
    padding: 15px;
    margin: 10px 0;
}
.challenge-completed {
    border-color: #21a366;
    background: linear-gradient(145deg, rgba(33,163,102,0.1) 0%, rgba(0,0,0,0.2) 100%);
}

/* shortcut key style */
.key-tag {
    display: inline-block;
    font-family: 'DM Mono', monospace;
    font-size: 0.88rem;
    font-weight: 500;
    background: rgba(33,163,102,0.08);
    border: 1px solid rgba(33,163,102,0.25);
    border-radius: 6px;
    padding: 3px 10px;
    color: #3dbb7e;
    margin: 2px;
}

.lv-ini { background: rgba(33,163,102,0.12); color: #3dbb7e; border: 1px solid rgba(33,163,102,0.25);
    border-radius: 100px; padding: 2px 10px; font-size: 0.72rem; font-weight: 700; }
.lv-ava { background: rgba(240,180,0,0.1); color: #f0c040; border: 1px solid rgba(240,180,0,0.2);
    border-radius: 100px; padding: 2px 10px; font-size: 0.72rem; font-weight: 700; }
.lv-pow { background: rgba(200,80,80,0.1); color: #e08080; border: 1px solid rgba(200,80,80,0.2);
    border-radius: 100px; padding: 2px 10px; font-size: 0.72rem; font-weight: 700; }

/* inputs */
.stSelectbox > div > div {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(33,163,102,0.2) !important;
    color: #e2e8f0 !important;
    border-radius: 12px !important;
}
.stTextArea > div > div {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(33,163,102,0.2) !important;
    color: #e2e8f0 !important;
    border-radius: 12px !important;
}
div[data-testid="stTextInput"] input {
    background-color: rgba(255,255,255,0.03) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(33,163,102,0.25) !important;
    border-radius: 14px !important;
    padding: 14px 22px !important;
    font-size: 0.95rem !important;
}
hr {
    border: none !important;
    border-top: 1px solid rgba(33,163,102,0.1) !important;
    margin: 40px 0 !important;
}
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #060912; }
::-webkit-scrollbar-thumb { background: rgba(33,163,102,0.2); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(33,163,102,0.4); }

.success-box {
    background: linear-gradient(145deg, rgba(33,163,102,0.1) 0%, rgba(33,163,102,0.05) 100%);
    border: 1px solid rgba(33,163,102,0.3);
    border-radius: 12px;
    padding: 15px;
    margin-top: 10px;
    color: #3dbb7e;
    font-weight: 500;
}
.error-box {
    background: linear-gradient(145deg, rgba(239,68,68,0.1) 0%, rgba(239,68,68,0.05) 100%);
    border: 1px solid rgba(239,68,68,0.3);
    border-radius: 12px;
    padding: 15px;
    margin-top: 10px;
    color: #ff6b6b;
}
</style>
""", unsafe_allow_html=True)

# ── DADOS ──────────────────────────────────────────────────────────────────────
PRACTICES = [
    # ── ATALHOS INICIANTE ──
    {"icon": "📋", "title": "Copiar e Colar",          "category": "Atalhos Essenciais", "difficulty": "Iniciante",
     "atalho": "Ctrl + C / Ctrl + V",
     "descricao": "Copie células, intervalos ou formatação com rapidez.",
     "dica": "Use Ctrl+C para copiar, Ctrl+V para colar. Após copiar, a célula fica com borda tracejada animada.",
     "exemplo": "Selecione A1:D10 → Ctrl+C → clique em F1 → Ctrl+V",
     "beneficio": "Economiza cliques repetidos e reduz erros de digitação."},

    {"icon": "↩️", "title": "Desfazer / Refazer",      "category": "Atalhos Essenciais", "difficulty": "Iniciante",
     "atalho": "Ctrl + Z / Ctrl + Y",
     "descricao": "Desfaça ações erradas ou refaça o que foi desfeito.",
     "dica": "O Excel mantém histórico de até 100 ações. Ctrl+Y refaz ou repete a última ação.",
     "exemplo": "Deletou dados sem querer? Ctrl+Z restaura imediatamente.",
     "beneficio": "Segurança total ao trabalhar — erros são facilmente revertidos."},

    {"icon": "💾", "title": "Salvar Arquivo",           "category": "Atalhos Essenciais", "difficulty": "Iniciante",
     "atalho": "Ctrl + S",
     "descricao": "Salve o arquivo atual instantaneamente.",
     "dica": "Use Ctrl+Shift+S para 'Salvar Como'. Salve frequentemente para evitar perda de dados.",
     "exemplo": "Após editar dados → Ctrl+S → arquivo salvo sem abrir diálogo.",
     "beneficio": "Hábito essencial: nunca perca trabalho por queda de energia."},

    {"icon": "🔍", "title": "Localizar e Substituir",   "category": "Atalhos Essenciais", "difficulty": "Iniciante",
     "atalho": "Ctrl + L / Ctrl + H",
     "descricao": "Encontre valores ou substitua em massa pela planilha inteira.",
     "dica": "Ctrl+L abre Localizar. Ctrl+H abre Substituir. Use * como curinga para busca parcial.",
     "exemplo": "Ctrl+H → 'SP' → 'São Paulo' → Substituir Tudo = altera 500 células em 1 clique.",
     "beneficio": "Substitui manualmente o trabalho de horas em segundos."},

    {"icon": "📌", "title": "Selecionar Coluna/Linha",  "category": "Atalhos Essenciais", "difficulty": "Iniciante",
     "atalho": "Ctrl + Espaço / Shift + Espaço",
     "descricao": "Selecione a coluna ou linha inteira da célula ativa.",
     "dica": "Ctrl+Espaço = coluna inteira. Shift+Espaço = linha inteira. Combine com Ctrl+Shift+'+' para inserir.",
     "exemplo": "Clique em B5 → Ctrl+Espaço → coluna B inteira selecionada.",
     "beneficio": "Seleção instantânea sem usar o mouse para clicar no cabeçalho."},

    {"icon": "🏠", "title": "Ir para Célula A1",        "category": "Atalhos Essenciais", "difficulty": "Iniciante",
     "atalho": "Ctrl + Home",
     "descricao": "Navegue instantaneamente ao início da planilha.",
     "dica": "Ctrl+End vai para a última célula com dados. Ctrl+Home volta ao início.",
     "exemplo": "Em Z1000 → Ctrl+Home → cursor volta para A1 imediatamente.",
     "beneficio": "Navegar em planilhas grandes sem rolar manualmente."},

    {"icon": "⬇️", "title": "Ir para Última Célula",    "category": "Atalhos Essenciais", "difficulty": "Iniciante",
     "atalho": "Ctrl + ↓ / ↑ / ← / →",
     "descricao": "Navegue até a última célula preenchida na direção da seta.",
     "dica": "Segure Shift enquanto usa Ctrl+seta para selecionar o intervalo até o final dos dados.",
     "exemplo": "A1 → Ctrl+↓ pula direto para A1000 se toda a coluna tiver dados.",
     "beneficio": "Navegação ultrarrápida em tabelas com milhares de linhas."},

    {"icon": "🖊️", "title": "Editar Célula Ativa",       "category": "Atalhos Essenciais", "difficulty": "Iniciante",
     "atalho": "F2",
     "descricao": "Entre no modo de edição da célula sem precisar dar dois cliques.",
     "dica": "Após F2, use as teclas de seta para mover o cursor dentro do texto da célula.",
     "exemplo": "Selecione B5 com fórmula → F2 → edite a fórmula diretamente.",
     "beneficio": "Edição precisa de fórmulas sem risco de apagar o conteúdo acidentalmente."},

    {"icon": "📊", "title": "Inserir Tabela",            "category": "Atalhos Essenciais", "difficulty": "Iniciante",
     "atalho": "Ctrl + T",
     "descricao": "Converta um intervalo de dados em Tabela do Excel com filtros automáticos.",
     "dica": "Tabelas se expandem automaticamente ao adicionar dados e facilitam a criação de fórmulas.",
     "exemplo": "Selecione A1:D100 → Ctrl+T → tabela formatada com filtros em 1 segundo.",
     "beneficio": "Referências estruturadas, filtros automáticos e expansão dinâmica."},

    {"icon": "🖨️", "title": "Formatar como Moeda",      "category": "Atalhos Essenciais", "difficulty": "Iniciante",
     "atalho": "Ctrl + Shift + $",
     "descricao": "Aplique formato de moeda (R$ ou $) nas células selecionadas.",
     "dica": "Ctrl+Shift+% aplica porcentagem. Ctrl+Shift+# aplica formato de data.",
     "exemplo": "Selecione B2:B100 → Ctrl+Shift+$ → valores formatados como R$ 1.234,56.",
     "beneficio": "Formatação de colunas financeiras inteiras em um atalho."},

    # ── ATALHOS AVANÇADO ──
    {"icon": "🔗", "title": "Colar Especial",            "category": "Atalhos Avançados", "difficulty": "Avançado",
     "atalho": "Ctrl + Alt + V",
     "descricao": "Abra o menu de Colar Especial para colar apenas valores, formatos ou fórmulas.",
     "dica": "Após Ctrl+C, use Ctrl+Alt+V → V → Enter para colar somente valores (remove fórmulas).",
     "exemplo": "Copiar coluna com fórmulas → Ctrl+Alt+V → V → Enter = apenas números colados.",
     "beneficio": "Elimina fórmulas quebradas ao copiar entre planilhas diferentes."},

    {"icon": "🎨", "title": "Pincel de Formatação",      "category": "Atalhos Avançados", "difficulty": "Avançado",
     "atalho": "Alt + H + F + P",
     "descricao": "Aplique a formatação de uma célula em outras com o Pincel.",
     "dica": "Dê duplo clique no Pincel para aplicar em múltiplas seleções sem soltar.",
     "exemplo": "Selecione célula formatada → Alt+H+F+P → clique nas células destino.",
     "beneficio": "Replica cores, fontes e bordas em segundos sem reconfigurar manualmente."},

    {"icon": "🔢", "title": "AutoSoma Rápida",            "category": "Atalhos Avançados", "difficulty": "Avançado",
     "atalho": "Alt + =",
     "descricao": "Insira automaticamente a função =SOMA() para o intervalo acima ou ao lado.",
     "dica": "Selecione uma faixa de células antes de pressionar Alt+= para somar múltiplas colunas de uma vez.",
     "exemplo": "Clique em B11 (abaixo de 10 valores) → Alt+= → =SOMA(B1:B10) inserida automaticamente.",
     "beneficio": "Cria somas em toda uma linha/coluna instantaneamente."},

    {"icon": "📐", "title": "Congelar Painéis",          "category": "Atalhos Avançados", "difficulty": "Avançado",
     "atalho": "Alt + W + F + F",
     "descricao": "Congele linhas e colunas para que fiquem visíveis ao rolar a planilha.",
     "dica": "Posicione o cursor abaixo e à direita da área que quer congelar antes de aplicar.",
     "exemplo": "Clique em B2 → Alt+W+F+F → linha 1 e coluna A sempre visíveis ao rolar.",
     "beneficio": "Essencial em relatórios grandes para manter cabeçalhos sempre visíveis."},

    {"icon": "🔄", "title": "Atualizar Tabela Dinâmica", "category": "Atalhos Avançados", "difficulty": "Avançado",
     "atalho": "Alt + F5",
     "descricao": "Atualize todos os dados de uma Tabela Dinâmica após alterações na fonte.",
     "dica": "Alt+Ctrl+F5 atualiza todas as Tabelas Dinâmicas da pasta de trabalho de uma vez.",
     "exemplo": "Após inserir novos dados na fonte → Alt+F5 → Tabela Dinâmica atualizada.",
     "beneficio": "Mantém relatórios atualizados sem precisar recriar a tabela."},

    # ── FÓRMULAS INICIANTE ──
    {"icon": "➕", "title": "SOMA",                      "category": "Fórmulas Essenciais", "difficulty": "Iniciante",
     "atalho": "=SOMA(intervalo)",
     "descricao": "Some todos os valores de um intervalo de células.",
     "dica": "=SOMA(A1:A10) soma de A1 até A10. =SOMA(A1,C1,E1) soma células específicas.",
     "exemplo": "=SOMA(B2:B13) → soma todos os valores de janeiro a dezembro na coluna B.",
     "beneficio": "Fórmula mais usada no Excel — base de qualquer relatório financeiro."},

    {"icon": "📊", "title": "MÉDIA",                     "category": "Fórmulas Essenciais", "difficulty": "Iniciante",
     "atalho": "=MÉDIA(intervalo)",
     "descricao": "Calcule a média aritmética de um intervalo de valores.",
     "dica": "Ignora células vazias automaticamente. Use MÉDIASE para média com condição.",
     "exemplo": "=MÉDIA(C2:C31) → média das vendas diárias do mês.",
     "beneficio": "Essencial para análises de desempenho e benchmarks."},

    {"icon": "🔀", "title": "SE",                        "category": "Fórmulas Essenciais", "difficulty": "Iniciante",
     "atalho": "=SE(teste;valor_verdadeiro;valor_falso)",
     "descricao": "Retorne valores diferentes com base em uma condição lógica.",
     "dica": "Pode ser aninhado: =SE(A1>90;\"Ótimo\";SE(A1>70;\"Bom\";\"Regular\")).",
     "exemplo": "=SE(B2>=7;\"Aprovado\";\"Reprovado\") → classifica notas automaticamente.",
     "beneficio": "Automação de classificações, alertas e regras de negócio."},

    {"icon": "🔍", "title": "PROCV",                     "category": "Fórmulas Essenciais", "difficulty": "Iniciante",
     "atalho": "=PROCV(valor;tabela;col;[0])",
     "descricao": "Busque um valor em uma tabela e retorne dados da mesma linha.",
     "dica": "Sempre use 0 (FALSO) como 4º argumento para busca exata. A coluna de busca deve ser a 1ª.",
     "exemplo": "=PROCV(A2;Produtos!A:C;2;0) → busca o código em A2 e retorna o nome do produto.",
     "beneficio": "Cruza dados de tabelas diferentes — base de qualquer dashboard."},

    {"icon": "🔢", "title": "CONT.SE",                   "category": "Fórmulas Essenciais", "difficulty": "Iniciante",
     "atalho": "=CONT.SE(intervalo;critério)",
     "descricao": "Conte células que atendem a um critério específico.",
     "dica": "Use curingas: =CONT.SE(A:A;\"SP*\") conta tudo que começa com SP.",
     "exemplo": "=CONT.SE(C2:C100;\">1000\") → conta quantas vendas foram acima de 1000.",
     "beneficio": "Análises rápidas de frequência e validação de dados."},

    {"icon": "🧮", "title": "SOMASE",                    "category": "Fórmulas Essenciais", "difficulty": "Iniciante",
     "atalho": "=SOMASE(intervalo;critério;intervalo_soma)",
     "descricao": "Some valores apenas onde uma condição é verdadeira.",
     "dica": "SOMASES (plural) aceita múltiplos critérios: =SOMASES(C:C;A:A;\"SP\";B:B;\"Jan\").",
     "exemplo": "=SOMASE(A:A;\"Sul\";C:C) → soma as vendas apenas da região Sul.",
     "beneficio": "Relatórios segmentados sem precisar filtrar manualmente."},

    # ── FÓRMULAS AVANÇADO ──
    {"icon": "🔎", "title": "ÍNDICE + CORRESP",           "category": "Fórmulas Avançadas", "difficulty": "Avançado",
     "atalho": "=ÍNDICE(retorno;CORRESP(valor;busca;0))",
     "descricao": "Combinação poderosa que substitui PROCV e permite busca em qualquer direção.",
     "dica": "Ao contrário do PROCV, busca da direita para esquerda e em qualquer coluna.",
     "exemplo": "=ÍNDICE(A:A;CORRESP(\"João\";B:B;0)) → retorna o ID mesmo estando à esquerda do nome.",
     "beneficio": "Sem limitações de direção — flexibilidade total em buscas complexas."},

    {"icon": "⚡", "title": "PROCX",                      "category": "Fórmulas Avançadas", "difficulty": "Avançado",
     "atalho": "=PROCX(valor;intervalo_busca;intervalo_retorno;[se_não_encontrado])",
     "descricao": "Substituto moderno do PROCV: mais flexível e com tratamento de erros nativo.",
     "dica": "Disponível no Excel 365/2021. Busca em qualquer direção e retorna múltiplas colunas.",
     "exemplo": "=PROCX(A2;Tabela[Código];Tabela[Nome];\"Não encontrado\") → busca com fallback.",
     "beneficio": "Elimina a necessidade de SEERRO + PROCV em uma só fórmula."},

    {"icon": "🌐", "title": "ÚNICO + FILTRO",             "category": "Fórmulas Avançadas", "difficulty": "Avançado",
     "atalho": "=ÚNICO(intervalo) / =FILTRO(intervalo;condição)",
     "descricao": "Fórmulas de matriz dinâmica que derramam resultados automaticamente.",
     "dica": "=ÚNICO(A2:A100) retorna lista sem duplicatas. =FILTRO(A:C;B:B=\"SP\") filtra linhas.",
     "exemplo": "=FILTRO(A2:C100;C2:C100>5000;\"Sem dados\") → exibe apenas vendas acima de 5000.",
     "beneficio": "Dashboards dinâmicos sem VBA — dados atualizam automaticamente."},

    {"icon": "📈", "title": "SOMARPRODUTO",               "category": "Fórmulas Avançadas", "difficulty": "Avançado",
     "atalho": "=SOMARPRODUTO(array1;array2)",
     "descricao": "Multiplica arrays e soma os resultados — extremamente versátil para análises.",
     "dica": "=SOMARPRODUTO((A:A=\"SP\")*(B:B>1000)*C:C) soma C onde A=SP E B>1000.",
     "exemplo": "=SOMARPRODUTO(B2:B10;C2:C10) → faturamento total (qtd × preço) sem coluna auxiliar.",
     "beneficio": "Substitui colunas auxiliares e faz cálculos matriciais em uma célula."},

    {"icon": "🛡️", "title": "SEERRO",                    "category": "Fórmulas Avançadas", "difficulty": "Avançado",
     "atalho": "=SEERRO(fórmula;valor_se_erro)",
     "descricao": "Trate erros de fórmulas exibindo um valor personalizado em vez de #N/D ou #VALOR!",
     "dica": "Use em conjunto com PROCV: =SEERRO(PROCV(...);\"-\") para tabelas limpas.",
     "exemplo": "=SEERRO(PROCV(A2;Tabela;2;0);\"Não cadastrado\") → sem erros visíveis.",
     "beneficio": "Relatórios profissionais sem mensagens de erro confusas para o usuário final."},

    {"icon": "📅", "title": "DATEDIF + HOJE",             "category": "Fórmulas Avançadas", "difficulty": "Avançado",
     "atalho": "=DATEDIF(data_ini;HOJE();\"Y\")",
     "descricao": "Calcule diferença entre datas em anos, meses ou dias.",
     "dica": "\"Y\" = anos, \"M\" = meses, \"D\" = dias, \"YM\" = meses restantes após anos completos.",
     "exemplo": "=DATEDIF(B2;HOJE();\"Y\")&\" anos e \"&DATEDIF(B2;HOJE();\"YM\")&\" meses\"",
     "beneficio": "Calcula idade, tempo de empresa e vencimentos de contratos automaticamente."},

    # ── POWER USER ──
    {"icon": "🎯", "title": "Tabela Dinâmica",            "category": "Power User", "difficulty": "Avançado",
     "atalho": "Alt + N + V",
     "descricao": "Crie relatórios dinâmicos que resumem grandes volumes de dados em segundos.",
     "dica": "Arraste campos para Linhas, Colunas e Valores. Use Segmentação de Dados para filtros visuais.",
     "exemplo": "Base com 50.000 vendas → Tabela Dinâmica → vendas por região e mês em 10 segundos.",
     "beneficio": "Análise de dados sem fórmulas — drag & drop para qualquer visão analítica."},

    {"icon": "🤖", "title": "Power Query",                "category": "Power User", "difficulty": "Avançado",
     "atalho": "Alt + A + P + N",
     "descricao": "Importe, transforme e combine dados de múltiplas fontes sem código.",
     "dica": "Cada passo de transformação fica registrado. Basta atualizar para reprocessar novos dados.",
     "exemplo": "Conectar ao banco de dados → remover duplicatas → mesclar tabelas → carregar limpo.",
     "beneficio": "ETL visual: substitui horas de limpeza manual de dados."},

    {"icon": "📉", "title": "Gráfico Sparkline",          "category": "Power User", "difficulty": "Avançado",
     "atalho": "Alt + N + S + L",
     "descricao": "Insira mini-gráficos dentro de células para visualização inline de tendências.",
     "dica": "Existem 3 tipos: Linha, Colunas e Ganhos/Perdas. Selecione o intervalo de dados e a célula destino.",
     "exemplo": "Linha de tendência dentro de E2 mostrando evolução de B2:D2 sem ocupar espaço.",
     "beneficio": "Dashboards compactos com visualização de tendência sem gráficos grandes."},

    {"icon": "🔧", "title": "Validação de Dados",         "category": "Power User", "difficulty": "Avançado",
     "atalho": "Alt + A + V + V",
     "descricao": "Restrinja a entrada de dados nas células com listas, números ou fórmulas customizadas.",
     "dica": "Use lista suspensa com =Tabela[Coluna] para dropdown dinâmico que se atualiza automaticamente.",
     "exemplo": "Coluna Status → Validação → Lista → \"Aberto,Em andamento,Concluído\" = dropdown.",
     "beneficio": "Elimina erros de digitação e padroniza entradas em planilhas compartilhadas."},

    {"icon": "🎨", "title": "Formatação Condicional",     "category": "Power User", "difficulty": "Avançado",
     "atalho": "Alt + H + L",
     "descricao": "Aplique cores e ícones automaticamente baseado no valor das células.",
     "dica": "Use Barras de Dados e Escalas de Cor para heatmaps instantâneos. Fórmulas permitem regras avançadas.",
     "exemplo": "=C2<MÉDIA($C$2:$C$100) → pinta de vermelho todas as vendas abaixo da média.",
     "beneficio": "Destaca outliers, metas e exceções sem análise manual linha a linha."},
]

QUIZ_QUESTIONS = [
    {"q": "Qual atalho copia células no Excel?",              "opts": ["Ctrl+X","Ctrl+C","Ctrl+V","Ctrl+Z"],   "a": 1},
    {"q": "Como abrir Localizar e Substituir?",               "opts": ["Ctrl+F","Ctrl+H","Ctrl+L","Ctrl+R"],   "a": 1},
    {"q": "Qual fórmula soma com condição?",                  "opts": ["SOMA","CONT.SE","SOMASE","MÉDIA"],      "a": 2},
    {"q": "O que faz Ctrl+Home?",                             "opts": ["Abre o menu","Vai para A1","Salva","Seleciona tudo"], "a": 1},
    {"q": "Qual atalho insere AutoSoma?",                     "opts": ["Ctrl+=","Alt+=","Shift+=","Ctrl+S"],    "a": 1},
    {"q": "Como entrar no modo de edição da célula?",         "opts": ["Enter","F2","F4","Tab"],                "a": 1},
    {"q": "O que faz =SEERRO(fórmula;0)?",                    "opts": ["Retorna erro","Retorna 0 se erro","Soma","Nada"], "a": 1},
    {"q": "Qual atalho cria uma Tabela (Ctrl+T) faz?",        "opts": ["Insere tabela dinâmica","Converte intervalo em tabela","Abre Power Query","Formata células"], "a": 1},
    {"q": "O que PROCV requer como 4º argumento para busca exata?", "opts": ["1","VERDADEIRO","0 ou FALSO","Vazio"], "a": 2},
    {"q": "Qual fórmula calcula a média de um intervalo?",    "opts": ["SOMA","MÁXIMO","MÉDIA","CONT.NÚM"],     "a": 2},
    {"q": "Como selecionar a coluna inteira?",                "opts": ["Shift+Espaço","Alt+Espaço","Ctrl+Espaço","Ctrl+A"], "a": 2},
    {"q": "Qual atalho abre Colar Especial?",                 "opts": ["Ctrl+V","Ctrl+Alt+V","Ctrl+Shift+V","Alt+V"], "a": 1},
    {"q": "O que faz a função ÚNICO()?",                      "opts": ["Conta únicos","Remove duplicatas da lista","Filtra valores","Ordena"], "a": 1},
    {"q": "Qual tecla entra no modo de edição de célula?",    "opts": ["F1","F2","F3","F4"],                   "a": 1},
    {"q": "SOMARPRODUTO multiplica arrays e faz o quê?",      "opts": ["Retorna o maior","Soma os produtos","Conta","Divide"], "a": 1},
]

# ── HELPERS ───────────────────────────────────────────────────────────────────
def get_current_level(xp):
    for lv in sorted(MASTERY_LEVELS.keys(), reverse=True):
        if xp >= MASTERY_LEVELS[lv]["xp_required"]:
            return lv
    return 1

def check_badges():
    learned = len(st.session_state.excel_learned)
    favs    = len(st.session_state.excel_favorites)
    pts     = st.session_state.excel_points
    qz      = st.session_state.excel_quiz_score
    new = set()
    if learned >= 1:  new.add("first_steps")
    if learned >= 10: new.add("ten_practices")
    if learned >= 20: new.add("twenty_practices")
    if favs   >= 10:  new.add("favorite_col")
    if qz     >= 10:  new.add("quiz_ace")
    if pts    >= 1000:new.add("code_master")
    shortcuts = [p for p in st.session_state.excel_learned
                 if PRACTICES[p]["category"] in ("Atalhos Essenciais","Atalhos Avançados")]
    formulas  = [p for p in st.session_state.excel_learned
                 if PRACTICES[p]["category"] in ("Fórmulas Essenciais","Fórmulas Avançadas")]
    if len(shortcuts) >= 15: new.add("shortcut_king")
    if len(formulas)  >= 15: new.add("formula_wizard")
    return new

total_practices = len(PRACTICES)
total_cats      = len(set(p["category"] for p in PRACTICES))

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero-wrapper">
    <div class="hero-badge">⚡ Microsoft Excel · Escola Interativa</div>
    <h1 class="hero-title">
        Domine cada <span class="accent">fórmula e atalho</span><br>e trabalhe no próximo nível
    </h1>
    <p class="hero-subtitle">
        A referência definitiva de atalhos, fórmulas e boas práticas do Excel —
        aprenda, pratique e evolua com gamificação.
    </p>
    <div class="hero-stats">
        <div class="hero-stat">
            <span class="hero-stat-number">{total_practices}</span>
            <span class="hero-stat-label">Práticas</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-number">{total_cats}</span>
            <span class="hero-stat-label">Categorias</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-number">{len(MASTERY_LEVELS)}</span>
            <span class="hero-stat-label">Níveis</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-number">⭐ {st.session_state.excel_points}</span>
            <span class="hero-stat-label">Pontos</span>
        </div>
    </div>
    <div class="hero-divider"></div>
</div>
""", unsafe_allow_html=True)

current_level = get_current_level(st.session_state.excel_xp)
level_info    = MASTERY_LEVELS[current_level]

col1, col2, col3 = st.columns([2,3,2])
with col2:
    st.markdown(f'<h3 style="text-align:center;color:#21a366;font-family:Syne,sans-serif;">Jornada de Maestria — {level_info["title"]}</h3>', unsafe_allow_html=True)

# ── TABS ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📚 Práticas", "🎯 Quiz", "🏆 Desafios", "🎖️ Badges", "📊 Perfil", "🖥️ Planilha Virtual"])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1: PRÁTICAS
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown('<h3 class="section-header">🔎 Filtrar Práticas</h3>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        cats = ["Todas"] + sorted(set(p["category"] for p in PRACTICES))
        selected_cat = st.selectbox("📂 Categoria", cats, key="excel_cat")
    with col2:
        selected_diff = st.selectbox("📈 Dificuldade", ["Todas","Iniciante","Avançado"], key="excel_diff")

    search = st.text_input("🔍 Buscar prática ou atalho", key="excel_search")

    filtered = PRACTICES
    if selected_cat  != "Todas":   filtered = [p for p in filtered if p["category"]   == selected_cat]
    if selected_diff != "Todas":   filtered = [p for p in filtered if p["difficulty"] == selected_diff]
    if search:                      filtered = [p for p in filtered if search.lower() in p["title"].lower()
                                                                     or search.lower() in p["atalho"].lower()
                                                                     or search.lower() in p["descricao"].lower()]

    lv_cls = {"Iniciante": "lv-ini", "Avançado": "lv-pow"}

    st.markdown('<h3 class="section-header">📖 Biblioteca de Práticas</h3>', unsafe_allow_html=True)
    st.markdown(f"**Mostrando {len(filtered)} de {total_practices} práticas**")

    for idx, p in enumerate(PRACTICES):
        if p not in filtered:
            continue
        real_idx    = PRACTICES.index(p)
        is_learned  = real_idx in st.session_state.excel_learned
        is_fav      = real_idx in st.session_state.excel_favorites
        cls         = lv_cls.get(p["difficulty"], "lv-ini")

        label = f"{p['icon']} {p['title']} — {p['difficulty']}"
        if is_learned: label += " ✅"
        if is_fav:     label += " ⭐"

        with st.expander(label, expanded=False):
            col_a, col_b = st.columns([3,1])
            with col_a:
                st.markdown(f"**Atalho / Fórmula:** `{p['atalho']}`")
                st.markdown(f"**Descrição:** {p['descricao']}")
                st.markdown(f"**💡 Dica:** {p['dica']}")
                st.markdown(f"**📋 Exemplo:** {p['exemplo']}")
                st.markdown(f"**✅ Benefício:** {p['beneficio']}")
                st.markdown(f"<span class='{cls}'>{p['difficulty']}</span> &nbsp; <code>{p['category']}</code>",
                            unsafe_allow_html=True)
            with col_b:
                fav_label = "★ Favoritado" if is_fav else "⭐ Favoritar"
                if st.button(fav_label, key=f"efav_{real_idx}"):
                    if is_fav:
                        st.session_state.excel_favorites.discard(real_idx)
                        st.session_state.excel_points -= 5
                        st.session_state.excel_xp     -= 5
                    else:
                        st.session_state.excel_favorites.add(real_idx)
                        st.session_state.excel_points += 5
                        st.session_state.excel_xp     += 5
                    st.rerun()

                if is_learned:
                    st.button("✅ Aprendida", key=f"elearn_{real_idx}", disabled=True)
                elif st.button("✅ Marcar Aprendida", key=f"elearn_{real_idx}"):
                    st.session_state.excel_learned.add(real_idx)
                    st.session_state.excel_points += 25
                    st.session_state.excel_xp     += 25
                    st.session_state.excel_badges  = check_badges()
                    st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2: QUIZ
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown('<h3 class="section-header">🎯 Quiz Interativo</h3>', unsafe_allow_html=True)
    st.markdown(f"**Pontuação atual: {st.session_state.excel_quiz_score} acertos de {st.session_state.excel_quiz_total} tentativas**")

    if 'quiz_q_idx' not in st.session_state:
        st.session_state.quiz_q_idx = 0
    if 'quiz_answered' not in st.session_state:
        st.session_state.quiz_answered = False
    if 'quiz_selected' not in st.session_state:
        st.session_state.quiz_selected = None

    q_idx = st.session_state.quiz_q_idx % len(QUIZ_QUESTIONS)
    question = QUIZ_QUESTIONS[q_idx]

    st.markdown(f"""
    <div class="challenge-box" style="padding:24px 28px;">
        <div style="font-size:0.72rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;
                    color:#21a366;margin-bottom:12px;">
            ⚡ Pergunta {q_idx+1} de {len(QUIZ_QUESTIONS)}
        </div>
        <div style="font-family:'Syne',sans-serif;font-size:1.2rem;font-weight:700;
                    color:#f0f4ff;line-height:1.4;">
            {question['q']}
        </div>
    </div>
    """, unsafe_allow_html=True)

    selected = st.radio("Escolha sua resposta:", question["opts"],
                        key=f"quiz_radio_{q_idx}", index=None)

    col_q1, col_q2 = st.columns([1,1])
    with col_q1:
        if st.button("✓ Confirmar Resposta", key="quiz_confirm", use_container_width=True):
            if selected is not None:
                st.session_state.quiz_answered = True
                st.session_state.quiz_selected = question["opts"].index(selected)
                st.session_state.excel_quiz_total += 1
                if st.session_state.quiz_selected == question["a"]:
                    st.session_state.excel_quiz_score += 1
                    st.session_state.excel_points     += 10
                    st.session_state.excel_xp         += 10
                    st.session_state.excel_badges      = check_badges()
                st.rerun()
    with col_q2:
        if st.button("➜ Próxima Pergunta", key="quiz_next", use_container_width=True):
            st.session_state.quiz_q_idx    += 1
            st.session_state.quiz_answered  = False
            st.session_state.quiz_selected  = None
            st.rerun()

    if st.session_state.quiz_answered and st.session_state.quiz_selected is not None:
        correct = st.session_state.quiz_selected == question["a"]
        if correct:
            st.markdown('<div class="success-box">✅ Correto! +10 XP e +10 pontos conquistados!</div>',
                        unsafe_allow_html=True)
        else:
            resp_correta = question["opts"][question["a"]]
            st.markdown(f'<div class="error-box">❌ Resposta correta: <strong>{resp_correta}</strong></div>',
                        unsafe_allow_html=True)

    st.divider()
    if st.session_state.excel_quiz_total > 0:
        taxa = (st.session_state.excel_quiz_score / st.session_state.excel_quiz_total) * 100
        st.markdown(f"📊 **Taxa de acerto:** {taxa:.1f}%")
    st.markdown(f"🎯 **Total de acertos:** {st.session_state.excel_quiz_score}")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 3: DESAFIOS
# ══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown('<h3 class="section-header">🏆 Desafios</h3>', unsafe_allow_html=True)
    st.markdown("Complete desafios para ganhar XP e subir de nível!")

    for ch in CHALLENGES:
        done = ch["id"] in st.session_state.excel_challenges_completed
        col_a, col_b = st.columns([4,1])
        with col_a:
            cls = "challenge-box challenge-completed" if done else "challenge-box"
            status = "✅ Completo" if done else f"🎯 {ch['difficulty']}"
            st.markdown(f"""
            <div class="{cls}">
                <h4>{ch['title']} &nbsp; {status}</h4>
                <p>{ch['description']}</p>
                <p><strong>Recompensa:</strong> +{ch['xp_reward']} XP</p>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            if not done:
                if st.button("Marcar ✓", key=f"ech_{ch['id']}"):
                    st.session_state.excel_challenges_completed.add(ch["id"])
                    st.session_state.excel_xp     += ch["xp_reward"]
                    st.session_state.excel_points += ch["xp_reward"]
                    st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# TAB 4: BADGES
# ══════════════════════════════════════════════════════════════════════════════
with tab4:
    st.markdown('<h3 class="section-header">🎖️ Conquistas</h3>', unsafe_allow_html=True)

    st.session_state.excel_badges = check_badges()
    learned_n = len(st.session_state.excel_learned)
    favs_n    = len(st.session_state.excel_favorites)

    st.markdown(f"""
    ### 📊 Estatísticas
    - **Práticas Aprendidas:** {learned_n}/{total_practices}
    - **Práticas Favoritadas:** {favs_n}
    - **Acertos no Quiz:** {st.session_state.excel_quiz_score}
    - **Pontos Totais:** {st.session_state.excel_points}
    - **XP Total:** {st.session_state.excel_xp}
    """)

    unlocked = [(bid, bi) for bid, bi in BADGES.items() if bid in st.session_state.excel_badges]
    locked   = [(bid, bi) for bid, bi in BADGES.items() if bid not in st.session_state.excel_badges]

    st.markdown("### 🎖️ Badges Desbloqueados")
    if unlocked:
        cols = st.columns(min(len(unlocked), 5))
        for i, (_, bi) in enumerate(unlocked):
            with cols[i % 5]:
                st.markdown(f'<div class="badge">{bi["icon"]}<br><small><b>{bi["title"]}</b></small></div>',
                            unsafe_allow_html=True)
    else:
        st.markdown("*Nenhum badge desbloqueado ainda. Comece aprendendo práticas!*")

    st.markdown("### 🔒 Badges Bloqueados")
    if locked:
        cols = st.columns(min(len(locked), 5))
        for i, (_, bi) in enumerate(locked):
            with cols[i % 5]:
                st.markdown(f"""<div class="badge badge-locked">{bi["icon"]}<br>
                    <small>{bi["title"]}</small><br>
                    <span style="font-size:0.7rem;color:#4a5568">{bi["description"]}</span>
                    </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 5: PERFIL
# ══════════════════════════════════════════════════════════════════════════════
with tab5:
    st.markdown('<h3 class="section-header">📊 Seu Perfil</h3>', unsafe_allow_html=True)

    current_level = get_current_level(st.session_state.excel_xp)
    level_info    = MASTERY_LEVELS[current_level]

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        ### 🏆 Estatísticas Gerais
        - **Nível Atual:** {current_level}/{len(MASTERY_LEVELS)}
        - **Título:** {level_info['title']}
        - **XP Total:** {st.session_state.excel_xp}
        - **Pontos:** {st.session_state.excel_points}
        """)
    with col2:
        taxa_txt = ""
        if st.session_state.excel_quiz_total > 0:
            taxa_txt = f"{(st.session_state.excel_quiz_score/st.session_state.excel_quiz_total)*100:.1f}%"
        else:
            taxa_txt = "—"
        st.markdown(f"""
        ### 📚 Progresso no Aprendizado
        - **Práticas Completadas:** {len(st.session_state.excel_learned)}/{total_practices}
        - **Taxa de Conclusão:** {(len(st.session_state.excel_learned)/total_practices)*100:.1f}%
        - **Favoritas:** {len(st.session_state.excel_favorites)}
        - **Acertos no Quiz:** {st.session_state.excel_quiz_score}
        - **Taxa Quiz:** {taxa_txt}
        - **Badges:** {len(st.session_state.excel_badges)}/{len(BADGES)}
        """)

    st.divider()
    st.markdown("### 🎯 Próximas Metas")
    if current_level < 5:
        next_xp    = MASTERY_LEVELS[current_level + 1]["xp_required"]
        xp_needed  = next_xp - st.session_state.excel_xp
        next_title = MASTERY_LEVELS[current_level + 1]["title"]
        st.markdown(f"⬆️ **Próximo Nível:** {next_title} — você precisa de **{xp_needed} XP**")
        progress_pct = min(100, int((st.session_state.excel_xp / next_xp) * 100))
        st.progress(progress_pct / 100)
    else:
        st.markdown("🏆 **Você é um Especialista Elite! Parabéns!**")

    st.divider()
    st.markdown("""
    ### 💪 Como Evoluir Rápido
    1. **Complete Desafios:** +50–200 XP cada
    2. **Acerte no Quiz:** +10 XP por resposta correta
    3. **Favoritar Práticas:** +5 XP cada
    4. **Marcar Aprendidas:** +25 XP cada
    5. **Meta:** Chegue ao nível Elite em 30 dias!
    """)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 6: PLANILHA VIRTUAL
# ══════════════════════════════════════════════════════════════════════════════
with tab6:
    st.markdown('<h3 class="section-header">🖥️ Planilha Virtual Interativa</h3>', unsafe_allow_html=True)
    st.markdown(
        "Treine fórmulas diretamente na planilha abaixo — com autocomplete, desafios guiados e validação de respostas.",
        unsafe_allow_html=False
    )
    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    html_path = "Views/curso_excel.html"
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=820, scrolling=False)
    except FileNotFoundError:
        st.markdown("""
        <div style="
            background: rgba(239,68,68,0.08);
            border: 1px solid rgba(239,68,68,0.25);
            border-radius: 12px;
            padding: 20px 24px;
            color: #ff6b6b;
            font-size: 0.9rem;
        ">
            ⚠️ <strong>Arquivo não encontrado:</strong> <code>Views/curso_excel.html</code><br><br>
            Certifique-se de que o arquivo <code>curso_excel.html</code> está dentro da pasta <code>Views/</code>
            no seu repositório.
        </div>
        """, unsafe_allow_html=True)
