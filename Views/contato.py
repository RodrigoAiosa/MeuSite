import streamlit as st
import gspread
from datetime import datetime
from utils import exibir_rodape, registrar_acesso, obter_credenciais

# Registro obrigatório de acesso
registrar_acesso("Página de Contato")

def main():
    st.markdown("<h1 style='text-align: center; color: #00b4d8;'>🚀 Vamos escalar seu projeto?</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form(key="contato_final", clear_on_submit=True):
            nome = st.text_input("👤 Nome Completo")
            email = st.text_input("📧 E-mail Profissional")
            whatsapp = st.text_input("📱 WhatsApp (DDD + Número)")
            mensagem = st.text_area("💬 Como posso te ajudar?")
            enviar = st.form_submit_button("Enviar Mensagem Agora")

        if enviar:
            if not nome or not email or not whatsapp or not mensagem:
                st.error("❌ Preencha todos os campos!")
            else:
                try:
                    with st.spinner("Gravando dados com segurança..."):
                        creds = obter_credenciais()
                        client = gspread.authorize(creds)
                        
                        # Usando o ID fixo da planilha para evitar falhas de permissão
                        url_id = "1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU"
                        sheet = client.open_by_key(url_id).sheet1
                        
                        # Adiciona nova linha preservando o histórico
                        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        sheet.append_row([data_hora, nome, email, whatsapp, mensagem])
                        
                        st.balloons()
                        st.success("✅ Sucesso! Dados gravados na planilha.")
                except Exception as e:
                    st.error(f"Erro Crítico: {e}")

if __name__ == "__main__":
    main()

exibir_rodape()
