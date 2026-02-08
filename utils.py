import streamlit as st

def exibir_rodape():
    """Função para centralizar e exibir o rodapé em todas as páginas."""
    st.markdown(
        "<p style='text-align: center; color: #6b7280; font-size: 1.1rem;'>Rodrigo Aiosa © 2026 | Especialista em BI & Treinamentos</p>",
        unsafe_allow_html=True
    )
    
    footer_html = """
    <div style='text-align: center; color: gray;'>
        <p style='margin-bottom: 5px;'>Desenvolvido por <b>Rodrigo AIOSA</b></p>
        <div style='display: flex; justify-content: center; gap: 20px; font-size: 24px;'>
            <a href='https://wa.me/5511977019335' target='_blank'>
                <img src='https://cdn-icons-png.flaticon.com/512/733/733585.png' width='25' height='25'>
            </a>
            <a href='https://www.linkedin.com/in/rodrigoaiosa/' target='_blank'>
                <img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' width='25' height='25'>
            </a>
        </div>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)