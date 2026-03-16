#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔════════════════════════════════════════════════════════════════════════════════╗
║                           SQL ACADEMY - TRAINING PLATFORM                      ║
║                                                                                ║
║  Uma plataforma profissional de treinamento em SQL com 3 níveis de             ║
║  dificuldade, quiz interativo, sistema de progressão e resultado final.        ║
║  Inclui seção de SQL em Libras para acessibilidade.                            ║
║                                                                                ║
║  Author: SQL Academy Team                                                      ║
║  Version: 2.0.0                                                                ║
║  License: MIT                                                                  ║
╚════════════════════════════════════════════════════════════════════════════════╝
"""

import streamlit as st
from datetime import datetime

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURAÇÃO DA PÁGINA
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="SQL Academy - Treinamento em SQL",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ═══════════════════════════════════════════════════════════════════════════════
# CSS CUSTOMIZADO
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Lora:wght@400;500&display=swap');
    
    * {
        font-family: 'Lora', serif;
    }
    
    .playfair {
        font-family: 'Playfair Display', serif;
    }
    
    body {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #0c4a6e 100%);
    }
    
    .main {
        padding-top: 2rem;
    }
    
    /* Estilos de Título Principal */
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #fbbf24 0%, #fcd34d 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .subtitle {
        text-align: center;
        color: #93c5fd;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* Cards de Nível */
    .level-card {
        padding: 2rem;
        border-radius: 1rem;
        border: 2px solid rgba(251, 191, 36, 0.3);
        text-align: center;
        transition: all 0.3s ease;
        background: rgba(30, 58, 138, 0.2);
        margin: 1rem 0;
    }
    
    .level-card:hover {
        border-color: #fbbf24;
        background: rgba(30, 58, 138, 0.3);
        transform: translateY(-5px);
    }
    
    .level-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .level-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #fcd34d;
    }
    
    .level-desc {
        color: #93c5fd;
        font-size: 0.95rem;
        margin-bottom: 1rem;
    }
    
    /* Explicação */
    .explanation-box {
        background: rgba(30, 58, 138, 0.3);
        border-left: 4px solid #fbbf24;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1.5rem;
    }
    
    .explanation-title {
        font-family: 'Playfair Display', serif;
        color: #fcd34d;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .explanation-text {
        color: #93c5fd;
        line-height: 1.6;
    }
    
    /* Progresso */
    .progress-info {
        display: flex;
        justify-content: space-between;
        margin-bottom: 1rem;
        color: #93c5fd;
        font-size: 0.9rem;
        font-weight: 600;
    }
    
    /* Resultado */
    .result-box {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 1rem;
        padding: 2rem;
        text-align: center;
        margin: 2rem 0;
    }
    
    .result-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        animation: bounce 0.6s ease;
    }
    
    .result-title {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        color: white;
        margin-bottom: 1rem;
        font-weight: 700;
    }
    
    .result-score {
        font-size: 3rem;
        color: #fcd34d;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .result-percentage {
        font-size: 1.5rem;
        color: #93c5fd;
        margin-bottom: 1.5rem;
    }
    
    .result-details {
        background: rgba(15, 23, 42, 0.5);
        border-radius: 0.5rem;
        padding: 1rem;
        color: #93c5fd;
    }
    
    .result-details p {
        margin: 0.5rem 0;
    }
    
    .stButton > button {
        width: 100%;
        padding: 0.75rem;
        border-radius: 0.5rem;
        font-weight: 600;
        font-family: 'Lora', serif;
        transition: all 0.3s ease;
        border: none;
        font-size: 1rem;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }

    /* ═══════════════════════════════════
       ESTILOS DA SEÇÃO LIBRAS
    ═══════════════════════════════════ */

    .libras-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #0c4a6e 100%);
        border: 2px solid rgba(251,191,36,0.4);
        border-radius: 1.2rem;
        padding: 2rem;
        text-align: center;
        margin-bottom: 2rem;
    }

    .libras-header-title {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 700;
        color: #fcd34d;
        margin-bottom: 0.4rem;
    }

    .libras-header-sub {
        color: #93c5fd;
        font-size: 1rem;
    }

    /* Card de conceito Libras */
    .libras-card {
        background: rgba(30, 58, 138, 0.25);
        border: 2px solid rgba(251,191,36,0.2);
        border-radius: 1rem;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        transition: border-color 0.3s;
    }

    .libras-card:hover {
        border-color: rgba(251,191,36,0.7);
    }

    .libras-card-title {
        font-family: 'Playfair Display', serif;
        color: #fcd34d;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .libras-card-desc {
        color: #93c5fd;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 1rem;
    }

    /* Avatar animado SVG */
    .avatar-stage {
        background: rgba(15, 23, 42, 0.6);
        border-radius: 0.8rem;
        padding: 1.2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.8rem;
        border: 1px solid rgba(251,191,36,0.15);
    }

    .avatar-label {
        color: #fcd34d;
        font-size: 0.85rem;
        font-weight: 600;
        text-align: center;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }

    .handshape-grid {
        display: flex;
        gap: 0.6rem;
        flex-wrap: wrap;
        justify-content: center;
        margin-top: 0.5rem;
    }

    .handshape-item {
        background: rgba(251,191,36,0.1);
        border: 1px solid rgba(251,191,36,0.3);
        border-radius: 0.5rem;
        padding: 0.5rem 0.8rem;
        text-align: center;
        font-size: 0.8rem;
        color: #e2e8f0;
    }

    .handshape-item span {
        display: block;
        font-size: 1.8rem;
        margin-bottom: 0.2rem;
    }

    .tip-box {
        background: rgba(251,191,36,0.08);
        border-left: 3px solid #fbbf24;
        border-radius: 0.4rem;
        padding: 0.8rem 1rem;
        color: #fcd34d;
        font-size: 0.88rem;
        margin-top: 0.8rem;
        line-height: 1.5;
    }

    /* Navegação de conceitos */
    .concept-nav {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
        margin-bottom: 1.5rem;
    }

    .nav-pill {
        background: rgba(30,58,138,0.4);
        border: 1px solid rgba(251,191,36,0.25);
        border-radius: 2rem;
        padding: 0.4rem 1rem;
        color: #93c5fd;
        font-size: 0.85rem;
        cursor: pointer;
        transition: all 0.2s;
    }

    .nav-pill.active {
        background: rgba(251,191,36,0.2);
        border-color: #fbbf24;
        color: #fcd34d;
        font-weight: 600;
    }

    .badge-accessibility {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        background: rgba(34,197,94,0.15);
        border: 1px solid rgba(34,197,94,0.4);
        border-radius: 2rem;
        padding: 0.3rem 0.9rem;
        color: #86efac;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    @media (max-width: 768px) {
        .main-title { font-size: 2rem; }
        .result-score { font-size: 2.5rem; }
        .libras-header-title { font-size: 1.5rem; }
    }
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# BANCO DE DADOS DE QUIZ
# ═══════════════════════════════════════════════════════════════════════════════

QUIZZES = {
    'básico': [
        {
            'id': 1,
            'title': 'O que é SQL?',
            'explanation': 'SQL (Structured Query Language) é uma linguagem padronizada para gerenciar e manipular bancos de dados relacionais. É essencial para qualquer pessoa que trabalha com dados.',
            'question': 'Qual é o principal propósito da linguagem SQL?',
            'options': [
                'Criar interfaces gráficas',
                'Gerenciar e manipular dados em bancos de dados',
                'Desenvolver aplicativos mobile',
                'Criar documentos em PDF',
                'Gerenciar conexões de rede'
            ],
            'correct': 1
        },
        {
            'id': 2,
            'title': 'Comando SELECT',
            'explanation': 'O SELECT é o comando fundamental para recuperar dados de uma tabela. A sintaxe básica é: SELECT coluna FROM tabela. Este é o comando mais utilizado em SQL.',
            'question': 'Qual comando SQL é usado para recuperar dados de uma tabela?',
            'options': [
                'INSERT',
                'UPDATE',
                'DELETE',
                'SELECT',
                'CREATE'
            ],
            'correct': 3
        },
        {
            'id': 3,
            'title': 'Cláusula WHERE',
            'explanation': 'A cláusula WHERE filtra registros com base em condições específicas. Exemplo: SELECT * FROM usuarios WHERE idade > 18. Permite refinar consultas para obter dados específicos.',
            'question': 'Qual cláusula SQL é usada para filtrar registros?',
            'options': [
                'GROUP BY',
                'ORDER BY',
                'WHERE',
                'JOIN',
                'HAVING'
            ],
            'correct': 2
        },
        {
            'id': 4,
            'title': 'Comando INSERT',
            'explanation': 'INSERT adiciona novos registros a uma tabela. Sintaxe: INSERT INTO tabela (colunas) VALUES (valores). É fundamental para adicionar dados ao banco.',
            'question': 'Como inserir um novo registro em uma tabela?',
            'options': [
                'INSERT INTO tabela (colunas) VALUES (valores)',
                'ADD INTO tabela VALUES (valores)',
                'PUT INTO tabela (colunas) VALUES (valores)',
                'APPEND tabela (colunas) VALUES (valores)',
                'NEW INTO tabela VALUES (valores)'
            ],
            'correct': 0
        },
        {
            'id': 5,
            'title': 'Tipos de Dados',
            'explanation': 'SQL suporta vários tipos de dados: INT (inteiro), VARCHAR (texto variável), DATE (data), DECIMAL (número decimal), BOOLEAN (verdadeiro/falso). Cada tipo serve para um propósito específico.',
            'question': 'Qual tipo de dados SQL é apropriado para armazenar texto?',
            'options': [
                'INT',
                'VARCHAR',
                'DATE',
                'BOOLEAN',
                'DECIMAL'
            ],
            'correct': 1
        }
    ],
    'intermediário': [
        {
            'id': 1,
            'title': 'JOINs',
            'explanation': 'JOINs combinam registros de duas ou mais tabelas. INNER JOIN retorna apenas registros que correspondem em ambas as tabelas. Existem também LEFT, RIGHT, FULL e CROSS JOIN.',
            'question': 'Qual tipo de JOIN retorna apenas registros que existem em ambas as tabelas?',
            'options': [
                'LEFT JOIN',
                'RIGHT JOIN',
                'INNER JOIN',
                'FULL JOIN',
                'CROSS JOIN'
            ],
            'correct': 2
        },
        {
            'id': 2,
            'title': 'Agregações',
            'explanation': 'Funções de agregação como COUNT(), SUM(), AVG(), MAX(), MIN() executam cálculos sobre grupos de registros. São fundamentais para análise de dados.',
            'question': 'Qual função SQL retorna o valor máximo de uma coluna?',
            'options': [
                'COUNT()',
                'SUM()',
                'MAX()',
                'AVG()',
                'MIN()'
            ],
            'correct': 2
        },
        {
            'id': 3,
            'title': 'GROUP BY',
            'explanation': 'GROUP BY agrupa registros que possuem o mesmo valor em uma coluna específica, geralmente usado com funções de agregação. Permite análise de dados por categorias.',
            'question': 'Para agrupar resultados por categoria, qual cláusula usar?',
            'options': [
                'WHERE categoria = valor',
                'ORDER BY categoria',
                'GROUP BY categoria',
                'PARTITION BY categoria',
                'DISTINCT categoria'
            ],
            'correct': 2
        },
        {
            'id': 4,
            'title': 'Subconsultas',
            'explanation': 'Uma subconsulta é uma consulta dentro de outra consulta. Pode ser usada em SELECT, FROM, WHERE ou HAVING. Permite consultas mais complexas e aninhadas.',
            'question': 'O que é uma subconsulta em SQL?',
            'options': [
                'Uma consulta que ordena resultados',
                'Uma consulta que filtra por intervalo',
                'Uma consulta dentro de outra consulta',
                'Uma consulta com múltiplas tabelas',
                'Uma consulta com agregação'
            ],
            'correct': 2
        },
        {
            'id': 5,
            'title': 'LIKE e Wildcards',
            'explanation': 'LIKE é usado para buscar padrões em texto. % representa zero ou mais caracteres, _ representa um caractere. Exemplo: SELECT * FROM usuarios WHERE nome LIKE \'A%\'.',
            'question': 'Qual é a função do operador % em uma cláusula LIKE?',
            'options': [
                'Representar um caractere exato',
                'Representar zero ou mais caracteres',
                'Representar um intervalo de números',
                'Comparar datas',
                'Calcular percentuais'
            ],
            'correct': 1
        }
    ],
    'avançado': [
        {
            'id': 1,
            'title': 'Window Functions',
            'explanation': 'Window Functions realizam cálculos sobre um conjunto de linhas (janela). Exemplos: ROW_NUMBER(), RANK(), DENSE_RANK(), LAG(), LEAD(). São poderosas para análise de dados complexa.',
            'question': 'Qual função window calcula a posição de uma linha dentro de uma partição?',
            'options': [
                'AGGREGATE()',
                'ROW_NUMBER()',
                'DISTRIBUTE()',
                'PARTITION_SUM()',
                'CALCULATE()'
            ],
            'correct': 1
        },
        {
            'id': 2,
            'title': 'CTEs (Common Table Expressions)',
            'explanation': 'CTEs (WITH clause) criam tabelas temporárias nomeadas dentro de uma consulta, melhorando legibilidade e reutilização. Sintaxe: WITH nome_cte AS (SELECT ...) SELECT ...',
            'question': 'Qual cláusula SQL cria uma tabela temporária nomeada (CTE)?',
            'options': [
                'TEMPORARY TABLE',
                'CREATE TEMP',
                'WITH',
                'DECLARE',
                'DEFINE'
            ],
            'correct': 2
        },
        {
            'id': 3,
            'title': 'Índices',
            'explanation': 'Índices aceleram buscas em tabelas. Tipos incluem PRIMARY KEY, UNIQUE, COMPOSITE. Sintaxe: CREATE INDEX nome ON tabela (coluna). Melhoram performance mas usam espaço em disco.',
            'question': 'Qual é o principal benefício de criar um índice em uma coluna?',
            'options': [
                'Aumentar o tamanho do banco de dados',
                'Reduzir a memória RAM necessária',
                'Acelerar consultas de busca',
                'Melhorar a inserção de dados',
                'Evitar duplicatas automaticamente'
            ],
            'correct': 2
        },
        {
            'id': 4,
            'title': 'Transações e ACID',
            'explanation': 'Transações garantem que operações sejam atômicas (tudo ou nada). Propriedades ACID: Atomicidade, Consistência, Isolamento, Durabilidade. São críticas para integridade de dados.',
            'question': 'O que significa a propriedade "Atomicidade" em uma transação?',
            'options': [
                'Vários usuários podem acessar simultaneamente',
                'Os dados são permanentes após commit',
                'Ou toda a operação ocorre ou nenhuma',
                'Os dados permanecem consistentes',
                'As operações são isoladas entre si'
            ],
            'correct': 2
        },
        {
            'id': 5,
            'title': 'Query Optimization',
            'explanation': 'Otimização envolve usar EXPLAIN para analisar planos de execução, evitar SELECT *, usar índices apropriados e reescrever consultas. É essencial para performance.',
            'question': 'Qual comando mostra o plano de execução de uma consulta?',
            'options': [
                'ANALYZE',
                'EXECUTE',
                'EXPLAIN',
                'PROFILE',
                'BENCHMARK'
            ],
            'correct': 2
        }
    ]
}

# ═══════════════════════════════════════════════════════════════════════════════
# CONTEÚDO LIBRAS — Conceitos básicos de SQL em Libras
# ═══════════════════════════════════════════════════════════════════════════════
# Cada conceito traz:
#   - title / icon / description_pt  (explicação em português)
#   - sign_description               (descrição textual do sinal em Libras)
#   - handshapes                     (configurações de mão usadas)
#   - movement                       (movimento do sinal)
#   - location                       (local de articulação)
#   - tip                            (dica mnemônica)
#   - avatar_svg                     (avatar SVG animado representando o sinal)
# ═══════════════════════════════════════════════════════════════════════════════

LIBRAS_CONCEPTS = [
    {
        "id": "banco_dados",
        "title": "Banco de Dados",
        "icon": "🗄️",
        "description_pt": "Um banco de dados é um sistema organizado para armazenar, gerenciar e recuperar informações. Em SQL, trabalhamos diretamente com bancos de dados relacionais.",
        "sign_description": "Sinal de ARMAZENAR/GUARDAR combinado com o sinal de ORGANIZADO. Ambas as mãos em configuração B (dedos unidos, palma aberta) se fecham simultaneamente em direção ao corpo, como se guardasse algo.",
        "handshapes": [
            {"emoji": "🤲", "label": "Mão B"},
            {"emoji": "✊", "label": "Fechar"},
            {"emoji": "📦", "label": "Guardar"},
        ],
        "movement": "As duas mãos se fecham em direção ao peito (movimento de guardar/arquivar).",
        "location": "Frente ao corpo, altura do peito.",
        "tip": "💡 Pense em 'guardar uma caixa cheia de informações' — esse movimento de fechar as mãos representa o armazenamento de dados.",
        "avatar_key": "storage",
    },
    {
        "id": "tabela",
        "title": "Tabela",
        "icon": "📋",
        "description_pt": "Uma tabela organiza dados em linhas e colunas, como uma planilha. Cada linha é um registro e cada coluna é um atributo desse registro.",
        "sign_description": "Sinal de TABELA em Libras: as duas mãos espalmadas se posicionam horizontalmente formando um retângulo no ar, representando as bordas de uma tabela.",
        "handshapes": [
            {"emoji": "🤚", "label": "Mão B aberta"},
            {"emoji": "📐", "label": "Retângulo"},
            {"emoji": "⬜", "label": "Grade"},
        ],
        "movement": "As mãos traçam um retângulo no ar (horizontal), depois os dedos indicadores de ambas as mãos fazem linhas verticais e horizontais alternadas, indicando a grade da tabela.",
        "location": "Na frente do corpo, nível da cintura.",
        "tip": "💡 Desenhe a tabela no ar! O movimento de traçar linhas é intuitivo — você está literalmente desenhando a estrutura da tabela.",
        "avatar_key": "table",
    },
    {
        "id": "select",
        "title": "SELECT",
        "icon": "🔍",
        "description_pt": "SELECT é o comando para consultar/buscar dados de uma tabela. É o comando mais utilizado em SQL e o ponto de partida de toda consulta.",
        "sign_description": "Sinal de BUSCAR/PESQUISAR: a mão dominante em configuração de pinça (polegar + indicador unidos) realiza um movimento circular no ar como se estivesse pesquisando, depois aponta para baixo indicando 'busca na tabela'.",
        "handshapes": [
            {"emoji": "🤌", "label": "Pinça"},
            {"emoji": "👇", "label": "Apontar"},
            {"emoji": "🔄", "label": "Circular"},
        ],
        "movement": "Movimento circular da mão dominante em configuração de pinça, seguido de movimento descendente (apontando para a tabela imaginária).",
        "location": "Frente ao corpo, nível do rosto/ombro.",
        "tip": "💡 A pinça + movimento circular lembra uma lupa de pesquisa — SELECT é exatamente isso: pesquisar e selecionar dados.",
        "avatar_key": "select",
    },
    {
        "id": "where",
        "title": "WHERE",
        "icon": "🎯",
        "description_pt": "WHERE é a cláusula que filtra registros segundo uma condição. Só retorna os dados que atendem ao critério especificado.",
        "sign_description": "Sinal de CONDIÇÃO/FILTRO: a mão dominante em configuração de dedo indicador estendido aponta para a lateral, depois as duas mãos em configuração F (polegar + indicador formam círculo) se unem representando um filtro/peneira.",
        "handshapes": [
            {"emoji": "☝️", "label": "Indicador"},
            {"emoji": "👌", "label": "Configuração F"},
            {"emoji": "⚗️", "label": "Filtrar"},
        ],
        "movement": "O indicador aponta para um lado (condição), depois as duas mãos em F se encostam e afastam como uma peneira filtrando.",
        "location": "Frente ao corpo, lateral direita.",
        "tip": "💡 Pense numa peneira — WHERE filtra os dados, deixando passar apenas o que satisfaz a condição.",
        "avatar_key": "where",
    },
    {
        "id": "insert",
        "title": "INSERT",
        "icon": "➕",
        "description_pt": "INSERT adiciona novos registros a uma tabela. É o comando usado para incluir dados novos no banco de dados.",
        "sign_description": "Sinal de INSERIR/INCLUIR: a mão dominante em configuração de dedo indicador estendido entra por baixo da mão não-dominante (espalmada horizontalmente como uma tabela), representando a inserção de um dado.",
        "handshapes": [
            {"emoji": "☝️", "label": "Indicador"},
            {"emoji": "🤚", "label": "Palma horizontal"},
            {"emoji": "⬆️", "label": "Inserir"},
        ],
        "movement": "A mão não-dominante permanece horizontal (a tabela). A mão dominante sobe por baixo e entra, como inserindo uma ficha.",
        "location": "Frente ao corpo, nível da cintura.",
        "tip": "💡 Imagine inserir um cartão em uma caixa — o movimento de 'enfiar por baixo' é exatamente o conceito de adicionar dados a uma tabela.",
        "avatar_key": "insert",
    },
    {
        "id": "coluna_linha",
        "title": "Coluna e Linha",
        "icon": "⬜",
        "description_pt": "Colunas organizam os atributos (nome, idade, email…) e linhas organizam cada registro. A interseção entre coluna e linha é uma célula.",
        "sign_description": "COLUNA: dedo indicador da mão dominante traça uma linha vertical de cima para baixo. LINHA: dedo indicador traça uma linha horizontal da esquerda para a direita.",
        "handshapes": [
            {"emoji": "☝️", "label": "Indicador"},
            {"emoji": "⬇️", "label": "Coluna (vertical)"},
            {"emoji": "➡️", "label": "Linha (horizontal)"},
        ],
        "movement": "Para COLUNA: trace uma linha vertical de cima para baixo. Para LINHA: trace uma linha horizontal da esquerda para a direita.",
        "location": "Frente ao corpo, nível do peito.",
        "tip": "💡 Coluna = movimento VERTICAL (como uma coluna de prédio). Linha = movimento HORIZONTAL (como uma linha do horizonte). Simples de memorizar!",
        "avatar_key": "colrow",
    },
]

# SVG dos avatares animados (representações estilizadas dos sinais)
def get_avatar_svg(avatar_key: str) -> str:
    """Retorna o SVG do avatar animado conforme o sinal"""

    # Paleta compartilhada
    skin = "#F5CBA7"
    skin_dark = "#E59866"
    shirt = "#1e3a8a"
    hair = "#2c3e50"
    bg = "rgba(15,23,42,0)"

    avatars = {

        # ── BANCO DE DADOS: mãos fechando em direção ao peito ──────────────
        "storage": f"""
