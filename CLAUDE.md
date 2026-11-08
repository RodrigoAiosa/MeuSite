# Instruções do Projeto - MeuSite

## Escopo

- Só fazer mudanças no site da Vercel (`index.html`, `assets/`, `data/`).
  Não alterar a versão Streamlit (`main.py`, `Views/`).
- Pull requests: sempre mesclar automaticamente e, depois da mesclagem,
  confirmar que a Vercel publicou o deploy de produção (projeto `rodrigoaiosa`).

## Novo case de sucesso

Sempre que for pedido um novo case, fazer as três etapas:

1. **Imagem**: infográfico 1460×973 no padrão dos cases existentes
   (paleta de cores do site do cliente, nome do cliente no topo e no rodapé,
   pelo menos 10 processos). Entregar PNG em alta resolução e JPG 1460×973.
2. **Site**: salvar o JPG em `assets/img_cases_suceso/<próximo número>.jpg`
   e incluir na lista `CASES` do `index.html` (`{ f, t: cliente, s: setor }`).
   Depois rodar `python ocr_cases.py` para atualizar `data/cases_texto.json`,
   que alimenta a pesquisa por texto da seção Cases de Sucesso.
3. **Currículo**: atualizar `_Rodrigo_Aiosa_CV 2026.docx` no repositório
   `RodrigoAiosa/AIOSA_IA`, adicionando o case em "Cases de Sucesso"
   (mesmo formato dos demais: `Cliente | Setor` + 3 a 4 bullets, o último
   com "Resultado:") e incluindo o cliente na lista do resumo profissional.
   Não inventar números de resultado que o usuário não informou.
