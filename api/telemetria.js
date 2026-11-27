// Telemetria do site: recebe os eventos do navegador, junta IP e localização
// (cabeçalhos da Vercel) e grava no Supabase pela função registrar_telemetria.
// Sem aceite de cookies: grava só dados anônimos (sem IP, cidade, coordenadas nem user agent).
const SUPABASE_URL = "https://qggvnsoxkjqwsxpfutyi.supabase.co";
// chave publicável (pública por definição): só consegue chamar registrar_telemetria; as tabelas não podem ser lidas com ela
const SUPABASE_KEY = process.env.SUPABASE_PUBLISHABLE_KEY || "sb_publishable_YwVIhm1KANQSEJyNTGP3yA_pIkKtyog";
const ESTADOS = { AC: "Acre", AL: "Alagoas", AP: "Amapá", AM: "Amazonas", BA: "Bahia", CE: "Ceará", DF: "Distrito Federal", ES: "Espírito Santo", GO: "Goiás", MA: "Maranhão", MT: "Mato Grosso", MS: "Mato Grosso do Sul", MG: "Minas Gerais", PA: "Pará", PB: "Paraíba", PR: "Paraná", PE: "Pernambuco", PI: "Piauí", RJ: "Rio de Janeiro", RN: "Rio Grande do Norte", RS: "Rio Grande do Sul", RO: "Rondônia", RR: "Roraima", SC: "Santa Catarina", SP: "São Paulo", SE: "Sergipe", TO: "Tocantins" };
const BOT = /bot|crawl|spider|slurp|bingpreview|facebookexternalhit|whatsapp|telegram|headless|lighthouse|pingdom|uptime|curl|wget|python|axios|node-fetch/i;
const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

const cab = (req, n) => { const v = req.headers[n]; return Array.isArray(v) ? v[0] : v || ""; };
const dec = v => { try { return decodeURIComponent(v); } catch (_) { return v; } };

module.exports = async function handler(req, res) {
  if (req.method !== "POST") { res.setHeader("Allow", "POST"); return res.status(405).end(); }
  let corpo = req.body;
  try { if (typeof corpo === "string") corpo = JSON.parse(corpo); else if (Buffer.isBuffer(corpo)) corpo = JSON.parse(corpo.toString("utf8")); } catch (_) { return res.status(400).end(); }
  const sessao = corpo && corpo.sessao, eventos = Array.isArray(corpo && corpo.eventos) ? corpo.eventos.slice(0, 100) : [];
  if (!sessao || !UUID.test(sessao.id || "") || !UUID.test(sessao.visitante_id || "")) return res.status(400).end();

  // só deste site
  const origem = cab(req, "origin") || cab(req, "referer");
  if (origem && !/^https?:\/\/(www\.)?(skydatasolution\.com\.br|rodrigoaiosa\.vercel\.app|[a-z0-9-]+\.vercel\.app|localhost(:\d+)?)/i.test(origem)) return res.status(403).end();

  const ua = cab(req, "user-agent");
  const aceite = sessao.consentimento === true;
  const uf = cab(req, "x-vercel-ip-country-region").toUpperCase();
  const pais = cab(req, "x-vercel-ip-country").toUpperCase();
  const dados = {
    ...sessao,
    pais_codigo: pais || null,
    pais: pais === "BR" ? "Brasil" : pais || null,
    estado_codigo: uf || null,
    estado: pais === "BR" ? ESTADOS[uf] || uf || null : uf || null,
    fuso_horario: cab(req, "x-vercel-ip-timezone") || null,
    eh_bot: BOT.test(ua) || sessao.eh_bot === true,
  };
  if (aceite) {
    const ip = (cab(req, "x-forwarded-for").split(",")[0] || cab(req, "x-real-ip")).trim();
    const cidade = dec(cab(req, "x-vercel-ip-city")) || null;
    Object.assign(dados, {
      ip: ip || null, cidade, municipio: cidade,
      cep: cab(req, "x-vercel-ip-postal-code") || null,
      latitude: cab(req, "x-vercel-ip-latitude") || null,
      longitude: cab(req, "x-vercel-ip-longitude") || null,
      origem_localizacao: cab(req, "x-vercel-ip-latitude") ? "ip" : null,
      user_agent: ua.slice(0, 500),
    });
  } else {
    for (const k of ["ip", "cidade", "municipio", "cep", "latitude", "longitude", "origem_localizacao", "user_agent"]) dados[k] = null;
  }

  try {
    const r = await fetch(`${SUPABASE_URL}/rest/v1/rpc/registrar_telemetria`, {
      method: "POST",
      headers: { apikey: SUPABASE_KEY, Authorization: `Bearer ${SUPABASE_KEY}`, "Content-Type": "application/json" },
      body: JSON.stringify({ p_sessao: dados, p_eventos: eventos }),
    });
    if (!r.ok) { console.error("telemetria", r.status, (await r.text()).slice(0, 300)); return res.status(502).end(); }
    return res.status(204).end();
  } catch (e) {
    console.error("telemetria", e.message);
    return res.status(502).end();
  }
};
