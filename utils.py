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

        # 2. INSERIR NOVA LINHA (Garantindo início na linha 2 da Coluna A)
        ua = st.context.headers.get("User-Agent", "").lower()
        dispositivo = "Celular" if "mobile" in ua else "PC"
        
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
        
        # Evita pular linhas: busca o fim real dos dados na Coluna A
        valores_coluna_a = sheet.col_values(1)
        proxima_linha = len(valores_coluna_a) + 1
        if proxima_linha < 2: proxima_linha = 2
            
        sheet.insert_row(nova_linha, proxima_linha)
        
        # 3. ATUALIZAR ESTADOS DE SESSÃO
        st.session_state["ultima_linha_acesso"] = proxima_linha
        st.session_state["entrada_pagina"] = agora
        st.session_state["leu_ate_o_fim"] = False # Reseta para a nova página
        
    except Exception:
        pass

def detectar_fim_da_pagina():
    """Injeta JavaScript para monitorar o scroll e atualizar a coluna 'acao'."""
    js_code = """
    <script>
    const monitorarScroll = () => {
        const alturaJanela = window.innerHeight;
        const alturaDocumento = document.documentElement.scrollHeight;
        const posicaoScroll = window.pageYOffset || document.documentElement.scrollTop;
        
        // Gatilho: 95% da página percorrida
        if ((alturaJanela + posicaoScroll) >= (alturaDocumento - 100)) {
            window.parent.postMessage({type: 'streamlit:setComponentValue', value: true}, '*');
        }
    }
    window.parent.document.addEventListener('scroll', monitorarScroll);
    </script>
    """
    # Componente oculto para detectar o sinal do JS
    chegou_ao_fim = components.html(js_code, height=0, width=0)
    
    if chegou_ao_fim and not st.session_state.get("leu_ate_o_fim"):
        try:
            creds = obter_credenciais()
            client = gspread.authorize(creds)
            id_planilha_acessos = "1TCx1sTDaPsygvh-FvzalJ3JlBKJBOTbfoD-7CZmhCVI"
            sheet = client.open_by_key(id_planilha_acessos).sheet1
            
            # Atualiza coluna I (9) da linha de acesso atual
            sheet.update_cell(st.session_state["ultima_linha_acesso"], 9, "Leu até o fim")
            st.session_state["leu_ate_o_fim"] = True
        except:
            pass

def salvar_formulario_contato(dados):
    """Salva os dados do formulário na planilha de contatos sem apagar os existentes."""
    try:
        creds = obter_credenciais()
        if not creds: return False
        client = gspread.authorize(creds)
        
        # ID da planilha de CONTATOS (Formulário)
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
    """Exibe o rodapé e chama a detecção de scroll."""
    detectar_fim_da_pagina()
    st.markdown("<hr style='border: 0.5px solid rgba(255, 255, 255, 0.1); margin-top: 50px;'><div style='text-align:center; color:gray; font-size: 0.8rem; padding-bottom: 20px;'>SKY DATA SOLUTION © 2026 | Rodrigo Aiosa</div>", unsafe_allow_html=True)
