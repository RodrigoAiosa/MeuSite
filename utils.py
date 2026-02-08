import streamlit as st
import gspread
import uuid
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta, timezone

# --- CONFIGURAÇÃO DE SESSÃO ---
# Gera um ID único para o visitante assim que ele abre o site
if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())[:8]

def registrar_acesso(nome_pagina, acao="Visualização"):
    """
    Registra informações de acesso no Google Sheets com a nova estrutura:
    data_hora | session_id | dispositivo | so | navegador | ip | origem | pagina | acao
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

        # 4. Ajuste do Fuso Horário (Brasília)
        fuso_brasilia = timezone(timedelta(hours=-3))
        agora = datetime.now(fuso_brasilia).strftime("%d/%m/%Y %H:%M:%S")

        # 5. Coleta de dados do visitante
        headers = st.context.headers
        ua_string = headers.get("User-Agent", "").lower()
        ip = headers.get("X-Forwarded-For", "Localhost").split(',')[0]
        origem = headers.get("Referer", "Direto")
        session_id = st.session_state['session_id']

        # 6. Identificação do Dispositivo
        if "ipad" in ua_string or ("android" in ua_string and "mobile" not in ua_string):
            dispositivo = "Tablet"
        elif "mobile" in ua_string or "android" in ua_string or "iphone" in ua_string:
            dispositivo = "Celular"
        else:
            dispositivo = "PC"
            
        # 7. Identificação do Sistema Operacional
        sos = {
            "windows": "Windows", 
            "android": "Android", 
            "iphone": "iOS", 
            "ipad": "iOS", 
            "macintosh": "Mac OS", 
            "linux": "Linux"
        }
        so = next((v for k, v in sos.items() if k in ua_string), "Outro")

        # 8. Identificação do Navegador
        if "edg" in ua_string: 
            navegador = "Edge"
        elif "chrome" in ua_string: 
            navegador = "Chrome"
        elif "safari" in ua_string: 
            navegador = "Safari"
        elif "firefox" in ua_string: 
            navegador = "Firefox"
        else: 
            navegador = "Outro"

        # 9. Gravação conforme a nova ordem das colunas
        # A: data_hora | B: session_id | C: dispositivo | D: so | E: navegador | F: ip | G: origem | H: pagina | I: acao
        sheet.append_row([
            agora, 
            session_id, 
            dispositivo, 
            so, 
            navegador, 
            ip, 
            origem, 
            nome_pagina, 
            acao
        ])

        print(f"✅ SUCESSO: {nome_pagina} ({acao}) registrado para {session_id}")

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
