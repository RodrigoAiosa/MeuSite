import streamlit as st
import json
from datetime import datetime

# --- CONFIGURAÇÃO DE PÁGINA ---
st.set_page_config(
    page_title="SQL - Melhores Práticas Pro | Rodrigo Aiosa",
    page_icon="🗄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- INICIALIZAR SESSION STATE ---
def init_session_state():
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
    if 'current_menu' not in st.session_state:
        st.session_state.current_menu = "📖 Todas as Práticas"
    if 'daily_streak' not in st.session_state:
        st.session_state.daily_streak = 1

init_session_state()

# --- CUSTOM CSS ---
st.markdown("""
<style>
    :root {
        --primary: #0F172A;
        --secondary: #1E293B;
        --accent: #D4AF37;
        --text-light: #E2E8F0;
        --border: #334155;
        --success: #22c55e;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0F172A 0%, #1a2744 100%);
    }
    
    .hero-section {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        border-bottom: 2px solid var(--accent);
        padding: 60px 20px;
        margin-bottom: 40px;
        border-radius: 12px;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        color: var(--text-light);
        margin: 0;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: var(--accent);
        margin: 10px 0 20px 0;
        font-weight: 500;
    }
    
    .stat-card {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 30px;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        border-color: var(--accent);
        box-shadow: 0 8px 25px rgba(212, 175, 55, 0.15);
        transform: translateY(-3px);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--accent);
        margin: 0;
    }
    
    .progress-container {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 25px;
        margin: 30px 0;
    }
    
    .progress-bar {
        width: 100%;
        height: 12px;
        background: var(--border);
        border-radius: 6px;
        overflow: hidden;
    }
    
    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, var(--accent), #60a5fa);
        transition: width 0.5s ease;
        border-radius: 6px;
    }
    
    .badge {
        display: inline-block;
        background: linear-gradient(135deg, var(--accent), #fbbf24);
        color: var(--text-dark);
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.8rem;
        margin: 5px;
    }
    
    .streak-badge {
        display: inline-block;
        background: linear-gradient(135deg, #ef4444, #dc2626);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.9rem;
        margin: 5px;
    }
    
    .practice-card {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 20px;
        margin: 15px 0;
        transition: all 0.3s ease;
    }
    
    .practice-card:hover {
        border-color: var(--accent);
        box-shadow: 0 5px 15px rgba(212, 175, 55, 0.1);
    }
    
    .notes-section {
        background: rgba(212, 175, 55, 0.1);
        border-left: 4px solid var(--accent);
        border-radius: 8px;
        padding: 15px;
        margin: 15px 0;
    }
    
    .favorite-btn {
        cursor: pointer;
        font-size: 1.3rem;
        transition: all 0.2s;
    }
    
    .favorite-btn:hover {
        transform: scale(1.25);
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 20px 0; border-bottom: 2px solid var(--accent); margin-bottom: 20px;">
        <h1 style="font-size: 1.8rem; color: var(--accent); margin: 0;">📊 SQL Pro</h1>
        <p style="color: #cbd5e1; font-size: 0.9rem; margin: 5px 0;">Domine SQL em 60 práticas</p>
    </div>
    """, unsafe_allow_html=True)
    
    # --- SIDEBAR STATS ---
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #1E293B 0%, #334155 100%); border: 1px solid var(--border); border-radius: 8px; padding: 15px; text-align: center;">
            <p style="color: var(--accent); font-weight: 700; font-size: 1.5rem; margin: 0;">⭐ {st.session_state.user_points}</p>
            <p style="color: #cbd5e1; font-size: 0.8rem; margin: 5px 0;">Pontos</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #1E293B 0%, #334155 100%); border: 1px solid var(--border); border-radius: 8px; padding: 15px; text-align: center;">
            <p style="color: var(--accent); font-weight: 700; font-size: 1.5rem; margin: 0;">🔥 {st.session_state.daily_streak}</p>
            <p style="color: #cbd5e1; font-size: 0.8rem; margin: 5px 0;">Streak</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # --- MENU ---
    st.markdown("### 📚 Navegação")
    menu = st.radio(
        "Escolha:",
        ["📖 Todas as Práticas", "⭐ Meus Favoritos", "✅ Já Aprendi", "🏆 Progresso", "🎯 Desafios"],
        label_visibility="collapsed",
        key="main_menu"
    )
    st.session_state.current_menu = menu
    
    st.markdown("---")
    st.markdown("### 🔍 Buscar")
    search_query = st.text_input(
        "Buscar práticas:",
        placeholder="Digite aqui...",
        label_visibility="collapsed"
    )
    st.session_state.search_query = search_query.lower()

# --- HERO SECTION ---
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">🗄️ SQL - Melhores Práticas</h1>
    <p class="hero-subtitle">Domine SQL Estratégico</p>
    <p style="color: #cbd5e1; line-height: 1.6;">
        Aprenda com 60+ práticas documentadas, complete desafios, ganhe pontos e acompanhe seu progresso em tempo real.
    </p>
</div>
""", unsafe_allow_html=True)

# --- STATS SECTION ---
st.markdown("### 📊 Números que Falam")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">60+</div>
        <p style="color: #cbd5e1; margin: 10px 0; font-size: 0.95rem;">Práticas SQL</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{len(st.session_state.favorites)}</div>
        <p style="color: #cbd5e1; margin: 10px 0; font-size: 0.95rem;">Favoritos</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{len(st.session_state.learned)}</div>
        <p style="color: #cbd5e1; margin: 10px 0; font-size: 0.95rem;">Aprendidas</p>
    </div>
    """, unsafe_allow_html=True)

