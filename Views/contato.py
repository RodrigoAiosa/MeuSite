import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def salvar_contato(dados):
    # Configuração de escopo e credenciais usando seu arquivo existente
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("meuprojetocadsite-5ecb421b15a7.json", scope)
    client = gspread.authorize(creds)
    
    # URL da sua planilha
    url = "https://docs.google.com/spreadsheets/d/1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU/edit#gid=0"
    sheet = client.open_by_url(url).sheet1
    
    # Adiciona a nova linha (Preservando os dados anteriores)
    sheet.append_row(dados)

def main():
    st.title("📬 Entre em Contato")
    st.write("Preencha o formulário abaixo para enviar sua mensagem.")

    with st.form(key="form_contato", clear_on_submit=True):
        nome = st.text_input("Nome Completo")
        email = st.text_input("E-mail")
        whatsapp = st.text_input("WhatsApp (com DDD)")
        mensagem = st.text_area("Sua Mensagem")
        
        botao_enviar = st.form_submit_button("Enviar Mensagem")

    if botao_enviar:
        if nome and email and mensagem:
            try:
                # Captura data e hora atual no formato brasileiro
                data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                
                # Prepara a lista com as colunas solicitadas
                lista_dados = [data_hora, nome, email, whatsapp, mensagem]
                
                salvar_contato(lista_dados)
                st.success("✅ Mensagem enviada com sucesso!")
            except Exception as e:
                st.error(f"Erro ao conectar com a planilha: {e}")
        else:
            st.warning("Por favor, preencha todos os campos obrigatórios (Nome, E-mail e Mensagem).")

    # Rodapé padrão Rodrigo AIOSA
    st.markdown("---")
    footer_html = """
    <div style='text-align: center; color: gray;'>
        <p style='margin-bottom: 5px;'>Desenvolvido por <b>Rodrigo AIOSA</b></p>
        <div style='display: flex; justify-content: center; gap: 20px; font-size: 24px;'>
            <a href='https://wa.me/5511977019335' target='_blank' style='text-decoration: none;'>
                <img src='https://cdn-icons-png.flaticon.com/512/733/733585.png' width='25' height='25'>
            </a>
            <a href='https://www.linkedin.com/in/rodrigoaiosa/' target='_blank' style='text-decoration: none;'>
                <img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' width='25' height='25'>
            </a>
        </div>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()