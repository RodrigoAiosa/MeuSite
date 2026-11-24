/* ═══════════════════════════════════════════════════════════════════
   "Um painel, três visões" + "Antes e depois"
   Demonstração com dados fictícios, inspirada no projeto entregue na
   Pernambucanas: o mesmo painel muda conforme o perfil de acesso e a
   trilha dos dados (origem → Python/SQL → base → painel) se atualiza
   sozinha. Abaixo, uma barra deslizante compara a planilha manual com
   o painel pronto, usando os cases.
   ═══════════════════════════════════════════════════════════════════ */
(() => {
  const raiz = document.getElementById("vs");
  if (!raiz) return;
  const reduz = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const nf = (n, d = 0) => Number(n).toLocaleString("pt-BR", { minimumFractionDigits: d, maximumFractionDigits: d });
  const brl = n => n >= 1e6 ? "R$ " + nf(n / 1e6, 1) + " mi" : n >= 1e3 ? "R$ " + nf(n / 1e3, 0) + " mil" : "R$ " + nf(n, 0);
  const evento = (n, d) => { try { if (window.va) window.va("event", { name: n, data: d }); } catch (_) {} };
  const MESES = ["dez", "jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov"];

  /* ── perfis e o que cada um enxerga (dados fictícios) ── */
  const PERFIS = {
    dir: { nome: "Diretoria", ico: "👔", escopo: "Brasil · todas as regionais", fat: 48.6e6, meta: 96.4, ticket: 187, rec: 1284, margem: 38.2, folha: 6.9e6,
      rank: { tit: "Faturamento por regional", itens: [["Sudeste", 14.2e6], ["Sul", 10.1e6], ["Nordeste", 9.8e6], ["Centro-Oeste", 7.6e6], ["Norte", 6.9e6]] } },
    ger: { nome: "Gerência", ico: "📊", escopo: "Regional Sudeste · 38 lojas", fat: 14.2e6, meta: 101.3, ticket: 192, rec: 356, margem: 39.1,
      rank: { tit: "Ranking das lojas da regional", itens: [["Loja Centro", 0.94e6], ["Loja Paulista", 0.88e6], ["Loja Norte", 0.71e6], ["Loja Campinas", 0.61e6], ["Loja Santos", 0.55e6]] } },
    sup: { nome: "Supervisão", ico: "🧑‍💼", escopo: "Loja Campinas · 12 vendedores", fat: 0.612e6, meta: 92.8, ticket: 176, rec: 14,
      rank: { tit: "Vendas da equipe no mês", itens: [["Ana", 71e3], ["Bruno", 64e3], ["Carla", 58e3], ["Diego", 52e3], ["Elisa", 47e3]] } },
  };
  // blocos do painel: quem pode ver cada um
  const BLOCOS = [
    { id: "fat", tipo: "kpi", rot: "Faturamento do mês", ver: ["dir", "ger", "sup"] },
    { id: "meta", tipo: "kpi", rot: "% da meta", ver: ["dir", "ger", "sup"] },
    { id: "margem", tipo: "kpi", rot: "Margem bruta", ver: ["dir", "ger"] },
    { id: "folha", tipo: "kpi", rot: "Custo de pessoal", ver: ["dir"] },
    { id: "ticket", tipo: "kpi", rot: "Ticket médio", ver: ["dir", "ger", "sup"] },
    { id: "rec", tipo: "kpi", rot: "Reclamações em aberto", ver: ["dir", "ger", "sup"] },
    { id: "evol", tipo: "graf", rot: "Faturamento, últimos 12 meses", ver: ["dir", "ger", "sup"], largo: true },
    { id: "rank", tipo: "graf", rot: "Ranking", ver: ["dir", "ger", "sup"] },
    { id: "dre", tipo: "graf", rot: "Resultado financeiro (DRE resumida)", ver: ["dir"] },
    { id: "motivos", tipo: "graf", rot: "Reclamações por motivo", ver: ["dir", "ger", "sup"] },
  ];
  const DONO = { dir: "Diretoria", ger: "Gerência", sup: "Supervisão" };
  let perfil = "dir", mostrarBloqueios = true, rodada = 0;

  // série de 12 meses determinística por perfil (com variação a cada atualização)
  function serie(p) {
    const base = PERFIS[p].fat, s = [];
    for (let i = 0; i < 12; i++) s.push(base * (0.78 + 0.22 * i / 11 + 0.05 * Math.sin(i * 1.7 + p.length)));
    s[11] = PERFIS[p].fat; return s;
  }

  /* ── gráficos em SVG ── */
  function gLinha(v) {
    const W = 520, H = 150, mx = Math.max(...v) * 1.08, mn = Math.min(...v) * 0.9;
    const x = i => 8 + i * (W - 16) / (v.length - 1), y = n => 10 + (H - 34) * (1 - (n - mn) / (mx - mn));
    const d = v.map((n, i) => `${i ? "L" : "M"}${x(i).toFixed(1)} ${y(n).toFixed(1)}`).join(" ");
    return `<svg viewBox="0 0 ${W} ${H}" class="vs-svg" aria-hidden="true"><defs><linearGradient id="vsG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#00b4d8" stop-opacity=".35"/><stop offset="1" stop-color="#00b4d8" stop-opacity="0"/></linearGradient></defs>
      <path d="${d} L${x(v.length - 1)} ${H - 24} L${x(0)} ${H - 24} Z" fill="url(#vsG)"/><path d="${d}" fill="none" stroke="#00b4d8" stroke-width="2.4" stroke-linejoin="round"/>
      ${v.map((n, i) => `<circle cx="${x(i)}" cy="${y(n)}" r="${i === v.length - 1 ? 4.5 : 2.5}" fill="${i === v.length - 1 ? "#48cae4" : "#00b4d8"}"/>`).join("")}
      ${v.map((n, i) => i % 2 ? "" : `<text x="${x(i)}" y="${H - 6}" text-anchor="middle" class="vs-eixo">${MESES[i]}</text>`).join("")}</svg>`;
  }
  function gRank(itens) {
    const mx = Math.max(...itens.map(i => i[1]));
    return `<ol class="vs-rank">${itens.map(([k, v]) => `<li><span>${k}</span><i><b style="width:${(v / mx * 100).toFixed(1)}%"></b></i><em>${brl(v)}</em></li>`).join("")}</ol>`;
  }
  function gDre() {
    const linhas = [["Receita líquida", 48.6, "pos"], ["CMV", -30.0, "neg"], ["Despesas operacionais", -11.3, "neg"], ["EBITDA", 7.3, "res"]];
    return `<ul class="vs-dre">${linhas.map(([k, v, c]) => `<li class="${c}"><span>${k}</span><b>${v < 0 ? "− " : ""}R$ ${nf(Math.abs(v), 1)} mi</b></li>`).join("")}</ul>`;
  }
  function gMotivos(total) {
    const m = [["Entrega atrasada", .34], ["Cobrança", .24], ["Troca e devolução", .19], ["Atendimento", .14], ["Outros", .09]];
    return `<div class="vs-motivos">${m.map(([k, f], i) => `<div style="--f:${f};--c:${["#00b4d8", "#48cae4", "#90e0ef", "#7b8ba8", "#4b5563"][i]}"><span>${k}</span><b>${nf(Math.round(total * f))}</b></div>`).join("")}</div>`;
  }

  /* ── render do painel ── */
  function valorKpi(id, P) {
    if (id === "fat") return brl(P.fat);
    if (id === "meta") return `<span class="${P.meta >= 100 ? "vs-up" : "vs-down"}">${nf(P.meta, 1)}%</span>`;
    if (id === "margem") return nf(P.margem, 1) + "%";
    if (id === "folha") return brl(P.folha);
    if (id === "ticket") return "R$ " + nf(P.ticket);
    if (id === "rec") return nf(P.rec);
  }
  function conteudoGraf(id, P) {
    if (id === "evol") return gLinha(serie(perfil));
    if (id === "rank") return gRank(P.rank.itens);
    if (id === "dre") return gDre();
    if (id === "motivos") return gMotivos(P.rec);
  }
  function render(animar) {
    const P = PERFIS[perfil];
    const vis = BLOCOS.filter(b => b.ver.includes(perfil)).length;
    raiz.querySelectorAll("[data-vs-perfil]").forEach(b => { const on = b.dataset.vsPerfil === perfil; b.classList.toggle("on", on); b.setAttribute("aria-pressed", on); });
    raiz.querySelector("#vsLogin").innerHTML = `<span class="vs-cadeado">🔐</span> Logado como <b>${P.nome}</b> · escopo: <b>${P.escopo}</b><span class="vs-conta">vê ${vis} de ${BLOCOS.length} blocos</span>`;
    const blocoHtml = b => {
      const ok = b.ver.includes(perfil);
      if (!ok && !mostrarBloqueios) return "";
      const dono = b.ver.map(p => DONO[p]).join(" e ");
      const rot = b.id === "rank" ? P.rank.tit : b.rot;
      if (b.tipo === "kpi") return `<div class="vs-kpi${ok ? "" : " vs-bloq"}" data-b="${b.id}"><small>${rot}</small>${ok ? `<b>${valorKpi(b.id, P)}</b>` : `<b class="vs-fake">R$ 00,0 mi</b><span class="vs-tranca">🔒 Só ${dono}</span>`}</div>`;
      return `<div class="vs-graf${b.largo ? " vs-largo" : ""}${ok ? "" : " vs-bloq"}" data-b="${b.id}"><h4>${rot}</h4>${ok ? conteudoGraf(b.id, P) : `<div class="vs-fake-graf"></div><span class="vs-tranca">🔒 Restrito: ${dono}</span>`}</div>`;
    };
    const kpis = BLOCOS.filter(b => b.tipo === "kpi").map(blocoHtml).join(""), grafs = BLOCOS.filter(b => b.tipo === "graf").map(blocoHtml).join("");
    const painel = raiz.querySelector("#vsPainel");
    painel.innerHTML = `<div class="vs-kpis">${kpis}</div><div class="vs-grafs">${grafs}</div>`;
    if (animar && !reduz) { painel.classList.remove("vs-troca"); void painel.offsetWidth; painel.classList.add("vs-troca"); }
  }

  /* ── trilha dos dados: atualização automática ── */
  const CICLO = 20; let falta = CICLO, rodando = false, visivel = false;
  function hora() { return new Date().toLocaleTimeString("pt-BR", { hour: "2-digit", minute: "2-digit", second: "2-digit" }); }
  async function atualizar(manual) {
    if (rodando) return; rodando = true; rodada++;
    const nos = [...raiz.querySelectorAll(".vs-no")];
    for (const n of nos) { n.classList.add("ativo"); await new Promise(r => setTimeout(r, reduz ? 60 : 450)); }
    // dados novos: pequenas variações nos três escopos
    const f = 1 + (0.002 + Math.random() * 0.006);
    Object.values(PERFIS).forEach(P => { P.fat *= f; P.rec = Math.max(0, Math.round(P.rec * (0.97 + Math.random() * 0.05))); P.meta = Math.round(P.meta * f * 10) / 10; });
    const linhas = 8000 + Math.floor(Math.random() * 9000), arq = 3 + Math.floor(Math.random() * 4);
    const log = raiz.querySelector("#vsLog");
    log.insertAdjacentHTML("afterbegin", `<li><time>${hora()}</time> ${arq} arquivos lidos · ${nf(linhas)} linhas tratadas · 0 erros · painel atualizado${manual ? " (manual)" : ""}</li>`);
    while (log.children.length > 4) log.lastElementChild.remove();
    render(false);
    raiz.querySelectorAll(".vs-kpi:not(.vs-bloq) b").forEach(b => { b.classList.remove("vs-pisca"); void b.offsetWidth; b.classList.add("vs-pisca"); });
    raiz.querySelector("#vsUlt").textContent = hora();
    setTimeout(() => nos.forEach(n => n.classList.remove("ativo")), 900);
    falta = CICLO; rodando = false;
  }
  setInterval(() => {
    if (!visivel || document.hidden) return;
    falta--; const el = raiz.querySelector("#vsFalta"); if (el) el.textContent = `00:${String(Math.max(falta, 0)).padStart(2, "0")}`;
    if (falta <= 0) atualizar(false);
  }, 1000);
  new IntersectionObserver(es => es.forEach(e => { visivel = e.isIntersecting; }), { threshold: 0.15 }).observe(raiz);

  /* ── antes e depois ── */
  const CASES = {
    pernambucanas: { nome: "Pernambucanas", img: "21.jpg", cor: "#1A285B", cor2: "#FFDD00", txt2: "#1A285B",
      antes: ["Reclamações em várias planilhas", "Consolidação manual toda semana", "Mesmo arquivo para todos os cargos"],
      depois: "Base atualizada sozinha em painéis com acesso por perfil",
      kpis: [["Acesso", "Por perfil"], ["Atualização", "Automática"], ["Fontes", "Consolidadas"]] },
    bradesco: { nome: "Bradesco", img: "20.jpg", cor: "#CC092F", cor2: "#F36279", txt2: "#fff",
      antes: ["Extrações SQL e Excel separadas", "Copia e cola entre arquivos", "Conferência linha a linha"],
      depois: "Consolidação de grande volume de dados em dashboards",
      kpis: [["Bases", "Consolidadas"], ["Volume", "Alto"], ["Ferramentas", "SQL · Python"]] },
    renner: { nome: "Renner", img: "18.jpg", cor: "#191919", cor2: "#D71920", txt2: "#fff",
      antes: ["Faturamento por loja em arquivos soltos", "Folha de ponto à parte", "Relatório montado à mão"],
      depois: "Faturamento consolidado e folha de ponto",
      kpis: [["Faturamento", "Consolidado"], ["Folha de ponto", "Integrada"], ["Relatório", "Automático"]] },
  };
  let caseAtual = "pernambucanas";
  function planilha(c) {
    const cel = (t, cls = "") => `<td class="${cls}">${t}</td>`;
    const lin = [
      ["Loja", "Jan", "Fev", "Mar", "Total"],
      ["Centro", "94.210", "88.904", "#REF!", "=SOMA(B2:D2)"],
      ["Paulista", "87.115", "  91203", "90.488", "268.806"],
      ["norte ", "71.330", "#N/D", "69.912", "141.242"],
      ["Campinas", "61.002", "60.874", "63.1", "184.976"],
      ["Santos", "", "55.410", "57.003", "112.413"],
      ["TOTAL", "313.657", "?", "conferir", "707.437"],
    ];
    return `<div class="ad-xls"><div class="ad-xls-bar"><span>📄 ${c.antes[0].toLowerCase().includes("reclama") ? "reclamacoes_consolidado_v7_FINAL.xlsx" : "base_consolidada_v3_agora_vai.xlsx"}</span></div>
      <table>${lin.map((l, i) => `<tr>${l.map((t, j) => cel(t, i === 0 ? "h" : /#|\?|conferir/.test(t) ? "err" : (i + j) % 5 === 0 ? "amarelo" : "")).join("")}</tr>`).join("")}</table>
      <div class="ad-post">⚠️ ${c.antes[1]}!!<br>${c.antes[2]}</div>
      <div class="ad-ilustra">ilustração</div><div class="ad-abas"><span>Plan1</span><span>Plan1 (2)</span><span>COPIA não mexer</span></div></div>`;
  }
  function painelPronto(c) {
    return `<div class="ad-dash" style="--ca:${c.cor};--cb:${c.cor2};--ct:${c.txt2}"><div class="ad-dash-top"><b>${c.nome}</b><span>atualizado automaticamente</span></div>
      <div class="ad-dash-kpis">${c.kpis.map(([k, v]) => `<div><small>${k}</small><b>${v}</b></div>`).join("")}</div>
      <div class="ad-dash-graf" role="img" aria-label="Gráfico mensal ilustrativo de janeiro a dezembro">${[42, 55, 48, 63, 58, 71, 69, 77, 74, 82, 79, 88].map((h, i) => `<div class="ad-col" style="--hn:${(h / 88).toFixed(3)}"><div class="ad-area"><i></i><em>${h}</em></div><span>${["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"][i]}</span></div>`).join("")}</div>
      <small class="ad-dash-nota">valores ilustrativos</small>
      <p>${c.depois}</p></div>`;
  }
  function renderAD() {
    const c = CASES[caseAtual];
    raiz.querySelectorAll("[data-ad-case]").forEach(b => { const on = b.dataset.adCase === caseAtual; b.classList.toggle("on", on); b.setAttribute("aria-pressed", on); });
    raiz.querySelector("#adAntes").innerHTML = planilha(c);
    raiz.querySelector("#adDepois").innerHTML = painelPronto(c);
    raiz.querySelector("#adVerCase").dataset.img = "assets/img_cases_suceso/" + c.img;
    raiz.querySelector("#adVerCase").textContent = `Ver o case ${c.nome} completo`;
  }
  function posicao(p) {
    p = Math.max(0, Math.min(100, p));
    const box = raiz.querySelector("#adBox"); box.style.setProperty("--p", p + "%");
    raiz.querySelector("#adRange").value = p;
  }

  /* ── montagem inicial ── */
  raiz.innerHTML = `
    <div class="vs-grade">
      <div class="vs-col">
        <div class="vs-perfis" role="group" aria-label="Entrar como">
          ${Object.entries(PERFIS).map(([k, P]) => `<button type="button" data-vs-perfil="${k}" aria-pressed="false"><span>${P.ico}</span><b>${P.nome}</b><small>${P.escopo}</small></button>`).join("")}
        </div>
        <div class="vs-tela">
          <div class="vs-login" id="vsLogin"></div>
          <div id="vsPainel" aria-live="polite"></div>
          <label class="vs-toggle"><input type="checkbox" id="vsMostra" checked> Mostrar os blocos bloqueados (desmarque para ver como o usuário enxerga: eles somem)</label>
        </div>
      </div>
      <aside class="vs-trilha" aria-label="Caminho dos dados">
        <h3>Caminho dos dados</h3>
        <p class="vs-trilha-sub">Sem ninguém abrir planilha: a cada ciclo os dados passam por aqui e o painel se atualiza.</p>
        <ol class="vs-nos">
          <li class="vs-no"><span>🗂️</span><div><b>Origem</b><small>ERP, planilhas das lojas e base de reclamações</small></div></li>
          <li class="vs-no"><span>🐍</span><div><b>Python + SQL</b><small>leitura, limpeza, regras de negócio e validação</small></div></li>
          <li class="vs-no"><span>🗄️</span><div><b>Base consolidada</b><small>tabelas tratadas, histórico e perfis de acesso</small></div></li>
          <li class="vs-no"><span>📊</span><div><b>Painel</b><small>cada login recebe só o seu escopo</small></div></li>
        </ol>
        <div class="vs-status"><div><small>Próxima atualização</small><b id="vsFalta">00:${CICLO}</b></div><div><small>Última</small><b id="vsUlt">—</b></div>
          <button type="button" class="btn btn-ghost" id="vsAgora">⟳ Atualizar agora</button></div>
        <ul class="vs-log" id="vsLog"><li><time>—</time> aguardando o primeiro ciclo…</li></ul>
      </aside>
    </div>

    <div class="ad">
      <div class="ad-topo"><div><h3>Antes e depois</h3><p>Arraste a barra: da planilha manual ao painel pronto.</p></div>
        <div class="ad-cases" role="group" aria-label="Escolha o case">${Object.entries(CASES).map(([k, c]) => `<button type="button" data-ad-case="${k}" aria-pressed="false">${c.nome}</button>`).join("")}</div></div>
      <div class="ad-box" id="adBox" style="--p:50%">
        <div class="ad-camada ad-depois" id="adDepois"></div>
        <div class="ad-camada ad-antes" id="adAntes"></div>
        <div class="ad-rot ad-rot-a">Antes</div><div class="ad-rot ad-rot-d">Depois</div>
        <div class="ad-alca" aria-hidden="true"><span>⇆</span></div>
        <input type="range" id="adRange" min="0" max="100" value="50" aria-label="Comparar antes e depois">
      </div>
      <div class="ad-rodape"><button type="button" class="btn btn-ghost" id="adVerCase">Ver o case completo</button>
        <button type="button" class="btn btn-primary" data-vs="cta">Quero isso na minha empresa →</button></div>
    </div>
    <p class="vs-aviso">Demonstração com dados fictícios. Nomes de lojas, valores e pessoas são ilustrativos.</p>`;
  render(false); renderAD();

  /* ── eventos ── */
  raiz.addEventListener("click", e => {
    const p = e.target.closest("[data-vs-perfil]");
    if (p && p.dataset.vsPerfil !== perfil) { perfil = p.dataset.vsPerfil; render(true); evento("visoes_perfil", { perfil }); }
    const c = e.target.closest("[data-ad-case]");
    if (c) { caseAtual = c.dataset.adCase; renderAD(); evento("antes_depois", { case: caseAtual }); }
    if (e.target.closest("#vsAgora")) atualizar(true);
    if (e.target.closest('[data-vs="cta"]')) { evento("visoes_cta"); if (typeof window.diagIniciar === "function") window.diagIniciar({ dor: "dashboards", origem: "tres-visoes" }); else location.hash = "#contato"; }
  });
  raiz.querySelector("#vsMostra").addEventListener("change", e => { mostrarBloqueios = e.target.checked; render(true); });
  raiz.querySelector("#adRange").addEventListener("input", e => posicao(+e.target.value));
  // arrastar direto na imagem (mouse e toque)
  const box = raiz.querySelector("#adBox"); let arrastando = false;
  const mover = x => { const r = box.getBoundingClientRect(); posicao((x - r.left) / r.width * 100); };
  box.addEventListener("pointerdown", e => { arrastando = true; box.setPointerCapture(e.pointerId); mover(e.clientX); });
  box.addEventListener("pointermove", e => { if (arrastando) mover(e.clientX); });
  ["pointerup", "pointercancel"].forEach(t => box.addEventListener(t, () => { arrastando = false; }));
})();
