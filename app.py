# import streamlit as st
# from urllib.parse import urlparse
# from phishguard_engine import analyze_url

# st.set_page_config(
#     page_title="PhishGuard",
#     page_icon="🛡️",
#     layout="wide"
# )

# st.markdown("""
# <style>
# .main {
#     padding-top: 2rem;
# }
# .hero {
#     padding: 2rem;
#     border-radius: 20px;
#     background: linear-gradient(135deg, #111827, #1f2937);
#     color: white;
#     margin-bottom: 2rem;
# }
# .hero h1 {
#     font-size: 3rem;
#     margin-bottom: 0.3rem;
# }
# .hero p {
#     color: #cbd5e1;
#     font-size: 1.1rem;
# }
# .result-card {
#     padding: 1.5rem;
#     border-radius: 18px;
#     border: 1px solid #334155;
#     background: #111827;
#     color: white;
# }
# .badge {
#     display: inline-block;
#     padding: 0.35rem 0.8rem;
#     border-radius: 999px;
#     font-weight: 700;
# }
# </style>
# """, unsafe_allow_html=True)

# st.markdown("""
# <div class="hero">
#     <h1>🛡️ PhishGuard</h1>
#     <p>AI-powered phishing URL risk analysis with explainable security intelligence.</p>
# </div>
# """, unsafe_allow_html=True)

# st.subheader("🔎 Analyze a URL")

# url = st.text_input(
#     "Enter a website URL",
#     placeholder="https://example.com/login"
# )

# analyze = st.button("🚀 Analyze URL", use_container_width=True)

# if analyze:
#     if not url.strip():
#         st.warning("Please enter a URL.")
#     else:
#         if not url.startswith(("http://", "https://")):
#             url = "https://" + url

#         try:
#             parsed = urlparse(url)

#             if not parsed.netloc:
#                 st.error("Please enter a valid URL.")
#             else:
#                 result = analyze_url(url)

#                 st.divider()

#                 col1, col2, col3 = st.columns(3)

#                 col1.metric(
#                     "Overall Risk",
#                     f"{result['score']}%"
#                 )

#                 col2.metric(
#                     "ML Score",
#                     f"{result['ml_score']}%"
#                 )

#                 col3.metric(
#                     "Security Intelligence",
#                     f"{result['intelligence_score']}/100"
#                 )

#                 st.subheader(f"🎯 Verdict: {result['verdict']}")

#                 st.progress(min(result["score"] / 100, 1.0))

#                 st.divider()

#                 left, right = st.columns(2)

#                 with left:
#                     st.subheader("🧠 Security Intelligence")

#                     if result["brand_impersonation"]:
#                         st.error(
#                             "Brand impersonation: "
#                             + ", ".join(result["brand_impersonation"])
#                         )

#                     if result["suspicious_keywords"]:
#                         st.warning(
#                             "Suspicious keywords: "
#                             + ", ".join(result["suspicious_keywords"])
#                         )

#                     for reason in result["intelligence_reasons"]:
#                         st.write("•", reason)

#                 with right:
#                     st.subheader("🔍 URL Analysis")

#                     for icon, title, description in result["security_findings"]:
#                         st.write(f"{icon} **{title}**")
#                         st.caption(description)

#                 st.divider()

#                 st.caption(
#                     "PhishGuard analyzes URL characteristics and does not visit or execute the target website."
#                 )

#         except Exception as e:
#             st.error(f"Unable to analyze this URL: {e}")


















import streamlit as st
from urllib.parse import urlparse
from phishguard_engine import analyze_url

st.set_page_config(
    page_title="PhishGuard | URL Threat Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────────────────────
# CUSTOM UI
# ─────────────────────────────────────────────────────────────

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 15% 5%, rgba(37,99,235,.12), transparent 28%),
        radial-gradient(circle at 85% 15%, rgba(124,58,237,.10), transparent 25%),
        #080b12;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Header */
.brand {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 4px;
}

.brand-icon {
    font-size: 42px;
}

.brand-name {
    font-size: 38px;
    font-weight: 800;
    letter-spacing: -1.5px;
}

.subtitle {
    color: #8b95a7;
    font-size: 15px;
    margin-bottom: 28px;
}

/* Cards */
.card {
    background: rgba(17, 23, 36, .88);
    border: 1px solid #20293a;
    border-radius: 18px;
    padding: 22px;
    box-shadow: 0 12px 35px rgba(0,0,0,.18);
}

.card-title {
    font-size: 14px;
    font-weight: 700;
    color: #aeb8c8;
    text-transform: uppercase;
    letter-spacing: .8px;
    margin-bottom: 14px;
}

.big-number {
    font-size: 32px;
    font-weight: 800;
    margin-top: 3px;
}

