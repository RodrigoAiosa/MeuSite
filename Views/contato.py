import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import re  # Importando para usar Regex

def salvar_contato(dados):
    # Configuração de escopo e credenciais
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("meuprojetocadsite-5ecb421b15a7.json", scope)
    client = gspread.authorize(creds)
    
    # URL da sua planilha
    url = "https://docs.google.com/spreadsheets/d/1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU/edit#gid=0"
    sheet = client.open_by_url(url).sheet1
    
    # Adiciona a nova linha (Preservando os dados anteriores como solicitado)
    sheet.append_row(dados)

def validar_email(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email)

def main():
    st.title("📬 Entre em Contato")
    st.write("Preencha o formulário abaixo para enviar sua mensagem.")

    with st.form(key="form_contato", clear_on_submit=True):
        nome = st.text_input("Nome Completo")
        email = st.text_input("E-mail")
        whatsapp = st.text_input("WhatsApp (Somente 11 números com DD)")
        mensagem = st.text_area("Sua Mensagem")
        
        botao_enviar = st.form_submit_button("Enviar Mensagem")

    if botao_enviar:
        # 1. Validação de Nome (Mínimo 10 caracteres)
        if len(nome.strip()) < 10:
            st.error("❌ O nome deve ter no mínimo 10 caracteres.")
        
        # 2. Validação de E-mail
        elif not validar_email(email):
            st.error("❌ Por favor, insira um e-mail válido.")
        
        # 3. Validação de WhatsApp (Somente números e exatamente 11 caracteres)
        # O regex \D remove tudo que não for número para teste, ou verificamos se é numérico
        elif not (whatsapp.isdigit() and len(whatsapp) == 11):
            st.error("❌ O WhatsApp deve conter apenas números e ter exatamente 11 dígitos (DDD + Número).")
            
        # 4. Verificação de Mensagem
        elif not mensagem:
            st.error("❌ Por favor, escreva sua mensagem.")
            
        else:
            try:
                # Captura data e hora atual no formato brasileiro
                data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                
                # Prepara a lista com as colunas (Preservando a ordem da sua planilha)
                lista_dados = [data_hora, nome, email, whatsapp, mensagem]
                
                salvar_contato(lista_dados)
                st.success("✅ Mensagem enviada com sucesso!")
            except Exception as e:
                st.error(f"Erro ao conectar com a planilha: {e}")

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