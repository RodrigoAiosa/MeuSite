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
╚════════════════════════════════════════════════════════════════════════════════╝
"""

from flask import Flask, render_template_string, request, jsonify, session
from datetime import datetime
from functools import wraps
import json
import os

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURAÇÃO DO APLICATIVO
# ═══════════════════════════════════════════════════════════════════════════════

app = Flask(__name__)
app.secret_key = 'sql_academy_secret_key_2024'

# ═══════════════════════════════════════════════════════════════════════════════
# DATABASE DE QUIZ
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
# TEMPLATE HTML PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════════

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SQL Academy - Plataforma de Treinamento</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Lora:wght@400;500&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Lora', serif;
        }

        body {
            background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #0c4a6e 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .playfair {
            font-family: 'Playfair Display', serif;
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        /* TELA 1: CADASTRO                                         */
        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

        #screen-name {
            width: 100%;
            max-width: 500px;
            animation: slideIn 0.6s ease;
        }

        .header {
            text-align: center;
            margin-bottom: 50px;
        }

        .logo {
            display: inline-block;
            background: linear-gradient(135deg, #fbbf24 0%, #fcd34d 100%);
            padding: 20px;
            border-radius: 50%;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(251, 191, 36, 0.3);
        }

        .logo svg {
            width: 50px;
            height: 50px;
            color: #1e3a8a;
        }

        .header h1 {
            font-size: 48px;
            color: white;
            margin-bottom: 10px;
            font-weight: 700;
        }

        .header p {
            font-size: 18px;
            color: #93c5fd;
        }

        .form-container {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }

        .form-group {
            margin-bottom: 30px;
        }

        label {
            display: block;
            color: white;
            font-size: 13px;
            font-weight: 600;
            letter-spacing: 1px;
            margin-bottom: 12px;
        }

        input[type="text"] {
            width: 100%;
            padding: 15px;
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid rgba(147, 197, 253, 0.3);
            border-radius: 10px;
            color: white;
            font-size: 16px;
            font-family: 'Lora', serif;
            transition: all 0.3s;
        }

        input[type="text"]::placeholder {
            color: #93c5fd;
        }

        input[type="text"]:focus {
            outline: none;
            border-color: #fbbf24;
            background: rgba(255, 255, 255, 0.15);
            box-shadow: 0 0 20px rgba(251, 191, 36, 0.3);
        }

        .btn {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #fbbf24 0%, #fcd34d 100%);
            color: #1e3a8a;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            font-family: 'Lora', serif;
        }

        .btn:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 30px rgba(251, 191, 36, 0.4);
        }

        .features {
            margin-top: 40px;
            text-align: center;
            color: #93c5fd;
            font-size: 14px;
            line-height: 2;
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        /* TELA 2: SELEÇÃO DE NÍVEL                                 */
        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

        #screen-level {
            width: 100%;
            max-width: 1000px;
            animation: slideIn 0.6s ease;
        }

        .level-header h1 {
            font-size: 42px;
            color: white;
            margin-bottom: 10px;
            text-align: center;
        }

        .level-header p {
            text-align: center;
            color: #93c5fd;
            font-size: 16px;
            margin-bottom: 50px;
        }

        .levels-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            margin-bottom: 20px;
        }

        .level-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(147, 197, 253, 0.3);
            border-radius: 15px;
            padding: 40px 30px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }

        .level-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 3px;
            background: linear-gradient(90deg, transparent, #fbbf24, transparent);
            opacity: 0;
            transition: opacity 0.3s;
        }

        .level-card:hover {
            transform: translateY(-10px);
            background: rgba(255, 255, 255, 0.15);
            border-color: #fbbf24;
        }

        .level-card:hover::before {
            opacity: 1;
        }

        .level-icon {
            font-size: 48px;
            margin-bottom: 15px;
        }

        .level-card h3 {
            font-size: 24px;
            color: white;
            margin-bottom: 5px;
            font-weight: 700;
        }

        .level-card p {
            color: #93c5fd;
            font-size: 14px;
            margin-bottom: 20px;
        }

        .level-badge {
            display: inline-block;
            background: rgba(251, 191, 36, 0.2);
            color: #fcd34d;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        /* TELA 3: QUIZ                                             */
        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

        #screen-quiz {
            width: 100%;
            max-width: 800px;
            animation: slideIn 0.6s ease;
        }

        .progress-bar {
            margin-bottom: 30px;
        }

        .progress-info {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
            color: #93c5fd;
            font-size: 13px;
            font-weight: 600;
        }

        .progress-fill {
            width: 100%;
            height: 8px;
            background: rgba(15, 23, 42, 0.5);
            border-radius: 10px;
            overflow: hidden;
        }

        .progress-bar-inner {
            height: 100%;
            background: linear-gradient(90deg, #fbbf24, #fcd34d);
            border-radius: 10px;
            transition: width 0.5s ease;
        }

        .quiz-container {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        }

        .explanation {
            background: rgba(30, 58, 138, 0.3);
            border-left: 4px solid #fbbf24;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 30px;
        }

        .explanation h2 {
            color: white;
            font-size: 22px;
            margin-bottom: 10px;
        }

        .explanation p {
            color: #93c5fd;
            line-height: 1.6;
        }

        .question-title {
            font-size: 20px;
            color: white;
            margin-bottom: 25px;
            font-weight: 500;
        }

        .options {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-bottom: 30px;
        }

        .option-btn {
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid rgba(147, 197, 253, 0.3);
            border-radius: 10px;
            padding: 15px 20px;
            text-align: left;
            color: #93c5fd;
            cursor: pointer;
            transition: all 0.3s;
            font-family: 'Lora', serif;
            font-size: 15px;
            position: relative;
            overflow: hidden;
        }

        .option-btn:hover:not(:disabled) {
            background: rgba(255, 255, 255, 0.15);
            border-color: #fbbf24;
            transform: translateX(10px);
        }

        .option-btn:disabled {
            cursor: not-allowed;
        }

        .option-btn.correct {
            background: rgba(34, 197, 94, 0.2);
            border-color: #22c55e;
            color: #86efac;
        }

        .option-btn.incorrect {
            background: rgba(239, 68, 68, 0.2);
            border-color: #ef4444;
            color: #fca5a5;
        }

        .option-icon {
            margin-left: 10px;
        }

        .next-btn {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #fbbf24 0%, #fcd34d 100%);
            color: #1e3a8a;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            font-family: 'Lora', serif;
        }

        .next-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 30px rgba(251, 191, 36, 0.4);
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        /* TELA 4: RESULTADO FINAL                                  */
        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

        #screen-results {
            width: 100%;
            max-width: 600px;
            text-align: center;
            animation: slideIn 0.6s ease;
        }

        .results-icon {
            font-size: 80px;
            margin-bottom: 30px;
            animation: bounce 0.6s ease;
        }

        .results-title {
            font-size: 36px;
            color: white;
            margin-bottom: 20px;
            font-weight: 700;
        }

        .results-box {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 20px;
            padding: 40px;
            margin-bottom: 30px;
        }

        .results-text {
            color: #93c5fd;
            font-size: 16px;
            margin-bottom: 15px;
        }

        .results-text strong {
            color: #fcd34d;
            font-weight: 600;
        }

        .results-score {
            font-size: 56px;
            color: #fcd34d;
            margin-bottom: 15px;
            font-weight: 700;
        }

        .results-percentage {
            color: #93c5fd;
            font-size: 18px;
            margin-bottom: 20px;
        }

        .results-details {
            background: rgba(15, 23, 42, 0.5);
            border-radius: 10px;
            padding: 20px;
            margin-top: 25px;
        }

        .results-details p {
            color: #93c5fd;
            font-size: 14px;
            margin: 10px 0;
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }

        .hidden {
            display: none !important;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @media (max-width: 768px) {
            .header h1 { font-size: 36px; }
            .cert-title { font-size: 36px; }
            .cert-name { font-size: 28px; }
            .levels-grid { grid-template-columns: 1fr; }
            .cert-score { flex-direction: column; gap: 30px; }
            .cert-footer { flex-direction: column; gap: 30px; align-items: center; }
            .cert-content { padding: 40px 20px; }
        }

        @media print {
            body {
                background: white;
            }
            .cert-buttons {
                display: none;
            }
        }
    </style>
</head>
<body>
    <!-- TELA 1: CADASTRO DE NOME -->
    <div id="screen-name">
        <div class="header">
            <div class="logo">
                <svg fill="currentColor" viewBox="0 0 20 20">
                    <path d="M10 12a2 2 0 100-4 2 2 0 000 4z"/>
                    <path fill-rule="evenodd" d="M3 8.5a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zm5-2a2 2 0 10-4 0 2 2 0 004 0z"/>
                </svg>
            </div>
            <h1 class="playfair">SQL Academy</h1>
            <p>Domine a Linguagem de Dados</p>
        </div>

        <div class="form-container">
            <form id="name-form" onsubmit="submitName(event)">
                <div class="form-group">
                    <label for="full-name">NOME COMPLETO</label>
                    <input type="text" id="full-name" placeholder="Digite seu nome completo" required>
                </div>
                <button type="submit" class="btn">
                    Começar
                    <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                    </svg>
                </button>
            </form>
        </div>

        <div class="features">
            <p>✓ 3 Níveis de Dificuldade</p>
            <p>✓ 15 Questões Totais</p>
            <p>✓ Certificado ao Final</p>
        </div>
    </div>

    <!-- TELA 2: SELEÇÃO DE NÍVEL -->
    <div id="screen-level" class="hidden">
        <div class="level-header">
            <h1 class="playfair" id="welcome-name">Bem-vindo!</h1>
            <p>Escolha seu nível de dificuldade</p>
        </div>

        <div class="levels-grid">
            <button class="level-card" onclick="selectLevel('básico')">
                <div class="level-icon">📚</div>
                <h3>BÁSICO</h3>
                <p>Fundamentos de SQL</p>
                <span class="level-badge">5 questões</span>
            </button>

            <button class="level-card" onclick="selectLevel('intermediário')">
                <div class="level-icon">⚡</div>
                <h3>INTERMEDIÁRIO</h3>
                <p>Consultas Avançadas</p>
                <span class="level-badge">5 questões</span>
            </button>

            <button class="level-card" onclick="selectLevel('avançado')">
                <div class="level-icon">🚀</div>
                <h3>AVANÇADO</h3>
                <p>Otimização & Performance</p>
                <span class="level-badge">5 questões</span>
            </button>
        </div>
    </div>

    <!-- TELA 3: QUIZ -->
    <div id="screen-quiz" class="hidden">
        <div class="progress-bar">
            <div class="progress-info">
                <span id="question-counter">Questão 1 de 5</span>
                <span id="score-display">0 pontos</span>
            </div>
            <div class="progress-fill">
                <div class="progress-bar-inner" id="progress-fill" style="width: 0%"></div>
            </div>
        </div>

        <div class="quiz-container">
            <div class="explanation">
                <h2 id="explanation-title">Título</h2>
                <p id="explanation-text">Explicação</p>
            </div>

            <div class="question-title" id="question-text">Pergunta?</div>

            <div class="options" id="options-container">
                <!-- Opções serão adicionadas por JavaScript -->
            </div>

            <button class="next-btn hidden" id="next-btn" onclick="nextQuestion()">
                Próxima Questão →
            </button>
        </div>
    </div>

    <!-- TELA 4: RESULTADO FINAL -->
    <div id="screen-results" class="hidden">
        <div class="results-icon" id="results-icon">🎉</div>
        <h1 class="results-title" id="results-title">Quiz Concluído!</h1>

        <div class="results-box">
            <p class="results-text">Você completou o treinamento de <strong id="results-level">NÍVEL</strong></p>
            <div class="results-score" id="results-score">0/5</div>
            <div class="results-percentage" id="results-percentage">0%</div>

            <div class="results-details">
                <p><strong>Questões Certas:</strong> <span id="results-correct">0</span> de <span id="results-total">5</span></p>
                <p><strong>Taxa de Acerto:</strong> <span id="results-percent">0</span>%</p>
            </div>
        </div>

        <button class="btn" onclick="resetApp()">← Tentar Outro Nível</button>
    </div>

    <script>
        // ═════════════════════════════════════════════════════════════════════
        // VARIÁVEIS GLOBAIS
        // ═════════════════════════════════════════════════════════════════════

        const quizData = {{ quiz_data | safe }};
        
        let appState = {
            fullName: '',
            selectedLevel: null,
            currentQuestion: 0,
            score: 0,
            answers: [],
            showResult: false
        };

        // ═════════════════════════════════════════════════════════════════════
        // FUNÇÃO: TELA 1 - CADASTRO
        // ═════════════════════════════════════════════════════════════════════

        function submitName(event) {
            event.preventDefault();
            const nameInput = document.getElementById('full-name');
            const fullName = nameInput.value.trim();

            if (fullName) {
                appState.fullName = fullName;
                document.getElementById('welcome-name').textContent = `Bem-vindo, ${fullName}!`;
                showScreen('level');
            }
        }

        // ═════════════════════════════════════════════════════════════════════
        // FUNÇÃO: TELA 2 - SELEÇÃO DE NÍVEL
        // ═════════════════════════════════════════════════════════════════════

        function selectLevel(level) {
            appState.selectedLevel = level;
            appState.currentQuestion = 0;
            appState.score = 0;
            appState.answers = [];
            appState.showResult = false;
            
            loadQuestion();
            showScreen('quiz');
        }

        // ═════════════════════════════════════════════════════════════════════
        // FUNÇÃO: TELA 3 - QUIZ
        // ═════════════════════════════════════════════════════════════════════

        function loadQuestion() {
            const quiz = quizData[appState.selectedLevel];
            const question = quiz[appState.currentQuestion];
            const totalQuestions = quiz.length;

            // Atualizar informações
            document.getElementById('question-counter').textContent = 
                `Questão ${appState.currentQuestion + 1} de ${totalQuestions}`;
            document.getElementById('score-display').textContent = 
                `${appState.score} pontos`;

            // Progresso
            const progress = ((appState.currentQuestion + 1) / totalQuestions) * 100;
            document.getElementById('progress-fill').style.width = progress + '%';

            // Explicação
            document.getElementById('explanation-title').textContent = question.title;
            document.getElementById('explanation-text').textContent = question.explanation;

            // Pergunta
            document.getElementById('question-text').textContent = question.question;

            // Opções
            const optionsContainer = document.getElementById('options-container');
            optionsContainer.innerHTML = '';

            question.options.forEach((option, index) => {
                const btn = document.createElement('button');
                btn.className = 'option-btn';
                btn.textContent = String.fromCharCode(65 + index) + '. ' + option;
                btn.onclick = () => selectAnswer(index);
                btn.id = `option-${index}`;
                optionsContainer.appendChild(btn);
            });

            // Esconder botão de próximo
            document.getElementById('next-btn').classList.add('hidden');
        }

        function selectAnswer(index) {
            if (appState.showResult) return;

            const quiz = quizData[appState.selectedLevel];
            const question = quiz[appState.currentQuestion];
            const isCorrect = index === question.correct;

            // Mostrar feedback
            const correctBtn = document.getElementById(`option-${question.correct}`);
            const selectedBtn = document.getElementById(`option-${index}`);

            correctBtn.classList.add('correct');
            correctBtn.disabled = true;

            if (!isCorrect) {
                selectedBtn.classList.add('incorrect');
            }

            // Desabilitar todas as opções
            for (let i = 0; i < question.options.length; i++) {
                document.getElementById(`option-${i}`).disabled = true;
            }

            // Atualizar estado
            appState.answers.push({ question: appState.currentQuestion, selected: index, correct: isCorrect });
            if (isCorrect) {
                appState.score++;
                document.getElementById('score-display').textContent = `${appState.score} pontos`;
            }

            appState.showResult = true;

            // Mostrar botão de próximo
            document.getElementById('next-btn').classList.remove('hidden');
        }

        function nextQuestion() {
            const quiz = quizData[appState.selectedLevel];
            
            if (appState.currentQuestion + 1 < quiz.length) {
                appState.currentQuestion++;
                appState.showResult = false;
                loadQuestion();
            } else {
                // Fim do quiz - mostrar resultados
                showResults();
                showScreen('results');
            }
        }

        // ═════════════════════════════════════════════════════════════════════
        // FUNÇÃO: TELA 4 - RESULTADO FINAL
        // ═════════════════════════════════════════════════════════════════════

        function showResults() {
            const quiz = quizData[appState.selectedLevel];
            const percentage = Math.round((appState.score / quiz.length) * 100);

            // Atualizar ícone e título baseado no desempenho
            const icon = document.getElementById('results-icon');
            const title = document.getElementById('results-title');

            if (percentage >= 90) {
                icon.textContent = '🏆';
                title.textContent = 'Excelente Desempenho!';
            } else if (percentage >= 80) {
                icon.textContent = '👏';
                title.textContent = 'Muito Bom!';
            } else if (percentage >= 70) {
                icon.textContent = '✅';
                title.textContent = 'Aprovado!';
            } else if (percentage >= 50) {
                icon.textContent = '📚';
                title.textContent = 'Pode Melhorar!';
            } else {
                icon.textContent = '💪';
                title.textContent = 'Tente Novamente!';
            }

            // Atualizar dados
            document.getElementById('results-level').textContent = appState.selectedLevel.toUpperCase();
            document.getElementById('results-score').textContent = `${appState.score}/${quiz.length}`;
            document.getElementById('results-percentage').textContent = percentage + '%';
            document.getElementById('results-correct').textContent = appState.score;
            document.getElementById('results-total').textContent = quiz.length;
            document.getElementById('results-percent').textContent = percentage;
        }

        // ═════════════════════════════════════════════════════════════════════
        // FUNÇÕES AUXILIARES
        // ═════════════════════════════════════════════════════════════════════

        function showScreen(screenName) {
            document.getElementById('screen-name').classList.add('hidden');
            document.getElementById('screen-level').classList.add('hidden');
            document.getElementById('screen-quiz').classList.add('hidden');
            document.getElementById('screen-results').classList.add('hidden');

            document.getElementById(`screen-${screenName}`).classList.remove('hidden');
        }

        function resetApp() {
            appState = {
                fullName: '',
                selectedLevel: null,
                currentQuestion: 0,
                score: 0,
                answers: [],
                showResult: false
            };
            document.getElementById('full-name').value = '';
            showScreen('name');
        }
    </script>
</body>
</html>
'''

# ═══════════════════════════════════════════════════════════════════════════════
# ROTAS FLASK
# ═══════════════════════════════════════════════════════════════════════════════

@app.route('/')
def index():
    """Rota principal - renderiza a página HTML com o quiz"""
    return render_template_string(HTML_TEMPLATE, quiz_data=json.dumps(QUIZZES))

@app.route('/api/quiz/<level>')
def get_quiz(level):
    """API para obter quiz de um nível específico"""
    if level in QUIZZES:
        return jsonify(QUIZZES[level])
    return jsonify({'error': 'Nível não encontrado'}), 404

@app.route('/api/submit', methods=['POST'])
def submit_quiz():
    """API para submeter respostas do quiz"""
    data = request.json
    level = data.get('level')
    answers = data.get('answers')
    
    if not level or not answers or level not in QUIZZES:
        return jsonify({'error': 'Dados inválidos'}), 400
    
    quiz = QUIZZES[level]
    score = 0
    
    for answer in answers:
        if answer.get('correct'):
            score += 1
    
    percentage = (score / len(quiz)) * 100
    passed = percentage >= 70
    
    return jsonify({
        'score': score,
        'total': len(quiz),
        'percentage': round(percentage, 2),
        'passed': passed,
        'timestamp': datetime.now().isoformat()
    })

# ═══════════════════════════════════════════════════════════════════════════════
# INFORMAÇÕES ADICIONAIS
# ═══════════════════════════════════════════════════════════════════════════════

def print_welcome():
    """Imprime mensagem de boas-vindas"""
    print("""
    ╔════════════════════════════════════════════════════════════════════════════════╗
    ║                                                                                ║
    ║                        🎓 SQL ACADEMY - WELCOME 🎓                             ║
    ║                                                                                ║
    ║  Plataforma completa de treinamento em SQL com:                               ║
    ║  ✓ 3 Níveis de Dificuldade (Básico, Intermediário, Avançado)                  ║
    ║  ✓ 15 Questões Totais (5 por nível)                                           ║
    ║  ✓ Sistema de Progresso em Tempo Real                                         ║
    ║  ✓ Resultado Final com Pontuação Detalhada                                    ║
    ║  ✓ Interface Responsiva e Intuitiva                                           ║
    ║                                                                                ║
    ║  Para iniciar:                                                                ║
    ║  1. Instale as dependências: pip install flask                                ║
    ║  2. Execute o script: python cursos_sql.py                                    ║
    ║  3. Abra o navegador em: http://localhost:5000                                ║
    ║                                                                                ║
    ║  Você será redirecionado para a plataforma de treinamento!                    ║
    ║                                                                                ║
    ╚════════════════════════════════════════════════════════════════════════════════╝
    """)

# ═══════════════════════════════════════════════════════════════════════════════
# PONTO DE ENTRADA
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print_welcome()
    
    # Configurar e iniciar o servidor Flask
    app.run(
        debug=True,
        host='localhost',
        port=5000,
        use_reloader=True
    )
