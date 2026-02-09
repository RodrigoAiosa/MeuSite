import streamlit as st
import gspread
import uuid
import os
import time
import json
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone

# --- CONFIGURAÇÃO DE SESSÃO ---
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())[:8]
if "start_time" not in st.session_state:
    st.session_state["start_time"] = time.time()

def obter_credenciais():
    """Busca o JSON e limpa a chave privada para evitar o erro invalid_grant."""
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    caminho_json = "meuprojetocadsite-5ecb421b15a7.json"
    
    if not os.path.exists(caminho_json):
        # Fallback para busca caso o script esteja em subpastas
        caminho_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        caminho_json = os.path.join(caminho_base, "meuprojetocadsite-5ecb421b15a7.json")

    with open(caminho_json, 'r') as f:
        info = json.load(f)
    
    # Tratamento crucial para que o Google reconheça a conta de serviço
    info["private_key"] = info["private_key"].replace("\\n", "\n")
    
    return Credentials.from_service_account_info(info, scopes=scope)

def registrar_acesso(nome_pagina, acao="Visualização"):
    """Registra logs preservando os dados anteriores na planilha."""
    try:
        creds = obter_credenciais()
        client = gspread.authorize(creds)
        # ID direto da sua planilha para evitar erro de 'account not found' por nome
        sheet = client.open_by_key("1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU").sheet1

        fuso = timezone(timedelta(hours=-3))
        agora_str = datetime.now(fuso).strftime("%d/%m/%Y %H:%M:%S")
        
        ua = st.context.headers.get("User-Agent", "").lower()
        dispositivo = "Celular" if "mobile" in ua else "PC"

        sheet.append_row([
            agora_str, st.session_state["session_id"], dispositivo, 
            "Ativo", "Navegador", "Remote", "Direto", 
            nome_pagina, acao, "00:00"
        ])
    except Exception as e:
        print(f"Log Error: {e}")

def exibir_rodape():
    st.markdown("<hr style='border: 0.5px solid rgba(255,255,255,0.1);'>", unsafe_allow_html=True)
    st.markdown(
        "<div style='text-align:center; color:gray; font-size: 0.8rem; padding-bottom: 20px;'>"
        "SKY DATA SOLUTION © 2026 | Rodrigo Aiosa</div>",
        unsafe_allow_html=True
    )
