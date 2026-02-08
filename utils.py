import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta, timezone

def registrar_acesso(nome_pagina):
    """
    Registra informações de acesso no Google Sheets via Secrets.
    Colunas: data_hora | dispositivo | sistema operacional | ip | página
    """
    try:
        # 1. Configuração de Escopo
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        
        # 2. Carregamento via Secrets (Obrigatório para Deploy)
        if "gcp_service_account" in st.secrets:
            creds_info = dict(st.secrets["gcp_service_account"])
            creds_info["private_key"] = creds_info["private_key"].replace('\\n', '\n')
            creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_info, scope)
        else:
            print("❌ ERRO: Secrets não configurados no Streamlit Cloud.")
            return

        # 3. Autenticação e Abertura da Planilha
        client = gspread.authorize(creds)
        sheet = client.open("Relatorio_Acessos_Site").sheet1 

        # 4. Fuso Horário Brasília (UTC-3)
        fuso_brasilia = timezone(timedelta(hours=-3))
        agora = datetime.now(fuso_brasilia).strftime("%d/%m/%Y %H:%M:%S")
        
        # 5. Coleta de Headers
        headers = st.context.headers
        ua = headers.get("User-Agent", "").lower()
        ip = headers.get("X-Forwarded-For", "Localhost").split(',')[0]

        # 6. Identificação de Dispositivo e SO
        dispositivo = "Tablet" if "ipad" in ua or ("android" in ua and "mobile" not in ua) else \
                      "Celular" if "mobile" in ua or "android" in ua or "iphone" in ua else "PC"
        
        so = "Windows" if "windows" in ua else "Android" if "android" in ua else \
             "iOS" if "iphone" in ua or "ipad" in ua else "Mac OS" if "mac os" in ua else "Outro"

        # 7. Gravação na ordem exata da sua planilha
        # data_hora | dispositivo | sistema operacional | ip | página
        sheet.append_row([agora, dispositivo, so, ip, nome_pagina])
        
        print(f"✅ SUCESSO: Acesso em '{nome_pagina}' registrado.")

    except Exception as e:
        print(f"❌ ERRO NO REGISTRO: {str(e)}")
