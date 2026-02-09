import streamlit as st
import gspread
import uuid
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone

# --- CONFIGURAÇÃO DE SESSÃO ---
if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())[:8]

def conectar_google_sheets():
    """
    Autentica no Google Sheets usando st.secrets com tratamento de chave PEM.
    """
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    
    try:
        if "gcp_service_account" in st.secrets:
            creds_info = dict(st.secrets["gcp_service_account"])
            
            # Converte a string salva nos Secrets para o formato de chave real
            if "private_key" in creds_info:
                creds_info["private_key"] = creds_info["private_key"].replace("\\n", "\n")
            
            creds = Credentials.from_service_account_info(creds_info, scopes=scope)
            return gspread.authorize(creds)
        return None
    except Exception as e:
        st.error(f"Erro Crítico de Autenticação: {e}")
        return None

def registrar_acesso(nome_pagina, acao="Visualização"):
    """
    Registra o acesso na planilha Relatorio_Acessos_Site (9 colunas).
    Preserva dados existentes.
    """
    try:
        client = conectar_google_sheets()
        if client:
            sheet = client.open("Relatorio_Acessos_Site").sheet1
            
            fuso_brasilia = timezone(timedelta(hours=-3))
            agora = datetime.now(fuso_brasilia).strftime("%d/%m/%Y %H:%M:%S")
            
            headers = st.context.headers
            ua_string = headers.get("User-Agent", "").lower()
            ip = headers.get("X-Forwarded-For", "Localhost").split(',')[0]
            dispositivo = "Celular" if "mobile" in ua_string else "PC"
            
            # Linha formatada para as colunas A até I da sua planilha
            linha = [
                agora,                          # data_hora
                st.session_state['session_id'], # session_id
                dispositivo,                    # dispositivo
                "Detectado",                    # sistema_operacional
                "Navegador",                    # navegador
                ip,                             # ip
                "Direto",                       # origem
                nome_pagina,                    # pagina
                acao                            # acao
            ]
            
            sheet.append_row(linha)
    except Exception as e:
        # Erro silencioso para não impactar o usuário final
        print(f"Erro no log de acesso: {e}")

def salvar_formulario_contato(dados_lista):
    """
    Salva contato na planilha bd_contato_form_site preservando o histórico.
    """
    try:
        client = conectar_google_sheets()
        if client:
            sheet = client.open("bd_contato_form_site").sheet1
            fuso_brasilia = timezone(timedelta(hours=-3))
            agora = datetime.now(fuso_brasilia).strftime("%d/%m/%Y %H:%M:%S")
            
            sheet.append_row([agora] + dados_lista)
            return True
    except Exception as e:
        st.error(f"Erro ao salvar formulário: {e}")
        return False

def exibir_rodape():
    """
    Exibe o rodapé padrão em todas as páginas.
    """
    st.markdown("---")
    st.markdown("<div style='text-align: center; color: gray;'>Desenvolvido por Rodrigo Aiosa © 2026</div>", unsafe_allow_html=True)
