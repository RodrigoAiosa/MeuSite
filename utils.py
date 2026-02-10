import streamlit as st
import gspread
import uuid
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone

# --- CONFIGURAÇÃO DE SESSÃO ---
# Inicializa variáveis para controle de tempo e ID de sessão
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())[:8]
if "entrada_pagina" not in st.session_state:
    st.session_state["entrada_pagina"] = datetime.now(timezone(timedelta(hours=-3)))
if "ultima_linha_acesso" not in st.session_state:
    st.session_state["ultima_linha_acesso"] = None

def obter_credenciais():
    """Conecta ao Google usando Secrets do Streamlit."""
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
    """Registra acessos a partir da linha 2 e calcula a duração da permanência."""
    try:
        creds = obter_credenciais()
        if not creds: return
        client = gspread.authorize(creds)
        
        # ID da planilha Relatorio_Acessos_Site
        id_planilha_acessos = "1TCx1sTDaPsygvh-FvzalJ3JlBKJBOTbfoD-7CZmhCVI"
        sheet = client.open_by_key(id_planilha_acessos).sheet1
        
        fuso = timezone(timedelta(hours=-3))
        agora = datetime.now(fuso)
        agora_str = agora.strftime("%d/%m/%Y %H:%M:%S")
        
        # 1. ATUALIZAR DURAÇÃO DA PÁGINA ANTERIOR
        if st.session_state["ultima_linha_acesso"]:
            delta = agora - st.session_state["entrada_pagina"]
            minutos, segundos = divmod(int(delta.total_seconds()), 60)
            duracao_str = f"{minutos:02d}:{segundos:02d}"
            
            # Atualiza a coluna J (índice 10) da linha anterior
            try:
                sheet.update_cell(st.session_state["ultima_linha_acesso"], 10, duracao_str)
            except:
                pass

        # 2. INSERIR NOVA LINHA (Sempre abaixo dos títulos)
        ua = st.context.headers.get("User-Agent", "").lower()
        dispositivo = "Celular" if "mobile" in ua else "PC"
        
        # Dados conforme a estrutura: data_hora, session_id, dispositivo, sistema_operacional, 
        # navegador, ip, origem, pagina, acao, duracao
        nova_linha = [
            agora_str, 
            st.session_state["session_id"], 
            dispositivo, 
            "Ativo", 
            "Navegador", 
            "Remote", 
            "Direto", 
            nome_pagina, 
            acao, 
            "00:00" # Duração inicial para a nova página
        ]
        
        # O gspread.append_row insere os dados preservando o cabeçalho da linha 1
        sheet.append_row(nova_linha)
        
        # 3. ATUALIZAR ESTADO PARA O PRÓXIMO REGISTRO
        # Define qual linha foi acabada de criar para que possamos atualizar a duração depois
        registros = sheet.get_all_values()
        st.session_state["ultima_linha_acesso"] = len(registros)
        st.session_state["entrada_pagina"] = agora
        
    except Exception:
        pass

def exibir_rodape():
    st.markdown("<hr style='border: 0.5px solid rgba(255, 255, 255, 0.1); margin-top: 50px;'><div style='text-align:center; color:gray; font-size: 0.8rem; padding-bottom: 20px;'>SKY DATA SOLUTION © 2026 | Rodrigo Aiosa</div>", unsafe_allow_html=True)
