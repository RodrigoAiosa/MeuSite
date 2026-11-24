/* ═══════════════════════════════════════════════════════════════════
   Raio-X dos seus dados
   Lê uma planilha (.xlsx ou .csv) NO NAVEGADOR do visitante e monta um
   painel automático: indicadores, evolução no tempo, ranking, qualidade
   dos dados e sugestões de indicadores. Nada é enviado para servidor:
   o arquivo não sai do computador de quem testa.
   Bibliotecas (carregadas só quando a pessoa usa): read-excel-file (MIT)
   e PapaParse (MIT), em assets/vendor/.
   ═══════════════════════════════════════════════════════════════════ */
(() => {
  const raiz = document.getElementById("rx");
  if (!raiz) return;
  const q = s => raiz.querySelector(s);
  const LIMITE_MB = 15, LIMITE_LINHAS = 200000;
  const LIBS = { xlsx: ["assets/vendor/read-excel-file-9.3.20.min.js", "readXlsxFile"], csv: ["assets/vendor/papaparse-5.7.1.min.js", "Papa"], dash: ["assets/raiox-dash.js?v=1", "RaioXDash"] };
  const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const semAc = s => String(s ?? "").normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase().replace(/\s+/g, " ").trim();
  const evento = (n, d) => { try { if (window.va) window.va("event", { name: n, data: d }); } catch (_) {} };
  const nf = (n, d = 0) => Number(n).toLocaleString("pt-BR", { minimumFractionDigits: d, maximumFractionDigits: d });
  const abrev = n => { const a = Math.abs(n); return a >= 1e9 ? nf(n / 1e9, 1) + " bi" : a >= 1e6 ? nf(n / 1e6, 1) + " mi" : a >= 1e4 ? nf(n / 1e3, 1) + " mil" : nf(n, a < 10 && n % 1 ? 2 : 0); };
  const MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"];

  /* ── carregamento sob demanda das bibliotecas ── */
  const carregadas = {};
  function lib(tipo) {
    const [src, global] = LIBS[tipo];
    if (window[global]) return Promise.resolve(window[global]);
    return carregadas[tipo] ||= new Promise((ok, erro) => {
      const s = document.createElement("script"); s.src = src; s.async = true;
      s.onload = () => ok(window[global]); s.onerror = () => erro(new Error("Não foi possível carregar o leitor de planilhas."));
      document.head.appendChild(s);
    });
  }

  /* ── leitura do arquivo ── */
  async function lerArquivo(arq) {
    const ext = (arq.name.split(".").pop() || "").toLowerCase();
    if (arq.size > LIMITE_MB * 1024 * 1024) throw new Error(`O arquivo tem ${nf(arq.size / 1048576, 1)} MB. Para o teste no navegador, use até ${LIMITE_MB} MB.`);
    if (ext === "xls") throw new Error("Esse é o formato antigo do Excel (.xls). Abra no Excel e use “Salvar como” .xlsx ou .csv.");
    if (["xlsx", "xlsm"].includes(ext)) {
      const ler = await lib("xlsx");
      let r = await ler(arq);
      // a versão 9 devolve todas as abas: [{ sheet, data }]; usa a aba com mais linhas preenchidas
      if (r.length && r[0] && !Array.isArray(r[0]) && Array.isArray(r[0].data)) {
        const cheias = d => d.filter(l => l.some(c => !vazio(c))).length;
        r = r.reduce((a, b) => cheias(b.data) > cheias(a.data) ? b : a).data;
      }
      // datas do Excel chegam em UTC à meia-noite: usa o dia do calendário, sem fuso
      return r.map(l => l.map(c => c instanceof Date ? new Date(c.getUTCFullYear(), c.getUTCMonth(), c.getUTCDate(), c.getUTCHours(), c.getUTCMinutes()) : c));
    }
    if (["csv", "txt", "tsv"].includes(ext)) {
      const Papa = await lib("csv");
      return await new Promise((ok, erro) => Papa.parse(arq, { skipEmptyLines: "greedy", complete: r => ok(r.data), error: erro }));
    }
    throw new Error("Use uma planilha .xlsx ou .csv.");
  }

  /* ── conversões ── */
  function numero(v) {
    if (typeof v === "number") return isFinite(v) ? v : NaN;
    if (typeof v !== "string") return NaN;
    let s = v.trim().replace(/^R\$\s*/i, "").replace(/\s|%$/g, "");
    if (!s || !/^[-+(]?[\d.,]+\)?$/.test(s)) return NaN;
    const neg = /^\(.*\)$/.test(s) || s.startsWith("-"); s = s.replace(/[()+-]/g, "");
    const nV = (s.match(/,/g) || []).length, nP = (s.match(/\./g) || []).length;
    if (nV && nP) {            // "1.234,56" ou "1,234.56": o último separador é o decimal
      const dec = s.lastIndexOf(",") > s.lastIndexOf(".") ? "," : ".";
      s = s.split(dec === "," ? "." : ",").join("").replace(dec, ".");
    } else if (nV) {           // "1234,56" (decimal) ou "1,234,567" (milhar)
      s = nV > 1 ? s.replace(/,/g, "") : s.replace(",", ".");
    } else if (nP && (nP > 1 || /^\d{1,3}\.\d{3}$/.test(s))) {
      s = s.replace(/\./g, "");  // "1.234" e "1.234.567" no padrão brasileiro = milhar
    }
    const n = parseFloat(s);
    return isNaN(n) ? NaN : neg ? -n : n;
  }
  function data(v) {
    if (v instanceof Date) return isNaN(v) ? null : v;
    if (typeof v !== "string") return null;
    const s = v.trim(); let m;
    if ((m = s.match(/^(\d{1,2})[/.-](\d{1,2})[/.-](\d{2,4})(?:[ T](\d{1,2}):(\d{2}))?/))) {
      const a = +m[3] < 100 ? 2000 + +m[3] : +m[3], d = new Date(a, +m[2] - 1, +m[1]);
      return d.getMonth() === +m[2] - 1 ? d : null;
    }
    if ((m = s.match(/^(\d{4})-(\d{1,2})-(\d{1,2})/))) { const d = new Date(+m[1], +m[2] - 1, +m[3]); return d.getMonth() === +m[2] - 1 ? d : null; }
    if ((m = s.match(/^(\d{1,2})[/-](\d{4})$/))) return new Date(+m[2], +m[1] - 1, 1);
    return null;
  }
  const vazio = v => v === null || v === undefined || (typeof v === "string" && !v.trim());

  /* ── tabela: acha o cabeçalho e as linhas ── */
  function montarTabela(linhas) {
    linhas = (linhas || []).filter(l => Array.isArray(l));
    const ini = linhas.findIndex(l => l.filter(c => !vazio(c)).length >= 2);
    if (ini < 0) throw new Error("Não encontrei dados na planilha. Ela precisa ter um cabeçalho e pelo menos uma linha.");
    const larg = Math.max(...linhas.slice(ini, ini + 50).map(l => l.length));
    const usados = {};
    const cab = Array.from({ length: larg }, (_, i) => {
      let n = String(linhas[ini][i] ?? "").trim() || `Coluna ${i + 1}`;
      if (usados[n]) n += ` (${++usados[n]})`; else usados[n] = 1;
      return n;
    });
    let dados = linhas.slice(ini + 1).filter(l => l.some(c => !vazio(c)));
    const cortado = dados.length > LIMITE_LINHAS; if (cortado) dados = dados.slice(0, LIMITE_LINHAS);
    if (!dados.length) throw new Error("A planilha tem só o cabeçalho. Coloque algumas linhas de dados e tente de novo.");
    return { cab, dados, cortado };
  }

  /* ── perfil de cada coluna ── */
  const RE_ID = /(^|\b)(id|cod|codigo|cpf|cnpj|cep|telefone|celular|fone|matricula|pedido|nota|nf|chave|sku|ean)(\b|$)/;
  const RE_METRICA = /valor|receita|venda|fatur|total|preco|custo|montante|lucro|margem|quantidade|qtd|qtde|volume|saldo|pagamento|despesa|peso|horas|salario|remunera|r\$|reais|enps|nps|nota|idade|score|preco|ticket/;
  const RE_CATEG = /produto|categoria|regiao|cliente|vendedor|loja|cidade|estado|uf|canal|setor|segmento|filial|marca|departamento|area|tipo|status|grupo|unidade|fornecedor|representante|equipe/;
  function perfil(nome, i, dados) {
    const brutos = dados.map(l => l[i]), cheios = brutos.filter(v => !vazio(v));
    const p = { nome, i, vazios: brutos.length - cheios.length, total: brutos.length, chave: semAc(nome) };
    let nNum = 0, nNumTexto = 0, nData = 0;
    for (const v of cheios) {
      if (v instanceof Date || (typeof v === "string" && data(v))) nData++;
      else if (!isNaN(numero(v))) { nNum++; if (typeof v === "string") nNumTexto++; }
    }
    const unicos = new Set(cheios.map(v => v instanceof Date ? +v : semAc(v)));
    p.unicos = unicos.size; p.numTexto = nNumTexto;
    const c = cheios.length || 1;
    if (nData / c >= 0.8) p.tipo = "data";
    else if (nNum / c >= 0.8) p.tipo = RE_ID.test(p.chave) || (unicos.size > 0.95 * c && c > 30 && cheios.every(v => Number.isInteger(numero(v))) && !RE_METRICA.test(p.chave)) ? "id" : "numero";
    else if (unicos.size >= 2 && unicos.size <= Math.max(60, c * 0.05) && !RE_ID.test(p.chave)) p.tipo = "categoria";
    else p.tipo = RE_ID.test(p.chave) ? "id" : "texto";
    if (p.tipo === "numero") p.valores = brutos.map(numero);
    if (p.tipo === "data") p.datas = brutos.map(data);
    return p;
  }

  /* ── qualidade dos dados ── */
  function qualidade(t, cols) {
    const alertas = []; let pena = 0;
    const al = (grav, txt) => { alertas.push({ grav, txt }); pena += grav === "alta" ? 14 : grav === "media" ? 7 : 3; };
    // linhas duplicadas
    const vistos = new Map(); let dup = 0;
    for (const l of t.dados) { const k = JSON.stringify(l.map(v => v instanceof Date ? +v : semAc(v))); if (vistos.has(k)) dup++; else vistos.set(k, 1); }
    if (dup) al(dup / t.dados.length > 0.02 ? "alta" : "media", `<b>${nf(dup)}</b> linha(s) duplicada(s): podem inflar totais e médias.`);
    // vazios
    for (const c of cols) {
      const pct = c.vazios / c.total;
      if (pct >= 0.3) al("alta", `Coluna <b>${esc(c.nome)}</b> com ${nf(pct * 100)}% das células vazias.`);
      else if (pct >= 0.05) al("media", `Coluna <b>${esc(c.nome)}</b> com ${nf(pct * 100)}% das células vazias.`);
    }
    // números gravados como texto
    for (const c of cols) if (c.tipo === "numero" && c.numTexto > 0) al("media", `Coluna <b>${esc(c.nome)}</b> tem ${nf(c.numTexto)} número(s) gravado(s) como texto, que fórmulas e somas do Excel ignoram.`);
    // categorias escritas de jeitos diferentes
    for (const c of cols) {
      if (c.tipo !== "categoria") continue;
      const grupos = new Map();
      for (const l of t.dados) { const v = l[c.i]; if (vazio(v) || typeof v !== "string") continue; const k = semAc(v); if (!grupos.has(k)) grupos.set(k, new Set()); grupos.get(k).add(v); }
      const var_ = [...grupos.values()].filter(s => s.size > 1);
      if (var_.length) al("media", `Coluna <b>${esc(c.nome)}</b> tem o mesmo valor escrito de formas diferentes, como ${[...var_[0]].slice(0, 3).map(x => "“" + esc(x) + "”").join(", ")}. Isso divide os totais.`);
    }
    // valores fora do padrão
    for (const c of cols) {
      if (c.tipo !== "numero") continue;
      const v = c.valores.filter(x => !isNaN(x)).sort((a, b) => a - b); if (v.length < 20) continue;
      const q1 = v[Math.floor(v.length * 0.25)], q3 = v[Math.floor(v.length * 0.75)], iqr = q3 - q1;
      if (iqr <= 0) continue;
      const fora = v.filter(x => x > q3 + 3 * iqr || x < q1 - 3 * iqr).length;
      if (fora) al("baixa", `Coluna <b>${esc(c.nome)}</b> tem ${nf(fora)} valor(es) muito fora do padrão. Vale conferir se não é erro de digitação.`);
      if (RE_METRICA.test(c.chave) && /quant|qtd|qtde|preco|valor|venda/.test(c.chave)) { const neg = v.filter(x => x < 0).length; if (neg) al("media", `Coluna <b>${esc(c.nome)}</b> tem ${nf(neg)} valor(es) negativo(s).`); }
    }
    // datas estranhas
    const hoje = Date.now() + 86400000;
    for (const c of cols) {
      if (c.tipo !== "data") continue;
      const fut = c.datas.filter(d => d && +d > hoje).length, velhas = c.datas.filter(d => d && d.getFullYear() < 1950).length;
      if (fut) al("baixa", `Coluna <b>${esc(c.nome)}</b> tem ${nf(fut)} data(s) no futuro.`);
      if (velhas) al("media", `Coluna <b>${esc(c.nome)}</b> tem ${nf(velhas)} data(s) anteriores a 1950, provável erro de digitação.`);
    }
    if (t.cortado) al("baixa", `A planilha tem mais de ${nf(LIMITE_LINHAS)} linhas; o teste analisou as primeiras ${nf(LIMITE_LINHAS)}.`);
    return { alertas: alertas.sort((a, b) => "alta media baixa".indexOf(a.grav) - "alta media baixa".indexOf(b.grav)), nota: Math.max(0, Math.min(100, 100 - pena)), dup };
  }

  /* ── escolhas automáticas ── */
  const pontua = (c, re) => (re.test(c.chave) ? 10 : 0);
  function escolher(cols) {
    const nums = cols.filter(c => c.tipo === "numero"), cats = cols.filter(c => c.tipo === "categoria" && c.unicos <= 40), datas = cols.filter(c => c.tipo === "data");
    const soma = c => c.valores.reduce((s, x) => s + (isNaN(x) ? 0 : Math.abs(x)), 0);
    const met = nums.slice().sort((a, b) => (pontua(b, /valor|receita|venda|fatur|total|montante/) + pontua(b, RE_METRICA) / 2) - (pontua(a, /valor|receita|venda|fatur|total|montante/) + pontua(a, RE_METRICA) / 2) || soma(b) - soma(a))[0];
    const cat = cats.slice().sort((a, b) => pontua(b, RE_CATEG) - pontua(a, RE_CATEG) || Math.abs(a.unicos - 8) - Math.abs(b.unicos - 8))[0];
    return { met: met ? met.i : -1, cat: cat ? cat.i : -1, dat: datas[0] ? datas[0].i : -1 };
  }
  const ehDinheiro = c => c && /valor|receita|venda|fatur|preco|custo|montante|lucro|saldo|pagamento|despesa|ticket|r\$/.test(c.chave) && !/quant|qtd|qtde/.test(c.chave);

  /* ── gráficos em SVG ── */
  function graficoMeses(pontos, dinheiro) {
    if (pontos.length < 2) return `<p class="rx-vazio">Poucas datas para mostrar uma evolução.</p>`;
    const W = Math.round(Math.max(300, Math.min(1000, raiz.clientWidth - 40))), H = W < 500 ? 200 : 240, mE = 64, mB = 28, mT = 14, max = Math.max(...pontos.map(p => p.v), 0) || 1;
    const bw = (W - mE - 8) / pontos.length;
    const y = v => mT + (H - mT - mB) * (1 - v / max);
    let s = `<svg viewBox="0 0 ${W} ${H}" class="rx-svg" role="img" aria-label="Evolução mensal">`;
    for (let k = 0; k <= 4; k++) { const v = max * k / 4, yy = y(v); s += `<line x1="${mE}" x2="${W - 4}" y1="${yy}" y2="${yy}" class="rx-grade"/><text x="${mE - 6}" y="${yy + 4}" class="rx-eixo" text-anchor="end">${esc(abrev(v))}</text>`; }
    const passo = Math.ceil(pontos.length / Math.max(3, Math.floor((W - mE) / 58)));
    pontos.forEach((p, k) => {
      const x = mE + k * bw + bw * 0.15, h = H - mB - y(p.v);
      s += `<rect x="${x}" y="${y(p.v)}" width="${bw * 0.7}" height="${Math.max(h, 0.5)}" rx="3" class="rx-barra"><title>${esc(p.rot)}: ${dinheiro ? "R$ " : ""}${esc(nf(p.v, dinheiro ? 2 : 0))}</title></rect>`;
      if (k % passo === 0 || k === pontos.length - 1) s += `<text x="${x + bw * 0.35}" y="${H - 9}" class="rx-eixo" text-anchor="middle">${esc(p.curto)}</text>`;
    });
    return s + `</svg>`;
  }
  function ranking(itens, dinheiro) {
    const tot = itens.reduce((s, x) => s + x.v, 0) || 1, max = Math.max(...itens.map(x => x.v)) || 1;
    return `<ol class="rx-rank">${itens.map(x => `<li><span class="rx-rank-n" title="${esc(x.k)}">${esc(x.k)}</span>
      <span class="rx-rank-bar"><i style="width:${Math.max(2, x.v / max * 100)}%"></i></span>
      <span class="rx-rank-v">${dinheiro ? "R$ " : ""}${esc(abrev(x.v))} <small>${nf(x.v / tot * 100, 1)}%</small></span></li>`).join("")}</ol>`;
  }

  /* ── estado e painel ── */
  let T = null, COLS = [], ESC = null, ORIGEM = "";
  const ICONE = { numero: "🔢", data: "📅", categoria: "🏷️", texto: "🔤", id: "🆔" };
  const NOME_TIPO = { numero: "número", data: "data", categoria: "categoria", texto: "texto", id: "código" };

  function analisar(linhas, origem) {
    T = montarTabela(linhas);
    COLS = T.cab.map((n, i) => perfil(n, i, T.dados));
    ESC = escolher(COLS);
    ORIGEM = origem;
    render();
  }

  function render() {
    const met = COLS[ESC.met], cat = COLS[ESC.cat], dat = COLS[ESC.dat];
    const dinheiro = ehDinheiro(met), Q = qualidade(T, COLS);
    const valorLinha = l => met ? numero(l[met.i]) : 1;
    // KPIs
    let total = 0, n = 0, maior = -Infinity;
    for (const l of T.dados) { const v = valorLinha(l); if (!isNaN(v)) { total += v; n++; if (v > maior) maior = v; } }
    const fmt = v => (dinheiro ? "R$ " : "") + abrev(v);
    // evolução mensal
    let meses = [], periodo = "";
    if (dat) {
      const m = new Map();
      T.dados.forEach((l, k) => { const d = dat.datas[k]; if (!d || d.getFullYear() < 1950 || +d > Date.now() + 86400000 * 400) return; const v = valorLinha(l); if (isNaN(v)) return; const key = d.getFullYear() * 12 + d.getMonth(); m.set(key, (m.get(key) || 0) + v); });
      const ks = [...m.keys()].sort((a, b) => a - b);
      if (ks.length) {
        const ult = ks.slice(-36);
        for (let k = ult[0]; k <= ult[ult.length - 1]; k++) meses.push({ v: m.get(k) || 0, rot: `${MESES[k % 12]}/${Math.floor(k / 12)}`, curto: `${MESES[k % 12]}/${String(Math.floor(k / 12)).slice(2)}` });
        periodo = `${MESES[ks[0] % 12]}/${Math.floor(ks[0] / 12)} a ${MESES[ks[ks.length - 1] % 12]}/${Math.floor(ks[ks.length - 1] / 12)}`;
      }
    }
    let varMes = "";
    if (meses.length >= 2) { const a = meses[meses.length - 2].v, b = meses[meses.length - 1].v; if (a) { const p = (b - a) / Math.abs(a) * 100; varMes = `<b class="${p >= 0 ? "rx-up" : "rx-down"}">${p >= 0 ? "+" : ""}${nf(p, 1)}%</b>`; } }
    // ranking
    let rank = "";
    if (cat) {
      const m = new Map();
      for (const l of T.dados) { const raw = l[cat.i]; if (vazio(raw)) continue; const k = String(raw).trim(); const v = valorLinha(l); if (isNaN(v)) continue; m.set(k, (m.get(k) || 0) + v); }
      const ord = [...m.entries()].map(([k, v]) => ({ k, v })).sort((a, b) => b.v - a.v);
      const top = ord.slice(0, 8); if (ord.length > 8) top.push({ k: `Outros (${ord.length - 8})`, v: ord.slice(8).reduce((s, x) => s + x.v, 0) });
      rank = ranking(top, dinheiro);
    }
    // sugestões de indicadores
    const nm = met ? met.nome : "Linhas", sug = [];
    if (dat) sug.push(`<b>${esc(nm)} por mês</b>, com variação sobre o mês anterior e sobre o mesmo mês do ano passado`);
    if (cat) sug.push(`<b>Participação de cada ${esc(cat.nome)}</b> no total, com ranking e curva ABC`);
    if (met && cat) sug.push(`<b>Média de ${esc(nm)} por ${esc(cat.nome)}</b>, para comparar desempenho em igualdade`);
    const outraCat = COLS.find(c => c.tipo === "categoria" && c !== cat && c.unicos <= 40);
    if (cat && outraCat) sug.push(`<b>Cruzamento ${esc(cat.nome)} × ${esc(outraCat.nome)}</b>, para achar onde estão as maiores oportunidades`);
    if (met && dat) sug.push(`<b>Meta × realizado</b> de ${esc(nm)}, com alerta automático quando ficar abaixo do esperado`);
    sug.push(`<b>Atualização automática</b> do painel sempre que a planilha ou o sistema de origem mudar`);
    // seletores
    const opt = (lista, sel, vaziaTxt) => `<option value="-1">${vaziaTxt}</option>` + lista.map(c => `<option value="${c.i}"${c.i === sel ? " selected" : ""}>${esc(c.nome)}</option>`).join("");
    const nota = Q.nota, corNota = nota >= 80 ? "ok" : nota >= 55 ? "medio" : "ruim";

    q("#rxPainel").innerHTML = `
      <div class="rx-topo">
        <div><div class="rx-arq">📄 ${esc(ORIGEM)}</div><div class="rx-sub">${nf(T.dados.length)} linhas · ${nf(T.cab.length)} colunas${T.cortado ? " · analisadas as primeiras " + nf(LIMITE_LINHAS) : ""}</div></div>
        <div class="rx-acoes"><button type="button" class="btn btn-primary rx-novo" data-rx="dash">⬇ Baixar dashboard interativo (.html)</button>
        <button type="button" class="btn btn-ghost rx-novo" data-rx="novo">↺ Analisar outra planilha</button></div>
      </div>
      <div class="rx-sel">
        <label>Indicador <select data-rx-sel="met">${opt(COLS.filter(c => c.tipo === "numero"), ESC.met, "Quantidade de linhas")}</select></label>
        <label>Agrupar por <select data-rx-sel="cat">${opt(COLS.filter(c => c.tipo === "categoria"), ESC.cat, "Nenhum")}</select></label>
        <label>Data <select data-rx-sel="dat">${opt(COLS.filter(c => c.tipo === "data"), ESC.dat, "Nenhuma")}</select></label>
      </div>
      <div class="rx-kpis">
        <div><small>${met ? "Total de " + esc(met.nome) : "Linhas com dados"}</small><b>${esc(fmt(total))}</b></div>
        <div><small>${met ? "Média por linha" : "Colunas"}</small><b>${met ? esc(fmt(n ? total / n : 0)) : nf(T.cab.length)}</b></div>
        <div><small>${dat ? "Período" : met ? "Maior valor" : "Células vazias"}</small><b class="${dat ? "rx-peq" : ""}">${dat ? esc(periodo || "—") : met ? esc(fmt(maior)) : nf(COLS.reduce((s, c) => s + c.vazios, 0))}</b></div>
        <div><small>${varMes ? "Último mês × anterior" : "Qualidade dos dados"}</small>${varMes || `<b class="rx-nota-${corNota}">${nota}/100</b>`}</div>
      </div>
      <div class="rx-grid">
        <div class="rx-card rx-largo"><h4>${dat ? `${esc(met ? met.nome : "Linhas")} por mês` : "Evolução no tempo"}</h4>${dat ? graficoMeses(meses, dinheiro) : `<p class="rx-vazio">Não encontrei uma coluna de data. Com ela, o painel mostra a evolução mês a mês.</p>`}</div>
        <div class="rx-card"><h4>${cat ? `Ranking por ${esc(cat.nome)}` : "Ranking"}</h4>${rank || `<p class="rx-vazio">Não encontrei uma coluna de categorias (produto, região, cliente…). Com ela, o painel mostra o ranking.</p>`}</div>
        <div class="rx-card">
          <h4>Qualidade dos dados <span class="rx-nota rx-nota-${corNota}">${nota}/100</span></h4>
          ${Q.alertas.length ? `<ul class="rx-alertas">${Q.alertas.slice(0, 7).map(a => `<li class="rx-${a.grav}">${a.txt}</li>`).join("")}</ul>${Q.alertas.length > 7 ? `<p class="rx-vazio">+ ${Q.alertas.length - 7} ponto(s) de atenção.</p>` : ""}`
            : `<p class="rx-ok">✔ Nenhum problema relevante encontrado: sem duplicidades, sem colunas muito vazias e sem números gravados como texto.</p>`}
        </div>
        <div class="rx-card">
          <h4>Colunas reconhecidas</h4>
          <div class="rx-cols">${COLS.map(c => `<span title="${esc(NOME_TIPO[c.tipo])} · ${nf(c.vazios / c.total * 100)}% vazio">${ICONE[c.tipo]} ${esc(c.nome)}</span>`).join("")}</div>
          <h4 class="rx-h4b">Indicadores que eu acompanharia</h4>
          <ul class="rx-sug">${sug.slice(0, 5).map(x => `<li>${x}</li>`).join("")}</ul>
        </div>
      </div>
      <div class="rx-cta">
        <div><strong>Gostou do Raio-X? Imagine isso com os seus sistemas, atualizado sozinho.</strong>
        <span>Eu transformo planilhas e bases como essa em painéis automáticos, com os dados tratados e os indicadores certos para cada área.</span></div>
        <button type="button" class="btn btn-primary" data-rx="cta">Quero esse painel completo →</button>
      </div>`;
    q("#rxPainel").hidden = false;
    q("#rxEntrada").hidden = true;
    lib("dash").catch(() => {}); // já deixa o gerador pronto para o clique
  }

  /* ── dashboard em .html para baixar (gerado aqui mesmo, sem enviar nada) ── */
  const iso = d => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
  function linhasDash() {
    return T.dados.map(l => COLS.map(c => {
      const v = l[c.i];
      if (vazio(v)) return c.tipo === "numero" || c.tipo === "data" ? null : "";
      if (c.tipo === "numero") { const n = numero(v); return isNaN(n) ? null : n; }
      if (c.tipo === "data") { const d = data(v); return d ? iso(d) : null; }
      return v instanceof Date ? iso(v) : String(v).trim();
    }));
  }
  async function baixarDash(botao) {
    const txt = botao.textContent; botao.disabled = true; botao.textContent = "Montando o dashboard…";
    try {
      const gerador = await lib("dash");
      const arquivo = ORIGEM.replace(/\s*\(.*\)$/, "");
      const html = gerador.gerar({ arquivo, cols: COLS.map(c => ({ nome: c.nome, tipo: c.tipo })), linhas: linhasDash() });
      const url = URL.createObjectURL(new Blob([html], { type: "text/html;charset=utf-8" }));
      const a = document.createElement("a"); a.href = url; a.download = arquivo.replace(/\.[^.]+$/, "") + "_dashboard.html";
      document.body.appendChild(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(url), 60000);
      aviso("Pronto! O dashboard foi baixado. Abra o arquivo .html no navegador: ele funciona sem internet e os dados ficam só nele.");
      evento("raiox_dash", { faixa: T.dados.length < 1000 ? "<1k" : T.dados.length < 50000 ? "1k-50k" : "50k+" });
    } catch (e) { aviso("Não consegui montar o dashboard. Tente de novo ou use outra planilha.", true); evento("raiox_erro"); }
    finally { botao.disabled = false; botao.textContent = txt; }
  }

  /* ── planilha de exemplo (vendas fictícias, com alguns problemas de propósito) ── */
  function exemplo() {
    let sem = 7;
    const rnd = () => (sem = (sem * 16807) % 2147483647) / 2147483647;
    const reg = ["Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Norte"], pesoR = [0.42, 0.2, 0.2, 0.1, 0.08];
    const prod = [["Notebook", 3900], ["Monitor", 1150], ["Mouse", 95], ["Teclado", 180], ["Headset", 320], ["Webcam", 260], ["Cadeira", 1450], ["Mesa", 980]];
    const vend = ["Ana", "Bruno", "Carla", "Diego", "Elisa", "Fábio"];
    const pick = (arr, pesos) => { if (!pesos) return arr[Math.floor(rnd() * arr.length)]; let r = rnd(); for (let k = 0; k < arr.length; k++) { r -= pesos[k]; if (r <= 0) return arr[k]; } return arr[arr.length - 1]; };
    const linhas = [["Data", "Pedido", "Região", "Vendedor", "Produto", "Quantidade", "Valor total"]];
    for (let k = 0; k < 1200; k++) {
      const mes = Math.floor(rnd() * 12), dia = 1 + Math.floor(rnd() * 28), d = new Date(2025, mes, dia);
      const [p, preco] = pick(prod), qt = 1 + Math.floor(rnd() * (preco > 1000 ? 3 : 8)), cres = 1 + mes * 0.025;
      let r = pick(reg, pesoR); if (k % 97 === 0) r = r.toLowerCase() + " "; // mesmo valor escrito diferente
      let v = +(qt * preco * cres * (0.9 + rnd() * 0.2)).toFixed(2);
      let vCel = v; if (k % 151 === 0) vCel = nf(v, 2); // número gravado como texto
      linhas.push([d, 10000 + k, r, k % 61 === 0 ? "" : pick(vend), p, qt, vCel]);
    }
    linhas.push([new Date(2025, 6, 14), 99999, "Sudeste", "Ana", "Notebook", 30, 117000]); // fora do padrão
    for (let k = 1; k <= 6; k++) linhas.push(linhas[k * 50].slice()); // duplicadas
    return linhas;
  }

  /* ── eventos ── */
  const entrada = q("#rxEntrada"), input = q("#rxArquivo"), msg = q("#rxMsg");
  function aviso(t, erro) { msg.textContent = t; msg.className = "rx-msg" + (erro ? " rx-erro" : ""); msg.hidden = !t; }
  async function processar(arq) {
    if (!arq) return;
    aviso("Lendo a planilha no seu navegador…"); entrada.classList.add("rx-carregando");
    try {
      const linhas = await lerArquivo(arq);
      analisar(linhas, arq.name);
      aviso("");
      evento("raiox_arquivo", { tipo: (arq.name.split(".").pop() || "").toLowerCase(), faixa: T.dados.length < 1000 ? "<1k" : T.dados.length < 50000 ? "1k-50k" : "50k+" });
      raiz.scrollIntoView({ behavior: "smooth", block: "start" });
    } catch (e) { aviso(e.message || "Não consegui ler esse arquivo. Confira se é uma planilha .xlsx ou .csv.", true); evento("raiox_erro"); }
    finally { entrada.classList.remove("rx-carregando"); input.value = ""; }
  }
  input.addEventListener("change", () => processar(input.files[0]));
  ["dragenter", "dragover"].forEach(t => entrada.addEventListener(t, e => { e.preventDefault(); entrada.classList.add("rx-sobre"); }));
  ["dragleave", "drop"].forEach(t => entrada.addEventListener(t, e => { e.preventDefault(); entrada.classList.remove("rx-sobre"); }));
  entrada.addEventListener("drop", e => processar(e.dataTransfer.files[0]));
  raiz.addEventListener("click", e => {
    const b = e.target.closest("[data-rx]"); if (!b) return;
    const a = b.dataset.rx;
    if (a === "exemplo") { analisar(exemplo(), "vendas_exemplo.xlsx (dados fictícios)"); evento("raiox_exemplo"); raiz.scrollIntoView({ behavior: "smooth", block: "start" }); }
    if (a === "dash") baixarDash(b);
    if (a === "novo") { T = null; q("#rxPainel").hidden = true; q("#rxPainel").innerHTML = ""; entrada.hidden = false; aviso(""); }
    if (a === "cta") { evento("raiox_cta"); if (typeof window.diagIniciar === "function") window.diagIniciar({ dor: "dashboards", origem: "raio-x" }); else location.hash = "#contato"; }
  });
  // redesenha o painel quando a largura muda de verdade (girar o celular, redimensionar a janela)
  let largura = raiz.clientWidth, tm;
  addEventListener("resize", () => { clearTimeout(tm); tm = setTimeout(() => {
    if (T && Math.abs(raiz.clientWidth - largura) > 40) { largura = raiz.clientWidth; render(); } }, 200); });
  raiz.addEventListener("change", e => {
    const s = e.target.closest("[data-rx-sel]"); if (!s || !T) return;
    ESC[s.dataset.rxSel] = +s.value; render();
  });
})();
