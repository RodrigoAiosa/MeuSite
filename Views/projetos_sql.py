import streamlit as st
from utils import exibir_rodape, registrar_acesso

# --- CONFIGURAÇÃO DE PÁGINA ---
st.set_page_config(
    page_title="SQL - Melhores Práticas | Rodrigo Aiosa",
    page_icon="🗄️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- REGISTRO DE ACESSO ---
registrar_acesso("SQL - Melhores Práticas")

# --- CUSTOM CSS - Design Profissional com Autoridade ---
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    :root {
        --primary: #0F172A;
        --secondary: #1E293B;
        --accent: #D4AF37;
        --text-light: #E2E8F0;
        --text-dark: #0F172A;
        --border: #334155;
    }
    
    body {
        background: linear-gradient(135deg, #0F172A 0%, #1a2744 100%);
        color: var(--text-light);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #0F172A 0%, #1a2744 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #0F172A 0%, #1a2744 100%);
    }
    
    /* Header Hero */
    .hero-section {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        border-bottom: 2px solid var(--accent);
        padding: 60px 0;
        margin-bottom: 50px;
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -10%;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(212, 175, 55, 0.1) 0%, transparent 70%);
        border-radius: 50%;
        pointer-events: none;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        color: var(--text-light);
        margin-bottom: 15px;
        text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        position: relative;
        z-index: 1;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: var(--accent);
        margin-bottom: 30px;
        font-weight: 500;
        position: relative;
        z-index: 1;
    }
    
    .hero-description {
        font-size: 1.1rem;
        color: #cbd5e1;
        line-height: 1.6;
        max-width: 600px;
        position: relative;
        z-index: 1;
    }
    
    /* Stats Cards */
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 25px;
        margin: 60px 0;
    }
    
    .stat-card {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 40px;
        text-align: center;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        border-color: var(--accent);
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(212, 175, 55, 0.15);
    }
    
    .stat-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--accent), transparent);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .stat-card:hover::before {
        opacity: 1;
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 700;
        color: var(--accent);
        margin-bottom: 10px;
    }
    
    .stat-label {
        font-size: 1rem;
        color: #cbd5e1;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stat-sublabel {
        font-size: 0.85rem;
        color: #94a3b8;
        margin-top: 8px;
    }
    
    /* Section Headers */
    .section-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: var(--text-light);
        margin: 60px 0 40px 0;
        padding-bottom: 20px;
        border-bottom: 2px solid var(--accent);
        position: relative;
    }
    
    .section-header::before {
        content: '';
        position: absolute;
        bottom: -2px;
        left: 0;
        width: 60px;
        height: 3px;
        background: var(--accent);
    }
    
    /* Expander Cards */
    .stExpander {
        background-color: #1E293B !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
    }
    
    .stExpander > div {
        border-color: var(--border) !important;
    }
    
    .stExpander [data-testid="stExpanderToggleButton"] {
        color: var(--accent) !important;
        font-weight: 600;
    }
    
    /* Code Blocks */
    .stCode {
        background-color: #0F172A !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
    }
    
    code {
        color: #60a5fa !important;
        background: transparent !important;
    }
    
    /* Info/Warning Boxes */
    .stInfo {
        background-color: rgba(212, 175, 55, 0.1) !important;
        border: 1px solid var(--accent) !important;
        border-radius: 8px !important;
        padding: 20px !important;
    }
    
    .stSuccess {
        background-color: rgba(34, 197, 94, 0.1) !important;
        border: 1px solid #22c55e !important;
        border-radius: 8px !important;
    }
    
    .stError {
        background-color: rgba(239, 68, 68, 0.1) !important;
        border: 1px solid #ef4444 !important;
        border-radius: 8px !important;
    }
    
    /* Divider */
    hr {
        border-color: var(--border) !important;
        margin: 50px 0 !important;
    }
    
    /* Selectbox & Input */
    .stSelectbox > div > div {
        background-color: #1E293B !important;
        border: 1px solid var(--border) !important;
        color: var(--text-light) !important;
    }
    
    .stTextArea > div > div {
        background-color: #1E293B !important;
        border: 1px solid var(--border) !important;
        color: var(--text-light) !important;
    }
    
    /* Filter Section */
    .filter-section {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 30px;
        margin: 40px 0;
    }
    
    /* Editor Section */
    .editor-section {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 30px;
        margin: 40px 0;
    }
    
    .editor-title {
        font-size: 1.5rem;
        color: var(--accent);
        font-weight: 600;
        margin-bottom: 20px;
    }
    
    /* Challenges Section */
    .challenges-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
        margin: 40px 0;
    }
    
    /* Metrics */
    .metric-box {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 20px;
        text-align: center;
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--accent);
    }
    
    .metric-label {
        color: #cbd5e1;
        font-weight: 600;
        margin-top: 10px;
    }
    
    /* Hover Effects */
    a {
        color: var(--accent) !important;
        transition: all 0.3s ease;
    }
    
    a:hover {
        text-decoration: underline;
        filter: brightness(1.2);
    }
    
    /* Footer */
    footer {
        border-top: 1px solid var(--border);
        padding-top: 40px;
        margin-top: 60px;
    }
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">🗄️ SQL - Melhores Práticas</h1>
    <p class="hero-subtitle">Domine SQL Estratégico</p>
    <p class="hero-description">
        Estratégias avançadas para queries eficientes, escaláveis e precisas. 
        Transforme seus dados em vantagem competitiva com 60+ práticas documentadas.
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
<p style="text-align: center; color: #cbd5e1; margin: 40px 0; font-size: 1.1rem; line-height: 1.8;">
    Queries eficientes são a base de dashboards que escalam. 
    Boas práticas em SQL reduzem tempo de processamento e amplificam a precisão das análises.
    <br><br>
    <span style="color: var(--accent); font-weight: 600;">
    Este é um guia completo para transformar você em um especialista SQL.
    </span>