<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" width="200" height="220">
  <style>
    .lh {{ animation: closeL 1.6s ease-in-out infinite; transform-origin: 60px 140px; }}
    .rh {{ animation: closeR 1.6s ease-in-out infinite; transform-origin: 140px 140px; }}
    @keyframes closeL {{
      0%,100% {{ transform: translateX(0) rotate(0deg); }}
      50%      {{ transform: translateX(18px) rotate(-20deg); }}
    }}
    @keyframes closeR {{
      0%,100% {{ transform: translateX(0) rotate(0deg); }}
      50%      {{ transform: translateX(-18px) rotate(20deg); }}
    }}
  </style>
  <!-- Corpo/torso -->
  <rect x="75" y="110" width="50" height="60" rx="8" fill="{shirt}"/>
  <!-- Cabeça -->
  <circle cx="100" cy="75" r="28" fill="{skin}"/>
  <rect x="78" y="50" width="44" height="18" rx="9" fill="{hair}"/>
  <!-- Olhos -->
  <circle cx="91" cy="78" r="3" fill="#2c3e50"/>
  <circle cx="109" cy="78" r="3" fill="#2c3e50"/>
  <!-- Boca sorridente -->
  <path d="M93 88 Q100 94 107 88" stroke="#e67e22" stroke-width="2" fill="none" stroke-linecap="round"/>
  <!-- Mão esquerda (B fechando) -->
  <g class="lh">
    <rect x="42" y="128" width="32" height="22" rx="8" fill="{skin}"/>
    <rect x="44" y="124" width="6" height="12" rx="3" fill="{skin_dark}"/>
    <rect x="52" y="122" width="6" height="14" rx="3" fill="{skin_dark}"/>
    <rect x="60" y="124" width="6" height="12" rx="3" fill="{skin_dark}"/>
  </g>
  <!-- Mão direita (B fechando) -->
  <g class="rh">
    <rect x="126" y="128" width="32" height="22" rx="8" fill="{skin}"/>
    <rect x="128" y="124" width="6" height="12" rx="3" fill="{skin_dark}"/>
    <rect x="136" y="122" width="6" height="14" rx="3" fill="{skin_dark}"/>
    <rect x="144" y="124" width="6" height="12" rx="3" fill="{skin_dark}"/>
  </g>
  <!-- Ícone banco de dados -->
  <ellipse cx="100" cy="192" rx="18" ry="7" fill="#fbbf24" opacity="0.8"/>
  <rect x="82" y="192" width="36" height="14" fill="#fbbf24" opacity="0.6"/>
  <ellipse cx="100" cy="206" rx="18" ry="7" fill="#f59e0b" opacity="0.9"/>