.muted {
    color: #7f8a9d;
    font-size: 13px;
}

.mono {
    font-family: 'JetBrains Mono', monospace;
    word-break: break-all;
}

/* Threat banner */
.threat {
    border-radius: 18px;
    padding: 22px 26px;
    margin: 22px 0;
    background: linear-gradient(135deg, rgba(127,29,29,.30), rgba(30,41,59,.75));
    border: 1px solid #7f1d1d;
}

.threat-low {
    background: linear-gradient(135deg, rgba(6,78,59,.25), rgba(17,24,39,.8));
    border-color: #065f46;
}

.threat-medium {
    background: linear-gradient(135deg, rgba(120,53,15,.28), rgba(17,24,39,.8));
    border-color: #92400e;
}

.threat-high {
    background: linear-gradient(135deg, rgba(127,29,29,.32), rgba(17,24,39,.8));
    border-color: #991b1b;
}

.threat-label {
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: #94a3b8;
}

.threat-value {
    font-size: 31px;
    font-weight: 800;
    margin-top: 5px;
}

/* Pills */
.pill {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 999px;
    background: #182235;
    border: 1px solid #29364c;
    color: #cbd5e1;
    font-size: 12px;
    margin: 3px;
}

/* Section */
.section {
    font-size: 22px;
    font-weight: 800;
    margin: 28px 0 14px;
}

