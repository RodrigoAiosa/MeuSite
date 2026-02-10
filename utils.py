import streamlit as st
import gspread
import uuid
import streamlit.components.v1 as components
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone

# --- CONFIGURAÇÃO DE SESSÃO ---
# O session_id é gerado para qualquer dispositivo (Mobile ou PC) ao abrir o site
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())[:8]
if "entrada_pagina" not in st.session_state:
    st.session_state["entrada_pagina"] = datetime.now(timezone(timedelta(hours=-3)))
if "ultima_linha_acesso" not in st.session_state:
    st.session_state["ultima_linha_acesso"] = None
if "leu_ate_o_fim" not in st.session_state:
    st.session_state["leu_ate_o_fim"] = False

def obter_credenciais():
    """Conecta ao Google usando Secrets do Streamlit Cloud."""
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
    """Registra acessos sequencialmente a partir da linha 2 e calcula duração."""
    try:
        creds = obter_credenciais()
        if not creds: return
        client = gspread.authorize(creds)
        
        # ID da planilha de MONITORAMENTO (Acessos)
        id_planilha_acessos = "1TCx1sTDaPsygvh-FvzalJ3JlBKJBOTbfoD-7CZmhCVI"
        sheet = client.open_by_key(id_planilha_acessos).sheet1
        
        fuso = timezone(timedelta(hours=-3))
        agora = datetime.now(fuso)
        agora_str = agora.strftime("%d/%m/%Y %H:%M:%S")
        
        # 1. ATUALIZAR DURAÇÃO DA PÁGINA ANTERIOR (Coluna J)
        if st.session_state.get("ultima_linha_acesso"):
            delta = agora - st.session_state["entrada_pagina"]
            minutos, segundos = divmod(int(delta.total_seconds()), 60)
            duracao_str = f"{minutos:02d}:{segundos:02d}"
            try:
                sheet.update_cell(st.session_state["ultima_linha_acesso"], 10, duracao_str)
            except:
                pass

        # 2. IDENTIFICAR DISPOSITIVO (Qualquer Celular vs PC)
        ua = st.context.headers.get("User-Agent", "").lower()
        # Detecta Android, iPhone, iPad e outros móveis
        if any(mobile in ua for mobile in ["android", "iphone", "ipad", "mobile", "windows phone"]):
            dispositivo = "Celular"
        else:
            dispositivo = "PC"
        
        nova_linha = [
            agora_str, 
            st.session_state.get("session_id"), 
            dispositivo, 
            "Ativo", 
            "Navegador", 
            "Remote", 
            "Direto", 
            nome_pagina, 
            acao, 
            "00:00"
        ]
        
        # Busca o fim real dos dados na Coluna A para evitar saltos
        valores_coluna_a = sheet.col_values(1)
        proxima_linha = len(valores_coluna_a) + 1
        if proxima_linha < 2: proxima_linha = 2
            
        sheet.insert_row(nova_linha, proxima_linha)
        
        # 3. ATUALIZAR ESTADOS DE SESSÃO
        st.session_state["ultima_linha_acesso"] = proxima_linha
        st.session_state["entrada_pagina"] = agora
        st.session_state["leu_ate_o_fim"] = False 
        
    except Exception:
        pass

def detectar_fim_da_pagina():
    """JavaScript para monitorar scroll e atualizar coluna I."""
    js_code = """
    <script>
    const monitorarScroll = () => {
        const h = document.documentElement;
        const b = document.body;
        const st = 'scrollTop';
        const sh = 'scrollHeight';
        const porcentagem = (h[st]||b[st]) / ((h[sh]||b[sh]) - h.clientHeight) * 100;
        
        if (porcentagem >= 95) {
            window.parent.postMessage({type: 'streamlit:setComponentValue', value: true}, '*');
        }
    }
    window.parent.document.addEventListener('scroll', monitorarScroll);
    </script>
    """
    chegou_ao_fim = components.html(js_code, height=0, width=0)
    
    if chegou_ao_fim and not st.session_state.get("leu_ate_o_fim"):
        try:
            creds = obter_credenciais()
            client = gspread.authorize(creds)
            sheet = client.open_by_key("1TCx1sTDaPsygvh-FvzalJ3JlBKJBOTbfoD-7CZmhCVI").sheet1
            sheet.update_cell(st.session_state["ultima_linha_acesso"], 9, "Leu até o fim")
            st.session_state["leu_ate_o_fim"] = True
        except:
            pass

def salvar_formulario_contato(dados):
    """Salva formulário preservando dados existentes."""
    try:
        creds = obter_credenciais()
        if not creds: return False
        client = gspread.authorize(creds)
        id_planilha_contato = "1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU"
        sheet = client.open_by_key(id_planilha_contato).sheet1
        
        valores_coluna_a = sheet.col_values(1)
        proxima_linha = len(valores_coluna_a) + 1
        if proxima_linha < 2: proxima_linha = 2
        
        sheet.insert_row(dados, proxima_linha)
        return True
    except Exception as e:
        st.error(f"Erro ao salvar formulário: {e}")
        return False

def exibir_rodape():
    """Rodapé com detecção de scroll."""
    detectar_fim_da_pagina()
    st.markdown("<hr style='border: 0.5px solid rgba(255, 255, 255, 0.1); margin-top: 50px;'><div style='text-align:center; color:gray; font-size: 0.8rem; padding-bottom: 20px;'>SKY DATA SOLUTION © 2026 | Rodrigo Aiosa</div>", unsafe_allow_html=True)
