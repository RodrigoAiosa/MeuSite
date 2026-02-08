import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta, timezone

def registrar_acesso(nome_pagina):
    """
    Registra informações de acesso no Google Sheets com colunas específicas:
    data_hora | dispositivo | sistema operacional | ip | página
    """
    try:
        # 1. Configuração de Escopo
        scope = ["https://spreadsheets.google.com/feeds",
                 "https://www.googleapis.com/auth/drive"]

        # 2. Carregamento das Credenciais via Secrets (Evita erro de arquivo local)
        if "gcp_service_account" in st.secrets:
            creds_info = dict(st.secrets["gcp_service_account"])
            # Garante que a chave privada seja lida corretamente com quebras de linha
            creds_info["private_key"] = creds_info["private_key"].replace('\\n', '\n')
            creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_info, scope)
        else:
            # Erro exibido caso o secrets.toml não esteja configurado
            st.error("Configuração 'gcp_service_account' não encontrada nos Secrets.")
            return

        # 3. Autenticação e Abertura da Planilha
        client = gspread.authorize(creds)
        sheet = client.open("Relatorio_Acessos_Site").sheet1

        # 4. Ajuste do Fuso Horário para Brasília (UTC-3)
        fuso_brasilia = timezone(timedelta(hours=-3))
        agora = datetime.now(fuso_brasilia).strftime("%d/%m/%Y %H:%M:%S")

        # 5. Coleta de dados do visitante (User-Agent e IP)
        headers = st.context.headers
        ua_string = headers.get("User-Agent", "").lower()
        ip = headers.get("X-Forwarded-For", "Localhost").split(',')[0]

        # 6. Identificação do Dispositivo (PC, Celular ou Tablet)
        if "ipad" in ua_string or ("android" in ua_string and "mobile" not in ua_string):
            dispositivo = "Tablet"
        elif "mobile" in ua_string or "android" in ua_string or "iphone" in ua_string:
            dispositivo = "Celular"
        else:
            dispositivo = "PC"
            
        # 7. Identificação do Sistema Operacional
        if "windows" in ua_string:
            so = "Windows"
        elif "android" in ua_string:
            so = "Android"
        elif "iphone" in ua_string or "ipad" in ua_string:
            so = "iOS"
        elif "macintosh" in ua_string or "mac os" in ua_string:
            so = "Mac OS"
        elif "linux" in ua_string:
            so = "Linux"
        else:
            so = "Outro"

        # 8. Gravação conforme a ordem das colunas da planilha
        # data_hora | dispositivo | sistema operacional | ip | página
        sheet.append_row([agora, dispositivo, so, ip, nome_pagina])

        # Log interno (visto apenas no console do servidor)
        print(f"✅ SUCESSO: {nome_pagina} registrado para {dispositivo} ({so})")

    except Exception as e:
        # Captura erros como falha de parsing ou conexão
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