import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta, timezone
import json

def registrar_acesso(nome_pagina):
    """
    Registra informações de acesso no Google Sheets usando Streamlit Secrets.
    Ajusta o fuso horário para Brasília (UTC-3) e identifica o tipo de dispositivo.
    """
    try:
        # 1. Configuração de Escopo
        scope = ["https://spreadsheets.google.com/feeds",
                 "https://www.googleapis.com/auth/drive"]

        # 2. Carregamento das Credenciais via Secrets
        if "gcp_service_account" in st.secrets:
            creds_info = dict(st.secrets["gcp_service_account"])
            creds_info["private_key"] = creds_info["private_key"].replace('\\n', '\n')
            creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_info, scope)
        else:
            st.error("Configuração 'gcp_service_account' não encontrada nos Secrets.")
            return

        # 3. Autenticação e Abertura da Planilha
        client = gspread.authorize(creds)
        sheet = client.open("Relatorio_Acessos_Site").sheet1

        # 4. Ajuste do Fuso Horário (Brasília UTC-3)
        fuso_brasilia = timezone(timedelta(hours=-3))
        agora = datetime.now(fuso_brasilia).strftime("%d/%m/%Y %H:%M:%S")

        # 5. Coleta de dados do visitante
        headers = st.context.headers
        user_agent = headers.get("User-Agent", "").lower()
        ip = headers.get("X-Forwarded-For", "Localhost").split(',')[0]

        # 6. Identificação detalhada do Dispositivo
        if "ipad" in user_agent or ("android" in user_agent and "mobile" not in user_agent):
            dispositivo = "Tablet"
        elif "mobile" in user_agent or "android" in user_agent or "iphone" in user_agent:
            dispositivo = "Celular"
        else:
            dispositivo = "PC"

        # 7. Gravação dos dados conforme estrutura da planilha
        # Colunas: data_hora | título/fixo | dispositivo | ip | página
        sheet.append_row([agora, "Acesso Portfólio", dispositivo, ip, nome_pagina])

        print(f"✅ SUCESSO: Acesso registrado às {agora} ({dispositivo}) na página '{nome_pagina}'")

    except Exception as e:
        print(f"❌ ERRO NO REGISTRO: {str(e)}")


def exibir_rodape():
    """Exibe o rodapé padrão em todas as páginas."""
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