</p>
""", unsafe_allow_html=True)

st.divider()

# --- DATABASE DE PRÁTICAS SQL ---
sql_practices = [
    # INICIANTE (20+)
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
    {
        "icon": "📍",
        "title": "WHERE antes de JOINs",
        "category": "Performance",
        "difficulty": "Iniciante",
        "description": "Filtre antes de juntar tabelas.",
        "bad_query": "SELECT v.id, v.valor, u.nome, p.nome FROM vendas v JOIN usuarios u ON v.usuario_id = u.id JOIN produtos p ON v.produto_id = p.id WHERE v.ano = 2024;",
        "good_query": "SELECT\n    v.id,\n    v.valor,\n    u.nome,\n    p.nome\nFROM vendas v\nWHERE v.ano = 2024\nJOIN usuarios u\n    ON v.usuario_id = u.id\nJOIN produtos p\n    ON v.produto_id = p.id;",
        "benefit": "Reduz volume antes dos JOINs. Menos linhas para processar.",
        "context": "Filtre na tabela principal ANTES de fazer JOINs.",
        "explanation": "Aplicar filtros antes dos JOINs reduz o número de linhas que precisam ser processadas, economizando I/O e melhorando a performance geral."
    },
    {
        "icon": "🔤",
        "title": "Maiúsculas em SQL Keywords",
        "category": "Dados & Limpeza",
        "difficulty": "Iniciante",
        "description": "Use maiúsculas em SELECT, FROM, WHERE.",
        "bad_query": "select id, nome from usuarios where ativo = true;",
        "good_query": "SELECT\n    id,\n    nome\nFROM usuarios\nWHERE ativo = true;",
        "benefit": "Legibilidade, padrão da indústria.",
        "context": "Code style.",
        "explanation": "Usar maiúsculas em keywords SQL segue o padrão da indústria e melhora a legibilidade, facilitando a leitura e manutenção do código."
    },
    {
        "icon": "👥",
        "title": "Usar Aliases em JOINs",
        "category": "Lógica & Precisão",
        "difficulty": "Iniciante",
        "description": "Dê nomes curtos às tabelas.",
        "bad_query": "SELECT usuarios.id, vendas.valor FROM usuarios JOIN vendas ON usuarios.id = vendas.usuario_id;",
        "good_query": "SELECT\n    u.id,\n    v.valor\nFROM usuarios u\nJOIN vendas v\n    ON u.id = v.usuario_id;",
        "benefit": "Query mais legível e compacta.",
        "context": "Padrão obrigatório em queries.",
        "explanation": "Aliases reduzem a verbosidade da query, tornando-a mais legível e rápida de escrever, especialmente em queries com múltiplos JOINs."
    },
    {
        "icon": "📊",
        "title": "GROUP BY com Agregação",
        "category": "Análise de Dados",
        "difficulty": "Iniciante",
        "description": "Sempre usar COUNT, SUM em GROUP BY.",
        "bad_query": "SELECT usuario_id, status FROM vendas GROUP BY usuario_id, status;",
        "good_query": "SELECT\n    usuario_id,\n    status,\n    COUNT(*) AS total\nFROM vendas\nGROUP BY usuario_id, status;",
        "benefit": "Resultado com contexto numérico.",
        "context": "Análises de negócio.",
        "explanation": "Adicionar funções de agregação (COUNT, SUM) ao GROUP BY fornece contexto numérico essencial para interpretação dos dados agrupados."
    },
    {
        "icon": "🔍",
        "title": "DISTINCT para Remover Duplicatas",
        "category": "Dados & Limpeza",
        "difficulty": "Iniciante",
        "description": "Use DISTINCT quando necessário.",
        "bad_query": "SELECT email FROM usuarios;",
        "good_query": "SELECT DISTINCT email\nFROM usuarios;",
        "benefit": "Valores únicos apenas.",
        "context": "Limpeza de dados.",
        "explanation": "DISTINCT remove registros duplicados, essencial para análises de dados únicos como emails ou identificadores sem duplicação."
    },
    {
        "icon": "⏱️",
        "title": "Date Format Consistente",
        "category": "Lógica & Precisão",
        "difficulty": "Iniciante",
        "description": "Use ISO 8601 (YYYY-MM-DD).",
        "bad_query": "WHERE data = '01/03/2024';",
        "good_query": "WHERE data = '2024-03-01';",
        "benefit": "Sem ambiguidade de formatação.",
        "context": "Padrão internacional.",
        "explanation": "ISO 8601 (YYYY-MM-DD) é o padrão internacional que evita ambiguidade entre datas (Ex: 01/03/2024 pode ser janeiro ou março dependendo da região)."
    },
    {
        "icon": "🚫",
        "title": "Evitar UPDATE Sem WHERE",
        "category": "Segurança & Manutenção",
        "difficulty": "Iniciante",
        "description": "Sempre especifique condição.",
        "bad_query": "UPDATE usuarios SET ativo = false;",
        "good_query": "UPDATE usuarios\nSET ativo = false\nWHERE deletado_em IS NOT NULL;",
        "benefit": "Evita atualizar toda a tabela.",
        "context": "Proteção contra erros.",
        "explanation": "Sem WHERE, a query atualiza TODOS os registros. Sempre especifique a condição para evitar atualizações acidentais em massa."
    },
    {
        "icon": "📌",
        "title": "ORDER BY para Paginação",
        "category": "Performance",
        "difficulty": "Iniciante",
        "description": "Use ORDER BY com LIMIT.",
        "bad_query": "SELECT * FROM usuarios LIMIT 10;",
        "good_query": "SELECT *\nFROM usuarios\nORDER BY created_at DESC\nLIMIT 10;",
        "benefit": "Resultado consistente.",
        "context": "Paginação em aplicações.",
        "explanation": "ORDER BY garante uma ordem consistente antes de LIMIT, essencial para paginação previsível em aplicações web."
    },
    {
        "icon": "🎯",
        "title": "ILIKE para Case-Insensitive",
        "category": "Lógica & Precisão",
        "difficulty": "Iniciante",
        "description": "PostgreSQL: use ILIKE.",
        "bad_query": "WHERE email = 'TEST@MAIL.COM';",
        "good_query": "WHERE email ILIKE 'test@mail.com';",
        "benefit": "Busca sem considerar maiúsculas.",
        "context": "PostgreSQL specific.",
        "explanation": "ILIKE ignora diferenças de maiúsculas/minúsculas na busca, essencial para campos como email que não diferenciam case no banco."
    },
    {
        "icon": "📐",
        "title": "Validar Tipos de Dados",
        "category": "Lógica & Precisão",
        "difficulty": "Iniciante",
        "description": "Verifique tipos ao importar.",
        "bad_query": "INSERT INTO vendas (valor) VALUES ('abc');",
        "good_query": "INSERT INTO vendas (valor)\nVALUES (123.45);",
        "benefit": "Evita erros de tipo.",
        "context": "Data validation.",
        "explanation": "Inserir dados com tipos incorretos causa erros e corrupção de dados. Sempre valide tipos antes de inserir."
    },
    {
        "icon": "🔗",
        "title": "INNER vs LEFT JOIN",
        "category": "Lógica & Precisão",
        "difficulty": "Iniciante",
        "description": "INNER: ambas existem. LEFT: primeira.",
        "bad_query": "SELECT *\nFROM usuarios u\nLEFT JOIN vendas v\n    ON u.id = v.usuario_id;",
        "good_query": "SELECT *\nFROM usuarios u\nINNER JOIN vendas v\n    ON u.id = v.usuario_id;",
        "benefit": "Evita NULLs desnecessários.",
        "context": "Escolha do JOIN correto.",
        "explanation": "INNER JOIN retorna apenas registros que existem em ambas as tabelas. LEFT JOIN inclui todos da esquerda com NULLs se não houver match."
    },
    {
        "icon": "🧮",
        "title": "CAST para Conversão",
        "category": "Lógica & Precisão",
        "difficulty": "Iniciante",
        "description": "Converta tipos explicitamente.",
        "bad_query": "SELECT price + '5' FROM products;",
        "good_query": "SELECT price + CAST('5' AS INT)\nFROM products;",
        "benefit": "Operações seguras.",
        "context": "Type casting.",
        "explanation": "CAST converte tipos explicitamente, evitando coerções automáticas que podem causar comportamento inesperado ou erros."
    },
    {
        "icon": "⚠️",
        "title": "HAVING para Filtrar GROUP BY",
        "category": "Análise de Dados",
        "difficulty": "Iniciante",
        "description": "Use HAVING após GROUP BY.",
        "bad_query": "SELECT usuario_id, COUNT(*) FROM vendas WHERE COUNT(*) > 5 GROUP BY usuario_id;",
        "good_query": "SELECT usuario_id, COUNT(*) AS total\nFROM vendas\nGROUP BY usuario_id\nHAVING COUNT(*) > 5;",
        "benefit": "Sintaxe correta e eficiente.",
        "context": "Agregação com condição.",
        "explanation": "HAVING filtra grupos APÓS agregação, enquanto WHERE filtra antes. Usar WHERE para agregados causará erro, HAVING é a forma correta."
    },
    {
        "icon": "🔀",
        "title": "UNION para Combinar Resultados",
        "category": "Dados & Limpeza",
        "difficulty": "Iniciante",
        "description": "Combine dois SELECTs.",
        "bad_query": "SELECT id FROM usuarios; SELECT id FROM clientes;",
        "good_query": "SELECT id FROM usuarios\nUNION\nSELECT id FROM clientes;",
        "benefit": "Um resultado combinado.",
        "context": "Combinação de datasets.",
        "explanation": "UNION combina resultados de múltiplas queries, removendo duplicatas automaticamente. Use UNION ALL se quiser manter duplicatas."
    },
    {
        "icon": "📊",
        "title": "COUNT(*) vs COUNT(coluna)",
        "category": "Análise de Dados",
        "difficulty": "Iniciante",
        "description": "COUNT(*) inclui NULLs.",
        "bad_query": "SELECT COUNT(email) FROM usuarios;",
        "good_query": "SELECT COUNT(*) AS total_usuarios\nFROM usuarios;",
        "benefit": "Conta correta de registros.",
        "context": "Agregação.",
        "explanation": "COUNT(*) conta todos os registros incluindo NULLs, enquanto COUNT(coluna) ignora NULLs. Use COUNT(*) para contagem total de registros."
    },
    {
        "icon": "🎁",
        "title": "DEFAULT em CREATE TABLE",
        "category": "Lógica & Precisão",
        "difficulty": "Iniciante",
        "description": "Defina valores padrão.",
        "bad_query": "CREATE TABLE usuarios (\n    id INT,\n    ativo BOOLEAN\n);",
        "good_query": "CREATE TABLE usuarios (\n    id INT,\n    ativo BOOLEAN DEFAULT true\n);",
        "benefit": "Menos NULLs inesperados.",
        "context": "Schema design.",
        "explanation": "Definir DEFAULT no schema evita NULLs inesperados quando dados são inseridos sem especificar a coluna, garantindo valores consistentes."
    },

    # INTERMEDIÁRIO (20+)
    {
        "icon": "⚡",
        "title": "Usar INDEXES Estrategicamente",
        "category": "Performance",
        "difficulty": "Intermediário",
        "description": "Índices aceleram buscas, mas desaceleram inserts/updates.",
        "bad_query": "SELECT * FROM usuarios WHERE email = 'test@mail.com';",
        "good_query": "CREATE INDEX idx_usuarios_email ON usuarios(email);\nSELECT id, nome\nFROM usuarios\nWHERE email = 'test@mail.com';",
        "benefit": "Reduz tempo de busca O(n) para O(log n).",
        "context": "Use em WHERE clauses, JOINs e ORDER BY.",
        "explanation": "Índices aceleram buscas significativamente em colunas frequentemente consultadas, reduzindo de O(n) para O(log n). Crie em colunas de filtro."
    },
    {
        "icon": "📊",
        "title": "Usar JOINs em vez de Subconsultas",
        "category": "Performance",
        "difficulty": "Intermediário",
        "description": "JOINs são geralmente mais rápidos.",
        "bad_query": "SELECT id, nome\nFROM usuarios\nWHERE id IN (\n    SELECT usuario_id\n    FROM vendas\n    WHERE ano = 2024\n);",
        "good_query": "SELECT DISTINCT u.id, u.nome\nFROM usuarios u\nINNER JOIN vendas v\n    ON u.id = v.usuario_id\nWHERE v.ano = 2024;",
        "benefit": "JOINs usam índices melhor.",
        "context": "Crítico com muitos registros.",
        "explanation": "JOINs são otimizados pelos query planners e usam índices melhor que subconsultas, resultando em melhor performance em grandes datasets."
    },
    {
        "icon": "🔗",
        "title": "Validar com Constraints",
        "category": "Lógica & Precisão",
        "difficulty": "Intermediário",
        "description": "Use PRIMARY KEY, FOREIGN KEY, CHECK.",
        "bad_query": "CREATE TABLE vendas (\n    id INT,\n    valor FLOAT,\n    usuario_id INT\n);",
        "good_query": "CREATE TABLE vendas (\n    id INT PRIMARY KEY,\n    valor FLOAT CHECK (valor > 0),\n    usuario_id INT NOT NULL REFERENCES usuarios(id)\n);",
        "benefit": "Previne dados inválidos na origem.",
        "context": "Essencial em sistemas críticos.",
        "explanation": "Constraints garantem integridade de dados no nível do banco, impedindo dados inválidos antes de serem inseridos."
    },
    {
        "icon": "🧹",
        "title": "Normalizar em ETL",
        "category": "Dados & Limpeza",
        "difficulty": "Intermediário",
        "description": "Padronize formatos, remova duplicatas.",
        "bad_query": "SELECT TRIM(nome), COUNT(*)\nFROM usuarios\nWHERE email != ''\nGROUP BY TRIM(nome);",
        "good_query": "WITH clean_users AS (\n    SELECT DISTINCT\n        TRIM(LOWER(nome)) AS nome\n    FROM raw_usuarios\n    WHERE email IS NOT NULL\n)\nSELECT nome, COUNT(*)\nFROM clean_users\nGROUP BY nome;",
        "benefit": "Queries mais rápidas, dados confiáveis.",
        "context": "Use CTEs para ETL.",
        "explanation": "Normalizar dados em ETL (Extract-Transform-Load) garante consistência e qualidade, acelerando queries futuras e análises mais confiáveis."
    },
    {
        "icon": "📈",
        "title": "CTEs para Modularidade",
        "category": "Dados & Limpeza",
        "difficulty": "Intermediário",
        "description": "Quebre queries complexas em etapas.",
        "bad_query": "SELECT u.nome, SUM(CASE WHEN v.status='concluida' THEN v.valor ELSE 0 END) FROM usuarios u LEFT JOIN vendas v ON u.id = v.usuario_id WHERE u.created_at > '2024-01-01' GROUP BY u.id;",
        "good_query": "WITH usuarios_recentes AS (\n    SELECT id, nome\n    FROM usuarios\n    WHERE created_at > '2024-01-01'\n)\nSELECT u.nome\nFROM usuarios_recentes u;",
        "benefit": "Código legível, fácil testabilidade.",
        "context": "Padrão ouro em análise de dados.",
        "explanation": "CTEs (WITH clauses) quebram queries complexas em subqueries nomeadas e legíveis, facilitando manutenção e teste de lógica em etapas."
    },
    {
        "icon": "🛡️",
        "title": "Transactions (ACID)",
        "category": "Segurança & Manutenção",
        "difficulty": "Intermediário",
        "description": "Agrupe operações em transações.",
        "bad_query": "UPDATE contas SET saldo = saldo - 100 WHERE id = 1;\nUPDATE contas SET saldo = saldo + 100 WHERE id = 2;",
        "good_query": "BEGIN TRANSACTION;\nUPDATE contas\nSET saldo = saldo - 100\nWHERE id = 1;\nUPDATE contas\nSET saldo = saldo + 100\nWHERE id = 2;\nCOMMIT;",
        "benefit": "Impede data corruption.",
        "context": "Essencial em operações financeiras.",
        "explanation": "Transações garantem que múltiplas operações são executadas atomicamente (tudo ou nada), evitando inconsistências em dados críticos."
    },
    {
        "icon": "🎯",
        "title": "Pivotear com CASE WHEN",
        "category": "Análise de Dados",
        "difficulty": "Intermediário",
        "description": "Transforme linhas em colunas.",
        "bad_query": "SELECT mes, categoria, SUM(vendas)\nFROM vendas_agrupadas\nGROUP BY mes, categoria;",
        "good_query": "SELECT mes,\n    SUM(CASE WHEN categoria = 'A'\n        THEN vendas ELSE 0 END) AS categ_a,\n    SUM(CASE WHEN categoria = 'B'\n        THEN vendas ELSE 0 END) AS categ_b\nFROM vendas_agrupadas\nGROUP BY mes;",
        "benefit": "Facilita comparações.",
        "context": "Ideal para Excel/BI.",
        "explanation": "Usar CASE WHEN transforma linhas em colunas (pivot), permitindo comparações lado a lado de categorias em uma única linha."
    },
    {
        "icon": "🔍",
        "title": "LIKE com Pattern Matching",
        "category": "Lógica & Precisão",
        "difficulty": "Intermediário",
        "description": "Use % e _ para buscas parciais.",
        "bad_query": "SELECT *\nFROM usuarios\nWHERE nome = 'Maria';",
        "good_query": "SELECT *\nFROM usuarios\nWHERE nome LIKE 'Maria%';",
        "benefit": "Buscas flexíveis.",
        "context": "Full-text search básico.",
        "explanation": "LIKE com wildcards (% para múltiplos caracteres, _ para um caractere) permite buscas parciais e flexíveis em strings."
    },
    {
        "icon": "⏸️",
        "title": "Batch Processing",
        "category": "Performance",
        "difficulty": "Intermediário",
        "description": "Processe em lotes, não um por um.",
        "bad_query": "FOR each row:\n    INSERT INTO log VALUES (row);",
        "good_query": "INSERT INTO log\nSELECT *\nFROM staging;",
        "benefit": "Performance em 100x.",
        "context": "Bulk operations.",
        "explanation": "Processar em lotes (bulk insert) reduz overhead de transações individuais, melhorando performance em 10-100x comparado a inserts um por um."
    },
    {
        "icon": "🔀",
        "title": "LEFT JOIN com NULL Check",
        "category": "Lógica & Precisão",
        "difficulty": "Intermediário",
        "description": "Identifique registros sem match.",
        "bad_query": "SELECT u.id\nFROM usuarios u\nLEFT JOIN vendas v\n    ON u.id = v.usuario_id;",
        "good_query": "SELECT u.id\nFROM usuarios u\nLEFT JOIN vendas v\n    ON u.id = v.usuario_id\nWHERE v.id IS NULL;",
        "benefit": "Encontra registros órfãos.",
        "context": "Data reconciliation.",
        "explanation": "Usar IS NULL após LEFT JOIN identifica registros da tabela esquerda que não têm correspondência, essencial para encontrar dados órfãos."
    },
    {
        "icon": "📊",
        "title": "SUM + CASE para Condicional",
        "category": "Análise de Dados",
        "difficulty": "Intermediário",
        "description": "Soma condicional.",
        "bad_query": "SELECT SUM(valor)\nFROM vendas\nWHERE status = 'pago';",
        "good_query": "SELECT SUM(\n    CASE WHEN status = 'pago'\n        THEN valor ELSE 0 END\n) AS total_pago\nFROM vendas;",
        "benefit": "Flexibilidade em agregação.",
        "context": "Análises complexas.",
        "explanation": "CASE WHEN em funções de agregação permite somas condicionais em uma única query, evitando múltiplas subconsultas."
    },
    {
        "icon": "🎓",
        "title": "Usar COALESCE para NULLs",
        "category": "Lógica & Precisão",
        "difficulty": "Intermediário",
        "description": "Substitua NULLs por padrão.",
        "bad_query": "SELECT desconto\nFROM vendas;",
        "good_query": "SELECT COALESCE(desconto, 0) AS desconto\nFROM vendas;",
        "benefit": "Evita cálculos com NULL.",
        "context": "Data cleaning.",
        "explanation": "COALESCE substitui NULLs pelo primeiro valor não-nulo da lista, evitando que cálculos resultem em NULL."
    },
    {
        "icon": "🔢",
        "title": "BETWEEN para Ranges",
        "category": "Performance",
        "difficulty": "Intermediário",
        "description": "Mais eficiente que AND.",
        "bad_query": "SELECT *\nFROM vendas\nWHERE data >= '2024-01-01'\n    AND data <= '2024-12-31';",
        "good_query": "SELECT *\nFROM vendas\nWHERE data BETWEEN '2024-01-01'\n    AND '2024-12-31';",
        "benefit": "Sintaxe mais clara.",
        "context": "Range queries.",
        "explanation": "BETWEEN é mais legível e eficiente que AND para comparações de range, sendo otimizado pelo query planner para melhor performance."
    },
    {
        "icon": "⚡",
        "title": "Index Compostos para Multi-Coluna",
        "category": "Performance",
        "difficulty": "Intermediário",
        "description": "Índices em múltiplas colunas.",
        "bad_query": "CREATE INDEX idx_user ON vendas(usuario_id);\nCREATE INDEX idx_status ON vendas(status);",
        "good_query": "CREATE INDEX idx_user_status\n    ON vendas(usuario_id, status);",
        "benefit": "Melhor performance em queries com AND.",
        "context": "Index strategy.",
        "explanation": "Índices compostos (múltiplas colunas) são mais eficientes que múltiplos índices para queries com AND, reduzindo I/O significativamente."
    },
    {
        "icon": "🎯",
        "title": "IN com Subconsulta",
        "category": "Lógica & Precisão",
        "difficulty": "Intermediário",
        "description": "Filtre por resultados de query.",
        "bad_query": "SELECT *\nFROM usuarios\nWHERE id IN (1, 2, 3, 4, 5);",
        "good_query": "SELECT *\nFROM usuarios\nWHERE id IN (\n    SELECT user_id\n    FROM premium_users\n);",
        "benefit": "Dinâmico e escalável.",
        "context": "Filtros complexos.",
        "explanation": "IN com subconsultas é dinâmico e escalável, permitindo filtros baseados em outras queries sem hard-coding valores."
    },
    {
        "icon": "📌",
        "title": "NOT IN com Cuidado",
        "category": "Performance",
        "difficulty": "Intermediário",
        "description": "NOT IN ignora NULLs, use NOT EXISTS.",
        "bad_query": "SELECT *\nFROM usuarios\nWHERE id NOT IN (\n    SELECT user_id\n    FROM bloqueados\n);",
        "good_query": "SELECT *\nFROM usuarios u\nWHERE NOT EXISTS (\n    SELECT 1\n    FROM bloqueados b\n    WHERE b.user_id = u.id\n);",
        "benefit": "Comportamento esperado.",
        "context": "NULL handling.",
        "explanation": "NOT IN ignora NULLs na subconsulta, causando resultados inesperados. NOT EXISTS é seguro e mais eficiente em grandes datasets."
    },
    {
        "icon": "🔀",
        "title": "CROSS JOIN para Combinações",
        "category": "Análise de Dados",
        "difficulty": "Intermediário",
        "description": "Produto cartesiano.",
        "bad_query": "SELECT *\nFROM cidades, produtos;",
        "good_query": "SELECT *\nFROM cidades\nCROSS JOIN produtos;",
        "benefit": "Sintaxe explícita.",
        "context": "Combinações todas.",
        "explanation": "CROSS JOIN cria produto cartesiano (todas as combinações possíveis). Usar sintaxe explícita é melhor que vírgula, tornando a intenção clara."
    },
    {
        "icon": "📊",
        "title": "GROUP BY com HAVING",
        "category": "Análise de Dados",
        "difficulty": "Intermediário",
        "description": "Filtre grupos por agregação.",
        "bad_query": "SELECT usuario_id, COUNT(*)\nFROM vendas\nGROUP BY usuario_id;",
        "good_query": "SELECT usuario_id, COUNT(*) AS total\nFROM vendas\nGROUP BY usuario_id\nHAVING COUNT(*) > 10;",
        "benefit": "Filtra após agregação.",
        "context": "Análise de dados.",
        "explanation": "HAVING filtra grupos após agregação, permitindo encontrar padrões em grupos específicos sem precisar de subconsultas."
    },
    {
        "icon": "🎯",
        "title": "CAST para Data/Hora",
        "category": "Lógica & Precisão",
        "difficulty": "Intermediário",
        "description": "Converta string para date.",
        "bad_query": "SELECT *\nFROM vendas\nWHERE data = '2024-03-08';",
        "good_query": "SELECT *\nFROM vendas\nWHERE CAST(data AS DATE) = '2024-03-08';",
        "benefit": "Comparação correta.",
        "context": "Type conversion.",
        "explanation": "CAST garante comparação correta de tipos, evitando problemas quando a coluna é TIMESTAMP mas você quer comparar apenas a data."
    },

    # AVANÇADO (20+)
    {
        "icon": "🚀",
        "title": "Particionar Grandes Tabelas",
        "category": "Performance",
        "difficulty": "Avançado",
        "description": "Divida tabelas por critério (data, região).",
        "bad_query": "SELECT *\nFROM eventos\nWHERE data >= '2024-01-01';",
        "good_query": "CREATE TABLE eventos_202401\nPARTITION OF eventos\nFOR VALUES FROM ('2024-01-01')\n    TO ('2024-02-01');",
        "benefit": "Melhora performance em 10x+.",
        "context": "Use com tabelas maiores que 100GB.",
        "explanation": "Particionamento divide tabelas grandes em partes menores por critério (data, região), reduzindo I/O e acelerando queries em 10x+."
    },
    {
        "icon": "🎯",
        "title": "Window Functions para Ranking",
        "category": "Lógica & Precisão",
        "difficulty": "Avançado",
        "description": "Calcule rank, running total sem subconsultas.",
        "bad_query": "SELECT id, nome,\n    (SELECT COUNT(*) FROM usuarios\n     WHERE created_at < u.created_at) AS rank\nFROM usuarios u;",
        "good_query": "SELECT id, nome,\n    ROW_NUMBER() OVER\n    (ORDER BY created_at) AS rank\nFROM usuarios;",
        "benefit": "Código legível, performance superior.",
        "context": "Ótimo para ranking e moving averages.",
        "explanation": "Window functions (ROW_NUMBER, RANK, DENSE_RANK) substituem subconsultas correlacionadas, oferecendo performance superior e código mais legível."
    },
    {
        "icon": "⚙️",
        "title": "Desnormalizar para OLAP",
        "category": "Dados & Limpeza",
        "difficulty": "Avançado",
        "description": "Duplicar dados para análise acelera queries.",
        "bad_query": "SELECT v.id, u.nome, p.nome, c.nome, v.valor\nFROM vendas v\nJOIN usuarios u ON v.usuario_id = u.id\nJOIN produtos p ON v.produto_id = p.id\nJOIN categorias c ON p.categoria_id = c.id;",
        "good_query": "CREATE TABLE vendas_denorm AS\nSELECT v.id, u.nome, p.nome,\n       c.nome, v.valor\nFROM vendas v\nJOIN usuarios u ON v.usuario_id = u.id\nJOIN produtos p ON v.produto_id = p.id;",
        "benefit": "Queries muito mais rápidas.",
        "context": "OLTP normalizado, OLAP desnormalizado.",
        "explanation": "Desnormalizar para OLAP (data warehouse) duplica dados intencionalmente, acelerando queries de análise eliminando necessidade de múltiplos JOINs."
    },
    {
        "icon": "📊",
        "title": "EXPLAIN/ANALYZE",
        "category": "Otimização",
        "difficulty": "Avançado",
        "description": "Inspecione o plano de execução.",
        "bad_query": "SELECT *\nFROM vendas\nWHERE usuario_id = 123;",
        "good_query": "EXPLAIN ANALYZE\nSELECT *\nFROM vendas\nWHERE usuario_id = 123;",
        "benefit": "Identifica se usa índices.",
        "context": "Ferramenta imprescindível.",
        "explanation": "EXPLAIN mostra o plano de execução, revelando se a query usa índices e identificando gargalos. ANALYZE executa a query com estatísticas reais."
    },
    {
        "icon": "🔄",
        "title": "Recursion para Hierarquias",
        "category": "Análise de Dados",
        "difficulty": "Avançado",
        "description": "Navegue estruturas hierárquicas.",
        "bad_query": "SELECT *\nFROM categorias\nWHERE categoria_pai_id IS NULL;",
        "good_query": "WITH RECURSIVE categoria_tree AS (\n    SELECT id, nome, categoria_pai_id, 0 AS nivel\n    FROM categorias\n    WHERE categoria_pai_id IS NULL\n    UNION ALL\n    SELECT c.id, c.nome, c.categoria_pai_id,\n           ct.nivel + 1\n    FROM categorias c\n    JOIN categoria_tree ct\n        ON c.categoria_pai_id = ct.id\n)\nSELECT *\nFROM categoria_tree\nORDER BY nivel;",
        "benefit": "Simplifica navegação.",
        "context": "Para organograma e estruturas.",
        "explanation": "Recursive CTEs navegam hierarquias (árvores, organogramas) de forma elegante, evitando múltiplas queries ou stored procedures complexas."
    },
    {
        "icon": "📈",
        "title": "Row_Number, Rank, Dense_Rank",
        "category": "Análise de Dados",
        "difficulty": "Avançado",
        "description": "Diferentes formas de ranking.",
        "bad_query": "SELECT id, COUNT(*)\nFROM vendas\nGROUP BY id;",
        "good_query": "SELECT id,\n    ROW_NUMBER() OVER\n    (ORDER BY valor DESC) AS row_num,\n    RANK() OVER\n    (ORDER BY valor DESC) AS rank\nFROM vendas;",
        "benefit": "Ranking flexível.",
        "context": "Analytics avançado.",
        "explanation": "ROW_NUMBER (sem empates), RANK (com empates mantém gaps), DENSE_RANK (com empates sem gaps) oferecem diferentes estratégias de ranking."
    },
    {
        "icon": "🎯",
        "title": "LAG e LEAD para Comparação",
        "category": "Análise de Dados",
        "difficulty": "Avançado",
        "description": "Compare com linha anterior/próxima.",
        "bad_query": "SELECT data, valor\nFROM vendas\nORDER BY data;",
        "good_query": "SELECT data, valor,\n    LAG(valor) OVER\n    (ORDER BY data) AS prev_valor,\n    LEAD(valor) OVER\n    (ORDER BY data) AS next_valor\nFROM vendas;",
        "benefit": "Análise temporal.",
        "context": "Time series analysis.",
        "explanation": "LAG/LEAD acessam linhas anteriores/próximas sem subconsultas, essencial para análise temporal e cálculo de variações entre períodos."
    },
    {
        "icon": "🔀",
        "title": "PARTITION BY em Window Functions",
        "category": "Análise de Dados",
        "difficulty": "Avançado",
        "description": "Window functions por grupo.",
        "bad_query": "SELECT usuario_id, SUM(valor)\nFROM vendas\nGROUP BY usuario_id;",
        "good_query": "SELECT usuario_id, valor,\n    SUM(valor) OVER\n    (PARTITION BY usuario_id) AS total_user\nFROM vendas;",
        "benefit": "Agregação sem perder detalhes.",
        "context": "Advanced analytics.",
        "explanation": "PARTITION BY em window functions cria agregações por grupo mantendo todas as linhas, permitindo comparar registros com totalizações de seu grupo."
    },
    {
        "icon": "⚡",
        "title": "Materialized Views",
        "category": "Performance",
        "difficulty": "Avançado",
        "description": "Cache de queries complexas.",
        "bad_query": "SELECT *\nFROM vendas\nWHERE ano = 2024;",
        "good_query": "CREATE MATERIALIZED VIEW vendas_2024 AS\nSELECT *\nFROM vendas\nWHERE ano = 2024;\nREFRESH MATERIALIZED VIEW vendas_2024;",
        "benefit": "Queries pré-calculadas.",
        "context": "Performance otimizada.",
        "explanation": "Materialized Views pré-calculam e armazenam resultados de queries complexas, acelerando drasticamente consultas recorrentes."
    },
    {
        "icon": "🔐",
        "title": "Row-Level Security",
        "category": "Segurança & Manutenção",
        "difficulty": "Avançado",
        "description": "Controle de acesso por linha.",
        "bad_query": "SELECT * FROM usuarios;",
        "good_query": "CREATE POLICY user_policy ON usuarios\nUSING (usuario_atual = current_user);",
        "benefit": "Segurança de dados.",
        "context": "Multi-tenant systems.",
        "explanation": "Row-Level Security garante que usuários apenas acessem dados que lhes pertencem, essencial para sistemas multi-tenant com dados sensíveis."
    },
    {
        "icon": "📊",
        "title": "CUBE para Análise Multi-Dimensional",
        "category": "Otimização",
        "difficulty": "Avançado",
        "description": "Agregações em todas as combinações.",
        "bad_query": "SELECT categoria, regiao, SUM(vendas)\nFROM vendas\nGROUP BY categoria, regiao;",
        "good_query": "SELECT categoria, regiao, SUM(vendas)\nFROM vendas\nGROUP BY CUBE(categoria, regiao);",
        "benefit": "Análise multi-dimensional.",
        "context": "OLAP cubes.",
        "explanation": "CUBE gera agregações para todas as combinações de colunas em uma única query, essencial para OLAP e análises multi-dimensionais."
    },
    {
        "icon": "🎓",
        "title": "ROLLUP para Agregação Hierárquica",
        "category": "Otimização",
        "difficulty": "Avançado",
        "description": "Agregações por níveis.",
        "bad_query": "SELECT ano, mes, dia, SUM(vendas)\nFROM vendas\nGROUP BY ano, mes, dia;",
        "good_query": "SELECT ano, mes, dia, SUM(vendas)\nFROM vendas\nGROUP BY ROLLUP(ano, mes, dia);",
        "benefit": "Totalizações automáticas.",
        "context": "Hierarchical aggregation.",
        "explanation": "ROLLUP gera agregações em hierarquia (totais por ano, por mês dentro do ano, por dia), criando subtotais automaticamente."
    },
    {
        "icon": "🔄",
        "title": "Temporal Tables para Auditoria",
        "category": "Monitoramento",
        "difficulty": "Avançado",
        "description": "Rastreie histórico de dados.",
        "bad_query": "UPDATE usuarios\nSET email = 'new@mail.com'\nWHERE id = 1;",
        "good_query": "CREATE TABLE usuarios_history (\n    id, email, valid_from, valid_to\n);\nUPDATE usuarios\nSET email = 'new@mail.com'\nWHERE id = 1;",
        "benefit": "Auditoria completa.",
        "context": "Compliance requirements.",
        "explanation": "Temporal tables rastreiam histórico de dados automaticamente, permitindo auditar quando e como dados foram alterados, essencial para compliance."
    },
    {
        "icon": "⚙️",
        "title": "JSON Functions para Dados Semiestruturados",
        "category": "Arquitetura",
        "difficulty": "Avançado",
        "description": "Trabalhe com JSON no SQL.",
        "bad_query": "SELECT *\nFROM usuarios;",
        "good_query": "SELECT\n    data->>'nome',\n    data->'endereco'->>'cidade'\nFROM usuarios;",
        "benefit": "Flexibilidade estrutural.",
        "context": "NoSQL in SQL.",
        "explanation": "JSON functions permitem trabalhar com dados semiestruturados em SQL, oferecendo flexibilidade de NoSQL sem perder poder relacional."
    },
    {
        "icon": "📈",
        "title": "Full-Text Search",
        "category": "Performance",
        "difficulty": "Avançado",
        "description": "Busca textual otimizada.",
        "bad_query": "SELECT *\nFROM artigos\nWHERE conteudo LIKE '%postgres%';",
        "good_query": "SELECT *\nFROM artigos\nWHERE to_tsvector(conteudo)\n    @@ plainto_tsquery('postgres');",
        "benefit": "Busca semântica rápida.",
        "context": "Text search advanced.",
        "explanation": "Full-text search utiliza índices especializados e algoritmos semânticos, acelerando buscas em textos em 100x+ comparado a LIKE."
    },
    {
        "icon": "🎯",
        "title": "Array Functions",
        "category": "Arquitetura",
        "difficulty": "Avançado",
        "description": "Trabalhe com arrays no PostgreSQL.",
        "bad_query": "SELECT tags\nFROM posts;",
        "good_query": "SELECT tags\nFROM posts\nWHERE 'sql' = ANY(tags);",
        "benefit": "Dados estruturados flexíveis.",
        "context": "PostgreSQL specific.",
        "explanation": "Arrays em PostgreSQL permitem armazenar coleções em uma coluna com funções especializadas, oferecendo flexibilidade entre SQL e NoSQL."
    },
    {
        "icon": "🔐",
        "title": "Encryption at Rest",
        "category": "Segurança & Manutenção",
        "difficulty": "Avançado",
        "description": "Criptografe dados sensíveis.",
        "bad_query": "INSERT INTO usuarios (email, ssn)\nVALUES ('test@mail.com', '123-45-6789');",
        "good_query": "INSERT INTO usuarios (email, ssn)\nVALUES ('test@mail.com',\n    pgp_sym_encrypt(\n        '123-45-6789', 'key'\n    )\n);",
        "benefit": "Proteção de dados.",
        "context": "Security compliance.",
        "explanation": "Criptografia no banco protege dados sensíveis mesmo se o servidor for comprometido, essencial para PII (Personally Identifiable Information)."
    },
    {
        "icon": "📊",
        "title": "Approximate Aggregate Functions",
        "category": "Otimização",
        "difficulty": "Avançado",
        "description": "Aproximações rápidas de counts.",
        "bad_query": "SELECT COUNT(DISTINCT usuario_id)\nFROM vendas;",
        "good_query": "SELECT approx_distinct(usuario_id)\nFROM vendas;",
        "benefit": "Performance dramática.",
        "context": "BigData scenarios.",
        "explanation": "Funções aproximadas sacrificam precisão por velocidade, reduzindo tempo de execução em 100x+ para contagens distintas em datasets enormes."
    },
    {
        "icon": "⏱️",
        "title": "Query Timeout Strategy",
        "category": "Monitoramento",
        "difficulty": "Avançado",
        "description": "Configure timeout para queries.",
        "bad_query": "SELECT *\nFROM tabela_gigante;",
        "good_query": "SET statement_timeout = '5s';\nSELECT *\nFROM tabela_gigante\nLIMIT 1000;",
        "benefit": "Evita lock-ups.",
        "context": "Production safety.",
        "explanation": "Timeouts protegem produção de queries descontroladas que congelam servidores, evitando indisponibilidade causada por queries mal otimizadas."
    },
    {
        "icon": "🎓",
        "title": "Connection Pooling",
        "category": "Arquitetura",
        "difficulty": "Avançado",
        "description": "Reutilize conexões.",
        "bad_query": "# Criar nova conexão a cada query",
        "good_query": "# Usar PgBouncer ou similar\n# para pool de conexões",
        "benefit": "Escalabilidade.",
        "context": "System architecture.",
        "explanation": "Connection pooling reutiliza conexões entre múltiplas queries, reduzindo overhead de handshake TCP e escalando para milhares de usuários concorrentes."
    },
]

st.divider()

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

# --- APLICAR FILTROS ---
filtered_practices = sql_practices

if selected_category != "Todas":
    filtered_practices = [p for p in filtered_practices if p["category"] == selected_category]

if selected_difficulty != "Todas":
    filtered_practices = [p for p in filtered_practices if p["difficulty"] == selected_difficulty]

# --- RENDERIZAR PRÁTICAS ---
st.divider()

st.markdown(f"""
<div style="text-align: center; margin: 30px 0;">
    <p style="font-size: 1.1rem; color: #cbd5e1;">
        <span style="color: var(--accent); font-weight: 700;">📌 {len(filtered_practices)}</span> 
        de 
        <span style="color: var(--accent); font-weight: 700;">{len(sql_practices)}</span> 
        práticas
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

