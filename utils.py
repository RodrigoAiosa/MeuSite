import streamlit as st
import gspread
import uuid
import os
import time
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone

# --- CONFIGURAÇÃO DE SESSÃO ---
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())[:8]
if "start_time" not in st.session_state:
    st.session_state["start_time"] = time.time()

def obter_credenciais():
    """Busca o JSON na raiz de forma segura para o Streamlit Cloud."""
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    # O arquivo deve estar na RAIZ do GitHub
    arquivo_json = "meuprojetocadsite-5ecb421b15a7.json"
    
    if not os.path.exists(arquivo_json):
        raise FileNotFoundError(f"O arquivo {arquivo_json} não foi encontrado na raiz do projeto.")
        
    return Credentials.from_service_account_file(arquivo_json, scopes=scope)

def registrar_acesso(nome_pagina, acao="Visualização"):
    """Registra logs de acesso na planilha."""
    try:
        creds = obter_credenciais()
        client = gspread.authorize(creds)
        sheet = client.open("Relatorio_Acessos_Site").sheet1

        fuso = timezone(timedelta(hours=-3))
        agora_str = datetime.now(fuso).strftime("%d/%m/%Y %H:%M:%S")
        
        segundos = int(time.time() - st.session_state["start_time"])
        duracao = str(timedelta(seconds=segundos))

        ua = st.context.headers.get("User-Agent", "").lower()
        dispositivo = "Celular" if "mobile" in ua else "PC"

        sheet.append_row([
            agora_str, st.session_state["session_id"], dispositivo, 
            "Ativo", "Navegador", "Remote", "Direto", 
            nome_pagina, acao, duracao
        ])
    except Exception as e:
        print(f"Erro no log de acesso: {e}")

def exibir_rodape():
    st.markdown("---")
    st.markdown(
        "<div style='text-align:center; color:gray; font-size: 0.8rem;'>SKY DATA SOLUTION © 2026 | Rodrigo Aiosa</div>",
        unsafe_allow_html=True
    )
