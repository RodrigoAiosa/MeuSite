/* ═══════════════════════════════════════════════════════════════════
   Raio-X → Dashboard interativo em .html (estilo vidro)
   Recebe a tabela já lida pelo Raio-X e devolve um arquivo HTML
   independente: filtros, KPIs, gráficos clicáveis, tabela com busca,
   ordenação, paginação e exportação CSV. Tudo roda no navegador de
   quem abre o arquivo; ele não faz nenhuma chamada externa.
   ═══════════════════════════════════════════════════════════════════ */
(() => {
  const semAc = s => String(s ?? "").normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase().trim();
  const escH = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const MAX_LINHAS = 50000;
  // colunas de código (id, cod, matrícula, CPF…): nunca somar, só contar
  const ehCodigo = nome => {
    const bruto = String(nome ?? "").trim(), k = semAc(bruto).replace(/[_\-.\/#]+/g, " ").replace(/\s+/g, " ");
    if (/^idade\b/.test(k)) return false;
    return /(^|\s)(id|ids|cod|codigo|cd|cpf|cnpj|cep|matricula|sku|ean|gtin|chave|nf|nfe|nota fiscal|telefone|celular|fone|whatsapp|protocolo|pedido|ticket id|uuid|guid|placa|chassi|renavam|rg|pis|cnh|conta|agencia)(\s|$)/.test(k)
      || /^(n|no|nr|num|numero|nº|n°)\s/.test(k)
      || /^cod/.test(k)
      || /^(id|Id|ID|cd|Cd|CD)(?=[A-Z0-9])/.test(bruto)
      || /(?<=[a-z0-9])(Id|ID|Cod|COD)$/.test(bruto);
  };

  // papéis das colunas no dashboard
  const RE_ANO = /^(ano|year|exercicio|ano (de )?referencia|safra)$/;
  const RE_PERIODO = /^(mes|month|trimestre|semestre|semana|dia)$/;
  const RE_MEDIA = /salario|remunera|\bidade|nota|enps|nps|score|avalia|satisf|taxa|percent|%|preco|ticket|media|tempo|dias|prazo|duracao|temperatura|indice|rating/;
  const RE_DINHEIRO = /valor|receita|venda|fatur|preco|custo|montante|lucro|saldo|pagamento|despesa|ticket|salario|remunera|r\$|reais|orcamento|folha/;
  const RE_FILTRO = /departamento|setor|area|regiao|filial|loja|unidade|canal|categoria|segmento|status|situacao|contrato|tipo|senioridade|nivel|cargo|produto|marca|vendedor|equipe|genero|sexo|estado|uf|cidade|turno|faixa|grupo|fornecedor|cliente|origem|prioridade/;
  const RE_STATUS = /status|situacao|ativo|churn|cancel|desligad|aprovad|pago|entregue|resultado/;

  function planejar(cols, linhas) {
    const n = linhas.length;
    cols.forEach(c => {
      c.papel = c.tipo;
      if (ehCodigo(c.nome) || c.tipo === "id") { c.papel = "id"; c.tipo = "id"; return; }
      if (c.tipo === "numero") {
        const v = linhas.map(l => l[c.i]).filter(x => x !== null);
        const uni = new Set(v).size, inteiros = v.every(Number.isInteger);
        if (RE_ANO.test(c.chave) || (RE_PERIODO.test(c.chave) && inteiros && uni <= 31)) c.papel = "categoria";
        c.agg = RE_MEDIA.test(c.chave) || (inteiros && uni <= 11 && Math.max(...v) <= 10 && !/quant|qtd|qtde|volume|unidade|itens|pecas/.test(c.chave)) ? "media" : "soma";
        c.din = RE_DINHEIRO.test(c.chave) && !/quant|qtd|qtde/.test(c.chave);
      }
      if (c.papel === "categoria") {
        c.niveis = new Set(linhas.map(l => l[c.i]).filter(x => x !== null && x !== "")).size;
        if (c.niveis < 2 || c.niveis > 60 || (n >= 20 && c.niveis > n * 0.6)) c.papel = "texto";
      }
    });
    const cats = cols.filter(c => c.papel === "categoria");
    const mets = cols.filter(c => c.papel === "numero");
    const dataC = cols.find(c => c.papel === "data");
    const anoC = cats.find(c => RE_ANO.test(c.chave));
    const nota = c => (RE_FILTRO.test(c.chave) ? 20 : 0) + (RE_STATUS.test(c.chave) ? 4 : 0) - Math.abs(c.niveis - 6) / 3;

    // filtros: ano primeiro, depois as categorias mais "de negócio"
    const filtrosCat = cats.filter(c => c !== anoC && c.niveis <= 40).sort((a, b) => nota(b) - nota(a)).slice(0, anoC || dataC ? 3 : 4);
    const filtros = [...(anoC ? [anoC.i] : []), ...filtrosCat.map(c => c.i)];

    // métricas em ordem de importância
    const imp = c => (c.din ? 10 : 0) + (RE_MEDIA.test(c.chave) ? 3 : 0) + (/valor|receita|venda|fatur|total/.test(c.chave) ? 6 : 0);
    mets.sort((a, b) => imp(b) - imp(a));
    const m1 = mets[0], m2 = mets[1];

    // KPIs
    const idC = cols.find(c => c.papel === "id");
    const kpis = [{ tipo: "cont", c: idC ? idC.i : -1 }];
    const binarias = cats.filter(c => c.niveis === 2 && RE_STATUS.test(c.chave)).sort((a, b) => (RE_STATUS.test(b.chave) ? 1 : 0) - (RE_STATUS.test(a.chave) ? 1 : 0));
    const minoria = c => { const m = new Map(); linhas.forEach(l => { const v = l[c.i]; if (v !== null && v !== "") m.set(v, (m.get(v) || 0) + 1); }); return [...m.entries()].sort((a, b) => a[1] - b[1])[0][0]; };
    mets.slice(0, 3).forEach(c => kpis.push({ tipo: "met", c: c.i, agg: c.agg }));
    if (m1 && m1.agg === "media" && m1.din && kpis.length < 5) kpis.splice(2, 0, { tipo: "met", c: m1.i, agg: "soma" });
    binarias.slice(0, 5 - Math.min(kpis.length, 4)).forEach(c => { if (kpis.length < 5) kpis.push({ tipo: "pct", c: c.i, v: minoria(c) }); });
    if (kpis.length < 5 && dataC) kpis.push({ tipo: "periodo", c: dataC.i });
    if (kpis.length < 5 && cats[0]) kpis.push({ tipo: "niveis", c: (filtrosCat[0] || cats[0]).i });

    // gráficos
    const graficos = [];
    if (dataC) graficos.push({ tipo: "tempo", c: dataC.i, m: m1 ? m1.i : -1 });
    const porNivel = cats.filter(c => c !== anoC).sort((a, b) => nota(b) - nota(a));
    const c1 = porNivel[0], c2 = porNivel.find(c => c !== c1 && c.niveis > 2) || porNivel[1];
    if (c1) graficos.push({ tipo: "rosca", c: c1.i });
    if (m1 && (c2 || c1)) graficos.push({ tipo: "barra", c: (c2 || c1).i, m: m1.i });
    if (m2 && c1) graficos.push({ tipo: "barra", c: c1.i, m: m2.i });
    else if (m1 && c1 && c2) graficos.push({ tipo: "barra", c: c1.i, m: m1.i });
    const usados = new Set(graficos.map(g => g.c));
    const pequena = porNivel.find(c => c.niveis <= 5 && !usados.has(c.i)) || porNivel.find(c => !usados.has(c.i));
    if (pequena) graficos.push({ tipo: "pizza", c: pequena.i });
    if (!dataC && anoC && graficos.length < 6) graficos.unshift({ tipo: "barra", c: anoC.i, m: m1 ? m1.i : -1, largo: true, ordem: "rotulo" });
    if (!graficos.length && mets.length) graficos.push({ tipo: "hist", m: mets[0].i });
    return { filtros, anoDe: !anoC && dataC ? dataC.i : -1, kpis: kpis.slice(0, 5), graficos: graficos.slice(0, 6) };
  }

  /* ── tudo abaixo roda dentro do arquivo gerado ── */
  function painel() {
    const D = JSON.parse(document.getElementById("dados").textContent);
    const C = D.cols, L = D.linhas, P = D.plano;
    const $ = s => document.querySelector(s);
    const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
    const nf = (n, d = 0) => Number(n).toLocaleString("pt-BR", { minimumFractionDigits: d, maximumFractionDigits: d });
    const abrev = n => { const a = Math.abs(n); return a >= 1e9 ? nf(n / 1e9, 2) + " bi" : a >= 1e6 ? nf(n / 1e6, 2) + " mi" : a >= 1e4 ? nf(n / 1e3, 1) + " mil" : nf(n, a < 100 && n % 1 ? 1 : 0); };
    const fmtV = (c, v, curto) => v === null || v === undefined || isNaN(v) ? "—" : (C[c] && C[c].din ? "R$ " : "") + (curto ? abrev(v) : nf(v, C[c] && (C[c].din || v % 1) ? 2 : 0));
    const MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"];
    const CORES = ["#22d3ee", "#60a5fa", "#34d399", "#fbbf24", "#a78bfa", "#f472b6", "#fb7185", "#a3e635", "#38bdf8", "#f97316"];
    const vazio = v => v === null || v === undefined || v === "";
    const F = {}; let ano = "", busca = "", ord = null, pag = 1, tam = 15, filtradas = L;

    /* filtros */
    const opcoes = c => [...new Set(L.map(l => l[c]).filter(v => !vazio(v)))].sort((a, b) => typeof a === "number" ? a - b : String(a).localeCompare(String(b), "pt-BR"));
    let fh = "";
    if (P.anoDe >= 0) fh += `<label><span>Ano</span><select data-ano><option value="">Todos os anos</option>${[...new Set(L.map(l => (l[P.anoDe] || "").slice(0, 4)).filter(Boolean))].sort().map(a => `<option>${a}</option>`).join("")}</select></label>`;
    P.filtros.forEach(c => { fh += `<label><span>${esc(C[c].nome)}</span><select data-filtro="${c}"><option value="">Todos</option>${opcoes(c).map(v => `<option value="${esc(v)}">${esc(v)}</option>`).join("")}</select></label>`; });
    $("#filtros").innerHTML = fh || `<p class="mut">Sem colunas de categoria para filtrar. Use a busca da tabela.</p>`;

    function aplicar() {
      const b = busca.toLowerCase();
      filtradas = L.filter(l => {
        for (const c in F) if (String(l[c]) !== F[c]) return false;
        if (ano && !String(l[P.anoDe] || "").startsWith(ano)) return false;
        if (b && !l.some(v => !vazio(v) && String(v).toLowerCase().includes(b))) return false;
        return true;
      });
      pag = 1;
      document.querySelectorAll("[data-filtro]").forEach(s => { s.value = F[s.dataset.filtro] ?? ""; });
      const chips = Object.keys(F).filter(c => !P.filtros.includes(+c));
      $("#chips").innerHTML = chips.map(c => `<button type="button" class="chip" data-tira="${c}">${esc(C[c].nome)}: <b>${esc(F[c])}</b> ×</button>`).join("");
      $("#chips").hidden = !chips.length;
      kpis(); graficos(); tabela();
    }

    /* KPIs */
    const media = (c, ls) => { let s = 0, n = 0; ls.forEach(l => { const v = l[c]; if (typeof v === "number") { s += v; n++; } }); return n ? s / n : null; };
    const soma = (c, ls) => ls.reduce((s, l) => s + (typeof l[c] === "number" ? l[c] : 0), 0);
    const agg = (c, a, ls) => c < 0 ? ls.length : a === "media" ? media(c, ls) : soma(c, ls);
    const dataBR = s => s ? s.slice(8, 10) + "/" + s.slice(5, 7) + "/" + s.slice(0, 4) : "";
    const CORK = ["#22d3ee", "#34d399", "#fbbf24", "#a78bfa", "#fb7185"];
    function kpis() {
      const ls = filtradas;
      $("#kpis").innerHTML = P.kpis.map((k, i) => {
        let rot, val, sub, verso;
        if (k.tipo === "cont" && k.c >= 0) { const c = C[k.c], dist = new Set(ls.map(l => l[k.c]).filter(v => !vazio(v))).size, rep_ = ls.filter(l => !vazio(l[k.c])).length - dist; rot = "Qtd. de " + c.nome; val = nf(dist); sub = rep_ ? `distintos em ${nf(ls.length)} linhas` : `um por linha (${nf(ls.length)} linhas)`; verso = `Contagem de ${esc(c.nome)} distintos. Por ser um código, essa coluna é contada, nunca somada.`; }
        else if (k.tipo === "cont") { rot = "Registros"; val = nf(ls.length); sub = ls.length === L.length ? "na base completa" : `de ${nf(L.length)} na base`; verso = "Quantidade de linhas que atendem aos filtros escolhidos."; }
        if (k.tipo === "met") { const c = C[k.c]; rot = (k.agg === "media" ? "Média de " : "Total de ") + c.nome; const v = agg(k.c, k.agg, ls); val = fmtV(k.c, v, true); sub = k.agg === "media" ? "por registro" : `${nf(ls.filter(l => typeof l[k.c] === "number").length)} valores somados`; verso = k.agg === "media" ? `Média simples da coluna ${esc(c.nome)}, ignorando células vazias.` : `Soma da coluna ${esc(c.nome)} nos registros filtrados.`; }
        if (k.tipo === "pct") { const c = C[k.c], q = ls.filter(l => String(l[k.c]) === String(k.v)).length; rot = `% ${k.v}`; val = ls.length ? nf(q / ls.length * 100, 1) + "%" : "—"; sub = `${nf(q)} com ${esc(c.nome)} = ${esc(k.v)}`; verso = `(Registros com ${esc(c.nome)} “${esc(k.v)}” ÷ total filtrado) × 100.`; }
        if (k.tipo === "periodo") { const ds = ls.map(l => l[k.c]).filter(Boolean).sort(); rot = "Período"; val = ds.length ? `${MESES[+ds[0].slice(5, 7) - 1]}/${ds[0].slice(2, 4)} – ${MESES[+ds[ds.length - 1].slice(5, 7) - 1]}/${ds[ds.length - 1].slice(2, 4)}` : "—"; sub = esc(C[k.c].nome); verso = `Primeira e última data da coluna ${esc(C[k.c].nome)}.`; }
        if (k.tipo === "niveis") { const c = C[k.c]; rot = c.nome; val = nf(new Set(ls.map(l => l[k.c]).filter(v => !vazio(v))).size); sub = "valores diferentes"; verso = `Quantos ${esc(c.nome)} distintos aparecem na seleção.`; }
        return `<div class="flip" tabindex="0" style="--c:${CORK[i % 5]}"><div class="flip-in">
          <div class="face frente"><span class="k-rot">${esc(rot)}</span><b class="k-val">${val}</b><span class="k-sub">${sub}</span></div>
          <div class="face verso"><span class="k-rot" style="color:var(--c)">Como é calculado</span><p>${verso}</p></div></div></div>`;
      }).join("");
    }

    /* gráficos (SVG) */
    const tip = $("#tip");
    function agrupa(c, m, a, ls) {
      const g = new Map();
      ls.forEach(l => { const k = l[c]; if (vazio(k)) return; if (!g.has(k)) g.set(k, []); g.get(k).push(l); });
      return [...g.entries()].map(([k, arr]) => ({ k, v: agg(m, a, arr) ?? 0, n: arr.length }));
    }
    const topo = (itens, max) => { if (itens.length <= max) return itens; const r = itens.slice(0, max - 1); r.push({ k: `Outros (${itens.length - max + 1})`, v: itens.slice(max - 1).reduce((s, x) => s + x.v, 0), outros: true }); return r; };
    const larg = el => Math.max(260, Math.round(el.clientWidth));
    const tickN = (max) => { const p = Math.pow(10, Math.floor(Math.log10(max || 1))), n = max / p; const st = (n <= 2 ? 0.5 : n <= 5 ? 1 : 2) * p; return Math.ceil((max || 1) / st) * st; };

    function gBarra(el, g) {
      const m = g.m, a = m >= 0 ? C[m].agg : "cont";
      let itens = agrupa(g.c, m, a, filtradas);
      if (g.ordem === "rotulo") itens.sort((x, y) => String(x.k).localeCompare(String(y.k), "pt-BR", { numeric: true }));
      else itens.sort((x, y) => y.v - x.v);
      itens = a === "media" ? itens.slice(0, 12) : topo(itens, 12);
      if (!itens.length) return el.innerHTML = `<p class="mut">Sem dados para a seleção.</p>`;
      const W = larg(el), vert = itens.length <= 7 && Math.max(...itens.map(x => String(x.k).length)) * 6.6 < (W - 68) / itens.length - 4;
      const max = tickN(Math.max(...itens.map(x => x.v), 0)), cor = CORES[g.cor % CORES.length];
      let s = "";
      if (vert) {
        const H = 250, mE = 62, mB = 30, mT = 12, bw = (W - mE - 6) / itens.length, y = v => mT + (H - mT - mB) * (1 - v / max);
        s = `<svg viewBox="0 0 ${W} ${H}" width="100%">`;
        for (let k = 0; k <= 4; k++) { const v = max * k / 4; s += `<line x1="${mE}" x2="${W}" y1="${y(v)}" y2="${y(v)}" class="gr"/><text x="${mE - 6}" y="${y(v) + 4}" class="ex" text-anchor="end">${esc(fmtV(m, v, true))}</text>`; }
        itens.forEach((x, k) => {
          const bx = mE + k * bw + bw * 0.18, sel = String(F[g.c]) === String(x.k);
          s += `<rect x="${bx}" y="${y(x.v)}" width="${bw * 0.64}" height="${Math.max(1, H - mB - y(x.v))}" rx="7" fill="${cor}" fill-opacity="${sel || F[g.c] === undefined ? .55 : .2}" stroke="${cor}" class="mk" ${x.outros ? "" : `data-f="${g.c}" data-v="${esc(x.k)}"`} data-tip="${esc(x.k)}: ${esc(fmtV(m, x.v))}${a === "media" ? ` (${nf(x.n)} registros)` : ""}"/>`;
          s += `<text x="${bx + bw * 0.32}" y="${H - 10}" class="ex" text-anchor="middle">${esc(x.k)}</text>`;
        });
      } else {
        const lh = 30, mE = Math.min(150, W * 0.36), mD = 74, H = itens.length * lh + 8;
        s = `<svg viewBox="0 0 ${W} ${H}" width="100%">`;
        itens.forEach((x, k) => {
          const w = Math.max(2, (W - mE - mD) * x.v / max), yy = k * lh + 4, sel = String(F[g.c]) === String(x.k);
          s += `<text x="${mE - 8}" y="${yy + 17}" class="ex lab" text-anchor="end">${esc(String(x.k).length > 22 ? String(x.k).slice(0, 21) + "…" : x.k)}</text>
            <rect x="${mE}" y="${yy + 4}" width="${w}" height="18" rx="6" fill="${cor}" fill-opacity="${sel || F[g.c] === undefined ? .55 : .2}" stroke="${cor}" class="mk" ${x.outros ? "" : `data-f="${g.c}" data-v="${esc(x.k)}"`} data-tip="${esc(x.k)}: ${esc(fmtV(m, x.v))}"/>
            <text x="${mE + w + 6}" y="${yy + 17}" class="ex val">${esc(fmtV(m, x.v, true))}</text>`;
        });
      }
      el.innerHTML = s + `</svg>`;
    }

    function gRosca(el, g) {
      const itens = topo(agrupa(g.c, -1, "cont", filtradas).sort((x, y) => y.v - x.v), 8), tot = itens.reduce((s, x) => s + x.v, 0);
      if (!tot) return el.innerHTML = `<p class="mut">Sem dados para a seleção.</p>`;
      const R = 88, r = g.tipo === "pizza" ? 0 : 54, cx = 100, cy = 100;
      let ang = -Math.PI / 2, s = `<svg viewBox="0 0 200 200" class="rosca">`;
      const pt = (a, rr) => `${cx + rr * Math.cos(a)} ${cy + rr * Math.sin(a)}`;
      itens.forEach((x, k) => {
        const fr = x.v / tot, a2 = ang + fr * Math.PI * 2 - (fr === 1 ? 0.0001 : 0), gr = fr > 0.5 ? 1 : 0, cor = x.outros ? "#64748b" : CORES[k % CORES.length];
        const d = r ? `M ${pt(ang, R)} A ${R} ${R} 0 ${gr} 1 ${pt(a2, R)} L ${pt(a2, r)} A ${r} ${r} 0 ${gr} 0 ${pt(ang, r)} Z` : `M ${cx} ${cy} L ${pt(ang, R)} A ${R} ${R} 0 ${gr} 1 ${pt(a2, R)} Z`;
        const sel = F[g.c] === undefined || String(F[g.c]) === String(x.k);
        s += `<path d="${d}" fill="${cor}" fill-opacity="${sel ? .75 : .2}" stroke="rgba(255,255,255,.35)" stroke-width="1.2" class="mk" ${x.outros ? "" : `data-f="${g.c}" data-v="${esc(x.k)}"`} data-tip="${esc(x.k)}: ${nf(x.v)} (${nf(fr * 100, 1)}%)"/>`;
        ang = a2;
      });
      if (r) s += `<text x="100" y="98" text-anchor="middle" class="centro">${esc(abrev(tot))}</text><text x="100" y="116" text-anchor="middle" class="ex">registros</text>`;
      el.innerHTML = `<div class="rosca-box">${s}</svg><ul class="leg">${itens.map((x, k) => `<li ${x.outros ? "" : `data-f="${g.c}" data-v="${esc(x.k)}"`} class="mk"><i style="background:${x.outros ? "#64748b" : CORES[k % CORES.length]}"></i><span title="${esc(x.k)}">${esc(x.k)}</span><b>${nf(x.v / tot * 100, 1)}%</b></li>`).join("")}</ul></div>`;
    }

    function gTempo(el, g) {
      const mp = new Map();
      filtradas.forEach(l => { const d = l[g.c]; if (!d) return; const k = +d.slice(0, 4) * 12 + +d.slice(5, 7) - 1; if (!mp.has(k)) mp.set(k, []); mp.get(k).push(l); });
      const ks = [...mp.keys()].sort((a, b) => a - b);
      if (ks.length < 2) return el.innerHTML = `<p class="mut">Poucas datas na seleção para mostrar a evolução.</p>`;
      const pts = []; for (let k = Math.max(ks[0], ks[ks.length - 1] - 35); k <= ks[ks.length - 1]; k++) { const arr = mp.get(k) || []; pts.push({ k, n: arr.length, m: g.m >= 0 ? agg(g.m, C[g.m].agg, arr) : null }); }
      const vMes = k => { const arr = mp.get(k) || []; return { n: arr.length, m: g.m >= 0 && arr.length ? agg(g.m, C[g.m].agg, arr) : null }; };
      const temMes = k => k >= ks[0];
      const varPct = (a, b) => b === null || b === undefined || !b || a === null ? null : (a - b) / Math.abs(b) * 100;
      const pctH = v => v === null ? `<span class="t-nd">—</span>` : `<b class="${v >= 0 ? "t-up" : "t-down"}">${v >= 0 ? "▲ +" : "▼ "}${nf(v, 1)}%</b>`;
      const tipMes = p => {
        const ant = temMes(p.k - 1) ? vMes(p.k - 1) : null, aa = temMes(p.k - 12) ? vMes(p.k - 12) : null;
        const lin = (rot, val, mom, yoy) => `<tr><th>${rot}</th><td>${val}</td><td>${pctH(mom)}</td><td>${pctH(yoy)}</td></tr>`;
        let h = `<div class="t-tit">${MESES[p.k % 12]}/${Math.floor(p.k / 12)}</div><table class="t-tab"><tr><th></th><th></th><th>%MoM</th><th>%YoY</th></tr>`;
        h += lin("Registros", nf(p.n), ant ? varPct(p.n, ant.n) : null, aa ? varPct(p.n, aa.n) : null);
        if (g.m >= 0) h += lin(esc((C[g.m].agg === "media" ? "Média de " : "") + C[g.m].nome), esc(fmtV(g.m, p.m)), ant ? varPct(p.m, ant.m) : null, aa ? varPct(p.m, aa.m) : null);
        return h + `</table><div class="t-nota">MoM: contra o mês anterior · YoY: contra o mesmo mês do ano anterior</div>`;
      };
      const W = larg(el), H = 270, mE = 46, mD = g.m >= 0 ? 66 : 10, mB = 30, mT = 14, bw = (W - mE - mD) / pts.length;
      const maxN = tickN(Math.max(...pts.map(p => p.n))), mm = pts.map(p => p.m).filter(v => v !== null), maxM = tickN(Math.max(...mm, 0));
      const y1 = v => mT + (H - mT - mB) * (1 - v / maxN), y2 = v => mT + (H - mT - mB) * (1 - v / maxM);
      let s = `<svg viewBox="0 0 ${W} ${H}" width="100%">`;
      for (let k = 0; k <= 4; k++) {
        s += `<line x1="${mE}" x2="${W - mD}" y1="${y1(maxN * k / 4)}" y2="${y1(maxN * k / 4)}" class="gr"/><text x="${mE - 6}" y="${y1(maxN * k / 4) + 4}" class="ex c1" text-anchor="end">${esc(abrev(maxN * k / 4))}</text>`;
        if (g.m >= 0) s += `<text x="${W - mD + 6}" y="${y2(maxM * k / 4) + 4}" class="ex c2">${esc(fmtV(g.m, maxM * k / 4, true))}</text>`;
      }
      const passo = Math.ceil(pts.length / Math.max(3, Math.floor((W - mE - mD) / 54)));
      let linha = "";
      pts.forEach((p, i) => {
        const x = mE + i * bw, rot = `${MESES[p.k % 12]}/${String(Math.floor(p.k / 12)).slice(2)}`;
        s += `<rect x="${x + bw * 0.16}" y="${y1(p.n)}" width="${bw * 0.68}" height="${Math.max(0.5, H - mB - y1(p.n))}" rx="${Math.min(6, bw * 0.2)}" fill="#22d3ee" fill-opacity=".35" stroke="#67e8f9" stroke-opacity=".8" class="mk" data-tiph="${esc(tipMes(p))}"/>`;
        if (i % passo === 0 || i === pts.length - 1) s += `<text x="${x + bw / 2}" y="${H - 10}" class="ex" text-anchor="middle">${rot}</text>`;
        if (g.m >= 0 && p.m !== null) linha += `${linha ? "L" : "M"} ${x + bw / 2} ${y2(p.m)} `;
      });
      if (linha) { s += `<path d="${linha}" fill="none" stroke="#fb7185" stroke-width="2.4" stroke-linejoin="round"/>`; pts.forEach((p, i) => { if (p.m !== null) s += `<circle cx="${mE + i * bw + bw / 2}" cy="${y2(p.m)}" r="4" fill="#fb7185" class="mk" data-tiph="${esc(tipMes(p))}"/>`; }); }
      el.innerHTML = s + `</svg>`;
    }

    function gHist(el, g) {
      const v = filtradas.map(l => l[g.m]).filter(x => typeof x === "number").sort((a, b) => a - b);
      if (v.length < 2) return el.innerHTML = `<p class="mut">Sem dados para a seleção.</p>`;
      const mn = v[0], mx = v[v.length - 1], nb = 10, w = (mx - mn) / nb || 1, b = Array(nb).fill(0);
      v.forEach(x => b[Math.min(nb - 1, Math.floor((x - mn) / w))]++);
      const itens = b.map((n, i) => ({ k: abrev(mn + i * w), v: n }));
      const W = larg(el), H = 240, mE = 40, mB = 30, max = tickN(Math.max(...b)), bw = (W - mE) / nb, y = q => 12 + (H - 42) * (1 - q / max);
      let s = `<svg viewBox="0 0 ${W} ${H}" width="100%">`;
      itens.forEach((x, i) => { s += `<rect x="${mE + i * bw + 2}" y="${y(x.v)}" width="${bw - 4}" height="${H - mB - y(x.v)}" rx="4" fill="#a78bfa" fill-opacity=".5" class="mk" data-tip="a partir de ${x.k}: ${nf(x.v)} registros"/>`; if (i % 2 === 0) s += `<text x="${mE + i * bw + bw / 2}" y="${H - 10}" class="ex" text-anchor="middle">${x.k}</text>`; });
      el.innerHTML = s + `</svg>`;
    }

    const TIT = g => g.tipo === "tempo" ? `Evolução mensal${g.m >= 0 ? `: registros e ${C[g.m].agg === "media" ? "média de " : ""}${C[g.m].nome}` : " de registros"}`
      : g.tipo === "rosca" || g.tipo === "pizza" ? `Distribuição por ${C[g.c].nome}`
      : g.tipo === "hist" ? `Distribuição de ${C[g.m].nome}`
      : `${g.m < 0 ? "Registros" : (C[g.m].agg === "media" ? "Média de " : "Total de ") + C[g.m].nome} por ${C[g.c].nome}`;
    const DICA = g => g.tipo === "tempo" ? (g.m >= 0 ? `<span class="leg2"><i style="background:#22d3ee"></i>registros <i style="background:#fb7185"></i>${esc(C[g.m].nome)}</span>` : "") : g.tipo === "hist" ? "" : `<span class="dica">clique para filtrar</span>`;
    P.graficos.forEach((g, i) => { g.cor = i + 1; });
    // largura de cada cartão: preenche a linha inteira, sem buracos (3 colunas no computador, 2 no tablet)
    const encaixa = (spans, n) => { const r = []; let f = 0; spans.forEach((s0, i) => { const s1 = Math.min(s0, n); if (f && f + s1 > n) { r[i - 1] += n - f; f = 0; } r[i] = s1; f = (f + s1) % n; }); if (f && r.length) r[r.length - 1] += n - f; return r; };
    const sp = P.graficos.map(g => g.tipo === "tempo" || g.largo ? 2 : 1), d3 = encaixa(sp, 3), t2 = encaixa(sp, 2);
    $("#graficos").innerHTML = P.graficos.map((g, i) => `<section class="glass card" style="--d:${d3[i]};--t:${t2[i]}"><header><h2>${esc(TIT(g))}</h2>${DICA(g)}</header><div class="gbox" id="g${i}"></div></section>`).join("");
    function graficos() {
      P.graficos.forEach((g, i) => { const el = document.getElementById("g" + i); ({ tempo: gTempo, rosca: gRosca, pizza: gRosca, barra: gBarra, hist: gHist })[g.tipo](el, g); });
    }

    /* tabela */
    const binaria = C.map((c, i) => { if (c.papel !== "categoria" || c.niveis !== 2 || !c.status) return null; const m = new Map(); L.forEach(l => m.set(l[i], (m.get(l[i]) || 0) + 1)); return [...m.entries()].sort((a, b) => b[1] - a[1])[0][0]; });
    $("#thead").innerHTML = `<tr>${C.map((c, i) => `<th data-ord="${i}" class="${c.tipo === "numero" ? "num" : ""}">${esc(c.nome)}<span class="seta"></span></th>`).join("")}</tr>`;
    function cel(c, v) {
      if (vazio(v)) return `<td class="mut">—</td>`;
      const t = C[c];
      if (t.tipo === "numero" && t.papel === "categoria") return `<td class="num">${esc(v)}</td>`;
      if (t.tipo === "numero") return `<td class="num${t.din ? " din" : ""}">${esc(fmtV(c, v))}</td>`;
      if (t.tipo === "data") return `<td class="mono">${dataBR(v)}</td>`;
      if (t.tipo === "id") return `<td class="mono cod">${esc(v)}</td>`;
      if (binaria[c] !== null && binaria[c] !== undefined) return `<td><span class="badge ${String(v) === String(binaria[c]) ? "ok" : "alt"}">${esc(v)}</span></td>`;
      return `<td>${esc(v)}</td>`;
    }
    function tabela() {
      let ls = filtradas;
      if (ord) { const { c, dir } = ord; ls = ls.slice().sort((a, b) => { const x = a[c], y = b[c]; if (vazio(x)) return 1; if (vazio(y)) return -1; return (typeof x === "number" ? x - y : String(x).localeCompare(String(y), "pt-BR", { numeric: true })) * dir; }); }
      const tot = ls.length, ini = (pag - 1) * tam, fim = Math.min(ini + tam, tot);
      $("#tbody").innerHTML = ls.slice(ini, fim).map(l => `<tr>${l.map((v, c) => cel(c, v)).join("")}</tr>`).join("") || `<tr><td colspan="${C.length}" class="mut">Nenhum registro com esses filtros.</td></tr>`;
      $("#info").textContent = `Mostrando ${tot ? ini + 1 : 0}–${fim} de ${nf(tot)}`;
      $("#qtd").textContent = nf(tot);
      $("#pg").textContent = pag;
      $("#ant").disabled = pag === 1; $("#prox").disabled = fim >= tot;
      document.querySelectorAll("[data-ord]").forEach(th => { th.querySelector(".seta").textContent = ord && ord.c === +th.dataset.ord ? (ord.dir > 0 ? " ▲" : " ▼") : ""; });
    }

    /* exportação */
    function csv() {
      const q = v => { if (vazio(v)) return ""; const s = typeof v === "number" ? String(v).replace(".", ",") : String(v); return /[;"\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s; };
      const txt = "﻿" + [C.map(c => q(c.nome)).join(";"), ...filtradas.map(l => l.map(q).join(";"))].join("\r\n");
      const a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([txt], { type: "text/csv;charset=utf-8" }));
      a.download = (D.arquivo || "dados") + "_filtrado.csv"; document.body.appendChild(a); a.click(); a.remove();
    }

    /* eventos */
    document.addEventListener("change", e => {
      const s = e.target;
      if (s.dataset.filtro !== undefined) { if (s.value === "") delete F[s.dataset.filtro]; else F[s.dataset.filtro] = s.value; aplicar(); }
      if (s.dataset.ano !== undefined) { ano = s.value; aplicar(); }
      if (s.id === "tam") { tam = +s.value; pag = 1; tabela(); }
    });
    let tb; $("#busca").addEventListener("input", e => { clearTimeout(tb); tb = setTimeout(() => { busca = e.target.value.trim(); aplicar(); }, 150); });
    document.addEventListener("click", e => {
      const f = e.target.closest("[data-f]");
      if (f) { const c = f.dataset.f, v = f.dataset.v; if (String(F[c]) === v) delete F[c]; else F[c] = v; tip.hidden = true; aplicar(); return; }
      const t = e.target.closest("[data-tira]"); if (t) { delete F[t.dataset.tira]; aplicar(); return; }
      const th = e.target.closest("[data-ord]"); if (th) { const c = +th.dataset.ord; ord = ord && ord.c === c ? (ord.dir > 0 ? { c, dir: -1 } : null) : { c, dir: 1 }; pag = 1; tabela(); return; }
      if (e.target.closest("#limpar")) { Object.keys(F).forEach(k => delete F[k]); ano = ""; busca = ""; $("#busca").value = ""; const sa = $("[data-ano]"); if (sa) sa.value = ""; ord = null; aplicar(); }
      if (e.target.closest(".csv")) csv();
      if (e.target.closest("#ant") && pag > 1) { pag--; tabela(); }
      if (e.target.closest("#prox") && pag * tam < filtradas.length) { pag++; tabela(); }
    });
    document.addEventListener("mousemove", e => {
      const m = e.target.closest("[data-tip],[data-tiph]");
      if (!m) { tip.hidden = true; return; }
      if (m.dataset.tiph) tip.innerHTML = m.dataset.tiph; else tip.textContent = m.dataset.tip;
      tip.hidden = false;
      const x = Math.min(e.clientX + 14, innerWidth - tip.offsetWidth - 8), y = e.clientY - tip.offsetHeight - 12;
      tip.style.left = x + "px"; tip.style.top = (y < 8 ? e.clientY + 18 : y) + "px";
    });
    let lw = innerWidth, tr; addEventListener("resize", () => { clearTimeout(tr); tr = setTimeout(() => { if (Math.abs(innerWidth - lw) > 30) { lw = innerWidth; graficos(); } }, 150); });
    aplicar();
  }

  const CSS = `
:root{--bg:#070b1a;--txt:#f1f5f9;--mut:rgba(203,213,225,.72);--borda:rgba(255,255,255,.16);--vidro:linear-gradient(135deg,rgba(255,255,255,.11),rgba(255,255,255,.035));color-scheme:dark}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font:14px/1.5 Inter,"Segoe UI",system-ui,-apple-system,Roboto,Arial,sans-serif;color:var(--txt);background:var(--bg);min-height:100vh;overflow-x:hidden}
.fundo{position:fixed;inset:0;z-index:-1;overflow:hidden;background:radial-gradient(1200px 800px at 10% 0%,#14213d 0%,transparent 60%),radial-gradient(1000px 700px at 100% 100%,#2a1245 0%,transparent 60%),var(--bg)}
.orb{position:absolute;border-radius:50%;filter:blur(90px);opacity:.5;animation:flut 18s ease-in-out infinite}
.o1{width:520px;height:520px;background:#06b6d4;top:-140px;left:-120px}.o2{width:460px;height:460px;background:#8b5cf6;top:25%;right:-140px;animation-delay:-6s}
.o3{width:420px;height:420px;background:#ec4899;bottom:-140px;left:25%;opacity:.35;animation-delay:-11s}.o4{width:360px;height:360px;background:#10b981;top:58%;left:-140px;opacity:.28;animation-delay:-3s}
@keyframes flut{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(40px,-30px) scale(1.08)}66%{transform:translate(-30px,40px) scale(.95)}}
@media (prefers-reduced-motion:reduce){.orb{animation:none}.flip-in{transition:none!important}}
.glass{background:var(--vidro);backdrop-filter:blur(22px) saturate(160%);-webkit-backdrop-filter:blur(22px) saturate(160%);border:1px solid var(--borda);box-shadow:0 8px 32px rgba(0,0,0,.35),inset 0 1px 0 rgba(255,255,255,.22);border-radius:18px}
.wrap{max-width:1280px;margin:0 auto;padding:0 20px}
header.topo{position:sticky;top:12px;z-index:20;margin:12px auto 0}
.barra{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:12px 18px;flex-wrap:wrap}
.marca{display:flex;align-items:center;gap:12px;min-width:0}
.logo{width:40px;height:40px;border-radius:12px;background:linear-gradient(135deg,#22d3ee,#3b82f6);display:grid;place-items:center;box-shadow:0 6px 18px rgba(34,211,238,.3);flex:none}
.marca h1{margin:0;font-size:1.05rem;letter-spacing:-.01em;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.marca p{margin:0;font-size:.75rem;color:var(--mut)}
.acoes{display:flex;gap:8px;flex-wrap:wrap}
button,select,input{font:inherit;color:inherit}
.btn{background:rgba(255,255,255,.09);border:1px solid rgba(255,255,255,.18);border-radius:12px;padding:7px 13px;font-size:.8rem;font-weight:600;cursor:pointer;transition:background .2s,transform .2s;display:inline-flex;gap:6px;align-items:center}
.btn:hover{background:rgba(255,255,255,.18);transform:translateY(-1px)}.btn:disabled{opacity:.4;cursor:default;transform:none}
.btn.ciano{color:#67e8f9}.btn.verde{color:#6ee7b7}
main{display:grid;grid-template-columns:minmax(0,1fr);gap:20px;padding-top:22px;padding-bottom:30px}
#filtros{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:14px;padding:16px}
#filtros label span{display:block;font-size:.7rem;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:var(--mut);margin-bottom:5px}
select,input[type=search]{width:100%;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.16);border-radius:12px;padding:8px 11px;font-size:.86rem;outline:none;transition:border-color .2s,box-shadow .2s}
select:focus,input:focus{border-color:rgba(34,211,238,.7);box-shadow:0 0 0 3px rgba(34,211,238,.18)}
option{background:#111827;color:#f1f5f9}
#chips{display:flex;gap:8px;flex-wrap:wrap}
.chip{background:rgba(34,211,238,.14);border:1px solid rgba(34,211,238,.4);color:#cffafe;border-radius:99px;padding:4px 12px;font-size:.78rem;cursor:pointer}
#kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px}
.flip{perspective:1000px;height:126px;border-radius:18px;background:var(--vidro);backdrop-filter:blur(22px) saturate(160%);-webkit-backdrop-filter:blur(22px) saturate(160%);border:1px solid var(--borda);box-shadow:0 8px 32px rgba(0,0,0,.35),inset 0 1px 0 rgba(255,255,255,.22);position:relative;outline:none;overflow:hidden}
.flip::after{content:"";position:absolute;right:-30px;top:-30px;width:100px;height:100px;border-radius:50%;background:var(--c);filter:blur(45px);opacity:.35;pointer-events:none}
.flip-in{position:absolute;inset:0;transition:transform .6s cubic-bezier(.4,0,.2,1);transform-style:preserve-3d}
.flip:hover .flip-in,.flip:focus .flip-in{transform:rotateY(180deg)}
.face{position:absolute;inset:0;padding:16px 18px;display:flex;flex-direction:column;justify-content:space-between;backface-visibility:hidden;-webkit-backface-visibility:hidden}
.frente::before{content:"";position:absolute;left:0;top:16%;bottom:16%;width:3px;border-radius:3px;background:var(--c);box-shadow:0 0 14px var(--c)}
.verso{transform:rotateY(180deg)}.verso p{margin:0;font-size:.8rem;color:#e2e8f0;line-height:1.4}
.k-rot{font-size:.7rem;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:var(--mut);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.k-val{font-size:1.65rem;font-weight:700;letter-spacing:-.02em;overflow-wrap:anywhere;line-height:1.15}
.k-sub{font-size:.74rem;color:var(--mut);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
#graficos{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.card{padding:18px 20px;min-width:0;grid-column:span var(--d,1)}
.card header{display:flex;justify-content:space-between;align-items:baseline;gap:10px;margin-bottom:12px}
.card h2{margin:0;font-size:.9rem;font-weight:700}
.dica{font-size:.68rem;color:#67e8f9;opacity:.8;white-space:nowrap;font-family:ui-monospace,Consolas,monospace}
.leg2{font-size:.7rem;color:var(--mut);display:flex;align-items:center;gap:5px;white-space:nowrap}.leg2 i{width:9px;height:9px;border-radius:3px;display:inline-block;margin-left:6px}
.gbox svg{display:block;overflow:visible}
.gr{stroke:rgba(255,255,255,.08)}.ex{fill:rgba(226,232,240,.72);font-size:11px}.ex.c1{fill:#67e8f9}.ex.c2{fill:#fda4af}.ex.val{fill:#e2e8f0;font-weight:600}
.mk{cursor:pointer;transition:fill-opacity .2s}.mk:hover{fill-opacity:.85!important}
.centro{fill:#fff;font-size:22px;font-weight:700}
.rosca-box{display:flex;align-items:center;gap:16px;flex-wrap:wrap;justify-content:center}.rosca{width:min(190px,100%);flex:none}
.leg{list-style:none;margin:0;padding:0;display:grid;gap:5px;font-size:.78rem;flex:1 1 140px;min-width:0}
.leg li{display:grid;grid-template-columns:10px minmax(0,1fr) auto;gap:8px;align-items:center;padding:2px 6px;border-radius:8px}.leg li:hover{background:rgba(255,255,255,.06)}
.leg i{width:10px;height:10px;border-radius:3px}.leg span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.leg b{font-weight:600;color:#e2e8f0}
.tab{padding:18px 20px}.tab-topo{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:14px}
.tab-topo h2{margin:0;font-size:1rem}.tab-topo p{margin:2px 0 0;font-size:.75rem;color:var(--mut)}
.tab-busca{display:flex;gap:8px;align-items:center;flex:1 1 320px;max-width:460px}
.rolagem{overflow-x:auto;border:1px solid rgba(255,255,255,.1);border-radius:14px;background:rgba(0,0,0,.12)}
table{width:100%;border-collapse:collapse;font-size:.8rem}
th{position:sticky;top:0;background:rgba(255,255,255,.1);backdrop-filter:blur(6px);text-align:left;padding:10px 12px;font-size:.68rem;text-transform:uppercase;letter-spacing:.05em;color:#e2e8f0;white-space:nowrap;cursor:pointer;user-select:none}
th:hover{color:#67e8f9}td{padding:9px 12px;border-top:1px solid rgba(255,255,255,.05);white-space:nowrap;max-width:280px;overflow:hidden;text-overflow:ellipsis}
tbody tr:hover{background:rgba(255,255,255,.06)}.num{text-align:right;font-variant-numeric:tabular-nums}.din{color:#6ee7b7;font-weight:600}.mono{font-family:ui-monospace,Consolas,monospace}.cod{color:#67e8f9}.mut{color:var(--mut)}
.badge{padding:2px 9px;border-radius:99px;font-size:.68rem;font-weight:600;border:1px solid}.badge.ok{background:rgba(52,211,153,.14);color:#6ee7b7;border-color:rgba(110,231,183,.3)}.badge.alt{background:rgba(251,113,133,.14);color:#fda4af;border-color:rgba(253,164,175,.3)}
.pagina{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;font-size:.78rem;color:var(--mut);padding-top:12px}
.pagina select{width:auto;padding:4px 8px}.pagina .nav{display:flex;align-items:center;gap:6px}#pg{color:#67e8f9;font-weight:700;padding:0 8px}
.t-tit{font-weight:700;margin-bottom:4px}.t-tab{border-collapse:collapse;font-size:.76rem}.t-tab th,.t-tab td{padding:2px 6px;border:0;white-space:nowrap;text-align:right;background:none;position:static;text-transform:none;letter-spacing:0;font-size:.76rem;cursor:default}.t-tab th:first-child{text-align:left;color:var(--mut);font-weight:500}.t-tab tr:first-child th{color:var(--mut);font-weight:600;font-size:.68rem}.t-up{color:#4ade80}.t-down{color:#fb7185}.t-nd{color:var(--mut)}.t-nota{margin-top:5px;font-size:.66rem;color:var(--mut)}
#tip{position:fixed;z-index:50;pointer-events:none;background:rgba(15,23,42,.88);border:1px solid rgba(255,255,255,.2);backdrop-filter:blur(10px);border-radius:10px;padding:7px 11px;font-size:.78rem;max-width:380px}
footer{text-align:center;font-size:.75rem;color:var(--mut);padding:10px 0 34px}footer a{color:#67e8f9;text-decoration:none}footer a:hover{text-decoration:underline}
@media (max-width:1000px){#graficos{grid-template-columns:repeat(2,minmax(0,1fr))}.card{grid-column:span var(--t,1)}}
@media (max-width:680px){.wrap{padding:0 12px}#kpis{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.flip{height:118px}.k-val{font-size:1.3rem}.face{padding:13px 14px}#graficos{grid-template-columns:minmax(0,1fr)}.card{grid-column:auto}.acoes{width:100%}.acoes .btn{flex:1;justify-content:center}.marca h1{white-space:normal}header.topo{position:static}}
`;

  function gerar({ arquivo, cols, linhas, abas }) {
    const lin = linhas.slice(0, MAX_LINHAS);
    const cs = cols.map((c, i) => ({ nome: c.nome, tipo: c.tipo, chave: semAc(c.nome), i }));
    const plano = planejar(cs, lin);
    const titulo = arquivo.replace(/\.[^.]+$/, "").replace(/[_-]+/g, " ").trim() || "Dashboard";
    const hoje = new Date().toLocaleDateString("pt-BR");
    const dados = { arquivo: arquivo.replace(/\.[^.]+$/, ""), plano, linhas: lin,
      cols: cs.map(c => ({ nome: c.nome, tipo: c.papel === "categoria" && c.tipo === "numero" ? "numero" : c.tipo, papel: c.papel, niveis: c.niveis, agg: c.agg, din: !!c.din, status: RE_STATUS.test(c.chave) })) };
    const json = JSON.stringify(dados).replace(/</g, "\\u003c").replace(/[\u2028\u2029]/g, c => "\\u" + c.charCodeAt(0).toString(16));
    const corte = linhas.length > MAX_LINHAS ? ` (primeiras ${MAX_LINHAS.toLocaleString("pt-BR")} de ${linhas.length.toLocaleString("pt-BR")})` : "";
    return `<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${escH(titulo)} · Dashboard</title>
<meta name="generator" content="Raio-X dos dados · Sky Data Solution">
<style>${CSS}</style>
</head>
<body>
<div class="fundo" aria-hidden="true"><div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div><div class="orb o4"></div></div>
<header class="topo wrap"><div class="glass barra">
  <div class="marca"><div class="logo" aria-hidden="true"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"><path d="M21 12A9 9 0 1 1 12 3v9z"/><path d="M15 3.5A9 9 0 0 1 20.5 9H15z"/></svg></div>
    <div><h1>${escH(titulo)}</h1><p>${lin.length.toLocaleString("pt-BR")} registros${corte} · ${cols.length} colunas${abas ? ` · ${abas} abas consolidadas` : ""} · gerado em ${hoje}</p></div></div>
  <div class="acoes"><button type="button" class="btn" id="limpar">↺ Limpar filtros</button><button type="button" class="btn verde csv">⬇ Exportar CSV</button></div>
</div></header>
<main class="wrap">
  <section class="glass" id="filtros" aria-label="Filtros"></section>
  <div id="chips" hidden></div>
  <section id="kpis" aria-label="Indicadores"></section>
  <div id="graficos"></div>
  <section class="glass tab">
    <div class="tab-topo"><div><h2>Base de dados (<span id="qtd"></span> registros)</h2><p>Clique no título de uma coluna para ordenar. A busca procura em todas as colunas.</p></div>
      <div class="tab-busca"><input type="search" id="busca" placeholder="Buscar em qualquer coluna…" aria-label="Buscar na tabela"><button type="button" class="btn verde csv">CSV</button></div></div>
    <div class="rolagem"><table><thead id="thead"></thead><tbody id="tbody"></tbody></table></div>
    <div class="pagina"><label>Mostrar <select id="tam"><option>15</option><option>25</option><option>50</option><option>100</option></select> por página</label>
      <span id="info"></span><div class="nav"><button type="button" class="btn" id="ant">Anterior</button><span id="pg">1</span><button type="button" class="btn" id="prox">Próximo</button></div></div>
  </section>
</main>
<footer>Dashboard gerado automaticamente pelo <a href="https://skydatasolution.com.br/#raiox" target="_blank" rel="noopener">Raio-X dos dados · Sky Data Solution</a>. Os dados ficam só neste arquivo.</footer>
<div id="tip" hidden></div>
<script type="application/json" id="dados">${json}</script>
<script>(${painel.toString()})();</script>
</body>
</html>`;
  }

  window.RaioXDash = { gerar };
})();