</svg>""",

        # ── TABELA: mãos traçando retângulo e grade ─────────────────────────
        "table": f"""
<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" width="200" height="220">
  <style>
    .lh2 {{ animation: traceL 2s ease-in-out infinite; transform-origin: 55px 145px; }}
    .rh2 {{ animation: traceR 2s ease-in-out infinite; transform-origin: 145px 145px; }}
    @keyframes traceL {{
      0%   {{ transform: translate(0,0); }}
      25%  {{ transform: translate(0,-20px); }}
      50%  {{ transform: translate(30px,-20px); }}
      75%  {{ transform: translate(30px,0); }}
      100% {{ transform: translate(0,0); }}
    }}
    @keyframes traceR {{
      0%   {{ transform: translate(0,0); }}
      25%  {{ transform: translate(0,-20px); }}
      50%  {{ transform: translate(-30px,-20px); }}
      75%  {{ transform: translate(-30px,0); }}
      100% {{ transform: translate(0,0); }}
    }}
  </style>
  <rect x="75" y="110" width="50" height="60" rx="8" fill="{shirt}"/>
  <circle cx="100" cy="75" r="28" fill="{skin}"/>
  <rect x="78" y="50" width="44" height="18" rx="9" fill="{hair}"/>
  <circle cx="91" cy="78" r="3" fill="#2c3e50"/>
  <circle cx="109" cy="78" r="3" fill="#2c3e50"/>
  <path d="M93 88 Q100 94 107 88" stroke="#e67e22" stroke-width="2" fill="none" stroke-linecap="round"/>
  <!-- Grade de tabela abaixo -->
  <rect x="65" y="185" width="70" height="30" rx="3" fill="none" stroke="#fbbf24" stroke-width="1.5" opacity="0.7"/>
  <line x1="88" y1="185" x2="88" y2="215" stroke="#fbbf24" stroke-width="1" opacity="0.7"/>
  <line x1="112" y1="185" x2="112" y2="215" stroke="#fbbf24" stroke-width="1" opacity="0.7"/>
  <line x1="65" y1="200" x2="135" y2="200" stroke="#fbbf24" stroke-width="1" opacity="0.7"/>
  <!-- Mão esquerda -->
  <g class="lh2">
    <rect x="38" y="135" width="30" height="20" rx="7" fill="{skin}"/>
    <rect x="40" y="130" width="5" height="10" rx="2.5" fill="{skin_dark}"/>
    <rect x="47" y="128" width="5" height="12" rx="2.5" fill="{skin_dark}"/>
    <rect x="54" y="130" width="5" height="10" rx="2.5" fill="{skin_dark}"/>
  </g>
  <!-- Mão direita -->
  <g class="rh2">
    <rect x="132" y="135" width="30" height="20" rx="7" fill="{skin}"/>
    <rect x="134" y="130" width="5" height="10" rx="2.5" fill="{skin_dark}"/>
    <rect x="141" y="128" width="5" height="12" rx="2.5" fill="{skin_dark}"/>
    <rect x="148" y="130" width="5" height="10" rx="2.5" fill="{skin_dark}"/>
  </g>
