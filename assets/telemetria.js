/* ═══════════════════════════════════════════════════════════════════
   Telemetria do site (Supabase via /api/telemetria)
   - Faixa de cookies: com aceite grava a visita completa (IP, cidade,
     aparelho, cliques); sem aceite, só contagem anônima.
   - Nunca envia dados digitados em formulários nem planilhas do Raio-X.
   ═══════════════════════════════════════════════════════════════════ */
(() => {
  const ENDPOINT = "/api/telemetria";
  const CHAVE_ACEITE = "sky_telemetria_aceite"; // "sim" | "nao"
  const ls = { get: k => { try { return localStorage.getItem(k); } catch (_) { return null; } }, set: (k, v) => { try { localStorage.setItem(k, v); } catch (_) {} } };
  const ss = { get: k => { try { return sessionStorage.getItem(k); } catch (_) { return null; } }, set: (k, v) => { try { sessionStorage.setItem(k, v); } catch (_) {} } };
  const uuid = () => (crypto.randomUUID ? crypto.randomUUID() : "10000000-1000-4000-8000-100000000000".replace(/[018]/g, c => (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)));
  const agora = () => new Date().toISOString();
  const txt = (s, n = 120) => String(s || "").replace(/\s+/g, " ").trim().slice(0, n);

  let aceite = ls.get(CHAVE_ACEITE);

  // ── identificação ──
  // visitante: persistente só com aceite; sem aceite, vale só para esta aba
  let visitante = aceite === "sim" ? ls.get("sky_visitante") : ss.get("sky_visitante_tmp");
  if (!visitante) { visitante = uuid(); if (aceite === "sim") ls.set("sky_visitante", visitante); else ss.set("sky_visitante_tmp", visitante); }
  // sessão: nova após 30 min sem atividade
  let sessao = ss.get("sky_sessao"), ultima = +ss.get("sky_sessao_ult") || 0;
  if (!sessao || Date.now() - ultima > 30 * 60 * 1000) { sessao = uuid(); ss.set("sky_sessao", sessao); }
  const toque = () => ss.set("sky_sessao_ult", String(Date.now()));
  toque();

  // ── aparelho e navegador ──
  function ambiente() {
    const ua = navigator.userAgent || "", d = navigator.userAgentData;
    const tablet = /iPad|Tablet|PlayBook|Silk|(Android(?!.*Mobile))/i.test(ua) || (/Macintosh/.test(ua) && navigator.maxTouchPoints > 1);
    const mobile = !tablet && (/Mobi|iPhone|iPod|Android.*Mobile|Windows Phone/i.test(ua) || (d && d.mobile));
    const nav = [[/Edg\/([\d.]+)/, "Edge"], [/OPR\/([\d.]+)/, "Opera"], [/SamsungBrowser\/([\d.]+)/, "Samsung Internet"], [/Firefox\/([\d.]+)/, "Firefox"], [/CriOS\/([\d.]+)/, "Chrome"], [/Chrome\/([\d.]+)/, "Chrome"], [/Version\/([\d.]+).*Safari/, "Safari"]].find(([re]) => re.test(ua));
    const so = [[/Windows NT ([\d.]+)/, "Windows"], [/Android ([\d.]+)/, "Android"], [/(?:iPhone|iPad|iPod).*OS ([\d_]+)/, "iOS"], [/Mac OS X ([\d_]+)/, "macOS"], [/CrOS/, "ChromeOS"], [/Linux/, "Linux"]].find(([re]) => re.test(ua));
    const ref = document.referrer || "";
    let refDom = ""; try { refDom = ref ? new URL(ref).hostname : ""; } catch (_) {}
    const q = new URLSearchParams(location.search);
    const con = navigator.connection || {};
    const modelo = (ua.match(/Android [\d.]+; ([^;)]+)/) || [])[1];
    return {
      id: sessao, visitante_id: visitante, consentimento: aceite === "sim" ? true : aceite === "nao" ? false : null,
      dispositivo: tablet ? "tablet" : mobile ? "mobile" : "desktop",
      fabricante: /iPhone|iPad|Macintosh/.test(ua) ? "Apple" : /Samsung|SM-/.test(ua) ? "Samsung" : /Motorola|moto/i.test(ua) ? "Motorola" : /Xiaomi|Redmi|POCO/i.test(ua) ? "Xiaomi" : null,
      modelo: modelo ? txt(modelo, 80) : null,
      sistema_operacional: so ? so[1] : null, so_versao: so && ua.match(so[0]) && ua.match(so[0])[1] ? ua.match(so[0])[1].replace(/_/g, ".") : null,
      navegador: nav ? nav[1] : null, navegador_versao: nav ? (ua.match(nav[0])[1] || "").split(".")[0] : null,
      idioma: navigator.language || null, idiomas: (navigator.languages || []).join(",").slice(0, 120) || null,
      tela_largura: screen.width, tela_altura: screen.height, janela_largura: innerWidth, janela_altura: innerHeight,
      densidade_pixels: Math.round((devicePixelRatio || 1) * 100) / 100, toque: navigator.maxTouchPoints > 0,
      tipo_conexao: con.effectiveType || null, modo_escuro: matchMedia("(prefers-color-scheme: dark)").matches,
      eh_bot: !!navigator.webdriver,
      referrer: ref.slice(0, 500) || null, referrer_dominio: refDom && refDom !== location.hostname ? refDom : null,
      utm_source: q.get("utm_source"), utm_medium: q.get("utm_medium"), utm_campaign: q.get("utm_campaign"), utm_term: q.get("utm_term"), utm_content: q.get("utm_content"),
      gclid: q.get("gclid"), fbclid: q.get("fbclid"),
    };
  }

  // ── fila e envio ──
  let fila = [], tempoAtivo = 0, visivelDesde = document.visibilityState === "visible" ? Date.now() : 0;
  const ativoMs = () => tempoAtivo + (visivelDesde ? Date.now() - visivelDesde : 0);
  function registrar(tipo, extra = {}) {
    toque();
    fila.push({ tipo, ocorrido_em: agora(), pagina_url: location.pathname + location.hash, pagina_titulo: txt(document.title, 200), ...extra });
    if (fila.length >= 20) enviar();
  }
  function enviar(final) {
    if (!fila.length) return;
    const corpo = JSON.stringify({ sessao: ambiente(), eventos: fila.splice(0, 100) });
    const blob = new Blob([corpo], { type: "text/plain" }); // text/plain: sem pré-verificação CORS
    if (final && navigator.sendBeacon && navigator.sendBeacon(ENDPOINT, blob)) return;
    fetch(ENDPOINT, { method: "POST", body: blob, keepalive: true }).catch(() => {});
  }
  setInterval(() => enviar(), 8000);

  // ── eventos automáticos ──
  registrar("page_view", { dados: { largura: innerWidth } });

  // seções vistas (uma vez cada, quando ao menos 35% aparece)
  const vistas = new Set();
  const io = "IntersectionObserver" in window ? new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting && !vistas.has(e.target.id)) { vistas.add(e.target.id); registrar("secao_vista", { secao: "#" + e.target.id }); }
  }), { threshold: 0.35 }) : null;
  const observar = () => document.querySelectorAll("section[id], header[id]").forEach(s => io && io.observe(s));
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", observar); else observar();

  // rolagem: marcos de 25, 50, 75 e 100%
  let scrollMax = 0; const marcos = new Set();
  addEventListener("scroll", () => {
    const h = document.documentElement, p = Math.min(100, Math.round((scrollY + innerHeight) / Math.max(1, h.scrollHeight) * 100));
    if (p > scrollMax) scrollMax = p;
    [25, 50, 75, 100].forEach(m => { if (p >= m && !marcos.has(m)) { marcos.add(m); registrar("scroll", { scroll_pct: m }); } });
  }, { passive: true });

  // cliques em links e botões (texto do botão, nunca o que foi digitado)
  document.addEventListener("click", e => {
    const el = e.target.closest("a, button, [role=button], [data-cta], summary, label[for]");
    if (!el || el.closest("#telConsent")) return;
    const href = el.getAttribute("href") || "";
    const ext = /^https?:/i.test(href) && !href.includes(location.hostname);
    const download = el.hasAttribute("download") || /\.(pdf|xlsx|csv|zip|pptx|docx|mp4)(\?|$)/i.test(href);
    registrar(download ? "download" : el.dataset.cta ? "cta" : "clique", {
      nome: el.dataset.cta ? "cta_" + el.dataset.cta : el.dataset.rx ? "raiox_" + el.dataset.rx : null,
      secao: el.closest("section[id]") ? "#" + el.closest("section[id]").id : null,
      elemento: txt((el.id ? "#" + el.id : el.tagName.toLowerCase()) + (el.className && typeof el.className === "string" ? "." + el.className.trim().split(/\s+/).slice(0, 2).join(".") : ""), 200),
      elemento_texto: txt(el.getAttribute("aria-label") || el.textContent, 120),
      link_destino: href ? href.slice(0, 500) : null,
      posicao_x: Math.round(e.pageX), posicao_y: Math.round(e.pageY),
      dados: ext ? { externo: true } : {},
    });
  }, true);

  // vídeos (play, pausa, fim) — ex.: vídeo do Raio-X e da seção Sobre
  ["play", "pause", "ended"].forEach(t => document.addEventListener(t, e => {
    if (e.target.tagName !== "VIDEO") return;
    const v = e.target; registrar("video", { nome: "video_" + t, secao: v.closest("section[id]") ? "#" + v.closest("section[id]").id : null, valor: Math.round(v.currentTime), duracao_ms: Math.round((v.duration || 0) * 1000) });
  }, true));

  // eventos que o site já dispara (track → window.va): CTAs, diagnóstico, Raio-X, lead
  const vaOriginal = window.va;
  window.va = function (tipo, p) {
    try {
      if (tipo === "event" && p && p.name) {
        const n = String(p.name), d = p.data && typeof p.data === "object" ? p.data : {};
        const t = /^raiox/.test(n) ? "raiox" : /^(lead|diag)/.test(n) ? "formulario" : /^cta/.test(n) ? "cta" : /^visoes|^antes_depois/.test(n) ? "clique" : "custom";
        if (!/^cta_/.test(n)) registrar(t, { nome: txt(n, 80), dados: d }); // os cta_ já entram pelo clique
        if (n === "lead_enviado") enviar();
      }
    } catch (_) {}
    if (typeof vaOriginal === "function") return vaOriginal.apply(this, arguments);
  };

  // erros de JavaScript (para achar problemas no site)
  addEventListener("error", e => registrar("erro", { nome: "js", dados: { msg: txt(e.message, 200), arquivo: txt((e.filename || "").split("/").pop(), 80), linha: e.lineno } }));

  // aba visível / escondida e saída
  document.addEventListener("visibilitychange", () => {
    if (document.visibilityState === "hidden") {
      if (visivelDesde) { tempoAtivo += Date.now() - visivelDesde; visivelDesde = 0; }
      registrar("visibilidade", { nome: "aba_escondida", duracao_ms: ativoMs(), scroll_pct: scrollMax });
      enviar(true);
    } else { visivelDesde = Date.now(); }
  });
  addEventListener("pagehide", () => { registrar("saida", { duracao_ms: ativoMs(), scroll_pct: scrollMax }); enviar(true); });

  // ── faixa de cookies (LGPD) ──
  // Com aceite grava tudo (IP, cidade, coordenadas); sem aceite segue sem esses três.
  // Para esconder o aviso, troque para false.
  const MOSTRAR_AVISO = true;
  if (aceite || !MOSTRAR_AVISO) return;
  const css = `#telConsent{position:fixed;left:16px;right:16px;bottom:16px;z-index:9999;max-width:980px;margin:0 auto;background:#0d1320;color:#d9e6f2;border:1px solid rgba(0,180,216,.35);border-radius:14px;box-shadow:0 12px 40px rgba(0,0,0,.5);padding:16px 18px;display:flex;gap:12px 18px;align-items:center;flex-wrap:wrap;font:14px/1.5 inherit}
#telConsent p{margin:0;flex:1 1 420px}#telConsent b{color:#fff}#telConsent .tel-acoes{display:flex;gap:8px;flex-wrap:wrap}
#telConsent button{font:inherit;font-weight:600;border-radius:10px;padding:9px 16px;cursor:pointer;border:1px solid rgba(255,255,255,.2);background:transparent;color:#d9e6f2}
#telConsent button.tel-sim{background:#00b4d8;border-color:#00b4d8;color:#031018}#telConsent a{color:#48cae4}
#telPolitica{max-width:640px;width:calc(100% - 32px);border:1px solid rgba(0,180,216,.35);border-radius:14px;background:#0d1320;color:#d9e6f2;padding:22px 24px;font:14px/1.6 inherit}
#telPolitica::backdrop{background:rgba(0,0,0,.6)}#telPolitica h3{margin:0 0 10px;color:#fff}#telPolitica ul{padding-left:18px;margin:8px 0}#telPolitica button{margin-top:12px;font:inherit;font-weight:600;border-radius:10px;padding:8px 16px;cursor:pointer;border:0;background:#00b4d8;color:#031018}
@media (max-width:560px){#telConsent{left:10px;right:10px;bottom:10px;padding:14px}#telConsent .tel-acoes{width:100%}#telConsent button{flex:1}}`;
  function faixa() {
    const st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
    const div = document.createElement("div"); div.id = "telConsent"; div.setAttribute("role", "region"); div.setAttribute("aria-label", "Aviso de cookies");
    div.innerHTML = `<p>🍪 Usamos cookies e dados de navegação,<b></b>, para entender como o site é usado e melhorá-lo. <a href="#" data-tel="politica">Saiba mais</a></p>
      <div class="tel-acoes"><button type="button" data-tel="sim">Só o essencial</button><button type="button" class="tel-sim" data-tel="sim">Aceitar</button></div>`;
    document.body.appendChild(div);
    div.addEventListener("click", e => {
      const b = e.target.closest("[data-tel]"); if (!b) return; e.preventDefault();
      if (b.dataset.tel === "politica") return politica();
      aceite = b.dataset.tel; ls.set(CHAVE_ACEITE, aceite);
      if (aceite === "sim") { const tmp = visitante; ls.set("sky_visitante", tmp); }
      registrar("custom", { nome: aceite === "sim" ? "cookies_aceitos" : "cookies_recusados" }); enviar();
      div.remove();
    });
  }
  function politica() {
    let d = document.getElementById("telPolitica");
    if (!d) {
      d = document.createElement("dialog"); d.id = "telPolitica";
      d.innerHTML = `<h3>Como usamos os seus dados de navegação</h3>
        <p>Com o seu aceite, registramos:</p>
        <ul><li>endereço IP e localização aproximada a partir dele (país, estado, cidade);</li>
        <li>tipo de aparelho, sistema, navegador, idioma e tamanho da tela;</li>
        <li>de onde você veio (site de origem e campanha) e o que fez aqui: páginas e seções vistas, cliques, rolagem e tempo na página.</li></ul>
        <p>Sem o aceite, registramos só dados anônimos de uso, sem IP, cidade nem identificação do aparelho.</p>
        <p>Os dados servem apenas para medir e melhorar o site, não são vendidos nem compartilhados. Nunca registramos o que você digita nos formulários nem o conteúdo das planilhas enviadas ao Raio-X, que são analisadas só no seu navegador.</p>
        <p>Você pode mudar sua escolha limpando os dados do site no navegador. Para pedir acesso ou exclusão dos seus dados, fale conosco pelo formulário de contato.</p>
        <button type="button">Entendi</button>`;
      document.body.appendChild(d);
      d.querySelector("button").addEventListener("click", () => d.close());
    }
    if (d.showModal) d.showModal(); else d.setAttribute("open", "");
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", faixa); else faixa();
})();
