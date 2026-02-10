import streamlit as st
import gspread
import json
import os
import uuid
import time
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone

# --- CONFIGURAÇÃO DE SESSÃO GLOBAL ---
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())[:8]

if "start_time" not in st.session_state:
    st.session_state["start_time"] = time.time()

def obter_credenciais():
    """Conexão blindada: limpa a chave e valida o e-mail da conta."""
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    
    # Busca o JSON na raiz do projeto
    caminho_json = "meuprojetocadsite-5ecb421b15a7.json"
    
    if not os.path.exists(caminho_json):
        raise FileNotFoundError(f"Arquivo {caminho_json} não encontrado!")

    with open(caminho_json, 'r') as f:
        info = json.load(f)
    
    # Debug: Mostra o e-mail que o código está tentando usar
    # Se este e-mail não for o 'aiosaprojeto@...', o erro persistirá.
    client_email = info.get("client_email")
    
    # Tratamento da chave para Linux/Streamlit Cloud
    if "private_key" in info:
        info["private_key"] = info["private_key"].replace("\\n", "\n")
    
    return Credentials.from_service_account_info(info, scopes=scope), client_email

def registrar_acesso(nome_pagina, acao="Visualização"):
    """Registra acessos preservando dados antigos."""
    try:
        creds, _ = obter_credenciais()
        client = gspread.authorize(creds)
        id_planilha = "1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU"
        sheet = client.open_by_key(id_planilha).sheet1

        fuso = timezone(timedelta(hours=-3))
        agora_str = datetime.now(fuso).strftime("%d/%m/%Y %H:%M:%S")
        
        ua = st.context.headers.get("User-Agent", "").lower()
        dispositivo = "Celular" if "mobile" in ua else "PC"

        sheet.append_row([
            agora_str, st.session_state.get("session_id"), dispositivo,
            "Ativo", "Navegador", "Remote", "Direto", nome_pagina, acao, "00:00"
        ])
    except Exception as e:
        print(f"Erro Log: {e}")

def salvar_formulario_contato(dados):
    """Salva dados novos sem apagar os existentes."""
    try:
        creds, email_usado = obter_credenciais()
        client = gspread.authorize(creds)
        
        # ID extraído do seu navegador
        id_planilha = "1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU"
        sheet = client.open_by_key(id_planilha).sheet1
        
        sheet.append_row(dados)
        return True
    except Exception as e:
        # Exibe o e-mail para conferência se der erro
        st.error(f"Erro na API do Google: {str(e)}")
        st.info(f"O sistema tentou usar o e-mail: {email_usado}")
        return False

def exibir_rodape():
    st.markdown(
        """
        <hr style='border: 0.5px solid rgba(255, 255, 255, 0.1); margin-top: 50px;'>
        <div style='text-align:center; color:gray; font-size: 0.8rem;'>
            SKY DATA SOLUTION © 2026 | Rodrigo Aiosa
        </div>
        """,
        unsafe_allow_html=True
    )
