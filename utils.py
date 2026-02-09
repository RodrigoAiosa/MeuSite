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
    Autentica no Google Sheets usando exclusivamente st.secrets.
    """
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    
    try:
        # Prioriza 100% o Streamlit Secrets para o ambiente de produção
        if "gcp_service_account" in st.secrets:
            creds_info = dict(st.secrets["gcp_service_account"])
            
            # Correção para o erro 'Unable to load PEM file': 
            # Garante que as quebras de linha da chave privada sejam interpretadas corretamente
            if "\\n" in creds_info["private_key"]:
                creds_info["private_key"] = creds_info["private_key"].replace("\\n", "\n")
            
            creds = Credentials.from_service_account_info(creds_info, scopes=scope)
            return gspread.authorize(creds)
        else:
            st.error("Erro: Configuração 'gcp_service_account' não encontrada nos Secrets do Streamlit.")
            return None
    except Exception as e:
        st.error(f"Erro Crítico de Autenticação: {e}")
        return None

def registrar_acesso(nome_pagina, acao="Visualização"):
    """
    Registra o acesso anexando uma nova linha para preservar dados.
    """
    try:
        client = conectar_google_sheets()
        if client:
            # Abre a planilha de acessos
            sheet = client.open("Relatorio_Acessos_Site").sheet1
            
            fuso_brasilia = timezone(timedelta(hours=-3))
            agora = datetime.now(fuso_brasilia).strftime("%d/%m/%Y %H:%M:%S")
            
            headers = st.context.headers
            ua_string = headers.get("User-Agent", "").lower()
            ip = headers.get("X-Forwarded-For", "Localhost").split(',')[0]
            dispositivo = "Celular" if "mobile" in ua_string else "PC"
            
            # append_row adiciona ao final sem sobrescrever os dados existentes
            sheet.append_row([
                agora, 
                st.session_state['session_id'], 
                dispositivo, 
                "Detectado", 
                "Navegador", 
                ip, 
                "Direto", 
                nome_pagina, 
                acao
            ])
    except Exception as e:
        print(f"Erro silencioso no acesso: {e}")

def salvar_formulario_contato(dados_lista):
    """
    Anexa dados do formulário na planilha bd_contato_form_site.
    """
    try:
        client = conectar_google_sheets()
        if client:
            sheet = client.open("bd_contato_form_site").sheet1
            fuso_brasilia = timezone(timedelta(hours=-3))
            agora = datetime.now(fuso_brasilia).strftime("%d/%m/%Y %H:%M:%S")
            
            # Cria a linha: Data + Nome, Email, WhatsApp, Mensagem
            linha_completa = [agora] + dados_lista
            
            # O método append_row preserva o histórico da planilha
            sheet.append_row(linha_completa)
            return True
    except Exception as e:
        st.error(f"Erro ao salvar no formulário: {e}")
        return False

def exibir_rodape():
    st.markdown("---")
    st.markdown("<div style='text-align: center; color: gray;'>Rodrigo Aiosa © 2026</div>", unsafe_allow_html=True)
