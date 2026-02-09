import streamlit as st
import gspread
import uuid
import os
import json
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone

# --- CONFIGURAÇÃO DE SESSÃO ---
if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())[:8]

def obter_caminho_json():
    """
    Localiza o arquivo JSON de credenciais dinamicamente.
    """
    nome_arquivo = "meuprojetocadsite-5ecb421b15a7.json"
    
    # 1. Tenta no diretório atual (se estiver rodando da raiz)
    caminho_atual = os.path.join(os.getcwd(), nome_arquivo)
    if os.path.exists(caminho_atual):
        return caminho_atual
    
    # 2. Tenta na pasta pai (se o script estiver dentro de /Views)
    caminho_pai = os.path.join(os.path.dirname(os.getcwd()), nome_arquivo)
    if os.path.exists(caminho_pai):
        return caminho_pai
        
    # 3. Tenta baseado no local deste arquivo utils.py
    caminho_utils = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", nome_arquivo)
    if os.path.exists(caminho_utils):
        return os.path.normpath(caminho_utils)

    return None

def registrar_acesso(nome_pagina, acao="Visualização"):
    """
    Registra informações de acesso no Google Sheets.
    Preserva dados existentes e adiciona novos registros.
    """
    try:
        scope = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

        caminho_json = obter_caminho_json()
        
        if caminho_json:
            # Carregamento via arquivo físico (Local)
            creds = Credentials.from_service_account_file(caminho_json, scopes=scope)
            client = gspread.authorize(creds)
        else:
            # Fallback para Secrets (Streamlit Cloud)
            if "gcp_service_account" in st.secrets:
                creds_info = dict(st.secrets["gcp_service_account"])
                creds_info["private_key"] = creds_info["private_key"].replace("\\n", "\n")
                creds = Credentials.from_service_account_info(creds_info, scopes=scope)
                client = gspread.authorize(creds)
            else:
                # Se não achar o arquivo nem os secrets, encerra silenciosamente
                return

        # Abre a planilha (Certifique-se que o nome está idêntico no Google Drive)
        sheet = client.open("Relatorio_Acessos_Site").sheet1

        # Dados de Tempo (Brasília)
        fuso_brasilia = timezone(timedelta(hours=-3))
        agora = datetime.now(fuso_brasilia).strftime("%d/%m/%Y %H:%M:%S")
        
        # Metadados do Visitante
        headers = st.context.headers
        ua_string = headers.get("User-Agent", "").lower()
        ip = headers.get("X-Forwarded-For", "Localhost").split(',')[0]
        dispositivo = "Celular" if "mobile" in ua_string else "PC"
        
        # Envio das colunas para o Sheets (Preservando os dados antigos)
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
        # Usar st.error apenas se quiser debugar visualmente, senão mantenha o print
        print(f"❌ ERRO NO REGISTRO DE ACESSO: {str(e)}")

def exibir_rodape():
    """
    Exibe o rodapé oficial completo do Rodrigo Aiosa.
    """
    st.markdown("---")
    footer_html = """
    <div style='text-align: center; color: gray; padding: 10px;'>
        <p style='margin-bottom: 10px;'><b>Rodrigo Aiosa © 2026</b> | Especialista em BI & Treinamentos</p>
        <div style='display: flex; justify-content: center; gap: 25px; font-size: 30px;'>
            <a href='https://wa.me/5511977019335' target='_blank' style='text-decoration: none;'>
                <img src='https://cdn-icons-png.flaticon.com/512/733/733585.png' width='30' height='30'>
            </a>
            <a href='https://www.linkedin.com/in/rodrigoaiosa/' target='_blank' style='text-decoration: none;'>
                <img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' width='30' height='30'>
            </a>
        </div>
        <p style='font-size: 12px; margin-top: 10px; color: #666;'>Transformando dados em decisões estratégicas.</p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)