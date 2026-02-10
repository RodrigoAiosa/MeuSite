import streamlit as st
import re
from datetime import datetime
from utils import exibir_rodape, registrar_acesso, salvar_formulario_contato

# --- REGISTRO DE ACESSO ---
# Esta função usa o e-mail ativo aiosaprojeto para registrar sua visita sem apagar nada
registrar_acesso("Página de Contato")

def validar_email(email):
    # Regex corrigida para aceitar domínios modernos
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,4}$'
    return re.search(regex, email)

def main():
    # --- CONFIGURAÇÃO DE DESIGN ---
    st.markdown("""
        <style>
        .stForm {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 30px !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("🚀 Vamos escalar seu projeto?")
    
    with st.form("form_contato", clear_on_submit=True):
        nome = st.text_input("👤 Nome Completo")
        email = st.text_input("📧 E-mail Profissional")
        whatsapp = st.text_input("📱 WhatsApp (11 números)")
        mensagem = st.text_area("💬 Como posso te ajudar?", height=150)
        
        enviar = st.form_submit_button("Enviar Mensagem Agora")

        if enviar:
            # Validação robusta de campos
            if len(nome.strip()) < 10:
                st.error("Por favor, insira o nome completo (mínimo 10 caracteres).")
            elif not validar_email(email.lower()):
                st.error("O formato do e-mail é inválido.")
            elif not (whatsapp.isdigit() and len(whatsapp) == 11):
                st.error("O WhatsApp deve conter exatamente 11 números (DDD + número).")
            elif not mensagem.strip():
                st.error("A mensagem não pode estar vazia.")
            else:
                with st.spinner("Conectando ao Google Sheets..."):
                    # AJUSTE: Lista formatada para bater com as colunas da sua planilha
                    dados_lista = [
                        datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 
                        nome, 
                        email, 
                        whatsapp, 
                        mensagem
                    ]
                    
                    # Chamada única para evitar o erro de TypeError
                    sucesso = salvar_formulario_contato(dados_lista)
                    
                    if sucesso:
                        st.balloons()
                        st.success("Mensagem enviada com sucesso! Entrarei em contato em breve.")
                    else:
                        # Se falhar, é sinal que a conta aiosaprojeto precisa do JSON atualizado
                        st.error("Falha técnica no envio. Por favor, tente novamente em instantes.")

if __name__ == "__main__":
    main()

# Exibe o rodapé da SKY DATA SOLUTION
exibir_rodape()
