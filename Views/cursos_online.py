import streamlit as st
import pandas as pd
from datetime import datetime
import os

def registrar_acesso(nome_pagina):
    """
    Registra o acesso do usuário em um arquivo CSV para análise de métricas.
    Psicologia de Dados: Saber onde seus usuários clicam ajuda a otimizar o funil.
    """
    arquivo_log = "log_acessos.csv"
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Criar novo registro
    novo_acesso = pd.DataFrame([{
        "Data/Hora": data_hora, 
        "Página": nome_pagina,
        "Status": "Visualização"
    }])
    
    try:
        if not os.path.exists(arquivo_log):
            novo_acesso.to_csv(arquivo_log, index=False, sep=";", encoding="utf-8-sig")
        else:
            novo_acesso.to_csv(arquivo_log, mode='a', header=False, index=False, sep=";", encoding="utf-8-sig")
    except Exception as e:
        # Silencioso para o usuário, mas útil para debug
        print(f"Erro ao registrar acesso: {e}")

def exibir_rodape():
    """
    Exibe um rodapé profissional e minimalista.
    Design UI: Reforça a marca e fornece canais de suporte rápidos.
    """
    st.write("") # Espaçador
    st.divider()
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.markdown(f"**© {datetime.now().year} Rodrigo Aiosa**")
        st.caption("Especialista em Inteligência de Dados e Processos.")
    
    with col2:
        st.markdown("**Contato**")
        # WhatsApp com mensagem personalizada de suporte geral
        msg_suporte = "Olá Rodrigo, estou navegando no seu site e gostaria de tirar uma dúvida geral."
        link_wa = f"https://wa.me/5511977019335?text={msg_suporte.replace(' ', '%20')}"
        st.caption(f"📧 [rodrigoaiosa@gmail.com](mailto:rodrigoaiosa@gmail.com)")
        st.caption(f"💬 [WhatsApp Direct]({link_wa})")
        
    with col3:
        st.markdown("**Links Úteis**")
        st.caption("📅 [Agendar Reunião](https://calendly.com/rodrigoaiosa)")
        st.caption("🌐 [LinkedIn](https://www.linkedin.com/in/rodrigoaiosa/)")

    # Estilo visual para o rodapé ficar discreto mas elegante
    st.markdown("""
        <style>
        footer {visibility: hidden;}
        .stCaption {
            font-size: 0.85rem !important;
            color: #6B7280 !important;
        }
        </style>
    """, unsafe_allow_html=True)