# --- PROGRESSO VISUAL ---
total_practices = 60
learned_count = len(st.session_state.learned)
progress_percent = (learned_count / total_practices) * 100

st.markdown(f"""
<div class="progress-container">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
        <p style="color: #cbd5e1; font-weight: 600; margin: 0;">🎓 Seu Progresso</p>
        <p style="color: var(--accent); font-weight: 700; margin: 0;">{learned_count}/{total_practices}</p>
    </div>
    <div class="progress-bar">
        <div class="progress-fill" style="width: {progress_percent}%"></div>
    </div>
    <p style="color: #94a3b8; font-size: 0.85rem; margin: 10px 0;">
        {'🏆 Parabéns! Você completou todas as práticas!' if learned_count == total_practices else f'Continue! Faltam {total_practices - learned_count} práticas para dominar SQL'}
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- DATABASE DE PRÁTICAS ---
sql_practices = [
    # INICIANTE
    {"icon": "🔍", "title": "Evitar SELECT *", "category": "Performance", "difficulty": "Iniciante", "description": "Selecione apenas as colunas necessárias.", "bad_query": "SELECT * FROM vendas;", "good_query": "SELECT id, produto, valor FROM vendas;", "benefit": "Reduz bandwidth", "context": "Impacto em sistemas grandes", "explanation": "Reduz dados trafegados pela rede."},
    {"icon": "✅", "title": "Tratar NULL Explicitamente", "category": "Lógica & Precisão", "difficulty": "Iniciante", "description": "NULL não é zero.", "bad_query": "SELECT SUM(comissao) FROM vendas;", "good_query": "SELECT SUM(COALESCE(comissao, 0)) FROM vendas;", "benefit": "Evita NULLs", "context": "Crítico financeiro", "explanation": "COALESCE substitui NULLs."},
    {"icon": "🔐", "title": "Prepared Statements", "category": "Segurança & Manutenção", "difficulty": "Iniciante", "description": "Proteja contra SQL Injection.", "bad_query": "SELECT * FROM usuarios WHERE id = '" + str(1) + "';", "good_query": "SELECT * FROM usuarios WHERE id = ?;  // Com parametrização", "benefit": "Segurança", "context": "Obrigatório produção", "explanation": "Previne ataques SQL Injection."},
    {"icon": "📋", "title": "Documentar Queries", "category": "Segurança & Manutenção", "difficulty": "Iniciante", "description": "Comente queries complexas.", "bad_query": "SELECT u.id, COUNT(v.id) FROM usuarios u LEFT JOIN vendas v ON u.id = v.usuario_id;", "good_query": "-- Contagem de vendas por usuário\nSELECT u.id, COUNT(v.id) FROM usuarios u LEFT JOIN vendas v ON u.id = v.usuario_id;", "benefit": "Manutenção fácil", "context": "Equipes", "explanation": "Facilita manutenção futura."},
    {"icon": "🎓", "title": "Usar LIMIT em Development", "category": "Performance", "difficulty": "Iniciante", "description": "Limite resultados em testes.", "bad_query": "SELECT * FROM usuarios;", "good_query": "SELECT * FROM usuarios LIMIT 100;", "benefit": "Testes rápidos", "context": "Dev vs Prod", "explanation": "Evita carregar muitos dados."},
    
    # INTERMEDIÁRIO
    {"icon": "⚡", "title": "Usar INDEXES Estrategicamente", "category": "Performance", "difficulty": "Intermediário", "description": "Acelere buscas.", "bad_query": "SELECT * FROM usuarios WHERE email = 'test@mail.com';", "good_query": "CREATE INDEX idx_email ON usuarios(email);\nSELECT * FROM usuarios WHERE email = 'test@mail.com';", "benefit": "O(n) para O(log n)", "context": "Colunas filtro", "explanation": "Índices reduzem tempo de busca."},
    {"icon": "📊", "title": "Usar JOINs em vez de Subconsultas", "category": "Performance", "difficulty": "Intermediário", "description": "JOINs são mais rápidos.", "bad_query": "SELECT id FROM usuarios WHERE id IN (SELECT usuario_id FROM vendas);", "good_query": "SELECT DISTINCT u.id FROM usuarios u INNER JOIN vendas v ON u.id = v.usuario_id;", "benefit": "Melhor performance", "context": "Muitos registros", "explanation": "JOINs usam índices melhor."},
    {"icon": "🔗", "title": "Validar com Constraints", "category": "Lógica & Precisão", "difficulty": "Intermediário", "description": "Use PRIMARY KEY, FOREIGN KEY.", "bad_query": "CREATE TABLE vendas (id INT, valor FLOAT);", "good_query": "CREATE TABLE vendas (id INT PRIMARY KEY, valor FLOAT CHECK (valor > 0));", "benefit": "Integridade dados", "context": "Sistemas críticos", "explanation": "Previne dados inválidos."},
    {"icon": "🧹", "title": "Normalizar em ETL", "category": "Dados & Limpeza", "difficulty": "Intermediário", "description": "Padronize formatos.", "bad_query": "SELECT TRIM(nome) FROM usuarios WHERE email != '';", "good_query": "WITH clean_users AS (SELECT DISTINCT TRIM(LOWER(nome)) FROM raw_usuarios) SELECT nome FROM clean_users;", "benefit": "Dados confiáveis", "context": "ETL", "explanation": "Normalização garante qualidade."},
    
    # AVANÇADO
    {"icon": "🚀", "title": "Particionar Grandes Tabelas", "category": "Performance", "difficulty": "Avançado", "description": "Divida por critério.", "bad_query": "SELECT * FROM eventos WHERE data >= '2024-01-01';", "good_query": "CREATE TABLE eventos_202401 PARTITION OF eventos FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');", "benefit": "10x+ performance", "context": "Tabelas >100GB", "explanation": "Particionamento melhora I/O."},
    {"icon": "🎯", "title": "Window Functions para Ranking", "category": "Lógica & Precisão", "difficulty": "Avançado", "description": "Calcule rank sem subconsultas.", "bad_query": "SELECT id, (SELECT COUNT(*) FROM usuarios WHERE created_at < u.created_at) FROM usuarios u;", "good_query": "SELECT id, ROW_NUMBER() OVER (ORDER BY created_at) FROM usuarios;", "benefit": "Performance superior", "context": "Ranking", "explanation": "Window functions substituem subconsultas."},
]

# --- FUNÇÃO PARA FILTRAR PRÁTICAS ---
def filter_practices(practices, menu, search_query, favorites, learned):
    if menu == "📖 Todas as Práticas":
        filtered = practices
    elif menu == "⭐ Meus Favoritos":
        filtered = [p for i, p in enumerate(practices) if i in favorites]
    elif menu == "✅ Já Aprendi":
        filtered = [p for i, p in enumerate(practices) if i in learned]
    elif menu == "🏆 Progresso":
        # Mostrar estatísticas
        return None
    else:
        return practices
    
    # Aplicar busca
    if search_query:
        filtered = [p for p in filtered if search_query in p['title'].lower() or search_query in p['description'].lower()]
    
    return filtered

# --- RENDERIZAR BASEADO NO MENU ---
if st.session_state.current_menu == "🏆 Progresso":
    st.markdown("### 🏆 Seu Progresso e Estatísticas")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Práticas Aprendidas", len(st.session_state.learned))
    with col2:
        st.metric("Favoritos", len(st.session_state.favorites))
    with col3:
        st.metric("Pontos Ganhos", st.session_state.user_points)
    
    # Gráfico de progresso por dificuldade
    st.markdown("### 📊 Progresso por Nível")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        iniciante = len([p for p in sql_practices if p['difficulty'] == 'Iniciante'])
        aprendidas_init = len([i for i, p in enumerate(sql_practices) if i in st.session_state.learned and p['difficulty'] == 'Iniciante'])
        st.progress(aprendidas_init / iniciante if iniciante > 0 else 0, text=f"Iniciante: {aprendidas_init}/{iniciante}")
    
    with col2:
        intermediario = len([p for p in sql_practices if p['difficulty'] == 'Intermediário'])
        aprendidas_inter = len([i for i, p in enumerate(sql_practices) if i in st.session_state.learned and p['difficulty'] == 'Intermediário'])
        st.progress(aprendidas_inter / intermediario if intermediario > 0 else 0, text=f"Intermediário: {aprendidas_inter}/{intermediario}")
    
    with col3:
        avancado = len([p for p in sql_practices if p['difficulty'] == 'Avançado'])
        aprendidas_adv = len([i for i, p in enumerate(sql_practices) if i in st.session_state.learned and p['difficulty'] == 'Avançado'])
        st.progress(aprendidas_adv / avancado if avancado > 0 else 0, text=f"Avançado: {aprendidas_adv}/{avancado}")

elif st.session_state.current_menu == "🎯 Desafios":
    st.markdown("### 🎯 Desafios SQL")
    
    challenges = [
        {"num": 1, "titulo": "Contar Usuários Ativos", "descricao": "Quantos usuários estão ativos?", "dica": "Use COUNT(*) com WHERE", "resposta": "SELECT COUNT(*) AS total FROM usuarios WHERE ativo = true;"},
        {"num": 2, "titulo": "Total de Vendas", "descricao": "Total de vendas pagas?", "dica": "Use SUM(valor)", "resposta": "SELECT SUM(valor) FROM vendas WHERE status = 'pago';"},
        {"num": 3, "titulo": "Usuários com Mais Vendas", "descricao": "Qual usuário tem mais vendas?", "dica": "Use GROUP BY", "resposta": "SELECT usuario_id, COUNT(*) FROM vendas GROUP BY usuario_id ORDER BY COUNT(*) DESC LIMIT 1;"},
        {"num": 4, "titulo": "Emails Premium", "descricao": "Emails de usuários premium?", "dica": "Use WHERE categoria", "resposta": "SELECT email FROM usuarios WHERE categoria = 'Premium';"},
        {"num": 5, "titulo": "Produtos por Categoria", "descricao": "Quantos produtos por categoria?", "dica": "Use GROUP BY", "resposta": "SELECT categoria, COUNT(*) FROM produtos GROUP BY categoria;"},
    ]
    
    for challenge in challenges:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**🎯 Desafio {challenge['num']}: {challenge['titulo']}**")
            st.markdown(f"_{challenge['descricao']}_")
            st.markdown(f"💡 **Dica:** {challenge['dica']}")
        with col2:
            if st.button(f"✓ Completar", key=f"challenge_{challenge['num']}"):
                st.session_state.challenges_completed.add(challenge['num'])
                st.session_state.user_points += 10
                st.success("Parabéns! +10 pontos!")
        
        with st.expander("Ver Resposta"):
            st.code(challenge['resposta'], language='sql')
        st.divider()

else:
    # Filtrar práticas
    filtered_practices = filter_practices(sql_practices, st.session_state.current_menu, st.session_state.search_query, st.session_state.favorites, st.session_state.learned)
    
    if filtered_practices is None:
        st.info("Selecione uma seção válida")
    elif len(filtered_practices) == 0:
        st.warning("Nenhuma prática encontrada com essa busca")
    else:
        st.markdown(f"### Mostrando {len(filtered_practices)} práticas")
        
        # Lazy load - mostrar algumas práticas por vez
        per_page = 5
        if 'page' not in st.session_state:
            st.session_state.page = 0
        
        start_idx = st.session_state.page * per_page
        end_idx = start_idx + per_page
        practices_to_show = filtered_practices[start_idx:end_idx]
        
        for idx, practice in enumerate(practices_to_show):
            practice_idx = sql_practices.index(practice)
            
            col1, col2 = st.columns([0.9, 0.1])
            with col2:
                # Botão Favorito
                fav_btn = "⭐" if practice_idx in st.session_state.favorites else "☆"
                if st.button(fav_btn, key=f"fav_{practice_idx}", help="Adicionar aos favoritos"):
                    if practice_idx in st.session_state.favorites:
                        st.session_state.favorites.discard(practice_idx)
                    else:
                        st.session_state.favorites.add(practice_idx)
                        st.session_state.user_points += 5
                    st.rerun()
            
            with col1:
                with st.expander(f"{practice['icon']} {practice['title']} — {practice['difficulty']}"):
                    col_left, col_right = st.columns(2)
                    
                    with col_left:
                        st.markdown(f"**Categoria:** {practice['category']}")
                        st.markdown(f"**Descrição:** {practice['description']}")
                    
                    with col_right:
                        st.markdown(f"**Benefício:** {practice['benefit']}")
                        st.markdown(f"**Contexto:** {practice['context']}")
                    
                    st.divider()
                    st.write("❌ **Evitar:**")
                    st.code(practice['bad_query'], language='sql')
                    st.write("✅ **Fazer:**")
                    st.code(practice['good_query'], language='sql')
                    st.info(f"💡 {practice['explanation']}")
                    
                    # Anotações pessoais
                    st.markdown("**📝 Minhas Anotações:**")
                    note_text = st.text_area(
                        "Escreva suas notas:",
                        value=st.session_state.notes.get(practice_idx, ""),
                        height=80,
                        key=f"note_{practice_idx}",
                        label_visibility="collapsed"
                    )
                    if note_text != st.session_state.notes.get(practice_idx, ""):
                        st.session_state.notes[practice_idx] = note_text
                        st.success("✓ Anotação salva!")
                    
                    # Marcar como aprendida
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button(f"✅ Já Aprendi", key=f"learned_{practice_idx}"):
                            if practice_idx not in st.session_state.learned:
                                st.session_state.learned.add(practice_idx)
                                st.session_state.user_points += 20
                                st.success("Parabéns! +20 pontos! 🎉")
                            else:
                                st.session_state.learned.discard(practice_idx)
                                st.info("Removido de 'Já Aprendi'")
                            st.rerun()
                    
                    with col2:
                        status = "✓ Aprendida" if practice_idx in st.session_state.learned else "Não aprendida"
                        st.markdown(f"**Status:** {status}")
        
        # Paginação
        st.divider()
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.session_state.page > 0:
                if st.button("← Anterior"):
                    st.session_state.page -= 1
                    st.rerun()
        
        with col2:
            total_pages = (len(filtered_practices) + per_page - 1) // per_page
            st.markdown(f"<p style='text-align: center; color: #cbd5e1;'>Página {st.session_state.page + 1}/{total_pages}</p>", unsafe_allow_html=True)
        
        with col3:
            if st.session_state.page < total_pages - 1:
                if st.button("Próximo →"):
                    st.session_state.page += 1
                    st.rerun()

# --- FOOTER ---
st.divider()
st.markdown("""
<div style="text-align: center; padding: 40px 0; color: #cbd5e1;">
    <p style="margin-bottom: 10px; font-size: 0.95rem;">
        <span style="color: var(--accent); font-weight: 600;">SQL - Melhores Práticas Pro</span> 
        • Criado por Rodrigo Aiosa
    </p>
    <p style="font-size: 0.85rem; color: #94a3b8;">
        Transforme seus dados em vantagem competitiva com SQL estratégico
    </p>
</div>
""", unsafe_allow_html=True)