</svg>""",

        # ── SELECT: movimento circular de pesquisa ───────────────────────────
        "select": f"""
<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" width="200" height="220">
  <style>
    .search {{ animation: searchMove 1.8s ease-in-out infinite; transform-origin: 130px 120px; }}
    @keyframes searchMove {{
      0%   {{ transform: rotate(0deg) translate(8px,0) rotate(0deg); }}
      50%  {{ transform: rotate(180deg) translate(8px,0) rotate(-180deg); }}
      100% {{ transform: rotate(360deg) translate(8px,0) rotate(-360deg); }}
    }}
    .arr {{ animation: arrDrop 1.8s ease-in-out infinite; }}
    @keyframes arrDrop {{
      0%,60%,100% {{ transform: translateY(0); opacity:0; }}
      70%,90%     {{ transform: translateY(12px); opacity:1; }}
    }}
  </style>
  <rect x="75" y="110" width="50" height="60" rx="8" fill="{shirt}"/>
  <circle cx="100" cy="75" r="28" fill="{skin}"/>
  <rect x="78" y="50" width="44" height="18" rx="9" fill="{hair}"/>
  <circle cx="91" cy="78" r="3" fill="#2c3e50"/>
  <circle cx="109" cy="78" r="3" fill="#2c3e50"/>
  <path d="M93 88 Q100 94 107 88" stroke="#e67e22" stroke-width="2" fill="none" stroke-linecap="round"/>
  <!-- Lupa animada -->
  <g class="search">
    <circle cx="130" cy="118" r="14" fill="none" stroke="#fbbf24" stroke-width="3"/>
    <line x1="140" y1="128" x2="148" y2="136" stroke="#fbbf24" stroke-width="3" stroke-linecap="round"/>
    <!-- Dedo indicador no centro -->
    <circle cx="130" cy="118" r="4" fill="{skin}"/>
  </g>
  <!-- Mão esquerda estática -->
  <rect x="38" y="130" width="30" height="20" rx="7" fill="{skin}"/>
  <rect x="40" y="125" width="5" height="10" rx="2.5" fill="{skin_dark}"/>
  <!-- Seta descendo (busca) -->
  <g class="arr">
    <line x1="100" y1="172" x2="100" y2="184" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="round"/>
    <polyline points="95,180 100,186 105,180" fill="none" stroke="#fbbf24" stroke-width="2.5" stroke-linejoin="round"/>
  </g>
