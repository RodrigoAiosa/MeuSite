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
        
        # 2. Carregamento via Secrets (Obrigatório para Deploy no GitHub)
        # Certifique-se de que colou o JSON no painel do Streamlit Cloud como [gcp_service_account]
        if "gcp_service_account" in st.secrets:
            creds_info = dict(st.secrets["gcp_service_account"])
            creds_info["private_key"] = creds_info["private_key"].replace('\\n', '\n')
            creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_info, scope)
        else:
            # Se cair aqui, o segredo não foi configurado no painel Settings > Secrets do Streamlit
            print("❌ ERRO: Secrets não encontrados no Streamlit Cloud.")
            return

        # 3. Autenticação e Abertura
        client = gspread.authorize(creds)
        sheet = client.open("Relatorio_Acessos_Site").sheet1 

        # 4. Fuso Horário Brasília (UTC-3)
        fuso_brasilia = timezone(timedelta(hours=-3))
        agora = datetime.now(fuso_brasilia).strftime("%d/%m/%Y %H:%M:%S")
        
        # 5. Coleta de Headers de forma segura
        headers = st.context.headers
        ua = headers.get("User-Agent", "").lower()
        ip_visitante = headers.get("X-Forwarded-For", "Localhost").split(',')[0]

        # 6. Identificação de Dispositivo (Baseado no seu Excel)
        dispositivo = "Tablet" if "ipad" in ua or ("android" in ua and "mobile" not in ua) else \
                      "Celular" if "mobile" in ua or "android" in ua or "iphone" in ua else "PC"
        
        # 7. Identificação de Sistema Operacional
        so = "Windows" if "windows" in ua else "Android" if "android" in ua else \
             "iOS" if "iphone" in ua or "ipad" in ua else "Mac OS" if "mac os" in ua else "Outro"

        # 8. Gravação na ordem exata da sua planilha (data_hora | dispositivo | SO | ip | página)
        sheet.append_row([agora, dispositivo, so, ip_visitante, nome_pagina])
        
        print(f"✅ SUCESSO: Acesso em '{nome_pagina}' registrado.")

    except Exception as e:
        # Erro impresso nos logs do Streamlit (Manage App)
        print(f"❌ ERRO NO REGISTRO: {str(e)}")

def exibir_rodape():
    st.markdown("---")
    footer_html = """
    <div style='text-align: center; color: gray;'>
        <p style='margin-bottom: 5px;'><b>Rodrigo Aiosa © 2026</b> | Especialista em BI & Treinamentos</p>
        <div style='display: flex; justify-content: center; gap: 20px; font-size: 24px;'>
            <a href='https://wa.me/5511977019335' target='_blank'>
                <img src='https://cdn-icons-png.flaticon.com/512/733/733585.png' width='25' height='25'>
            </a>
            <a href='https://www.linkedin.com/in/rodrigoaiosa/' target='_blank'>
                <img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' width='25' height='25'>
            </a>
        </div>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)
