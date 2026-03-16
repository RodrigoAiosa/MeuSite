#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔════════════════════════════════════════════════════════════════════════════════╗
║                           SQL ACADEMY - TRAINING PLATFORM                      ║
║                                                                                ║
║  Uma plataforma profissional de treinamento em SQL com 3 níveis de             ║
║  dificuldade, quiz interativo, sistema de progressão e resultado final.        ║
║                                                                                ║
║  Author: SQL Academy Team                                                      ║
║  Version: 1.0.0                                                                ║
║  License: MIT                                                                  ║
║                                                                                ║
║  Construído com: Streamlit                                                     ║
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
    
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }
        
        .result-score {
            font-size: 2.5rem;
        }
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
# INICIALIZAÇÃO DO ESTADO DA SESSÃO
# ═══════════════════════════════════════════════════════════════════════════════

def init_session_state():
    """Inicializar variáveis de estado da sessão"""
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

init_session_state()

# ═══════════════════════════════════════════════════════════════════════════════
# TELA 1: CADASTRO DE NOME
# ═══════════════════════════════════════════════════════════════════════════════

def screen_name():
    """Tela de cadastro de nome completo"""
    name_container = st.container()
    
    with name_container:
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
            st.markdown("# 🎓")
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown('<p class="main-title">SQL Academy</p>', unsafe_allow_html=True)
            st.markdown('<p class="subtitle">Domine a Linguagem de Dados</p>', unsafe_allow_html=True)
            
            st.markdown("---")
            
            full_name = st.text_input(
                "NOME COMPLETO",
                placeholder="Digite seu nome completo",
                key="name_input"
            )
            
            if st.button("Começar →", use_container_width=True, type="primary"):
                if full_name.strip():
                    st.session_state.full_name = full_name.strip()
                    st.session_state.stage = 'level'
                    st.rerun()
            
            st.markdown("---")
            st.markdown("""
            <div style='text-align: center; color: #93c5fd; font-size: 0.9rem;'>
                <p>✓ 3 Níveis de Dificuldade</p>
                <p>✓ 15 Questões Totais</p>
                <p>✓ Resultado Final com Pontuação</p>
            </div>
            """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# TELA 2: SELEÇÃO DE NÍVEL
# ═══════════════════════════════════════════════════════════════════════════════

def screen_level():
    """Tela de seleção de nível de dificuldade"""
    header_container = st.container()
    with header_container:
        st.markdown(f'<h1 style="text-align: center; color: white;">Bem-vindo, {st.session_state.full_name}!</h1>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">Escolha seu nível de dificuldade</p>', unsafe_allow_html=True)
        st.markdown("---")
    
    levels_container = st.container()
    with levels_container:
        col1, col2, col3 = st.columns(3)
        
        levels = [
            {'key': 'básico', 'title': 'BÁSICO', 'icon': '📚', 'desc': 'Fundamentos de SQL', 'col': col1},
            {'key': 'intermediário', 'title': 'INTERMEDIÁRIO', 'icon': '⚡', 'desc': 'Consultas Avançadas', 'col': col2},
            {'key': 'avançado', 'title': 'AVANÇADO', 'icon': '🚀', 'desc': 'Otimização & Performance', 'col': col3}
        ]
        
        for level in levels:
            with level['col']:
                st.markdown(f"""
                <div class="level-card">
                    <div class="level-icon">{level['icon']}</div>
                    <div class="level-title">{level['title']}</div>
                    <div class="level-desc">{level['desc']}</div>
                    <div style='color: #fcd34d; font-size: 0.8rem;'>5 questões</div>
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

# ═══════════════════════════════════════════════════════════════════════════════
# TELA 3: QUIZ
# ═══════════════════════════════════════════════════════════════════════════════

def screen_quiz():
    """Tela do quiz com questões"""
    quiz = QUIZZES[st.session_state.selected_level]
    question_data = quiz[st.session_state.current_question]
    total_questions = len(quiz)
    
    # Container para progresso (não pisca)
    progress_container = st.container()
    with progress_container:
        progress = (st.session_state.current_question + 1) / total_questions
        st.progress(progress)
        
        col1, col2 = st.columns(2)
        with col1:
            st.text(f"Questão {st.session_state.current_question + 1} de {total_questions}")
        with col2:
            st.text(f"📊 {st.session_state.score} pontos")
    
    st.markdown("---")
    
    # Container para explicação
    explanation_container = st.container()
    with explanation_container:
        st.markdown(f"""
        <div class="explanation-box">
            <div class="explanation-title">{question_data['title']}</div>
            <div class="explanation-text">{question_data['explanation']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"<h3 style='color: white;'>{question_data['question']}</h3>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Container para opções
    options_container = st.container()
    with options_container:
        for idx, option in enumerate(question_data['options']):
            if st.button(
                f"{chr(65 + idx)}. {option}",
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
    
    # Container para resultado
    if st.session_state.show_result:
        result_container = st.container()
        with result_container:
            question_data = quiz[st.session_state.current_question]
            answer_data = st.session_state.answers[-1]
            
            if answer_data['correct']:
                st.success("✅ Resposta correta!")
            else:
                st.error(f"❌ Resposta incorreta! A resposta correta é: **{chr(65 + question_data['correct'])}. {question_data['options'][question_data['correct']]}**")
            
            st.markdown("---")
            
            # Botões de navegação
            col_next, col_empty = st.columns([1, 4])
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
    """Tela de resultado final"""
    quiz = QUIZZES[st.session_state.selected_level]
    percentage = (st.session_state.score / len(quiz)) * 100
    
    if percentage >= 90:
        icon = "🏆"
        title = "Excelente Desempenho!"
    elif percentage >= 80:
        icon = "👏"
        title = "Muito Bom!"
    elif percentage >= 70:
        icon = "✅"
        title = "Aprovado!"
    elif percentage >= 50:
        icon = "📚"
        title = "Pode Melhorar!"
    else:
        icon = "💪"
        title = "Tente Novamente!"
    
    # Container para resultado (não pisca)
    result_container = st.container()
    with result_container:
        st.markdown(f"""
        <div class="result-box">
            <div class="result-icon">{icon}</div>
            <div class="result-title">{title}</div>
            <div class="result-score">{st.session_state.score}/{len(quiz)}</div>
            <div class="result-percentage">{percentage:.0f}%</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Detalhes em colunas (sem HTML que pisca)
        st.markdown("---")
        
        detail_col1, detail_col2, detail_col3 = st.columns(3)
        
        with detail_col1:
            st.metric(label="Nível", value=st.session_state.selected_level.upper())
        
        with detail_col2:
            st.metric(label="Questões Certas", value=f"{st.session_state.score}/{len(quiz)}")
        
        with detail_col3:
            st.metric(label="Taxa de Acerto", value=f"{percentage:.1f}%")
    
    st.markdown("---")
    
    # Botões
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
            st.session_state.stage = 'name'
            st.session_state.full_name = ''
            st.session_state.selected_level = None
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.answers = []
            st.session_state.show_result = False
            st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# RENDERIZAÇÃO PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """Função principal que controla o fluxo da aplicação"""
    
    if st.session_state.stage == 'name':
        screen_name()
    elif st.session_state.stage == 'level':
        screen_level()
    elif st.session_state.stage == 'quiz':
        screen_quiz()
    elif st.session_state.stage == 'results':
        screen_results()

if __name__ == "__main__":
    main()
