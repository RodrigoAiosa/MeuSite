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
    Centraliza a conexão com o Google Sheets priorizando st.secrets.
    """
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    
    try:
        # Tenta usar Secrets (Ideal para Streamlit Cloud)
        if "gcp_service_account" in st.secrets:
            creds_info = dict(st.secrets["gcp_service_account"])
            # Removemos substituições manuais; o TOML com """ cuida disso.
            creds = Credentials.from_service_account_info(creds_info, scopes=scope)
            return gspread.authorize(creds)
        else:
            st.error("Credenciais 'gcp_service_account' não encontradas no Secrets.")
            return None
    except Exception as e:
        st.error(f"Erro na autenticação: {e}")
        return None

def registrar_acesso(nome_pagina, acao="Visualização"):
    """
    Registra acessos anexando uma nova linha (Preserva dados existentes).
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
            
            # append_row adiciona ao final sem apagar nada
            sheet.append_row([
                agora, st.session_state['session_id'], dispositivo, 
                "Detectado", "Navegador", ip, "Direto", nome_pagina, acao
            ])
    except Exception as e:
        print(f"Erro silencioso no acesso: {e}")

def salvar_formulario_contato(dados_lista):
    """
    Salva dados do formulário na planilha bd_contato_form_site.
    """
    try:
        client = conectar_google_sheets()
        if client:
            sheet = client.open("bd_contato_form_site").sheet1
            fuso_brasilia = timezone(timedelta(hours=-3))
            agora = datetime.now(fuso_brasilia).strftime("%d/%m/%Y %H:%M:%S")
            
            # Insere a data no início da lista de dados
            registro = [agora] + dados_lista
            sheet.append_row(registro)
            return True
    except Exception as e:
        st.error(f"Erro ao salvar formulário: {e}")
        return False

def exibir_rodape():
    st.markdown("---")
    footer_html = """
    <div style='text-align: center; color: gray; padding: 10px;'>
        <p><b>Rodrigo Aiosa © 2026</b> | Especialista em BI & Treinamentos</p>
        <div style='display: flex; justify-content: center; gap: 25px;'>
            <a href='https://wa.me/5511977019335' target='_blank'><img src='https://cdn-icons-png.flaticon.com/512/733/733585.png' width='30'></a>
            <a href='https://www.linkedin.com/in/rodrigoaiosa/' target='_blank'><img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' width='30'></a>
        </div>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)
