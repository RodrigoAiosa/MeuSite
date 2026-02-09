import streamlit as st
import gspread
import re
from datetime import datetime
from utils import exibir_rodape, registrar_acesso, obter_credenciais

# Registra que o usuário entrou na página
registrar_acesso("Página de Contato")

def salvar_contato(dados):
    """Salva os dados preservando o histórico da planilha."""
    try:
        creds = obter_credenciais()
        client = gspread.authorize(creds)
        
        # Link DIRETO para evitar qualquer erro de busca por nome
        url_planilha = "https://docs.google.com/spreadsheets/d/1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU/edit#gid=0"
        sheet = client.open_by_url(url_planilha).sheet1
        
        # O comando append_row adiciona ao final sem apagar nada
        sheet.append_row(dados)
    except Exception as e:
        # Repassa o erro detalhado para o Streamlit mostrar na tela se falhar
        raise Exception(f"Erro na API do Google: {str(e)}")

def validar_email(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.match(regex, email)

def main():
    st.markdown("<h1 style='text-align: center; color: #00b4d8;'>🚀 Vamos escalar seu projeto?</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>Entrarei em contato em até 24h.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        with st.form(key="form_contato_final", clear_on_submit=True):
            nome = st.text_input("👤 Nome Completo", placeholder="Seu nome aqui")
            
            f_col1, f_col2 = st.columns(2)
            with f_col1:
                email = st.text_input("📧 E-mail Profissional")
            with f_col2:
                whatsapp = st.text_input("📱 WhatsApp (DDD + Número)")
            
            mensagem = st.text_area("💬 Como posso te ajudar?", height=120)
            
            botao_enviar = st.form_submit_button("Enviar Mensagem Agora")

        if botao_enviar:
            if not nome or not email or not whatsapp or not mensagem:
                st.error("❌ Por favor, preencha todos os campos do formulário.")
            elif not validar_email(email.lower()):
                st.error("❌ O e-mail informado parece inválido.")
            else:
                try:
                    with st.spinner("Conectando ao servidor..."):
                        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        lista_para_salvar = [data_hora, nome, email, whatsapp, mensagem]
                        
                        salvar_contato(lista_para_salvar)
                        
                        st.balloons()
                        st.success("✅ Sucesso! Seus dados foram salvos na nossa base.")
                except Exception as e:
                    st.error(f"Erro ao enviar: {e}")

if __name__ == "__main__":
    main()

exibir_rodape()
