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
    """Conexão blindada: corrige a chave privada para evitar o erro de conta não encontrada."""
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    
    # Busca o JSON na raiz do projeto conforme seu repositório
    caminho_json = "meuprojetocadsite-5ecb421b15a7.json"
    
    if not os.path.exists(caminho_json):
        raise FileNotFoundError(f"Arquivo {caminho_json} não encontrado na raiz!")

    with open(caminho_json, 'r') as f:
        info = json.load(f)
    
    # RESOLUÇÃO DO ERRO: Trata as quebras de linha da chave para o Streamlit Cloud
    if "private_key" in info:
        info["private_key"] = info["private_key"].replace("\\n", "\n")
    
    return Credentials.from_service_account_info(info, scopes=scope)

def registrar_acesso(nome_pagina, acao="Visualização"):
    """
    Registra cada acesso na planilha de logs.
    Preserva todos os dados existentes conforme solicitado.
    """
    try:
        creds = obter_credenciais()
        client = gspread.authorize(creds)
        
        # ID da sua planilha de logs
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

        # Salva a nova linha no final da tabela
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
        # Log silencioso para não interromper a experiência do usuário
        print(f"Erro ao registrar acesso: {e}")

def salvar_formulario_contato(dados):
    """
    Salva os dados do formulário de contato.
    Garante a preservação do histórico da planilha.
    """
    try:
        creds = obter_credenciais()
        client = gspread.authorize(creds)
        
        # ID da planilha de contatos
        id_planilha = "1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU"
        sheet = client.open_by_key(id_planilha).sheet1
        
        # Adiciona os novos dados na próxima linha disponível
        sheet.append_row(dados)
        return True
    except Exception as e:
        st.error(f"Erro na API do Google: {str(e)}")
        return False

def exibir_rodape():
    """Exibe o rodapé padrão da SKY DATA SOLUTION em todas as páginas."""
    st.markdown(
        """
        <hr style='border: 0.5px solid rgba(255, 255, 255, 0.1); margin-top: 50px; margin-bottom: 20px;'>
        <div style='text-align:center; color:gray; font-size: 0.8rem; padding-bottom: 20px;'>
            SKY DATA SOLUTION © 2026 | Rodrigo Aiosa
        </div>
        """,
        unsafe_allow_html=True
    )
