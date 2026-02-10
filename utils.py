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
    except:
        try:
            return Credentials.from_service_account_file("meuprojetocadsite-5ecb421b15a7.json", scopes=scope)
        except:
            return None

def calcular_duracao():
    """Calcula a diferença entre agora e o início da sessão."""
    agora = datetime.now(timezone(timedelta(hours=-3)))
    duracao = agora - st.session_state["entrada_pagina"]
    # Retorna formato MM:SS
    minutos, segundos = divmod(int(duracao.total_seconds()), 60)
    return f"{minutos:02d}:{segundos:02d}"

def registrar_acesso(nome_pagina, acao="Visualização"):
    """Registra o acesso inicial e salva a linha para atualizações futuras."""
    try:
        creds = obter_credenciais()
        if not creds: return "---"
        
        client = gspread.authorize(creds)
        sheet = client.open_by_key("1TCx1sTDaPsygvh-FvzalJ3JlBKJBOTbfoD-7CZmhCVI").sheet1
        
        # Obter a próxima linha vazia
        total_atual = len(sheet.col_values(1))
        proxima_linha = total_atual + 1
        
        fuso = timezone(timedelta(hours=-3))
        agora = datetime.now(fuso)
        agora_str = agora.strftime("%d/%m/%Y %H:%M:%S")
        
        # Captura de Dispositivo
        headers = st.context.headers
        ua = headers.get("User-Agent", "").lower()
        ip = headers.get("X-Forwarded-For", "Privado").split(",")[0]
        
        dispositivo = "PC"
        if "iphone" in ua: dispositivo = "iPhone"
        elif "android" in ua: dispositivo = "Android"

        # Coluna J (10) é a Duração
        duracao_atual = calcular_duracao()

        nova_linha = [
            agora_str, 
            st.session_state["session_id"], 
            dispositivo, 
            "SO", "Navegador", ip, "Direto", 
            nome_pagina, 
            acao, 
            duracao_atual
        ]
        
        sheet.insert_row(nova_linha, proxima_linha)
        st.session_state["ultima_linha_acesso"] = proxima_linha
        
        return proxima_linha
    except Exception as e:
        return "---"

def atualizar_duracao_final():
    """
    Atualiza a célula de duração na planilha de acessos antes do script encerrar
    ou quando o usuário interage com algo.
    """
    if st.session_state["ultima_linha_acesso"]:
        try:
            creds = obter_credenciais()
            client = gspread.authorize(creds)
            sheet = client.open_by_key("1TCx1sTDaPsygvh-FvzalJ3JlBKJBOTbfoD-7CZmhCVI").sheet1
            
            nova_duracao = calcular_duracao()
            # Coluna 10 é a coluna J (Duração)
            sheet.update_cell(st.session_state["ultima_linha_acesso"], 10, nova_duracao)
        except:
            pass

def detectar_fim_da_pagina():
    # Componente JS para detectar scroll e avisar o Streamlit
    js_code = """
    <script>
    window.onscroll = function(ev) {
        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
            window.parent.postMessage({type: 'streamlit:setComponentValue', value: true}, '*');
        }
    };
    </script>
    """
    components.html(js_code, height=0)

def salvar_formulario_contato(dados):
    try:
        # Ao salvar contato, aproveitamos para atualizar a duração do acesso na outra planilha
        atualizar_duracao_final()
        
        creds = obter_credenciais()
        sheet = gspread.authorize(creds).open_by_key("1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU").sheet1
        proxima = len(list(filter(None, sheet.col_values(1)))) + 1
        sheet.insert_row(dados, max(2, proxima))
        return True
    except: return False

def exibir_rodape():
    # Sempre que o rodapé é renderizado, tentamos atualizar a duração do acesso
    atualizar_duracao_final()
    st.markdown("<hr style='border: 0.5px solid rgba(255, 255, 255, 0.1); margin-top: 50px;'><div style='text-align:center; color:gray; font-size: 0.8rem; padding-bottom: 20px;'>SKY DATA SOLUTION © 2026 | Rodrigo Aiosa</div>", unsafe_allow_html=True)