</svg>""",

        # ── WHERE: dedos formando peneira ────────────────────────────────────
        "where": f"""
<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" width="200" height="220">
  <style>
    .filter {{ animation: filterPulse 1.6s ease-in-out infinite; transform-origin: 100px 150px; }}
    @keyframes filterPulse {{
      0%,100% {{ transform: scaleY(1); }}
      50%      {{ transform: scaleY(0.85) translateY(6px); }}
    }}
    .dots {{ animation: dotsFall 1.6s ease-in-out infinite; }}
    @keyframes dotsFall {{
      0%   {{ transform: translateY(0); opacity:1; }}
      100% {{ transform: translateY(20px); opacity:0; }}
    }}
  </style>
  <rect x="75" y="110" width="50" height="60" rx="8" fill="{shirt}"/>
  <circle cx="100" cy="75" r="28" fill="{skin}"/>
  <rect x="78" y="50" width="44" height="18" rx="9" fill="{hair}"/>
  <circle cx="91" cy="78" r="3" fill="#2c3e50"/>
  <circle cx="109" cy="78" r="3" fill="#2c3e50"/>
  <path d="M93 88 Q100 94 107 88" stroke="#e67e22" stroke-width="2" fill="none" stroke-linecap="round"/>
  <!-- Peneira animada -->
  <g class="filter">
    <path d="M65 138 Q100 148 135 138" stroke="#fbbf24" stroke-width="3" fill="none" stroke-linecap="round"/>
    <line x1="80" y1="148" x2="83" y2="162" stroke="#fbbf24" stroke-width="2" stroke-linecap="round"/>
    <line x1="100" y1="150" x2="100" y2="164" stroke="#fbbf24" stroke-width="2" stroke-linecap="round"/>
    <line x1="120" y1="148" x2="117" y2="162" stroke="#fbbf24" stroke-width="2" stroke-linecap="round"/>
  </g>
  <!-- Pontos caindo (dados filtrados) -->
  <g class="dots">
    <circle cx="83" cy="168" r="3" fill="#93c5fd" opacity="0.8"/>
    <circle cx="100" cy="170" r="3" fill="#93c5fd" opacity="0.8"/>
    <circle cx="117" cy="168" r="3" fill="#93c5fd" opacity="0.8"/>
  </g>
  <!-- Mão esquerda (indicador apontando) -->
  <rect x="38" y="125" width="22" height="16" rx="6" fill="{skin}"/>
  <rect x="50" y="116" width="6" height="14" rx="3" fill="{skin_dark}"/>
  <!-- Mão direita (indicador) -->
  <rect x="140" y="125" width="22" height="16" rx="6" fill="{skin}"/>
  <rect x="144" y="116" width="6" height="14" rx="3" fill="{skin_dark}"/>