for idx, practice in enumerate(filtered_practices, 1):
    with st.expander(f"{practice['icon']} {practice['title']} — {practice['difficulty']}", expanded=False):
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.write(f"**Categoria:** {practice['category']}")
            st.write(f"**Descrição:** {practice['description']}")
            st.write(f"**Contexto:** {practice['context']}")
        
        with col2:
            st.write(f"**Benefício:** {practice['benefit']}")
        
        st.divider()
        
        st.write("❌ **EVITAR:**")
        st.code(practice['bad_query'], language='sql')
        
        st.write("✅ **FAZER:**")
        st.code(practice['good_query'], language='sql')
        st.info(f"💡 {practice.get('explanation', 'Esta é a abordagem recomendada para melhor performance e legibilidade.')}")

st.markdown("""
<div style="background: linear-gradient(135deg, #1E293B 0%, #334155 100%); border: 1px solid var(--border); border-radius: 12px; padding: 30px; margin: 40px 0;">
    <p style="color: var(--accent); font-weight: 600; font-size: 1.1rem; margin-bottom: 10px;">💡 Essas práticas são apenas o começo</p>
    <p style="color: #cbd5e1; font-size: 0.95rem;">
        Consultoria em SQL estratégico para transformar seus dados em vantagem competitiva. 
        Combine essas técnicas para criar queries que impressionam.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- SEÇÃO EDITOR SQL ---
st.markdown('<h2 class="section-header">✏️ Editor SQL Interativo</h2>', unsafe_allow_html=True)
st.markdown('<p style="color: #cbd5e1; margin-bottom: 30px;">Teste suas queries SQL em tempo real. Escolha um template ou escreva a sua própria query!</p>', unsafe_allow_html=True)

# --- EXEMPLOS PRÉ-DEFINIDOS ---
sql_templates = {
    "SELECT Básico": "SELECT * FROM usuarios LIMIT 10;",
    "WHERE Filtro": "SELECT id, nome, email FROM usuarios WHERE ativo = true;",
    "COUNT Agregação": "SELECT COUNT(*) AS total_usuarios FROM usuarios;",
    "GROUP BY": "SELECT categoria, COUNT(*) AS total FROM produtos GROUP BY categoria;",
    "JOIN Tabelas": "SELECT u.nome, v.valor FROM usuarios u INNER JOIN vendas v ON u.id = v.usuario_id LIMIT 5;",
    "ORDER BY": "SELECT id, nome, created_at FROM usuarios ORDER BY created_at DESC LIMIT 10;",
    "SUM com CASE": "SELECT usuario_id, SUM(CASE WHEN status = 'pago' THEN valor ELSE 0 END) AS total_pago FROM vendas GROUP BY usuario_id;",
    "LEFT JOIN": "SELECT u.id, u.nome, COUNT(v.id) AS total_vendas FROM usuarios u LEFT JOIN vendas v ON u.id = v.usuario_id GROUP BY u.id, u.nome;",
    "DISTINCT": "SELECT DISTINCT categoria FROM produtos ORDER BY categoria;",
    "BETWEEN": "SELECT * FROM vendas WHERE data BETWEEN '2024-01-01' AND '2024-03-31';",
    "IN Clause": "SELECT * FROM usuarios WHERE id IN (1, 2, 3, 4, 5);",
    "LIKE Pattern": "SELECT * FROM usuarios WHERE email LIKE '%@gmail.com';",
}

st.markdown('<div class="editor-section">', unsafe_allow_html=True)

# --- LAYOUT ---
col_template, col_editor = st.columns([1, 2], gap="large")

with col_template:
    st.markdown('<p class="editor-title">📚 Templates</p>', unsafe_allow_html=True)
    selected_template = st.selectbox(
        "Escolha um exemplo:",
        ["Escrever Manual"] + list(sql_templates.keys()),
        key="template_select",
        label_visibility="collapsed"
    )
    
    if selected_template != "Escrever Manual":
        template_query = sql_templates[selected_template]
    else:
        template_query = ""

with col_editor:
    st.markdown('<p class="editor-title">📝 Seu SQL</p>', unsafe_allow_html=True)
    user_query = st.text_area(
        "Escreva sua query SQL:",
        value=template_query,
        height=150,
        key="sql_editor",
        placeholder="SELECT * FROM usuarios;",
        label_visibility="collapsed"
    )

st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- SEÇÃO DE RESULTADO ---
st.markdown('<h2 class="section-header">📊 Resultado da Query</h2>', unsafe_allow_html=True)

col_result, col_info = st.columns([2, 1], gap="large")

with col_result:
    st.markdown('<div style="background: linear-gradient(135deg, #1E293B 0%, #334155 100%); border: 1px solid var(--border); border-radius: 8px; padding: 20px;">', unsafe_allow_html=True)
    
    if user_query.strip():
        try:
            import pandas as pd
            
            usuarios_df = pd.DataFrame({
                'id': [1, 2, 3, 4, 5],
                'nome': ['Alice Silva', 'Bob Santos', 'Carlos Oliveira', 'Diana Costa', 'Eduardo Pereira'],
                'email': ['alice@gmail.com', 'bob@gmail.com', 'carlos@hotmail.com', 'diana@gmail.com', 'edu@outlook.com'],
                'ativo': [True, True, False, True, True],
                'created_at': ['2023-01-15', '2023-02-20', '2023-03-10', '2023-04-05', '2023-05-12'],
                'categoria': ['Premium', 'Standard', 'Premium', 'Free', 'Standard']
            })
            
            vendas_df = pd.DataFrame({
                'id': [1, 2, 3, 4, 5, 6],
                'usuario_id': [1, 2, 1, 3, 2, 5],
                'valor': [150.00, 200.00, 75.50, 300.00, 120.00, 450.00],
                'status': ['pago', 'pago', 'pendente', 'pago', 'cancelado', 'pago'],
                'data': ['2024-01-10', '2024-01-15', '2024-02-01', '2024-02-10', '2024-02-15', '2024-03-01']
            })
            
            produtos_df = pd.DataFrame({
                'id': [1, 2, 3, 4],
                'nome': ['Produto A', 'Produto B', 'Produto C', 'Produto D'],
                'categoria': ['Eletrônicos', 'Eletrônicos', 'Livros', 'Livros'],
                'preco': [99.99, 199.99, 29.99, 49.99]
            })
            
            query_lower = user_query.lower()
            
            if 'usuarios' in query_lower and 'vendas' in query_lower:
                result = usuarios_df.merge(vendas_df, left_on='id', right_on='usuario_id', how='inner').head(10)
            elif 'vendas' in query_lower and 'group by' in query_lower:
                result = vendas_df.groupby('usuario_id').agg({'valor': 'sum', 'id': 'count'}).reset_index()
                result.columns = ['usuario_id', 'total_valor', 'total_vendas']
            elif 'usuarios' in query_lower and 'count' in query_lower:
                result = pd.DataFrame({'total_usuarios': [len(usuarios_df)]})
            elif 'distinct' in query_lower and 'categoria' in query_lower:
                result = pd.DataFrame({'categoria': produtos_df['categoria'].unique()})
            elif 'usuarios' in query_lower:
                result = usuarios_df.head(10)
            elif 'vendas' in query_lower:
                result = vendas_df.head(10)
            elif 'produtos' in query_lower:
                result = produtos_df.head(10)
            else:
                result = usuarios_df.head(10)
            
            st.dataframe(result, use_container_width=True)
            st.success(f"✅ Query executada com sucesso! {len(result)} registros retornados.")
            
        except Exception as e:
            st.error(f"❌ Erro ao executar query: {str(e)}")
    else:
        st.markdown("""
        <div style="text-align: center; padding: 40px; color: #94a3b8;">
            <p style="font-size: 1rem;">📝 Escreva uma query SQL no editor para ver o resultado</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col_info:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1E293B 0%, #334155 100%); border: 1px solid var(--border); border-radius: 8px; padding: 20px;">
        <p style="color: var(--accent); font-weight: 600; margin-bottom: 15px; font-size: 1rem;">ℹ️ Tabelas & Dicas</p>
        <p style="color: #cbd5e1; font-size: 0.85rem; line-height: 1.6; margin-bottom: 15px;">
            <strong>usuarios:</strong> id, nome, email, ativo, created_at, categoria
            <br><br>
            <strong>vendas:</strong> id, usuario_id, valor, status, data
            <br><br>
            <strong>produtos:</strong> id, nome, categoria, preco
        </p>
        <p style="color: #cbd5e1; font-size: 0.85rem; font-style: italic; border-top: 1px solid var(--border); padding-top: 15px;">
            💡 Teste SELECT, WHERE, JOIN, GROUP BY, LIMIT e mais!
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- DESAFIOS SQL ---
st.markdown('<h2 class="section-header">🎯 Desafios SQL</h2>', unsafe_allow_html=True)
st.markdown('<p style="color: #cbd5e1; margin-bottom: 30px;">Complete os desafios abaixo e teste seus conhecimentos!</p>', unsafe_allow_html=True)

challenges = [
    {
        "numero": 1,
        "titulo": "Contar Usuários Ativos",
        "descricao": "Quantos usuários estão com status ativo?",
        "dica": "Use COUNT(*) com WHERE ativo = true",
        "resposta": "SELECT COUNT(*) AS total_ativos FROM usuarios WHERE ativo = true;"
    },
    {
        "numero": 2,
        "titulo": "Total de Vendas Pagas",
        "descricao": "Qual é o valor total de vendas com status 'pago'?",
        "dica": "Use SUM(valor) com WHERE status = 'pago'",
        "resposta": "SELECT SUM(valor) AS total_pago FROM vendas WHERE status = 'pago';"
    },
    {
        "numero": 3,
        "titulo": "Usuários com Mais Vendas",
        "descricao": "Qual usuário tem mais vendas associadas?",
        "dica": "Use GROUP BY usuario_id com COUNT(*)",
        "resposta": "SELECT usuario_id, COUNT(*) AS total_vendas FROM vendas GROUP BY usuario_id ORDER BY total_vendas DESC LIMIT 1;"
    },
    {
        "numero": 4,
        "titulo": "Email de Usuários Premium",
        "descricao": "Quais são os emails dos usuários da categoria Premium?",
        "dica": "Use WHERE categoria = 'Premium'",
        "resposta": "SELECT email FROM usuarios WHERE categoria = 'Premium';"
    },
    {
        "numero": 5,
        "titulo": "Produtos por Categoria",
        "descricao": "Quantos produtos existem em cada categoria?",
        "dica": "Use GROUP BY categoria com COUNT(*)",
        "resposta": "SELECT categoria, COUNT(*) AS total_produtos FROM produtos GROUP BY categoria;"
    },
]

st.markdown('<h2 class="section-header">🎯 Desafios SQL</h2>', unsafe_allow_html=True)
st.markdown('<p style="color: #cbd5e1; margin-bottom: 30px;">Complete os desafios abaixo e teste seus conhecimentos!</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")
challenge_cols = [col1, col2] * 3

for idx, challenge in enumerate(challenges):
    with challenge_cols[idx]:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #1E293B 0%, #334155 100%); border: 1px solid var(--border); border-radius: 8px; padding: 20px; margin-bottom: 15px;">
            <p style="color: var(--accent); font-weight: 700; font-size: 1.1rem; margin-bottom: 10px;">
                🎯 Desafio {challenge['numero']}
            </p>
            <p style="color: var(--text-light); font-weight: 600; margin-bottom: 8px;">
                {challenge['titulo']}
            </p>
            <p style="color: #cbd5e1; font-size: 0.9rem; margin-bottom: 12px; line-height: 1.5;">
                {challenge['descricao']}
            </p>
            <p style="color: #94a3b8; font-size: 0.85rem; border-top: 1px solid var(--border); padding-top: 10px;">
                💡 <strong>Dica:</strong> {challenge['dica']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("✅ Ver Resposta"):
            st.code(challenge['resposta'], language='sql')
            st.success("Compare sua resposta com esta solução!")

st.divider()

# --- FOOTER ---
st.markdown("""
<div style="text-align: center; padding: 40px 0; border-top: 1px solid var(--border); color: #cbd5e1;">
    <p style="margin-bottom: 10px; font-size: 0.95rem;">
        <span style="color: var(--accent); font-weight: 600;">SQL - Melhores Práticas</span> 
        • Criado por Rodrigo Aiosa
    </p>
    <p style="font-size: 0.85rem; color: #94a3b8;">
        Transforme seus dados em vantagem competitiva com SQL estratégico
    </p>
</div>
""", unsafe_allow_html=True)

exibir_rodape()
