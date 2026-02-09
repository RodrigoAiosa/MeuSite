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
    """Conexão blindada: limpa a chave privada para evitar o erro invalid_grant."""
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    
    # Busca o JSON na raiz do projeto
    caminho_json = "meuprojetocadsite-5ecb421b15a7.json"
    
    if not os.path.exists(caminho_json):
        # Tenta localizar o arquivo de forma absoluta caso esteja em subpastas
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        caminho_json = os.path.join(base_path, "meuprojetocadsite-5ecb421b15a7.json")

    with open(caminho_json, 'r') as f:
        info = json.load(f)
    
    # RESOLUÇÃO DO ERRO: Garante que as quebras de linha da chave sejam interpretadas corretamente
    # Isso elimina o erro 'account not found' no Streamlit Cloud
    if "private_key" in info:
        info["private_key"] = info["private_key"].replace("\\n", "\n")
    
    return Credentials.from_service_account_info(info, scopes=scope)

def registrar_acesso(nome_pagina, acao="Visualização"):
    """Registra logs de acesso preservando o histórico da planilha."""
    try:
        creds = obter_credenciais()
        client = gspread.authorize(creds)
        
        # ID exato da sua planilha extraído da URL
        id_planilha = "1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU"
        sheet = client.open_by_key(id_planilha).sheet1

        fuso = timezone(timedelta(hours=-3))
        agora_str = datetime.now(fuso).strftime("%d/%m/%Y %H:%M:%S")

        segundos_decorridos = int(time.time() - st.session_state["start_time"])
        duracao_formatada = str(timedelta(seconds=segundos_decorridos))

        headers = st.context.headers
        ua = headers.get("User-Agent", "").lower()
        ip = headers.get("X-Forwarded-For", "Localhost").split(",")[0]
        dispositivo = "Celular" if "mobile" in ua else "PC"

        # Adiciona nova linha preservando os dados anteriores
        sheet.append_row([
            agora_str,
            st.session_state.get("session_id", "unknown"),
            dispositivo,
            "Detectado",
            "Navegador",
            ip,
            "Direto",
            nome_pagina,
            acao,
            duracao_formatada 
        ])
    except Exception as e:
        print(f"Erro no log de acesso: {e}")

def salvar_formulario_contato(dados):
    """Grava os dados do formulário preservando o histórico existente."""
    try:
        creds = obter_credenciais()
        client = gspread.authorize(creds)
        
        # Abre a planilha pelo ID direto
        id_planilha = "1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU"
        sheet = client.open_by_key(id_planilha).sheet1
        
        # Adiciona na próxima linha disponível (append_row)
        sheet.append_row(dados)
        return True
    except Exception as e:
        st.error(f"Erro na API do Google: {str(e)}")
        return False

def exibir_rodape():
    """Exibe o rodapé padrão SKY DATA SOLUTION."""
    st.markdown(
        """
        <hr style='border: 0.5px solid rgba(255, 255, 255, 0.1); margin-top: 50px; margin-bottom: 20px;'>
        <div style='text-align:center; color:gray; font-size: 0.8rem; padding-bottom: 20px;'>
            SKY DATA SOLUTION © 2026 | Rodrigo Aiosa
        </div>
        """,
        unsafe_allow_html=True
    )
