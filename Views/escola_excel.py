import streamlit as st
import pandas as pd
import json
import html
from difflib import get_close_matches

st.set_page_config(
    page_title="Atalhos Excel PT-BR | Master Shortcuts",
    page_icon="📗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── dados ──────────────────────────────────────────────────────────────────────
with open("Views/atalhos_excel.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

total_atalhos = len(df)
total_cats    = df["categoria"].nunique()
total_power   = (df["nivel"] == "Power User").sum()

# ── session state ──────────────────────────────────────────────────────────────
if "fav" not in st.session_state:
    st.session_state.fav = []
if "quiz_idx" not in st.session_state:
    st.session_state.quiz_idx = None
if "quiz_revealed" not in st.session_state:
    st.session_state.quiz_revealed = False

# ── CSS ────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, .main, [data-testid="stAppViewContainer"] {
    background-color: #060912 !important;
}

[data-testid="stAppViewContainer"] {
    background-color: #060912 !important;
    background-image:
        radial-gradient(ellipse 80% 50% at 50% -10%, rgba(33,115,70,0.13) 0%, transparent 60%),
        radial-gradient(ellipse 40% 30% at 80% 60%, rgba(16,124,65,0.07) 0%, transparent 50%);
}

[data-testid="stHeader"] { background: transparent !important; }
section[data-testid="stSidebar"] { display: none !important; }

.main h1,.main h2,.main h3,.main h4,
.main p,.main a,.main li,
[data-testid="stAppViewContainer"] div:not([data-testid="stSidebar"]) {
    font-family: 'DM Sans', sans-serif !important;
}

.material-symbols-rounded,.material-icons,
[data-testid*="Collapse"] span,[data-testid*="collapse"] span {
    font-family: 'Material Symbols Rounded','Material Icons' !important;
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
    position: relative;
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
    max-width: 720px;
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

/* ── SEARCH ── */
.search-label {
    text-align: center;
    font-size: 0.85rem;
    color: #4a5568;
    letter-spacing: 0.5px;
    margin-bottom: 10px;
}

div[data-testid="stTextInput"] input {
    background-color: rgba(255,255,255,0.03) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(33,163,102,0.25) !important;
    border-radius: 14px !important;
    padding: 14px 22px !important;
    font-size: 0.95rem !important;
    font-family: 'DM Sans', sans-serif !important;
    transition: all 0.3s ease !important;
}
div[data-testid="stTextInput"] input::placeholder { color: #2d3748 !important; }
div[data-testid="stTextInput"] input:focus {
    box-shadow: 0 0 0 3px rgba(33,163,102,0.15) !important;
    border-color: rgba(33,163,102,0.6) !important;
    background-color: rgba(33,163,102,0.04) !important;
}

div[data-testid="stSelectbox"] > div > div {
    background-color: rgba(255,255,255,0.03) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(33,163,102,0.25) !important;
    border-radius: 14px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.95rem !important;
}

div[data-testid="stTextInput"] label,
div[data-testid="stSelectbox"] label { display: none !important; }

.search-result-count {
    text-align: center;
    color: #4a5568;
    font-size: 0.88rem;
    margin: 14px 0 28px;
}
.search-result-count span { color: #21a366; font-weight: 600; }

/* ── SECTION LABEL ── */
.section-label {
    font-family: 'Syne', sans-serif !important;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #2d3748;
    margin-bottom: 32px;
    text-align: center;
}

/* ── TOP-10 TABLE ── */
.top-table-wrap { margin-bottom: 48px; }

.top-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
}
.top-table thead th {
    text-align: left;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #2d3748;
    padding: 0 16px 12px;
    border-bottom: 1px solid rgba(33,163,102,0.15);
}
.top-table tbody tr {
    border-bottom: 1px solid rgba(255,255,255,0.03);
    transition: background .15s;
}
.top-table tbody tr:hover { background: rgba(33,163,102,0.04); }
.top-table tbody td { padding: 13px 16px; vertical-align: middle; }
.top-rank {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    color: #21a366;
    width: 40px;
}
.top-key {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    font-weight: 500;
    background: rgba(33,163,102,0.08);
    border: 1px solid rgba(33,163,102,0.2);
    border-radius: 6px;
    padding: 3px 10px;
    color: #3dbb7e;
    display: inline-block;
}
.top-desc { color: #e2e8f0; font-size: 0.9rem; }
.top-cat { font-size: 0.78rem; color: #2d3748; letter-spacing: 0.5px; }

/* ── SHORTCUT CARD ── */
.shortcut-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%);
    padding: 28px 30px;
    border-radius: 20px;
    margin-bottom: 18px;
    border: 1px solid rgba(255,255,255,0.05);
    position: relative;
    overflow: hidden;
    transition: all 0.35s cubic-bezier(0.4,0,0.2,1);
}
.shortcut-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(33,163,102,0.4), transparent);
    opacity: 0;
    transition: opacity 0.35s ease;
}
.shortcut-card:hover {
    transform: translateY(-4px);
    border-color: rgba(33,163,102,0.2);
    box-shadow:
        0 20px 40px rgba(0,0,0,0.4),
        0 0 0 1px rgba(33,163,102,0.1),
        inset 0 1px 0 rgba(33,163,102,0.1);
    background: linear-gradient(145deg, rgba(33,163,102,0.04) 0%, rgba(0,0,0,0.25) 100%);
}
.shortcut-card:hover::before { opacity: 1; }

.sc-cat {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #2d3748;
    margin-bottom: 10px;
}
.sc-key {
    font-family: 'DM Mono', monospace;
    font-size: 1.1rem;
    font-weight: 500;
    background: rgba(33,163,102,0.08);
    border: 1px solid rgba(33,163,102,0.2);
    border-radius: 8px;
    padding: 5px 14px;
    color: #3dbb7e;
    display: inline-block;
    margin-bottom: 14px;
    letter-spacing: 0.5px;
}
.sc-desc {
    font-size: 0.95rem;
    font-weight: 400;
    color: #e2e8f0;
    line-height: 1.55;
    margin-bottom: 12px;
}
.sc-explain {
    font-size: 0.82rem;
    color: #4a5568;
    line-height: 1.6;
    border-top: 1px solid rgba(255,255,255,0.04);
    padding-top: 12px;
}
.sc-foot {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-top: 14px;
}
.sc-level {
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 100px;
}
.lv-ini { background: rgba(33,163,102,0.12); color: #3dbb7e; border: 1px solid rgba(33,163,102,0.25); }
.lv-ava { background: rgba(240,180,0,0.1); color: #f0c040; border: 1px solid rgba(240,180,0,0.2); }
.lv-pow { background: rgba(200,80,80,0.1); color: #e08080; border: 1px solid rgba(200,80,80,0.2); }
.sc-rank { font-family: 'DM Mono', monospace; font-size: 0.72rem; color: #2d3748; }
.sc-fav {
    position: absolute;
    top: 16px; right: 16px;
    width: 7px; height: 7px;
    border-radius: 50%;
    background: #21a366;
    box-shadow: 0 0 8px rgba(33,163,102,0.6);
}

/* ── QUIZ ── */
.quiz-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%);
    border: 1px solid rgba(33,163,102,0.15);
    border-radius: 20px;
    padding: 40px 48px;
    max-width: 620px;
    position: relative;
    overflow: hidden;
}
.quiz-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(33,163,102,0.5), transparent);
}
.quiz-label {
    font-family: 'Syne', sans-serif !important;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #21a366;
    margin-bottom: 16px;
}
.quiz-q {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.4rem;
    font-weight: 700;
    color: #f0f4ff;
    line-height: 1.3;
    margin-bottom: 8px;
}
.quiz-meta { font-size: 0.82rem; color: #2d3748; margin-bottom: 32px; }
.quiz-answer {
    background: rgba(33,163,102,0.07);
    border: 1px solid rgba(33,163,102,0.2);
    border-radius: 12px;
    padding: 20px 24px;
}
.quiz-answer .key {
    font-family: 'DM Mono', monospace;
    font-size: 1.5rem;
    font-weight: 500;
    color: #3dbb7e;
}
.quiz-answer .explain { font-size: 0.85rem; color: #4a5568; margin-top: 8px; line-height: 1.6; }

/* ── EMPTY ── */
.empty-state { text-align: center; padding: 80px 20px; }
.empty-icon { font-size: 3rem; margin-bottom: 16px; opacity: .4; }
.empty-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.1rem; font-weight: 700; color: #2d3748; margin-bottom: 8px;
}
.empty-sub { font-size: 0.88rem; color: #1a202c; }

/* ── BUTTONS ── */
button[kind="secondary"] {
    background: rgba(33,163,102,0.1) !important;
    color: #21a366 !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.5px !important;
    padding: 10px 20px !important;
    border-radius: 12px !important;
    border: 1px solid rgba(33,163,102,0.25) !important;
    transition: all 0.3s ease !important;
}
button[kind="secondary"]:hover {
    background: rgba(33,163,102,0.18) !important;
    border-color: rgba(33,163,102,0.5) !important;
    box-shadow: 0 4px 20px rgba(33,163,102,0.2) !important;
}

::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #060912; }
::-webkit-scrollbar-thumb { background: rgba(33,163,102,0.2); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(33,163,102,0.4); }

.footer-spacer { height: 60px; }

/* ── SEARCH BLOCK ── */
.search-block {
    text-align: center;
    margin-bottom: 16px;
}
.search-block-label {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.1rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 6px;
    letter-spacing: -0.3px;
}
.search-block-hint {
    font-size: 0.82rem;
    color: #4a5568;
    margin-bottom: 14px;
}

/* search input centralizado e maior */
div[data-testid="stTextInput"] input {
    text-align: center !important;
    font-size: 1rem !important;
    height: 52px !important;
    border-radius: 16px !important;
    border: 1.5px solid rgba(33,163,102,0.3) !important;
    letter-spacing: 0.2px;
}
div[data-testid="stTextInput"] input:focus {
    border-color: rgba(33,163,102,0.7) !important;
    box-shadow: 0 0 0 4px rgba(33,163,102,0.12) !important;
}

/* label "Refinar por" */
.filter-row-label {
    font-size: 0.72rem !important;
    font-weight: 700 !important;
    letter-spacing: 2.5px !important;
    text-transform: uppercase !important;
    color: #2d3748 !important;
    text-align: center !important;
    margin-bottom: 8px !important;
}
</style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero-wrapper">
    <div class="hero-badge">⚡ Microsoft Excel · PT-BR</div>
    <h1 class="hero-title">
        Domine cada <span class="accent">atalho do Excel</span><br>e trabalhe no próximo nível
    </h1>
    <p class="hero-subtitle">
        A referência definitiva de teclas de atalho para o Excel em português —
        filtre, explore e salve os favoritos.
    </p>
    <div class="hero-stats">
        <div class="hero-stat">
            <span class="hero-stat-number">{total_atalhos}</span>
            <span class="hero-stat-label">Atalhos únicos</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-number">{total_cats}</span>
            <span class="hero-stat-label">Categorias</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-number">{total_power}</span>
            <span class="hero-stat-label">Power User</span>
        </div>
    </div>
    <div class="hero-divider"></div>
</div>
""", unsafe_allow_html=True)

# ── FILTROS ────────────────────────────────────────────────────────────────────
# Campo de busca com label visível acima
st.markdown("""
<div class="search-block">
    <div class="search-block-label">🔍 &nbsp;Pesquise um atalho</div>
    <div class="search-block-hint">Digite o nome da ação ou a combinação de teclas</div>
</div>
""", unsafe_allow_html=True)

col_s1, col_s2, col_s3 = st.columns([1, 3, 1])
with col_s2:
    busca = st.text_input("busca", placeholder="Ex: copiar, tabela, soma, Ctrl + F2...", label_visibility="collapsed")

st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

# Filtros secundários centralizados
st.markdown("<p class='filter-row-label'>Refinar por</p>", unsafe_allow_html=True)
col_a, col_b, col_c, col_d, col_e = st.columns([1.5, 1.5, 0.3, 1.5, 1.5])
with col_b:
    categoria = st.selectbox("cat", ["Todas as categorias"] + sorted(df["categoria"].unique()), label_visibility="collapsed")
with col_d:
    nivel = st.selectbox("niv", ["Todos os níveis", "Iniciante", "Avançado", "Power User"], label_visibility="collapsed")

st.write("")

# ── APLICAR FILTROS ────────────────────────────────────────────────────────────
df_f = df.copy()
if busca:
    b = busca.lower()
    df_f = df_f[df_f["atalho"].str.lower().str.contains(b) | df_f["descricao"].str.lower().str.contains(b)]
    if df_f.empty:
        matches = get_close_matches(b, df["descricao"].str.lower(), n=10, cutoff=0.4)
        df_f = df[df["descricao"].str.lower().isin(matches)]
if categoria != "Todas as categorias":
    df_f = df_f[df_f["categoria"] == categoria]
if nivel != "Todos os níveis":
    df_f = df_f[df_f["nivel"] == nivel]

total_filtrado = len(df_f)
if busca:
    lbl = "resultado" if total_filtrado == 1 else "resultados"
    st.markdown(
        f'<div class="search-result-count">🔎 <span>{total_filtrado}</span> {lbl} para <span>"{busca}"</span></div>',
        unsafe_allow_html=True
    )

# ── TOP-10 ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">— Ranking corporativo — top 10 —</div>', unsafe_allow_html=True)

top10 = df.sort_values("ranking_corporativo").head(10)
rows_html = ""
for _, r in top10.iterrows():
    t_atalho = html.escape(str(r["atalho"]))
    t_desc   = html.escape(str(r["descricao"]))
    t_cat    = html.escape(str(r["categoria"]))
    t_rank   = int(r["ranking_corporativo"])
    rows_html += (
        f'<tr>'
        f'<td class="top-rank">#{t_rank}</td>'
        f'<td><span class="top-key">{t_atalho}</span></td>'
        f'<td class="top-desc">{t_desc}</td>'
        f'<td class="top-cat">{t_cat}</td>'
        f'</tr>'
    )

st.markdown(f"""
<div class="top-table-wrap">
<table class="top-table">
  <thead><tr><th>#</th><th>Atalho</th><th>Descrição</th><th>Categoria</th></tr></thead>
  <tbody>{rows_html}</tbody>
</table>
</div>
""", unsafe_allow_html=True)

# ── CARDS ──────────────────────────────────────────────────────────────────────
if df_f.empty:
    st.markdown("""
    <div class="empty-state">
        <div class="empty-icon">🔍</div>
        <div class="empty-title">Nenhum atalho encontrado.</div>
        <div class="empty-sub">Tente outro termo de pesquisa.</div>
    </div>""", unsafe_allow_html=True)
else:
    st.markdown(
        f'<div class="section-label">— Biblioteca · {total_filtrado} atalhos —</div>',
        unsafe_allow_html=True
    )
    lv_cls = {"Iniciante": "lv-ini", "Avançado": "lv-ava", "Power User": "lv-pow"}

    all_cards = ""
    for _, r in df_f.iterrows():
        fav_dot     = '<div class="sc-fav"></div>' if r["atalho"] in st.session_state.fav else ""
        cls         = lv_cls.get(r["nivel"], "lv-ini")
        atalho_e    = html.escape(str(r["atalho"]))
        descricao_e = html.escape(str(r["descricao"]))
        explicacao_e= html.escape(str(r["explicacao"]))
        categoria_e = html.escape(str(r["categoria"]))
        nivel_e     = html.escape(str(r["nivel"]))
        rank_e      = int(r["ranking_corporativo"])
        all_cards += (
            f'<div class="shortcut-card">{fav_dot}'
            f'<div class="sc-cat">{categoria_e}</div>'
            f'<div class="sc-key">{atalho_e}</div>'
            f'<div class="sc-desc">{descricao_e}</div>'
            f'<div class="sc-explain">{explicacao_e}</div>'
            f'<div class="sc-foot">'
            f'<span class="sc-level {cls}">{nivel_e}</span>'
            f'<span class="sc-rank">rank #{rank_e}</span>'
            f'</div></div>'
        )
    st.markdown(all_cards, unsafe_allow_html=True)

# ── FAVORITOS ──────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label" style="margin-top:48px">— Favoritos —</div>', unsafe_allow_html=True)

fav_cols = st.columns(5)
for i, (_, r) in enumerate(df_f.head(20).iterrows()):
    with fav_cols[i % 5]:
        is_fav = r["atalho"] in st.session_state.fav
        label_btn = f"★ {r['atalho']}" if is_fav else f"☆ {r['atalho']}"
        if st.button(label_btn, key=f"fav_{i}"):
            if is_fav:
                st.session_state.fav.remove(r["atalho"])
            else:
                st.session_state.fav.append(r["atalho"])
            st.rerun()

if st.session_state.fav:
    pills = "".join(
        f'<span style="font-family:\'DM Mono\',monospace;font-size:13px;'
        f'background:rgba(33,163,102,0.08);border:1px solid rgba(33,163,102,0.2);'
        f'border-radius:8px;padding:5px 14px;color:#3dbb7e;display:inline-block;margin:4px">{f}</span>'
        for f in st.session_state.fav
    )
    st.markdown(
        f'<div style="margin-top:16px;display:flex;flex-wrap:wrap;gap:6px">{pills}</div>',
        unsafe_allow_html=True
    )

# ── QUIZ ───────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label" style="margin-top:48px">— Modo quiz —</div>', unsafe_allow_html=True)

col_q, _ = st.columns([2, 3])
with col_q:
    if st.button("➜  Nova pergunta", key="quiz_new"):
        st.session_state.quiz_idx = int(df.sample(1).index[0])
        st.session_state.quiz_revealed = False
        st.rerun()

if st.session_state.quiz_idx is not None:
    row = df.loc[st.session_state.quiz_idx]
    q_desc  = html.escape(str(row["descricao"]))
    q_cat   = html.escape(str(row["categoria"]))
    q_nivel = html.escape(str(row["nivel"]))
    q_key   = html.escape(str(row["atalho"]))
    q_expl  = html.escape(str(row["explicacao"]))
    answer_html = (
        f'<div class="quiz-answer"><div class="key">{q_key}</div>'
        f'<div class="explain">{q_expl}</div></div>'
    ) if st.session_state.quiz_revealed else ""
    st.markdown(
        f'<div class="quiz-card">'
        f'<div class="quiz-label">⚡ Qual é o atalho para…</div>'
        f'<div class="quiz-q">{q_desc}</div>'
        f'<div class="quiz-meta">{q_cat} · {q_nivel}</div>'
        f'{answer_html}</div>',
        unsafe_allow_html=True
    )

    if not st.session_state.quiz_revealed:
        if st.button("Revelar resposta →", key="quiz_reveal"):
            st.session_state.quiz_revealed = True
            st.rerun()

st.markdown('<div class="footer-spacer"></div>', unsafe_allow_html=True)

# ── FOOTER ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="text-align:center;padding:32px 80px;font-size:13px;color:#2d3748;
border-top:1px solid rgba(33,163,102,0.1);font-family:'DM Sans',sans-serif">
    <span style="color:#21a366;font-weight:600">{total_atalhos} atalhos</span>
    &nbsp;·&nbsp; Excel PT-BR &nbsp;·&nbsp; Feito com Streamlit
</div>
""", unsafe_allow_html=True)
