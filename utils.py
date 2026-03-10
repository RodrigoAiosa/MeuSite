"""
Utilitários para a aplicação SQL Learning Platform
"""

import streamlit as st
from datetime import datetime

def registrar_acesso():
    """Registra o acesso do usuário à plataforma"""
    if 'primeiro_acesso' not in st.session_state:
        st.session_state.primeiro_acesso = datetime.now()
    
    if 'ultimo_acesso' not in st.session_state:
        st.session_state.ultimo_acesso = datetime.now()
    else:
        st.session_state.ultimo_acesso = datetime.now()
    
    return True

def exibir_rodape():
    """Exibe o rodapé da aplicação"""
    st.markdown("""
    <div style="text-align: center; padding: 40px 0; border-top: 1px solid #334155; color: #cbd5e1; margin-top: 60px;">
        <p style="margin-bottom: 10px; font-size: 0.95rem;">
            <span style="color: #D4AF37; font-weight: 600;">SQL - Melhores Práticas Pro</span> 
            • Criado por Rodrigo Aiosa
        </p>
        <p style="font-size: 0.85rem; color: #94a3b8;">
            Transforme seus dados em vantagem competitiva com SQL estratégico
        </p>
    </div>
    """, unsafe_allow_html=True)

def get_table_info():
    """Retorna informações sobre as tabelas disponíveis"""
    return {
        "usuarios": {
            "columns": ["id", "nome", "email", "ativo", "created_at", "categoria"],
            "description": "Tabela de usuários do sistema"
        },
        "vendas": {
            "columns": ["id", "usuario_id", "valor", "status", "data"],
            "description": "Tabela de vendas realizadas"
        },
        "produtos": {
            "columns": ["id", "nome", "categoria", "preco"],
            "description": "Tabela de produtos disponíveis"
        }
    }

def get_color_scheme():
    """Retorna o esquema de cores da aplicação"""
    return {
        'primary': '#0F172A',
        'secondary': '#1E293B',
        'accent': '#D4AF37',
        'text_light': '#E2E8F0',
        'text_dark': '#0F172A',
        'border': '#334155',
        'success': '#22c55e',
        'warning': '#f59e0b',
        'danger': '#ef4444'
    }

def formatar_pontos(pontos):
    """Formata pontos com separador de milhares"""
    return f"{pontos:,.0f}".replace(",", ".")

def validar_query_seguranca(query):
    """Valida se a query é segura para executar"""
    # Palavras-chave perigosas
    palavras_perigosas = ['DROP', 'DELETE', 'TRUNCATE', 'INSERT', 'UPDATE', 'ALTER']
    
    query_upper = query.upper().strip()
    
    for palavra in palavras_perigosas:
        if query_upper.startswith(palavra):
            return False, f"❌ Operação '{palavra}' não permitida neste ambiente de aprendizado."
    
    return True, "✅ Query segura para executar."

def get_achievement_badge(tipo):
    """Retorna badge de conquista baseado no tipo"""
    badges = {
        'beginner': '🌱 Iniciante',
        'intermediate': '⚡ Intermediário',
        'advanced': '🚀 Avançado',
        'expert': '👑 Expert'
    }
    return badges.get(tipo, '🎯 Desafio')

def calcular_tempo_aprendizado(desafios_completos):
    """Calcula tempo estimado de aprendizado baseado em desafios completos"""
    tempo_por_desafio = 10  # minutos
    return desafios_completos * tempo_por_desafio

def gerar_relatorio_progresso(pontos, desafios, nivel):
    """Gera um relatório de progresso do usuário"""
    relatorio = {
        'pontos_totais': pontos,
        'desafios_completos': len(desafios),
        'nivel': nivel,
        'tempo_aprendizado': calcular_tempo_aprendizado(len(desafios)),
        'taxa_conclusao': (len(desafios) / 10 * 100) if desafios else 0
    }
    return relatorio