/* Footer */
.footer {
    text-align: center;
    color: #667085;
    font-size: 12px;
    margin-top: 45px;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────────────────────

st.markdown("""
<div class="brand">
    <div class="brand-icon">🛡️</div>
    <div class="brand-name">PhishGuard</div>
</div>
<div class="subtitle">
    AI-powered URL threat intelligence • Explainable phishing detection
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("## 🛡️ PhishGuard")
    st.caption("Threat Intelligence Console")

    st.divider()

    st.markdown("### Detection Stack")
    st.markdown("""
    **🤖 ML Classifier**  
    Character-level URL pattern analysis

    **🧠 Intelligence Engine**  
    Structural security heuristics

    **🎭 Brand Detection**  
    Possible impersonation analysis

    **🔑 Keyword Analysis**  
    Suspicious terminology detection
    """)

    st.divider()

    st.markdown("### Privacy")
    st.caption(
        "URLs are analyzed as text. PhishGuard does not "
        "visit, execute, or interact with the target website."
    )


# ─────────────────────────────────────────────────────────────
# INPUT
# ─────────────────────────────────────────────────────────────

st.markdown('<div class="section">🔎 Threat Scanner</div>', unsafe_allow_html=True)

url = st.text_input(
    "Target URL",
    placeholder="https://example.com/login",
    label_visibility="collapsed"
)

scan = st.button(
    "🚀  RUN THREAT ANALYSIS",
    use_container_width=True,
    type="primary"
)

if scan:

    if not url.strip():
        st.warning("Enter a URL to begin the analysis.")

    else:
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        try:
            parsed = urlparse(url)

            if not parsed.netloc:
                st.error("Invalid URL. Please enter a valid website address.")

            else:

                result = analyze_url(url)

                score = result["score"]

                # ─────────────────────────────────────────
                # THREAT STATUS
                # ─────────────────────────────────────────

                if score >= 75:
                    threat_class = "threat-high"
                    threat_icon = "🚨"
                    threat_text = "HIGH RISK"
                    threat_message = "Strong indicators of malicious or deceptive behavior were detected."

                elif score >= 40:
                    threat_class = "threat-medium"
                    threat_icon = "⚠️"
                    threat_text = "SUSPICIOUS"
                    threat_message = "Some characteristics require additional caution."

                else:
                    threat_class = "threat-low"
                    threat_icon = "🟢"
                    threat_text = "LOW RISK"
                    threat_message = "No strong phishing indicators were detected."

                st.markdown(f"""
                <div class="threat {threat_class}">
                    <div class="threat-label">Threat Assessment</div>
                    <div class="threat-value">{threat_icon} {threat_text}</div>
                    <div class="muted">{threat_message}</div>
                </div>
                """, unsafe_allow_html=True)

                # ─────────────────────────────────────────
                # SCORE CARDS
                # ─────────────────────────────────────────

                c1, c2, c3, c4 = st.columns(4)

                with c1:
                    st.markdown(f"""
                    <div class="card">
                        <div class="card-title">Overall Risk</div>
                        <div class="big-number">{score:.1f}%</div>
                        <div class="muted">Combined assessment</div>
                    </div>
                    """, unsafe_allow_html=True)

                with c2:
                    st.markdown(f"""
                    <div class="card">
                        <div class="card-title">ML Probability</div>
                        <div class="big-number">{result["ml_score"]:.1f}%</div>
                        <div class="muted">Pattern classifier</div>
                    </div>
                    """, unsafe_allow_html=True)

                with c3:
                    st.markdown(f"""
                    <div class="card">
                        <div class="card-title">Security Score</div>
                        <div class="big-number">{result["intelligence_score"]}/100</div>
                        <div class="muted">Rule-based signals</div>
                    </div>
                    """, unsafe_allow_html=True)

                with c4:
                    findings_count = (
                        len(result["security_findings"])
                        + len(result["intelligence_reasons"])
                    )

                    st.markdown(f"""
                    <div class="card">
                        <div class="card-title">Indicators</div>
                        <div class="big-number">{findings_count}</div>
                        <div class="muted">Detected signals</div>
                    </div>
                    """, unsafe_allow_html=True)

                st.progress(min(score / 100, 1.0))

                # ─────────────────────────────────────────
                # URL ANATOMY
                # ─────────────────────────────────────────

                st.markdown(
                    '<div class="section">🧬 URL Anatomy</div>',
                    unsafe_allow_html=True
                )

                scheme = parsed.scheme or "—"
                domain = parsed.netloc or "—"
                path = parsed.path or "/"
                query = parsed.query or "—"

                a1, a2 = st.columns(2)

                with a1:
                    st.markdown(f"""
                    <div class="card">
                        <div class="card-title">Protocol</div>
                        <div class="mono">{scheme}</div>
                        <br>
                        <div class="card-title">Domain</div>
                        <div class="mono">{domain}</div>
                    </div>
                    """, unsafe_allow_html=True)

                with a2:
                    st.markdown(f"""
                    <div class="card">
                        <div class="card-title">Path</div>
                        <div class="mono">{path}</div>
                        <br>
                        <div class="card-title">Query Parameters</div>
                        <div class="mono">{query}</div>
                    </div>
                    """, unsafe_allow_html=True)

                # ─────────────────────────────────────────
                # INTELLIGENCE
                # ─────────────────────────────────────────

                st.markdown(
                    '<div class="section">🧠 Security Intelligence</div>',
                    unsafe_allow_html=True
                )

                i1, i2 = st.columns(2)

                with i1:
                    st.markdown(
                        '<div class="card"><div class="card-title">'
                        '🎭 Brand Impersonation</div>',
                        unsafe_allow_html=True
                    )

                    brands = result["brand_impersonation"]

                    if brands:
                        for brand in brands:
                            st.error(f"Possible impersonation: {brand}")
                    else:
                        st.success("No known brand impersonation detected.")

                    st.markdown("</div>", unsafe_allow_html=True)

                with i2:
                    st.markdown(
                        '<div class="card"><div class="card-title">'
                        '🔑 Suspicious Keywords</div>',
                        unsafe_allow_html=True
                    )

                    keywords = result["suspicious_keywords"]

                    if keywords:
                        for keyword in keywords:
                            st.markdown(
                                f'<span class="pill">{keyword}</span>',
                                unsafe_allow_html=True
                            )
                    else:
                        st.success("No suspicious keywords detected.")

                    st.markdown("</div>", unsafe_allow_html=True)

                # ─────────────────────────────────────────
                # STRUCTURAL ANALYSIS
                # ─────────────────────────────────────────

                st.markdown(
                    '<div class="section">🔬 Structural Analysis</div>',
                    unsafe_allow_html=True
                )

                for icon, title, description in result["security_findings"]:
                    if icon == "🚨":
                        st.error(f"**{title}** — {description}")
                    elif icon == "⚠️":
                        st.warning(f"**{title}** — {description}")
                    else:
                        st.success(f"**{title}** — {description}")

                # ─────────────────────────────────────────
                # WHY THE SCORE?
                # ─────────────────────────────────────────

                with st.expander("🧪 Why did PhishGuard give this score?"):

                    st.markdown("### ML assessment")
                    st.write(
                        "The machine-learning model analyzes character-level "
                        "patterns learned from hundreds of thousands of URLs."
                    )

                    st.markdown("### Rule-based assessment")

                    reasons = result["intelligence_reasons"]

                    if reasons:
                        for reason in reasons:
                            st.write(f"• {reason}")
                    else:
                        st.write("No rule-based warning indicators.")

                    st.caption(
                        "Overall score combines the ML probability (70%) "
                        "and security-intelligence score (30%)."
                    )

                # ─────────────────────────────────────────
                # RAW URL
                # ─────────────────────────────────────────

                with st.expander("📋 Scanned URL"):
                    st.code(url, language=None)

                st.markdown("""
                <div class="footer">
                    PhishGuard is an educational cybersecurity research project.
                    Predictions are probabilistic and should not be treated as
                    definitive proof that a website is malicious or safe.
                </div>
                """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Analysis failed: {e}")
