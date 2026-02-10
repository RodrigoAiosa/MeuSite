import streamlit as st
import gspread
import uuid
import re
import streamlit.components.v1 as components
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone

# --- CONFIGURAÇÃO DE SESSÃO ---
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())[:8]
if "entrada_pagina" not in st.session_state:
    st.session_state["entrada_pagina"] = datetime.now(timezone(timedelta(hours=-3)))
if "ultima_linha_acesso" not in st.session_state:
    st.session_state["ultima_linha_acesso"] = None
if "leu_ate_o_fim" not in st.session_state:
    st.session_state["leu_ate_o_fim"] = False

def obter_credenciais():
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    try:
        # Tenta pegar das Secrets do Streamlit Cloud
        creds_dict = {
            "type": st.secrets["type"],
            "project_id": st.secrets["project_id"],
            "private_key_id": st.secrets["private_key_id"],
            "private_key": st.secrets["private_key"].replace("\\n", "\n"),
            "client_email": st.secrets["client_email"],
            "client_id": st.secrets["client_id"],
            "auth_uri": st.secrets["auth_uri"],
            "token_uri": st.secrets["token_uri"],
            "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
            "client_x509_cert_url": st.secrets["client_x509_cert_url"]
        }
        return Credentials.from_service_account_info(creds_dict, scopes=scope)
    except Exception:
        # Fallback para arquivo local caso não encontre secrets (uso em desenvolvimento)
        try:
            return Credentials.from_service_account_file("meuprojetocadsite-5ecb421b15a7.json", scopes=scope)
        except:
            return None

def registrar_acesso(nome_pagina, acao="Visualização"):
    """Registra acesso classificando corretamente PC, iPhone, Android, etc."""
    try:
        creds = obter_credenciais()
        if not creds: return
        client = gspread.authorize(creds)
        # Abre a planilha pelo ID fornecido
        sheet = client.open_by_key("1TCx1sTDaPsygvh-FvzalJ3JlBKJBOTbfoD-7CZmhCVI").sheet1
        
        fuso = timezone(timedelta(hours=-3))
        agora = datetime.now(fuso)
        agora_str = agora.strftime("%d/%m/%Y %H:%M:%S")
        
        # 1. ATUALIZAR DURAÇÃO NA LINHA ANTERIOR (Coluna J)
        if st.session_state.get("ultima_linha_acesso"):
            delta = agora - st.session_state["entrada_pagina"]
            duracao_str = f"{int(delta.total_seconds() // 60):02d}:{int(delta.total_seconds() % 60):02d}"
            try:
                sheet.update_cell(st.session_state["ultima_linha_acesso"], 10, duracao_str)
            except: pass

        # 2. CAPTURA E CLASSIFICAÇÃO DO DISPOSITIVO
        headers = st.context.headers
        ua = headers.get("User-Agent", "").lower()
        ip_usuario = headers.get("X-Forwarded-For", "Privado").split(",")[0]
        
        # Lógica de Classificação para a Coluna C (Dispositivo) e D (SO)
        if "iphone" in ua:
            dispositivo = "Celular (iPhone)"
            so_final = "iOS"
        elif "ipad" in ua:
            dispositivo = "Tablet (iPad)"
            so_final = "iOS"
        elif "android" in ua:
            dispositivo = "Celular (Android)" if "mobile" in ua else "Tablet (Android)"
            so_final = "Android"
        elif any(x in ua for x in ["windows phone", "iemobile"]):
            dispositivo = "Celular (Windows)"
            so_final = "Windows Phone"
        elif "windows" in ua:
            dispositivo = "PC"
            so_final = "Windows"
        elif "macintosh" in ua or "mac os x" in ua:
            dispositivo = "PC"
            so_final = "MacOS"
        elif "linux" in ua:
            dispositivo = "PC"
            so_final = "Linux"
        else:
            dispositivo = "Outro Móvel" if "mobi" in ua else "PC"
            so_final = "Desconhecido"

        # Identificação do Navegador (Coluna E)
        if "edg/" in ua: navegador = "Edge"
        elif "opr/" in ua or "opera/" in ua: navegador = "Opera"
        elif "firefox/" in ua: navegador = "Firefox"
        elif "chrome/" in ua: navegador = "Chrome"
        elif "safari/" in ua: navegador = "Safari"
        else: navegador = "Outro"
        
        # Montagem da nova linha
        nova_linha = [
            agora_str,                     # A: Data/Hora
            st.session_state["session_id"], # B: ID Sessão
            dispositivo,                   # C: DISPOSITIVO (O que você pediu)
            so_final,                      # D: S.O.
            navegador,                     # E: Navegador
            ip_usuario,                    # F: IP
            "Direto",                      # G: Origem
            nome_pagina,                   # H: Página
            acao,                          # I: Ação
            "00:00"                        # J: Duração Inicial
        ]
        
        # Inserção preservando os dados existentes
        # Filtra valores vazios para achar a última linha preenchida real
        proxima_linha = len(list(filter(None, sheet.col_values(1)))) + 1
        if proxima_linha < 2: proxima_linha = 2
            
        sheet.insert_row(nova_linha, proxima_linha)
        
        # Atualiza estado para controle de duração e scroll
        st.session_state["ultima_linha_acesso"] = proxima_linha
        st.session_state["entrada_pagina"] = agora
        st.session_state["leu_ate_o_fim"] = False 
        
    except Exception as e:
        # Em produção, você pode deixar o pass para não exibir erro ao usuário
        # st.write(f"Erro ao registrar: {e}") 
        pass

def detectar_fim_da_pagina():
    js_code = """
    <script>
    const monitorar = () => {
        const pct = (window.innerHeight + window.pageYOffset) / document.documentElement.scrollHeight * 100;
        if (pct >= 95) window.parent.postMessage({type: 'streamlit:setComponentValue', value: true}, '*');
    }
    window.parent.document.addEventListener('scroll', monitorar);
    </script>
    """
    chegou_fim = components.html(js_code, height=0, width=0)
    if chegou_fim and not st.session_state.get("leu_ate_o_fim"):
        try:
            creds = obter_credenciais()
            sheet = gspread.authorize(creds).open_by_key("1TCx1sTDaPsygvh-FvzalJ3JlBKJBOTbfoD-7CZmhCVI").sheet1
            if st.session_state["ultima_linha_acesso"]:
                sheet.update_cell(st.session_state["ultima_linha_acesso"], 9, "Leu até o fim")
                st.session_state["leu_ate_o_fim"] = True
        except: pass

def salvar_formulario_contato(dados):
    try:
        creds = obter_credenciais()
        sheet = gspread.authorize(creds).open_by_key("1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU").sheet1
        proxima = len(list(filter(None, sheet.col_values(1)))) + 1
        sheet.insert_row(dados, max(2, proxima))
        return True
    except: return False

def exibir_rodape():
    detectar_fim_da_pagina()
    st.markdown("<hr style='border: 0.5px solid rgba(255, 255, 255, 0.1); margin-top: 50px;'><div style='text-align:center; color:gray; font-size: 0.8rem; padding-bottom: 20px;'>SKY DATA SOLUTION © 2026 | Rodrigo Aiosa</div>", unsafe_allow_html=True)
