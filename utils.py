import streamlit as st
import gspread
import uuid
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone

# --- CONFIGURAÇÃO DE SESSÃO ---
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())[:8]

def obter_credenciais():
    """Conecta ao Google usando Secrets."""
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    
    try:
        creds_dict = {
            "type": st.secrets["type"],
            "project_id": st.secrets["project_id"],
            "private_key_id": st.secrets["private_key_id"],
            "private_key": st.secrets["private_key"].replace("\\n", "\n"),
            "client_email": st.secrets["client_email"],
            "client_id": st.secrets["client_id"],
            "auth_uri": st.secrets["auth_uri"],
            "token_uri": st.secrets["token_uri"],
            "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
            "client_x509_cert_url": st.secrets["client_x509_cert_url"]
        }
        return Credentials.from_service_account_info(creds_dict, scopes=scope)
    except Exception as e:
        st.error(f"Erro nas Secrets: {e}")
        return None

def registrar_acesso(nome_pagina, acao="Visualização"):
    """Registra acessos na planilha de monitoramento 'Relatorio_Acessos_Site'."""
    try:
        creds = obter_credenciais()
        if not creds: return
        client = gspread.authorize(creds)
        
        # ID da planilha 'Relatorio_Acessos_Site' conforme solicitado
        id_planilha_acessos = "1TCx1sTDaPsygvh-FvzalJ3JlBKJBOTbfoD-7CZmhCVI"
        sheet = client.open_by_key(id_planilha_acessos).sheet1
        
        fuso = timezone(timedelta(hours=-3))
        agora_str = datetime.now(fuso).strftime("%d/%m/%Y %H:%M:%S")
        ua = st.context.headers.get("User-Agent", "").lower()
        dispositivo = "Celular" if "mobile" in ua else "PC"
        
        # append_row preserva o histórico e adiciona nova linha
        sheet.append_row([
            agora_str, 
            st.session_state.get("session_id"), 
            dispositivo, 
            "Ativo", 
            "Navegador", 
            "Remote", 
            "Direto", 
            nome_pagina, 
            acao, 
            "00:00"
        ])
    except:
        pass

def salvar_formulario_contato(dados):
    """Adiciona nova linha na planilha de CONTATOS preservando os dados anteriores."""
    try:
        creds = obter_credenciais()
        if not creds: return False
        client = gspread.authorize(creds)
        
        # ID da planilha de contatos (bd_contato_form_site)
        id_planilha_contato = "1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU"
        sheet = client.open_by_key(id_planilha_contato).sheet1
        
        sheet.append_row(dados)
        return True
    except Exception as e:
        st.error(f"Erro na conexão: {str(e)}")
        return False

def exibir_rodape():
    st.markdown("<hr style='border: 0.5px solid rgba(255, 255, 255, 0.1); margin-top: 50px;'><div style='text-align:center; color:gray; font-size: 0.8rem; padding-bottom: 20px;'>SKY DATA SOLUTION © 2026 | Rodrigo Aiosa</div>", unsafe_allow_html=True)
