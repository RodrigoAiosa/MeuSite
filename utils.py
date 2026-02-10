import streamlit as st
import gspread
import uuid
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
    except Exception as e:
        st.error(f"Erro nas Secrets: {e}")
        return None

def registrar_acesso(nome_pagina, acao="Visualização"):
    """Registra acessos detalhando Apple, Android ou PC e calcula duração."""
    try:
        creds = obter_credenciais()
        if not creds: return
        client = gspread.authorize(creds)
        sheet = client.open_by_key("1TCx1sTDaPsygvh-FvzalJ3JlBKJBOTbfoD-7CZmhCVI").sheet1
        
        fuso = timezone(timedelta(hours=-3))
        agora = datetime.now(fuso)
        agora_str = agora.strftime("%d/%m/%Y %H:%M:%S")
        
        # 1. ATUALIZAR DURAÇÃO DA PÁGINA ANTERIOR
        if st.session_state.get("ultima_linha_acesso"):
            delta = agora - st.session_state["entrada_pagina"]
            duracao_str = f"{int(delta.total_seconds() // 60):02d}:{int(delta.total_seconds() % 60):02d}"
            try:
                sheet.update_cell(st.session_state["ultima_linha_acesso"], 10, duracao_str)
            except: pass

        # 2. IDENTIFICAÇÃO DETALHADA DO DISPOSITIVO
        ua = st.context.headers.get("User-Agent", "").lower()
        so = "Ativo"
        
        if "ipad" in ua or ("android" in ua and "mobile" not in ua):
            dispositivo = "Tablet"
        elif "iphone" in ua:
            dispositivo = "Celular (Apple)"
            so = "iOS"
        elif "android" in ua:
            dispositivo = "Celular (Android)"
            so = "Android"
        else:
            dispositivo = "PC"
            so = "Windows/Mac/Linux"
        
        nova_linha = [agora_str, st.session_state["session_id"], dispositivo, so, "Navegador", "Remote", "Direto", nome_pagina, acao, "00:00"]
        
        # Busca a próxima linha disponível real
        proxima_linha = len(list(filter(None, sheet.col_values(1)))) + 1
        if proxima_linha < 2: proxima_linha = 2
            
        sheet.insert_row(nova_linha, proxima_linha)
        
        # Atualiza os dados na sessão
        st.session_state["ultima_linha_acesso"] = proxima_linha
        st.session_state["entrada_pagina"] = agora
        st.session_state["leu_ate_o_fim"] = False 
        
    except Exception as e:
        # Remova o 'pass' temporariamente se quiser ver o erro no terminal
        print(f"Erro ao registrar: {e}")

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
