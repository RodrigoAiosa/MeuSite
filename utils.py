import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta, timezone

def obter_credenciais_google():
    """Função interna para centralizar a autenticação via Secrets."""
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    if "gcp_service_account" in st.secrets:
        creds_info = dict(st.secrets["gcp_service_account"])
        creds_info["private_key"] = creds_info["private_key"].replace('\\n', '\n')
        return ServiceAccountCredentials.from_json_keyfile_dict(creds_info, scope)
    return None

def registrar_acesso(nome_pagina):
    """
    Registra informações de acesso na planilha: Relatorio_Acessos_Site
    Colunas: data_hora | dispositivo | sistema operacional | ip | página
    """
    try:
        creds = obter_credenciais_google()
        if not creds:
            print("❌ ERRO: Secrets 'gcp_service_account' não encontrados.")
            return

        client = gspread.authorize(creds)
        # Abre a planilha de logs de acesso
        sheet = client.open("Relatorio_Acessos_Site").sheet1 

        fuso_brasilia = timezone(timedelta(hours=-3))
        agora = datetime.now(fuso_brasilia).strftime("%d/%m/%Y %H:%M:%S")
        
        headers = st.context.headers
        ua = headers.get("User-Agent", "").lower()
        ip_visitante = headers.get("X-Forwarded-For", "Localhost").split(',')[0]

        dispositivo = "Tablet" if "ipad" in ua or ("android" in ua and "mobile" not in ua) else \
                      "Celular" if "mobile" in ua or "android" in ua or "iphone" in ua else "PC"
        
        so = "Windows" if "windows" in ua else "Android" if "android" in ua else \
             "iOS" if "iphone" in ua or "ipad" in ua else "Mac OS" if "mac os" in ua else "Outro"

        sheet.append_row([agora, dispositivo, so, ip_visitante, nome_pagina])
        print(f"✅ SUCESSO: Acesso em '{nome_pagina}' registrado.")

    except Exception as e:
        print(f"❌ ERRO NO REGISTRO DE ACESSO: {str(e)}")

def registrar_formulario_contato(nome, email, whatsapp, mensagem):
    """
    Registra os dados do formulário na planilha: bd_contato_form_site
    Colunas: data_hora | nome | email | whatsapp | mensagem
    """
    try:
        creds = obter_credenciais_google()
        if not creds:
            return False

        client = gspread.authorize(creds)
        # Abre especificamente a planilha do formulário de contato
        sheet = client.open("bd_contato_form_site").sheet1 

        fuso_brasilia = timezone(timedelta(hours=-3))
        agora = datetime.now(fuso_brasilia).strftime("%d/%m/%Y %H:%M:%S")

        # Grava os dados na ordem das colunas da planilha de contatos
        sheet.append_row([agora, nome, email, whatsapp, mensagem])
        return True

    except Exception as e:
        print(f"❌ ERRO AO SALVAR FORMULÁRIO: {str(e)}")
        return False

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
