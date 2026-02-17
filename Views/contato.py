import streamlit as st
import psycopg2
import re
from utils import exibir_rodape, salvar_formulario_contato, registrar_acesso

# Registro de acesso para controle interno
registrar_acesso("Contato")

# Configuração da página
st.set_page_config(page_title="Formulário de Contato", page_icon="📩")

def validar_whatsapp(numero):
    # Remove tudo que não for número e verifica se tem 11 dígitos
    apenas_numeros = re.sub(r'\D', '', numero)
    return len(apenas_numeros) == 11

def main():
    st.markdown("<h1 style='text-align: center; color: #00b4d8;'>🚀 Vamos escalar seu projeto?</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Preencha os campos abaixo para registrar sua solicitação em nossa base de dados.</p>", unsafe_allow_html=True)

    # Formulário de Cadastro integrado ao CRUD Aiven
    with st.form("contato_form", clear_on_submit=True):
        nome = st.text_input("👤 Nome Completo", placeholder="Digite seu nome aqui...")
        email = st.text_input("📧 E-mail Profissional", placeholder="exemplo@email.com")
        whatsapp = st.text_input("📱 WhatsApp", placeholder="11999999999", max_chars=11, help="Digite apenas os 11 números (DDD + número)")
        mensagem = st.text_area("💬 Sua Mensagem", placeholder="Como podemos ajudar?")
        
        submit_button = st.form_submit_button("Enviar Mensagem")

        if submit_button:
            # Validações básicas
            if not nome or not email or not whatsapp or not mensagem:
                st.error("⚠️ Por favor, preencha todos os campos.")
            elif not validar_whatsapp(whatsapp):
                st.error("⚠️ O WhatsApp deve conter exatamente 11 números (ex: 11977019335).")
            else:
                with st.spinner("Salvando dados no banco de dados..."):
                    # Organização dos dados para a função do banco
                    # Note: Ajustado para o formato que sua função 'salvar_formulario_contato' espera
                    dados_lista = [nome, email, whatsapp, mensagem]
                    
                    # Executa a gravação preservando os dados existentes
                    sucesso = salvar_formulario_contato(dados_lista)
                    
                    if sucesso:
                        st.success("✅ Mensagem enviada com sucesso! Logo entraremos em contato.")
                        st.balloons()
                    else:
                        st.error("❌ Ocorreu um erro ao salvar os dados. Verifique a conexão com o banco Aiven.")

if __name__ == "__main__":
    main()

# Exibe o rodapé padrão via utils
exibir_rodape()
