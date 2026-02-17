import streamlit as st
import gspread
import uuid
import psycopg2
import streamlit.components.v1 as components
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone

# --- INICIALIZAÇÃO SEGURA ---
def inicializar_estado():
    if "session_id" not in st.session_state:
        st.session_state["session_id"] = str(uuid.uuid4())[:8]
    if "entrada_pagina" not in st.session_state:
        st.session_state["entrada_pagina"] = datetime.now(timezone(timedelta(hours=-3)))
    if "ultima_linha_acesso" not in st.session_state:
        st.session_state["ultima_linha_acesso"] = None
    if "leu_ate_o_fim" not in st.session_state:
        st.session_state["leu_ate_o_fim"] = False

# Chamamos a inicialização imediatamente
inicializar_estado()

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

def calcular_duracao_texto():
    """Calcula o tempo decorrido desde a entrada em formato MM:SS."""
    agora = datetime.now(timezone(timedelta(hours=-3)))
    delta = agora - st.session_state["entrada_pagina"]
    segundos_totais = int(delta.total_seconds())
    minutos = segundos_totais // 60
    segundos = segundos_totais % 60
    return f"{minutos:02d}:{segundos:02d}"

def registrar_acesso(nome_pagina, acao="Visualização"):
    """Registra o acesso no Google Sheets e no Banco de Dados PostgreSQL."""
    try:
        inicializar_estado()
        
        # Coleta de metadados comum
        headers = st.context.headers
        ua = headers.get("User-Agent", "").lower()
        ip = headers.get("X-Forwarded-For", "Privado").split(",")[0]
        dispositivo = "iPhone" if "iphone" in ua else "Android" if "android" in ua else "PC"
        agora = st.session_state["entrada_pagina"]
        agora_str = agora.strftime("%d/%m/%Y %H:%M:%S")
        sid = st.session_state["session_id"]

        # --- 1. REGISTRO NO GOOGLE SHEETS ---
        if st.session_state["ultima_linha_acesso"] is None:
            try:
                creds = obter_credenciais()
                if creds:
                    client = gspread.authorize(creds)
                    sheet = client.open_by_key("1TCx1sTDaPsygvh-FvzalJ3JlBKJBOTbfoD-7CZmhCVI").sheet1
                    
                    nova_linha = [
                        agora_str, sid, dispositivo, "SO", "Navegador", 
                        ip, "Direto", nome_pagina, acao, "00:00"
                    ]
                    sheet.append_row(nova_linha)
                    st.session_state["ultima_linha_acesso"] = len(sheet.col_values(1))
            except Exception as e_gs:
                print(f"Erro Google Sheets: {e_gs}")

        # --- 2. REGISTRO NO POSTGRESQL (AIVEN) ---
        registrar_acesso_db(agora, sid, dispositivo, ip, nome_pagina, acao)

    except Exception as e:
        print(f"Erro geral no registro: {e}")

def registrar_acesso_db(data_hora, session_id, dispositivo, ip, pagina, acao):
    """Função interna para conexão e insert no BD PostgreSQL."""
    try:
        # Usando os dados da sua imagem do console Aiven
        conn = psycopg2.connect(
            host="pg-2e2874e2-rodrigoaiosa-skydatasoluction.l.aivencloud.com",
            database="defaultdb",
            user="avnadmin",
            password=st.secrets.get("DB_PASSWORD", "AVNS_LlZukuJoh_0Kbj0dhvK"),
            port="13191",
            sslmode="require"
        )
        cur = conn.cursor()

        query = """
            INSERT INTO controle_acesso_site 
            (data_hora, session_id, dispositivo, ip, pagina, acao) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (data_hora, session_id, dispositivo, ip, pagina, acao))
        
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Erro ao salvar no PostgreSQL: {e}")

def atualizar_duracao_na_planilha():
    """Atualiza a célula de duração da linha atual no Sheets."""
    linha = st.session_state.get("ultima_linha_acesso")
    if linha:
        try:
            creds = obter_credenciais()
            client = gspread.authorize(creds)
            sheet = client.open_by_key("1TCx1sTDaPsygvh-FvzalJ3JlBKJBOTbfoD-7CZmhCVI").sheet1
            tempo_duracao = calcular_duracao_texto()
            sheet.update_cell(linha, 10, tempo_duracao)
        except:
            pass

def exibir_rodape():
    atualizar_duracao_na_planilha()
    st.markdown("<hr style='border: 0.5px solid rgba(255, 255, 255, 0.1); margin-top: 50px;'><div style='text-align:center; color:gray; font-size: 0.8rem; padding-bottom: 20px;'>SKY DATA SOLUTION © 2026 | Rodrigo Aiosa</div>", unsafe_allow_html=True)

def salvar_formulario_contato(dados):
    try:
        atualizar_duracao_na_planilha()
        creds = obter_credenciais()
        sheet = gspread.authorize(creds).open_by_key("1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU").sheet1
        sheet.append_row(dados)
        
        # Opcional: Criar mensagem personalizada para WhatsApp
        msg = f"Olá Rodrigo! Recebi um novo contato de {dados[0]} através do formulário."
        # Link gerado dinamicamente: https://wa.me/11977019335?text=...
        
        return True
    except: return False