</svg>""",

        # ── INSERT: mão entrando por baixo ───────────────────────────────────
        "insert": f"""
<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" width="200" height="220">
  <style>
    .ins {{ animation: insertUp 1.8s ease-in-out infinite; transform-origin: 100px 165px; }}
    @keyframes insertUp {{
      0%,100% {{ transform: translateY(0); }}
      50%      {{ transform: translateY(-18px); }}
    }}
  </style>
  <rect x="75" y="110" width="50" height="60" rx="8" fill="{shirt}"/>
  <circle cx="100" cy="75" r="28" fill="{skin}"/>
  <rect x="78" y="50" width="44" height="18" rx="9" fill="{hair}"/>
  <circle cx="91" cy="78" r="3" fill="#2c3e50"/>
  <circle cx="109" cy="78" r="3" fill="#2c3e50"/>
  <path d="M93 88 Q100 94 107 88" stroke="#e67e22" stroke-width="2" fill="none" stroke-linecap="round"/>
  <!-- Tabela (mão não-dominante horizontal) -->
  <rect x="60" y="148" width="80" height="12" rx="5" fill="{skin}" opacity="0.9"/>
  <rect x="62" y="144" width="6" height="8" rx="3" fill="{skin_dark}"/>
  <rect x="70" y="143" width="6" height="9" rx="3" fill="{skin_dark}"/>
  <rect x="78" y="144" width="6" height="8" rx="3" fill="{skin_dark}"/>
  <!-- Mão dominante inserindo (sobe) -->
  <g class="ins">
    <rect x="88" y="162" width="24" height="16" rx="6" fill="{skin}"/>
    <rect x="96" y="156" width="8" height="12" rx="4" fill="{skin_dark}"/>
    <!-- Plus icon -->
    <text x="97" y="172" font-size="10" fill="#fbbf24" font-weight="bold">+</text>
  </g>
</svg>""",

        # ── COLUNA/LINHA: traçando linhas ────────────────────────────────────
        "colrow": f"""
<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" width="200" height="220">
  <style>
    .vline {{ stroke-dasharray: 60; stroke-dashoffset: 60;
              animation: drawV 2s ease-in-out infinite; }}
    .hline {{ stroke-dasharray: 60; stroke-dashoffset: 60;
              animation: drawH 2s ease-in-out infinite 1s; }}
    @keyframes drawV {{
      0%,100% {{ stroke-dashoffset: 60; opacity:0.3; }}
      40%,60% {{ stroke-dashoffset: 0;  opacity:1; }}
    }}
    @keyframes drawH {{
      0%,100% {{ stroke-dashoffset: 60; opacity:0.3; }}
      40%,60% {{ stroke-dashoffset: 0;  opacity:1; }}
    }}
    .finger {{ animation: fingerTrace 2s ease-in-out infinite; transform-origin: 110px 140px; }}
    @keyframes fingerTrace {{
      0%,100% {{ transform: translate(0,0); }}
      25%      {{ transform: translate(0,-30px); }}
      50%      {{ transform: translate(0,0); }}
      75%      {{ transform: translate(30px,0); }}
    }}
  </style>
  <rect x="75" y="110" width="50" height="60" rx="8" fill="{shirt}"/>
  <circle cx="100" cy="75" r="28" fill="{skin}"/>
  <rect x="78" y="50" width="44" height="18" rx="9" fill="{hair}"/>
  <circle cx="91" cy="78" r="3" fill="#2c3e50"/>
  <circle cx="109" cy="78" r="3" fill="#2c3e50"/>
  <path d="M93 88 Q100 94 107 88" stroke="#e67e22" stroke-width="2" fill="none" stroke-linecap="round"/>
  <!-- Linhas animadas -->
  <line class="vline" x1="80" y1="178" x2="80" y2="215" stroke="#fbbf24" stroke-width="3" stroke-linecap="round"/>
  <line class="hline" x1="65" y1="200" x2="125" y2="200" stroke="#93c5fd" stroke-width="3" stroke-linecap="round"/>
  <!-- Indicador traçando -->
  <g class="finger">
    <rect x="100" y="132" width="20" height="14" rx="5" fill="{skin}"/>
    <rect x="106" y="124" width="6" height="12" rx="3" fill="{skin_dark}"/>
  </g>
</svg>""",
    }

    return avatars.get(avatar_key, avatars["storage"])


# ═══════════════════════════════════════════════════════════════════════════════
# INICIALIZAÇÃO DO ESTADO DA SESSÃO
# ═══════════════════════════════════════════════════════════════════════════════

def init_session_state():
    if 'stage' not in st.session_state:
        st.session_state.stage = 'name'
    if 'full_name' not in st.session_state:
        st.session_state.full_name = ''
    if 'selected_level' not in st.session_state:
        st.session_state.selected_level = None
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'answers' not in st.session_state:
        st.session_state.answers = []
    if 'show_result' not in st.session_state:
        st.session_state.show_result = False
    if 'libras_concept_idx' not in st.session_state:
        st.session_state.libras_concept_idx = 0

init_session_state()

# ═══════════════════════════════════════════════════════════════════════════════
# TELA 1: CADASTRO DE NOME
# ═══════════════════════════════════════════════════════════════════════════════

def screen_name():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div style='text-align:center;font-size:3rem;'>🎓</div>", unsafe_allow_html=True)
        st.markdown('<p class="main-title">SQL Academy</p>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">Domine a Linguagem de Dados</p>', unsafe_allow_html=True)
        st.markdown("---")

        full_name = st.text_input("NOME COMPLETO", placeholder="Digite seu nome completo", key="name_input")

        if st.button("Começar →", use_container_width=True, type="primary"):
            if full_name.strip():
                st.session_state.full_name = full_name.strip()
                st.session_state.stage = 'level'
                st.rerun()

        st.markdown("---")
        st.markdown("""
        <div style='text-align:center;color:#93c5fd;font-size:0.9rem;'>
            <p>✓ 3 Níveis de Dificuldade</p>
            <p>✓ 15 Questões Totais</p>
            <p>✓ Resultado Final com Pontuação</p>
            <p>🤟 SQL em Libras — Acessibilidade Total</p>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# TELA 2: SELEÇÃO DE NÍVEL (com opção Libras)
