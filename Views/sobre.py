import streamlit as st
import time
from utils import registrar_acesso, exibir_rodape

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(layout="wide", page_title="Portfolio | Rodrigo Aiosa")

# 2. REGISTRO DE ACESSO
registrar_acesso("Sobre Mim")

# --- PALETA DE CORES PARA CONVERSÃO ---
CORES = {
    'primary': '#FF6B35',      # Laranja (urgência, ação)
    'secondary': '#004E89',    # Azul escuro (confiança)
    'accent': '#F77F00',       # Laranja vibrante (CTAs)
    'success': '#06D6A0',      # Verde (sucesso)
    'dark': '#0A0E27',         # Quase preto (elegância)
    'light': '#F8F9FA',        # Branco suave
    'text_muted': '#ADB5BD'    # Cinza
}

# --- ESTILO CSS COMPLETO OTIMIZADO PARA CONVERSÃO ---
st.markdown(f"""
    <style>
    /* RESET E CONFIGURAÇÕES GLOBAIS */
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}
    
    /* GRADIENT HERO SECTION */
    .hero-gradient {{
        background: linear-gradient(135deg, {CORES['dark']} 0%, #1a1f3a 100%);
        padding: 60px 20px 40px;
        border-radius: 0 0 50px 50px;
        margin-top: -80px;
        margin-bottom: 40px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    }}
    
    /* PROFILE PIC - Maior e com border animado */
    .profile-pic {{
        display: flex;
        justify-content: center;
        margin-bottom: 25px;
        position: relative;
    }}
    
    .profile-pic::before {{
        content: '';
        position: absolute;
        width: 220px;
        height: 220px;
        border-radius: 50%;
        background: linear-gradient(45deg, {CORES['primary']}, {CORES['accent']});
        animation: pulse-border 2s ease-in-out infinite;
        z-index: -1;
    }}
    
    @keyframes pulse-border {{
        0%, 100% {{ transform: scale(1); opacity: 0.5; }}
        50% {{ transform: scale(1.1); opacity: 0.8; }}
    }}
    
    .profile-pic img {{
        border-radius: 50%;
        width: 200px;
        height: 200px;
        object-fit: cover;
        border: 6px solid {CORES['dark']};
        box-shadow: 0 8px 30px rgba(255, 107, 53, 0.4);
    }}
    
    /* TÍTULO COM EFEITO GRADIENTE */
    .main-title {{
        text-align: center;
        font-size: 3.5em;
        font-weight: 800;
        background: linear-gradient(135deg, {CORES['primary']} 0%, {CORES['accent']} 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 15px 0;
        letter-spacing: -1px;
    }}
    
    /* SUBTITLE COM MAIS DESTAQUE */
    .subtitle {{
        text-align: center;
        font-size: 1.3em;
        color: {CORES['text_muted']};
        font-weight: 400;
        margin-bottom: 30px;
        line-height: 1.6;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }}
    
    /* TRUST BADGES */
    .trust-badge {{
        display: inline-block;
        background: {CORES['success']};
        color: white;
        padding: 8px 20px;
        border-radius: 20px;
        font-size: 0.9em;
        font-weight: 600;
        margin: 5px;
        box-shadow: 0 4px 15px rgba(6, 214, 160, 0.3);
    }}
    
    .trust-badges-container {{
        text-align: center;
        margin-top: 20px;
    }}
    
    /* CTA BUTTON - BOTÃO DE CONVERSÃO */
    .cta-button {{
        display: inline-block;
        background: linear-gradient(135deg, {CORES['primary']} 0%, {CORES['accent']} 100%);
        color: white;
        padding: 18px 45px;
        border-radius: 50px;
        font-size: 1.2em;
        font-weight: 700;
        text-decoration: none;
        box-shadow: 0 8px 25px rgba(255, 107, 53, 0.4);
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        text-align: center;
        margin: 20px auto;
        display: block;
        width: fit-content;
    }}
    
    .cta-button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(255, 107, 53, 0.6);
        text-decoration: none;
        color: white;
    }}
    
    .cta-secondary {{
        background: transparent;
        border: 2px solid {CORES['primary']};
        color: {CORES['primary']};
        box-shadow: none;
    }}
    
    .cta-secondary:hover {{
        background: rgba(255, 107, 53, 0.1);
        color: {CORES['primary']};
    }}
    
    /* CARDS MODERNOS - Diretos e limpos */
    .stat-card {{
        background: linear-gradient(135deg, #1a1f3a 0%, {CORES['dark']} 100%);
        border-radius: 20px;
        padding: 30px 20px;
        text-align: center;
        border: 1px solid rgba(255, 107, 53, 0.2);
        transition: all 0.3s ease;
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        position: relative;
        overflow: hidden;
        margin-bottom: 20px;
    }}
    
    .stat-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, {CORES['primary']}, {CORES['accent']});
    }}
    
    .stat-card:hover {{
        transform: translateY(-8px);
        box-shadow: 0 15px 40px rgba(255, 107, 53, 0.3);
        border-color: {CORES['primary']};
    }}
    
    .stat-icon {{ 
        font-size: 36px; 
        margin-bottom: 10px;
        filter: grayscale(0.3);
    }}
    
    .stat-number {{ 
        font-size: 42px; 
        font-weight: 900;
        background: linear-gradient(135deg, {CORES['primary']} 0%, {CORES['accent']} 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 10px 0;
    }}
    
    .stat-label {{ 
        font-size: 14px; 
        color: {CORES['text_muted']};
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    
    .stat-description {{
        font-size: 12px;
        color: #6C757D;
        margin-top: 8px;
        font-style: italic;
        line-height: 1.4;
    }}
    
    /* SEÇÃO DE BENEFÍCIOS */
    .benefit-card {{
        background: #1a1f3a;
        border-left: 4px solid {CORES['primary']};
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }}
    
    .benefit-card:hover {{
        background: #242945;
        transform: translateX(10px);
        box-shadow: -5px 5px 20px rgba(255, 107, 53, 0.2);
    }}
    
    .benefit-icon {{
        font-size: 28px;
        margin-right: 15px;
        vertical-align: middle;
    }}
    
    /* SECTION TITLE */
    .section-title {{
        font-size: 2.2em;
        font-weight: 700;
        margin: 40px 0 30px;
        text-align: center;
        color: white;
    }}
    
    .section-subtitle {{
        text-align: center;
        color: {CORES['text_muted']};
        font-size: 1.1em;
        margin-bottom: 40px;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }}
    
    /* SOCIAL PROOF - Logos de clientes */
    .client-logo-section {{
        background: linear-gradient(135deg, {CORES['light']} 0%, #e9ecef 100%);
        padding: 50px 30px;
        border-radius: 30px;
        margin: 40px 0;
        text-align: center;
    }}
    
    .client-logo-section h3 {{
        color: {CORES['dark']};
        margin-bottom: 15px;
        font-weight: 700;
        font-size: 2em;
    }}
    
    .client-subtitle {{
        color: #6C757D;
        margin-bottom: 30px;
        font-size: 1.1em;
    }}
    
    /* TESTIMONIAL CARD */
    .testimonial {{
        background: #1a1f3a;
        padding: 30px;
        border-radius: 20px;
        border-left: 5px solid {CORES['primary']};
        margin: 20px 0;
        position: relative;
    }}
    
    .testimonial::before {{
        content: '"';
        position: absolute;
        top: -10px;
        left: 20px;
        font-size: 80px;
        color: rgba(255, 107, 53, 0.2);
        font-family: Georgia, serif;
    }}
    
    .testimonial-text {{
        font-size: 1.1em;
        line-height: 1.7;
        color: #E9ECEF;
        position: relative;
        z-index: 1;
    }}
    
    .testimonial-author {{
        text-align: right;
        margin-top: 15px;
        color: {CORES['primary']};
        font-weight: 600;
    }}
    
    /* SCARCITY BANNER */
    .scarcity-banner {{
        background: linear-gradient(135deg, {CORES['primary']} 0%, #D64933 100%);
        color: white;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        font-weight: 700;
        margin: 30px 0;
        box-shadow: 0 5px 20px rgba(255, 107, 53, 0.4);
        animation: pulse-glow 2s ease-in-out infinite;
    }}
    
    @keyframes pulse-glow {{
        0%, 100% {{ box-shadow: 0 5px 20px rgba(255, 107, 53, 0.4); }}
        50% {{ box-shadow: 0 8px 30px rgba(255, 107, 53, 0.7); }}
    }}
    
    /* FOOTER CTA */
    .footer-cta {{
        background: linear-gradient(135deg, {CORES['dark']} 0%, #1a1f3a 100%);
        padding: 60px 30px;
        border-radius: 30px;
        text-align: center;
        margin: 50px 0 30px;
        border: 2px solid rgba(255, 107, 53, 0.3);
    }}
    
    .footer-cta h2 {{
        color: white;
        margin-bottom: 20px;
        font-size: 2.5em;
    }}
    
    .footer-cta-text {{
        color: {CORES['text_muted']};
        font-size: 1.1em;
        margin-bottom: 30px;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }}
    
    /* DIVIDER */
    hr {{
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, {CORES['primary']}, transparent);
        margin: 50px 0;
    }}
    
    /* RESPONSIVIDADE */
    @media (max-width: 768px) {{
        .main-title {{
            font-size: 2.5em;
        }}
        
        .subtitle {{
            font-size: 1.1em;
        }}
        
        .stat-card {{
            height: auto;
            min-height: 180px;
        }}
        
        .cta-button {{
            font-size: 1em;
            padding: 15px 35px;
        }}
    }}
    </style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown(f"""
    <div class="hero-gradient">
        <div class="profile-pic">
            <img src="https://media.licdn.com/dms/image/v2/D5603AQFTfyqJswUYwg/profile-displayphoto-scale_200_200/B56ZxDaPuZK4AY-/0/1770657482765?e=1772064000&v=beta&t=1PXFrPJTt5w46Y7NUTgqCQ3H2jjMmkE1QwFi-lwwwko">
        </div>
        <h1 class="main-title">Rodrigo Aiosa</h1>
        <p class="subtitle">
            Transformo dados em decisões estratégicas que <strong>aumentam lucros</strong><br>
            e <strong>reduzem custos operacionais em até 40%</strong>
        </p>
        
        <div class="trust-badges-container">
            <div class="trust-badge">✓ 450+ Empresas Confiaram</div>
            <div class="trust-badge">✓ 87% Taxa de Recompra</div>
            <div class="trust-badge">✓ 20 Anos de Experiência</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- CTA PRINCIPAL ---
st.markdown("""
    <a href="#contato" class="cta-button">
        🚀 Agendar Consultoria Gratuita
    </a>
""", unsafe_allow_html=True)

st.write("")

# --- CARDS DE ESTATÍSTICAS COM CONTADOR ANIMADO ---
st.markdown('<h2 class="section-title">⭐ Resultados Comprovados</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Números que falam por si: experiência, confiança e excelência em cada projeto</p>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
placeholders = [c1.empty(), c2.empty(), c3.empty(), c4.empty()]

stats_data = [
    ("20+", "Anos de<br>Experiência", "🏆", "Expertise consolidada em análise preditiva e BI"),
    ("450+", "Empresas<br>Atendidas", "🏢", "Soluções personalizadas para grandes players"),
    ("500+", "Projetos<br>Entregues", "📊", "Dashboards estratégicos focados em ROI"),
    ("87%", "Taxa de<br>Recompra", "🤝", "Baseado em resultados reais e confiança mútua")
]

# Animação dos números
for i in range(0, 101, 5):
    values = [
        int(20 * i / 100),
        int(450 * i / 100),
        int(500 * i / 100),
        int(87 * i / 100)
    ]
    
    for idx, (placeholder, value, (final, label, icon, desc)) in enumerate(zip(placeholders, values, stats_data)):
        display_val = f"{value}+" if idx < 3 else f"{value}%"
        placeholder.markdown(f"""
            <div class="stat-card">
                <div class="stat-icon">{icon}</div>
                <div class="stat-number">{display_val}</div>
                <div class="stat-label">{label}</div>
                <div class="stat-description">{desc}</div>
            </div>
        """, unsafe_allow_html=True)
    
    time.sleep(0.03)

st.markdown("---")

# --- SEÇÃO DE BENEFÍCIOS ---
st.markdown('<h2 class="section-title">💼 Como Posso Transformar Seu Negócio</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Soluções focadas em resultados mensuráveis e impacto direto no seu bottom line</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="benefit-card">
            <span class="benefit-icon">📈</span>
            <strong>Aumento de Receita:</strong> Dashboards inteligentes que identificam oportunidades de vendas escondidas nos seus dados
        </div>
        
        <div class="benefit-card">
            <span class="benefit-icon">⚡</span>
            <strong>Redução de Custos:</strong> Automações em Python que economizam até 200 horas/mês em processos manuais
        </div>
        
        <div class="benefit-card">
            <span class="benefit-icon">🎯</span>
            <strong>Decisões Mais Rápidas:</strong> Visualizações em tempo real para ações estratégicas imediatas
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="benefit-card">
            <span class="benefit-icon">🔒</span>
            <strong>Dados Confiáveis:</strong> Pipelines de ETL robustos que garantem precisão de 99,9%
        </div>
        
        <div class="benefit-card">
            <span class="benefit-icon">🚀</span>
            <strong>Escalabilidade:</strong> Arquiteturas preparadas para crescer junto com seu negócio
        </div>
        
        <div class="benefit-card">
            <span class="benefit-icon">💡</span>
            <strong>Insights Acionáveis:</strong> Análises que geram ações concretas, não apenas relatórios bonitos
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- COMPETÊNCIAS TÉCNICAS ---
st.markdown('<h2 class="section-title">🛠️ Stack Tecnológico</h2>', unsafe_allow_html=True)

tech_col1, tech_col2, tech_col3 = st.columns(3)

with tech_col1:
    st.markdown("""
        <div class="benefit-card">
            <span class="benefit-icon">🐍</span>
            <strong>Python & Análise</strong><br>
            <small>Pandas, NumPy, Scikit-learn, Automações</small>
        </div>
    """, unsafe_allow_html=True)

with tech_col2:
    st.markdown("""
        <div class="benefit-card">
            <span class="benefit-icon">📊</span>
            <strong>Business Intelligence</strong><br>
            <small>Power BI, DAX, M, Excel Avançado</small>
        </div>
    """, unsafe_allow_html=True)

with tech_col3:
    st.markdown("""
        <div class="benefit-card">
            <span class="benefit-icon">🗄️</span>
            <strong>Dados & ETL</strong><br>
            <small>SQL Server, PostgreSQL, Azure, AWS</small>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- SOCIAL PROOF - CLIENTES ---
st.markdown("""
    <div class="client-logo-section">
        <h3>🏆 Empresas que Confiam no Meu Trabalho</h3>
        <p class="client-subtitle">
            De startups a multinacionais, entrego soluções que geram resultados mensuráveis
        </p>
    </div>
""", unsafe_allow_html=True)

col_img1, col_img2, col_img3 = st.columns([1, 8, 1])
with col_img2:
    st.image("assets/clientes_atendidos.jpg", use_container_width=True)

st.write("")

# --- DEPOIMENTO ---
st.markdown("""
    <div class="testimonial">
        <p class="testimonial-text">
            "Rodrigo reduziu nosso tempo de análise em 60% e aumentou a precisão das previsões de demanda 
            em 35%. O ROI foi positivo em apenas 3 meses. Profissional excepcional que entende tanto 
            de tecnologia quanto de negócios."
        </p>
        <p class="testimonial-author">
            — Diretor de Operações, Empresa do Setor Farmacêutico
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- BANNER DE URGÊNCIA ---
st.markdown("""
    <div class="scarcity-banner">
        ⏰ VAGAS LIMITADAS: Apenas 3 consultorias estratégicas disponíveis este mês
    </div>
""", unsafe_allow_html=True)

# --- CTA FINAL FORTE ---
st.markdown("""
    <div class="footer-cta">
        <h2>Pronto para Transformar Seus Dados em Lucro Real?</h2>
        <p class="footer-cta-text">
            Agende uma consultoria estratégica gratuita de 30 minutos e descubra como posso 
            ajudar seu negócio a crescer com inteligência de dados
        </p>
        <a href="mailto:contato@rodrigoaiosa.com" class="cta-button">
            📧 Agendar Consultoria Agora
        </a>
        <a href="#portfolio" class="cta-button cta-secondary">
            📄 Ver Cases de Sucesso
        </a>
    </div>
""", unsafe_allow_html=True)

# --- RODAPÉ ---
exibir_rodape()
