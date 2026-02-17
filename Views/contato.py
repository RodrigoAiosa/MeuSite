import streamlit as st
import psycopg2
import re

# Configuração da página
st.set_page_config(page_title="Formulário de Contato", page_icon="📩")

# Função de Conexão (Usando os Secrets que você já configurou no Streamlit.io)
def get_connection():
    return psycopg2.connect(
        host=st.secrets["DB_HOST"],
        port=st.secrets["DB_PORT"],
        database=st.secrets["DB_NAME"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASS"],
        sslmode="require"
    )

def validar_whatsapp(numero):
    # Remove tudo que não for número e verifica se tem 11 dígitos
    apenas_numeros = re.sub(r'\D', '', numero)
    return len(apenas_numeros) == 11

st.title("📩 Fale Conosco")
st.markdown("Preencha os campos abaixo e entraremos em contato em breve.")

# Formulário de Cadastro
with st.form("contato_form", clear_on_submit=True):
    nome = st.text_input("Nome Completo", placeholder="Digite seu nome aqui...")
    email = st.text_input("E-mail", placeholder="exemplo@email.com")
    whatsapp = st.text_input("WhatsApp", placeholder="11999999999", max_chars=11, help="Digite apenas os 11 números (DDD + número)")
    mensagem = st.text_area("Sua Mensagem", placeholder="Como podemos ajudar?")
    
    submit_button = st.form_submit_button("Enviar Mensagem")

    if submit_button:
        # Validações básicas
        if not nome or not email or not whatsapp or not mensagem:
            st.error("⚠️ Por favor, preencha todos os campos.")
        elif not validar_whatsapp(whatsapp):
            st.error("⚠️ O WhatsApp deve conter exatamente 11 números (ex: 11977019335).")
        else:
            try:
                conn = get_connection()
                cur = conn.cursor()
                
                # SQL de Inserção (id_contato é automático via SERIAL)
                query = """
                    INSERT INTO contato_site (nome_completo, email, whatsapp, mensagem)
                    VALUES (%s, %s, %s, %s)
                """
                cur.execute(query, (nome, email, whatsapp, mensagem))
                
                conn.commit()
                cur.close()
                conn.close()
                
                st.success("✅ Mensagem enviada com sucesso! Logo entraremos em contato.")
                st.balloons()
                
            except Exception as e:
                st.error(f"❌ Ocorreu um erro ao salvar: {e}")

# Rodapé personalizado com seu contato
st.markdown("---")
st.caption("SkyData Solutions - Todos os direitos reservados.")