# ═══════════════════════════════════════════════════════════════════════════════

def screen_level():
    st.markdown(f'<h1 style="text-align:center;color:white;">Bem-vindo, {st.session_state.full_name}!</h1>',
                unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Escolha seu nível de dificuldade ou explore SQL em Libras</p>',
                unsafe_allow_html=True)
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    levels = [
        {'key': 'básico',        'title': 'BÁSICO',         'icon': '📚', 'desc': 'Fundamentos de SQL',         'col': col1},
        {'key': 'intermediário', 'title': 'INTERMEDIÁRIO',  'icon': '⚡', 'desc': 'Consultas Avançadas',         'col': col2},
        {'key': 'avançado',      'title': 'AVANÇADO',       'icon': '🚀', 'desc': 'Otimização & Performance',    'col': col3},
    ]

    for level in levels:
        with level['col']:
            st.markdown(f"""
            <div class="level-card">
                <div class="level-icon">{level['icon']}</div>
                <div class="level-title">{level['title']}</div>
                <div class="level-desc">{level['desc']}</div>
                <div style='color:#fcd34d;font-size:0.8rem;'>5 questões</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Começar {level['title']}", use_container_width=True, key=f"btn_{level['key']}"):
                st.session_state.selected_level = level['key']
                st.session_state.current_question = 0
                st.session_state.score = 0
                st.session_state.answers = []
                st.session_state.show_result = False
                st.session_state.stage = 'quiz'
                st.rerun()

    st.markdown("---")

    # Destaque Libras
    st.markdown("""
    <div style="background:linear-gradient(135deg,rgba(30,58,138,0.45),rgba(12,74,110,0.45));
                border:2px solid rgba(251,191,36,0.5); border-radius:1rem;
                padding:1.5rem; text-align:center; margin-top:0.5rem;">
        <div style="font-size:2.5rem; margin-bottom:0.4rem;">🤟</div>
        <div style="font-family:'Playfair Display',serif; font-size:1.5rem;
                    color:#fcd34d; font-weight:700; margin-bottom:0.4rem;">SQL em Libras</div>
        <div style="color:#93c5fd; font-size:0.95rem;">
            Aprenda os conceitos básicos de SQL através da Língua Brasileira de Sinais.<br>
            Conteúdo acessível com avatares animados, descrições detalhadas dos sinais e dicas mnemônicas.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:0.8rem;'></div>", unsafe_allow_html=True)

    if st.button("🤟  Entrar em SQL em Libras", use_container_width=True):
        st.session_state.libras_concept_idx = 0
        st.session_state.stage = 'libras'
        st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# TELA 3: QUIZ
# ═══════════════════════════════════════════════════════════════════════════════

def screen_quiz():
    quiz = QUIZZES[st.session_state.selected_level]
    question_data = quiz[st.session_state.current_question]
    total_questions = len(quiz)

    progress = (st.session_state.current_question + 1) / total_questions
    st.progress(progress)
    col1, col2 = st.columns(2)
    with col1:
        st.text(f"Questão {st.session_state.current_question + 1} de {total_questions}")
    with col2:
        st.text(f"📊 {st.session_state.score} pontos")

    st.markdown("---")

    st.markdown(f"""
    <div class="explanation-box">
        <div class="explanation-title">{question_data['title']}</div>
        <div class="explanation-text">{question_data['explanation']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"<h3 style='color:white;'>{question_data['question']}</h3>", unsafe_allow_html=True)
    st.markdown("---")

    for idx, option in enumerate(question_data['options']):
        if st.button(
            f"{chr(65+idx)}. {option}",
            use_container_width=True,
            key=f"option_{st.session_state.current_question}_{idx}",
            disabled=st.session_state.show_result
        ):
            st.session_state.show_result = True
            is_correct = idx == question_data['correct']
            st.session_state.answers.append({
                'question': st.session_state.current_question,
                'selected': idx,
                'correct': is_correct
            })
            if is_correct:
                st.session_state.score += 1

    st.markdown("---")

    if st.session_state.show_result:
        answer_data = st.session_state.answers[-1]
        if answer_data['correct']:
            st.success("✅ Resposta correta!")
        else:
            st.error(f"❌ Resposta incorreta! A resposta correta é: **{chr(65+question_data['correct'])}. {question_data['options'][question_data['correct']]}**")

        st.markdown("---")
        col_next, _ = st.columns([1, 4])
        with col_next:
            if st.session_state.current_question + 1 < total_questions:
                if st.button("Próxima →", use_container_width=True, type="primary"):
                    st.session_state.current_question += 1
                    st.session_state.show_result = False
                    st.rerun()
            else:
                if st.button("Ver Resultado", use_container_width=True, type="primary"):
                    st.session_state.stage = 'results'
                    st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# TELA 4: RESULTADO FINAL
# ═══════════════════════════════════════════════════════════════════════════════

def screen_results():
    quiz = QUIZZES[st.session_state.selected_level]
    percentage = (st.session_state.score / len(quiz)) * 100

    if percentage >= 90:   icon, title = "🏆", "Excelente Desempenho!"
    elif percentage >= 80: icon, title = "👏", "Muito Bom!"
    elif percentage >= 70: icon, title = "✅", "Aprovado!"
    elif percentage >= 50: icon, title = "📚", "Pode Melhorar!"
    else:                  icon, title = "💪", "Tente Novamente!"

    st.markdown(f"""
    <div class="result-box">
        <div class="result-icon">{icon}</div>
        <div class="result-title">{title}</div>
        <div class="result-score">{st.session_state.score}/{len(quiz)}</div>
        <div class="result-percentage">{percentage:.0f}%</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1: st.metric("Nível", st.session_state.selected_level.upper())
    with c2: st.metric("Questões Certas", f"{st.session_state.score}/{len(quiz)}")
    with c3: st.metric("Taxa de Acerto", f"{percentage:.1f}%")

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("← Tentar Outro Nível", use_container_width=True):
            st.session_state.stage = 'level'
            st.session_state.selected_level = None
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.answers = []
            st.session_state.show_result = False
            st.rerun()

    with col2:
        if st.button("🔄 Reiniciar Tudo", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# TELA 5: SQL EM LIBRAS ← NOVA
# ═══════════════════════════════════════════════════════════════════════════════

def screen_libras():
    """Seção completa de SQL em Libras com avatares animados e descrições dos sinais"""

    concept = LIBRAS_CONCEPTS[st.session_state.libras_concept_idx]
    total = len(LIBRAS_CONCEPTS)
    idx = st.session_state.libras_concept_idx

    # ── Cabeçalho ──────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="libras-header">
        <div style="font-size:2.5rem; margin-bottom:0.5rem;">🤟</div>
        <div class="libras-header-title">SQL em Libras</div>
        <div class="libras-header-sub">
            Conceitos básicos de SQL na Língua Brasileira de Sinais
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Badge acessibilidade
    st.markdown("""
    <div class="badge-accessibility">
        ♿ Conteúdo acessível em Libras — Língua Brasileira de Sinais
    </div>
    """, unsafe_allow_html=True)

    # ── Navegação de conceitos (pills) ─────────────────────────────────────────
    cols = st.columns(len(LIBRAS_CONCEPTS))
    for i, c in enumerate(LIBRAS_CONCEPTS):
        with cols[i]:
            label = f"{c['icon']} {c['title']}"
            is_active = i == idx
            style_extra = "background:rgba(251,191,36,0.2);border-color:#fbbf24;color:#fcd34d;font-weight:600;" if is_active else ""
            if st.button(label, key=f"pill_{i}", use_container_width=True):
                st.session_state.libras_concept_idx = i
                st.rerun()

    st.markdown("---")

    # Progresso
    st.progress((idx + 1) / total)
    st.markdown(f"<p style='color:#93c5fd;font-size:0.85rem;'>Conceito {idx+1} de {total}</p>",
                unsafe_allow_html=True)

    # ── Card principal ─────────────────────────────────────────────────────────
    st.markdown(f"""
    <div class="libras-card">
        <div class="libras-card-title">{concept['icon']} {concept['title']}</div>
        <div class="libras-card-desc">{concept['description_pt']}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Duas colunas: Avatar + Detalhes ────────────────────────────────────────
    col_avatar, col_details = st.columns([1, 1.6])

    with col_avatar:
        st.markdown("""
        <div class="avatar-stage">
            <div class="avatar-label">👤 Avatar do Sinal</div>
        """, unsafe_allow_html=True)
        st.markdown(get_avatar_svg(concept["avatar_key"]), unsafe_allow_html=True)
        st.markdown("""
            <div style="color:#93c5fd;font-size:0.75rem;text-align:center;margin-top:0.4rem;">
                ↕ Animação ilustrativa do sinal
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_details:
        # Descrição do sinal
        st.markdown(f"""
        <div class="explanation-box">
            <div class="explanation-title">📝 Como fazer o sinal</div>
            <div class="explanation-text">{concept['sign_description']}</div>
        </div>
        """, unsafe_allow_html=True)

        # Configurações de mão
        st.markdown('<div class="avatar-label" style="margin-bottom:0.5rem;">✋ Configurações de Mão</div>',
                    unsafe_allow_html=True)
        hs_html = '<div class="handshape-grid">'
        for hs in concept["handshapes"]:
            hs_html += f'<div class="handshape-item"><span>{hs["emoji"]}</span>{hs["label"]}</div>'
        hs_html += '</div>'
        st.markdown(hs_html, unsafe_allow_html=True)

    st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)

    # ── Movimento e Localização ────────────────────────────────────────────────
    col_m, col_l = st.columns(2)
    with col_m:
        st.markdown(f"""
        <div style="background:rgba(30,58,138,0.2);border:1px solid rgba(251,191,36,0.2);
                    border-radius:0.6rem;padding:1rem;height:100%;">
            <div style="color:#fcd34d;font-weight:700;margin-bottom:0.4rem;">🔄 Movimento</div>
            <div style="color:#93c5fd;font-size:0.9rem;line-height:1.5;">{concept['movement']}</div>
        </div>
        """, unsafe_allow_html=True)

    with col_l:
        st.markdown(f"""
        <div style="background:rgba(30,58,138,0.2);border:1px solid rgba(251,191,36,0.2);
                    border-radius:0.6rem;padding:1rem;height:100%;">
            <div style="color:#fcd34d;font-weight:700;margin-bottom:0.4rem;">📍 Localização</div>
            <div style="color:#93c5fd;font-size:0.9rem;line-height:1.5;">{concept['location']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)

    # ── Dica mnemônica ─────────────────────────────────────────────────────────
    st.markdown(f'<div class="tip-box">{concept["tip"]}</div>', unsafe_allow_html=True)

    st.markdown("---")

    # ── Navegação anterior / próximo ───────────────────────────────────────────
    col_prev, col_center, col_next = st.columns([1, 2, 1])

    with col_prev:
        if idx > 0:
            if st.button("← Anterior", use_container_width=True):
                st.session_state.libras_concept_idx -= 1
                st.rerun()

    with col_center:
        if st.button("← Voltar ao Menu", use_container_width=True):
            st.session_state.stage = 'level'
            st.rerun()

    with col_next:
        if idx < total - 1:
            if st.button("Próximo →", use_container_width=True, type="primary"):
                st.session_state.libras_concept_idx += 1
                st.rerun()
        else:
            if st.button("✅ Concluído!", use_container_width=True, type="primary"):
                st.session_state.stage = 'level'
                st.rerun()

    # ── Rodapé informativo ─────────────────────────────────────────────────────
    st.markdown("---")
    st.markdown("""
    <div style="background:rgba(30,58,138,0.15);border-radius:0.6rem;padding:1rem;
                text-align:center;color:#64748b;font-size:0.78rem;line-height:1.6;">
        🤟 As descrições dos sinais são aproximações para fins educacionais.<br>
        Para aprendizado aprofundado de Libras, consulte um professor certificado de Libras<br>
        ou utilize materiais do <strong style="color:#93c5fd;">INES — Instituto Nacional de Educação de Surdos</strong>.
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# RENDERIZAÇÃO PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    if st.session_state.stage == 'name':
        screen_name()
    elif st.session_state.stage == 'level':
        screen_level()
    elif st.session_state.stage == 'quiz':
        screen_quiz()
    elif st.session_state.stage == 'results':
        screen_results()
    elif st.session_state.stage == 'libras':
        screen_libras()

if __name__ == "__main__":
    main()
