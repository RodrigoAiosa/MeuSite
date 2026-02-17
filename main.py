import streamlit as st
# Importando as funções do utils.py que está na raiz
try:
    from utils import registrar_acesso_db, exibir_rodape, inicializar_estado
except ImportError:
    st.error("Erro: Arquivo utils.py não encontrado na raiz.")

# 1. INICIALIZAÇÃO DO ESTADO
inicializar_estado()

# 2. CONFIGURAÇÃO DE NAVEGAÇÃO (Apenas com o que existe)
# Removi as páginas que não estão na sua pasta para parar o erro
pages = [
    st.Page("Views/sobre.py", title="Sobre Mim", icon="👤", default=True)
]

# 3. EXECUÇÃO
pg = st.navigation(pages)
pg.run()
