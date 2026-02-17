import streamlit as st
import pandas as pd
# Importando as funções atualizadas do arquivo utils.py na raiz
try:
    from utils import registrar_acesso_db, exibir_rodape, inicializar_estado
except ImportError:
    st.error("Erro: Arquivo utils.py não encontrado ou funções renomeadas.")

# 1. INICIALIZAÇÃO DO ESTADO DA SESSÃO
# Garante que o session_id e o horário de entrada sejam criados antes de tudo
inicializar_estado()

# 2. CONFIGURAÇÃO DAS PÁGINAS (NAVEGAÇÃO)
# Ajuste os caminhos conforme a sua estrutura de pastas no GitHub
pages = {
    "Apresentação": [
        st.Page("Views/sobre.py", title="Sobre Mim", icon="👤", default=True),
    ],
    "Projetos": [
        st.Page("Views/dashboard_vendas.py", title="Dashboard de Vendas", icon="📊"),
        st.Page("Views/analise_dados.py", title="Análise de Dados", icon="📈"),
    ],
    "Contato": [
        st.Page("Views/contato.py", title="Fale Comigo", icon="📞"),
    ]
}

# 3. GERENCIAMENTO DE NAVEGAÇÃO
pg = st.navigation(pages)

# 4. EXECUÇÃO DA PÁGINA SELECIONADA
# O registro de acesso agora é feito dentro de cada página individual (como no seu sobre.py)
# para que possamos identificar qual página o usuário está visitando.
pg.run()
