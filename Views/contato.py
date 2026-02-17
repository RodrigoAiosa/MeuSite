import streamlit as st
import psycopg2
import re

# Configuração da página idêntica à sua estrutura atual
st.set_page_config(page_title="Formulário de Contato", page_icon="📩")

def get_connection():
    # Conecta usando os Secrets do Streamlit Cloud
    return psycopg2.connect(
        host=st.secrets["DB_HOST"],
        port=st.secrets["DB_PORT"],
        database=st.secrets["DB_NAME"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASS"],
        sslmode="require"
    )

def validar_whatsapp(numero):
    # Mantém apenas números e valida 11 dígitos
    apenas_numeros = re.sub(r'\D', '', numero)
    return len(apenas_numeros) == 11

# Título e Subtítulo estilizados (conforme imagem_233300.png)
st.markdown("<h1 style='text-align: center; color: #00b4d8;'>🚀 Vamos escalar seu projeto?</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Preencha os campos abaixo para registrar sua solicitação em nossa base de dados.</p>", unsafe_allow_html=True)

# Formulário de Cadastro
with st.form("contato_form", clear_on_submit=True):
    nome = st.text_input("👤 Nome Completo", placeholder="Digite seu nome aqui...")
    email = st.text_input("📧 E-mail Profissional", placeholder="exemplo@email.com")
    whatsapp = st.text_input("📱 WhatsApp", placeholder="11999999999", max_chars=11)
    mensagem = st.text_area("💬 Sua Mensagem", placeholder="Como podemos ajudar?")
    
    submit_button = st.form_submit_button("Enviar Mensagem")

    if submit_button:
        if not nome or not email or not whatsapp or not mensagem:
            st.error("⚠️ Por favor, preencha todos os campos.")
        elif not validar_whatsapp(whatsapp):
            st.error("⚠️ O WhatsApp deve conter exatamente 11 números.")
        else:
            try:
                with st.spinner("Conectando ao banco Aiven..."):
                    conn = get_connection()
                    cur = conn.cursor()
                    
                    # CORREÇÃO: Nome da tabela exatamente como aparece no seu terminal (MAIÚSCULO)
                    query = """
                        INSERT INTO "CONTATO_SITE" (nome_completo, email, whatsapp, mensagem)
                        VALUES (%s, %s, %s, %s)
                    """
                    cur.execute(query, (nome, email, whatsapp, mensagem))
                    
                    conn.commit()
                    cur.close()
                    conn.close()
                    
                    st.success("✅ Mensagem enviada com sucesso!")
                    st.balloons()
                
            except Exception as e:
                st.error(f"❌ Erro ao salvar: {e}")

# Rodapé (conforme imagem_239c7f.png)
st.markdown("---")
st.caption("SKY DATA SOLUTION © 2026 | Rodrigo Aiosa")
