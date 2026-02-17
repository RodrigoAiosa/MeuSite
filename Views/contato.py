import streamlit as st
import psycopg2
import re

# Configuração da página
st.set_page_config(page_title="Formulário de Contato", page_icon="📩")

# Função de Conexão (Utilizando os Secrets configurados no Streamlit Cloud)
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
    # Remove caracteres não numéricos e valida os 11 dígitos
    apenas_numeros = re.sub(r'\D', '', numero)
    return len(apenas_numeros) == 11

# Título e Instruções
st.markdown("<h1 style='text-align: center; color: #00b4d8;'>🚀 Vamos escalar seu projeto?</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Preencha os campos abaixo para registrar sua solicitação em nossa base de dados.</p>", unsafe_allow_html=True)

# Formulário de Cadastro
with st.form("contato_form", clear_on_submit=True):
    nome = st.text_input("👤 Nome Completo", placeholder="Digite seu nome aqui...")
    email = st.text_input("📧 E-mail Profissional", placeholder="exemplo@email.com")
    whatsapp = st.text_input("📱 WhatsApp", placeholder="11999999999", max_chars=11, help="Digite apenas os 11 números (DDD + número)")
    mensagem = st.text_area("💬 Sua Mensagem", placeholder="Como podemos ajudar?")
    
    submit_button = st.form_submit_button("Enviar Mensagem")

    if submit_button:
        # Validações de campos obrigatórios
        if not nome or not email or not whatsapp or not mensagem:
            st.error("⚠️ Por favor, preencha todos os campos.")
        elif not validar_whatsapp(whatsapp):
            st.error("⚠️ O WhatsApp deve conter exatamente 11 números (ex: 11977019335).")
        else:
            try:
                with st.spinner("Salvando dados no banco Aiven..."):
                    conn = get_connection()
                    cur = conn.cursor()
                    
                    # SQL de Inserção na tabela contato_site
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

# Rodapé simples
st.markdown("---")
st.caption("SKY DATA SOLUTION © 2026 | Rodrigo Aiosa")
