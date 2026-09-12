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


















# import streamlit as st
# from urllib.parse import urlparse
# from phishguard_engine import analyze_url

# st.set_page_config(
#     page_title="PhishGuard | URL Threat Intelligence",
#     page_icon="🛡️",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # ─────────────────────────────────────────────────────────────
# # CUSTOM UI
# # ─────────────────────────────────────────────────────────────

# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500&display=swap');

# html, body, [class*="css"] {
#     font-family: 'Inter', sans-serif;
# }

# .stApp {
#     background:
#         radial-gradient(circle at 15% 5%, rgba(37,99,235,.12), transparent 28%),
#         radial-gradient(circle at 85% 15%, rgba(124,58,237,.10), transparent 25%),
#         #080b12;
# }

# .block-container {
#     max-width: 1450px;
#     padding-top: 2rem;
#     padding-bottom: 4rem;
# }

# /* Header */
# .brand {
#     display: flex;
#     align-items: center;
#     gap: 14px;
#     margin-bottom: 4px;
# }

# .brand-icon {
#     font-size: 42px;
# }

# .brand-name {
#     font-size: 38px;
#     font-weight: 800;
#     letter-spacing: -1.5px;
# }

# .subtitle {
#     color: #8b95a7;
#     font-size: 15px;
#     margin-bottom: 28px;
# }

# /* Cards */
# .card {
#     background: rgba(17, 23, 36, .88);
#     border: 1px solid #20293a;
#     border-radius: 18px;
#     padding: 22px;
#     box-shadow: 0 12px 35px rgba(0,0,0,.18);
# }

# .card-title {
#     font-size: 14px;
#     font-weight: 700;
#     color: #aeb8c8;
#     text-transform: uppercase;
#     letter-spacing: .8px;
#     margin-bottom: 14px;
# }

# .big-number {
#     font-size: 32px;
#     font-weight: 800;
#     margin-top: 3px;
# }

# .muted {
#     color: #7f8a9d;
#     font-size: 13px;
# }

# .mono {
#     font-family: 'JetBrains Mono', monospace;
#     word-break: break-all;
# }

# /* Threat banner */
# .threat {
#     border-radius: 18px;
#     padding: 22px 26px;
#     margin: 22px 0;
#     background: linear-gradient(135deg, rgba(127,29,29,.30), rgba(30,41,59,.75));
#     border: 1px solid #7f1d1d;
# }

# .threat-low {
#     background: linear-gradient(135deg, rgba(6,78,59,.25), rgba(17,24,39,.8));
#     border-color: #065f46;
# }

# .threat-medium {
#     background: linear-gradient(135deg, rgba(120,53,15,.28), rgba(17,24,39,.8));
#     border-color: #92400e;
# }

# .threat-high {
#     background: linear-gradient(135deg, rgba(127,29,29,.32), rgba(17,24,39,.8));
#     border-color: #991b1b;
# }

# .threat-label {
#     font-size: 12px;
#     font-weight: 700;
#     letter-spacing: 1.2px;
#     text-transform: uppercase;
#     color: #94a3b8;
# }

# .threat-value {
#     font-size: 31px;
#     font-weight: 800;
#     margin-top: 5px;
# }

# /* Pills */
# .pill {
#     display: inline-block;
#     padding: 5px 10px;
#     border-radius: 999px;
#     background: #182235;
#     border: 1px solid #29364c;
#     color: #cbd5e1;
#     font-size: 12px;
#     margin: 3px;
# }

# /* Section */
# .section {
#     font-size: 22px;
#     font-weight: 800;
#     margin: 28px 0 14px;
# }

# /* Footer */
# .footer {
#     text-align: center;
#     color: #667085;
#     font-size: 12px;
#     margin-top: 45px;
# }
# </style>
# """, unsafe_allow_html=True)


# # ─────────────────────────────────────────────────────────────
# # HEADER
# # ─────────────────────────────────────────────────────────────

# st.markdown("""
# <div class="brand">
#     <div class="brand-icon">🛡️</div>
#     <div class="brand-name">PhishGuard</div>
# </div>
# <div class="subtitle">
#     AI-powered URL threat intelligence • Explainable phishing detection
# </div>
# """, unsafe_allow_html=True)


# # ─────────────────────────────────────────────────────────────
# # SIDEBAR
# # ─────────────────────────────────────────────────────────────

# with st.sidebar:
#     st.markdown("## 🛡️ PhishGuard")
#     st.caption("Threat Intelligence Console")

#     st.divider()

#     st.markdown("### Detection Stack")
#     st.markdown("""
#     **🤖 ML Classifier**  
#     Character-level URL pattern analysis

#     **🧠 Intelligence Engine**  
#     Structural security heuristics

#     **🎭 Brand Detection**  
#     Possible impersonation analysis

#     **🔑 Keyword Analysis**  
#     Suspicious terminology detection
#     """)

#     st.divider()

#     st.markdown("### Privacy")
#     st.caption(
#         "URLs are analyzed as text. PhishGuard does not "
#         "visit, execute, or interact with the target website."
#     )


# # ─────────────────────────────────────────────────────────────
# # INPUT
# # ─────────────────────────────────────────────────────────────

# st.markdown('<div class="section">🔎 Threat Scanner</div>', unsafe_allow_html=True)

# url = st.text_input(
#     "Target URL",
#     placeholder="https://example.com/login",
#     label_visibility="collapsed"
# )

# scan = st.button(
#     "🚀  RUN THREAT ANALYSIS",
#     use_container_width=True,
#     type="primary"
# )

# if scan:

#     if not url.strip():
#         st.warning("Enter a URL to begin the analysis.")

#     else:
#         if not url.startswith(("http://", "https://")):
#             url = "https://" + url

#         try:
#             parsed = urlparse(url)

#             if not parsed.netloc:
#                 st.error("Invalid URL. Please enter a valid website address.")

#             else:

#                 result = analyze_url(url)

#                 score = result["score"]

#                 # ─────────────────────────────────────────
#                 # THREAT STATUS
#                 # ─────────────────────────────────────────

#                 if score >= 75:
#                     threat_class = "threat-high"
#                     threat_icon = "🚨"
#                     threat_text = "HIGH RISK"
#                     threat_message = "Strong indicators of malicious or deceptive behavior were detected."

#                 elif score >= 40:
#                     threat_class = "threat-medium"
#                     threat_icon = "⚠️"
#                     threat_text = "SUSPICIOUS"
#                     threat_message = "Some characteristics require additional caution."

#                 else:
#                     threat_class = "threat-low"
#                     threat_icon = "🟢"
#                     threat_text = "LOW RISK"
#                     threat_message = "No strong phishing indicators were detected."

#                 st.markdown(f"""
#                 <div class="threat {threat_class}">
#                     <div class="threat-label">Threat Assessment</div>
#                     <div class="threat-value">{threat_icon} {threat_text}</div>
#                     <div class="muted">{threat_message}</div>
#                 </div>
#                 """, unsafe_allow_html=True)

#                 # ─────────────────────────────────────────
#                 # SCORE CARDS
#                 # ─────────────────────────────────────────

#                 c1, c2, c3, c4 = st.columns(4)

#                 with c1:
#                     st.markdown(f"""
#                     <div class="card">
#                         <div class="card-title">Overall Risk</div>
#                         <div class="big-number">{score:.1f}%</div>
#                         <div class="muted">Combined assessment</div>
#                     </div>
#                     """, unsafe_allow_html=True)

#                 with c2:
#                     st.markdown(f"""
#                     <div class="card">
#                         <div class="card-title">ML Probability</div>
#                         <div class="big-number">{result["ml_score"]:.1f}%</div>
#                         <div class="muted">Pattern classifier</div>
#                     </div>
#                     """, unsafe_allow_html=True)

#                 with c3:
#                     st.markdown(f"""
#                     <div class="card">
#                         <div class="card-title">Security Score</div>
#                         <div class="big-number">{result["intelligence_score"]}/100</div>
#                         <div class="muted">Rule-based signals</div>
#                     </div>
#                     """, unsafe_allow_html=True)

#                 with c4:
#                     findings_count = (
#                         len(result["security_findings"])
#                         + len(result["intelligence_reasons"])
#                     )

#                     st.markdown(f"""
#                     <div class="card">
#                         <div class="card-title">Indicators</div>
#                         <div class="big-number">{findings_count}</div>
#                         <div class="muted">Detected signals</div>
#                     </div>
#                     """, unsafe_allow_html=True)

#                 st.progress(min(score / 100, 1.0))

#                 # ─────────────────────────────────────────
#                 # URL ANATOMY
#                 # ─────────────────────────────────────────

#                 st.markdown(
#                     '<div class="section">🧬 URL Anatomy</div>',
#                     unsafe_allow_html=True
#                 )

#                 scheme = parsed.scheme or "—"
#                 domain = parsed.netloc or "—"
#                 path = parsed.path or "/"
#                 query = parsed.query or "—"

#                 a1, a2 = st.columns(2)

#                 with a1:
#                     st.markdown(f"""
#                     <div class="card">
#                         <div class="card-title">Protocol</div>
#                         <div class="mono">{scheme}</div>
#                         <br>
#                         <div class="card-title">Domain</div>
#                         <div class="mono">{domain}</div>
#                     </div>
#                     """, unsafe_allow_html=True)

#                 with a2:
#                     st.markdown(f"""
#                     <div class="card">
#                         <div class="card-title">Path</div>
#                         <div class="mono">{path}</div>
#                         <br>
#                         <div class="card-title">Query Parameters</div>
#                         <div class="mono">{query}</div>
#                     </div>
#                     """, unsafe_allow_html=True)

#                 # ─────────────────────────────────────────
#                 # INTELLIGENCE
#                 # ─────────────────────────────────────────

#                 st.markdown(
#                     '<div class="section">🧠 Security Intelligence</div>',
#                     unsafe_allow_html=True
#                 )

#                 i1, i2 = st.columns(2)

#                 with i1:
#                     st.markdown(
#                         '<div class="card"><div class="card-title">'
#                         '🎭 Brand Impersonation</div>',
#                         unsafe_allow_html=True
#                     )

#                     brands = result["brand_impersonation"]

#                     if brands:
#                         for brand in brands:
#                             st.error(f"Possible impersonation: {brand}")
#                     else:
#                         st.success("No known brand impersonation detected.")

#                     st.markdown("</div>", unsafe_allow_html=True)

#                 with i2:
#                     st.markdown(
#                         '<div class="card"><div class="card-title">'
#                         '🔑 Suspicious Keywords</div>',
#                         unsafe_allow_html=True
#                     )

#                     keywords = result["suspicious_keywords"]

#                     if keywords:
#                         for keyword in keywords:
#                             st.markdown(
#                                 f'<span class="pill">{keyword}</span>',
#                                 unsafe_allow_html=True
#                             )
#                     else:
#                         st.success("No suspicious keywords detected.")

#                     st.markdown("</div>", unsafe_allow_html=True)

#                 # ─────────────────────────────────────────
#                 # STRUCTURAL ANALYSIS
#                 # ─────────────────────────────────────────

#                 st.markdown(
#                     '<div class="section">🔬 Structural Analysis</div>',
#                     unsafe_allow_html=True
#                 )

#                 for icon, title, description in result["security_findings"]:
#                     if icon == "🚨":
#                         st.error(f"**{title}** — {description}")
#                     elif icon == "⚠️":
#                         st.warning(f"**{title}** — {description}")
#                     else:
#                         st.success(f"**{title}** — {description}")

#                 # ─────────────────────────────────────────
#                 # WHY THE SCORE?
#                 # ─────────────────────────────────────────

#                 with st.expander("🧪 Why did PhishGuard give this score?"):

#                     st.markdown("### ML assessment")
#                     st.write(
#                         "The machine-learning model analyzes character-level "
#                         "patterns learned from hundreds of thousands of URLs."
#                     )

#                     st.markdown("### Rule-based assessment")

#                     reasons = result["intelligence_reasons"]

#                     if reasons:
#                         for reason in reasons:
#                             st.write(f"• {reason}")
#                     else:
#                         st.write("No rule-based warning indicators.")

#                     st.caption(
#                         "Overall score combines the ML probability (70%) "
#                         "and security-intelligence score (30%)."
#                     )

#                 # ─────────────────────────────────────────
#                 # RAW URL
#                 # ─────────────────────────────────────────

#                 with st.expander("📋 Scanned URL"):
#                     st.code(url, language=None)

#                 st.markdown("""
#                 <div class="footer">
#                     PhishGuard is an educational cybersecurity research project.
#                     Predictions are probabilistic and should not be treated as
#                     definitive proof that a website is malicious or safe.
#                 </div>
#                 """, unsafe_allow_html=True)

#         except Exception as e:
#             st.error(f"Analysis failed: {e}")






































# import streamlit as st
# from urllib.parse import urlparse
# from phishguard_engine import analyze_url


# # ============================================================
# # PAGE CONFIG
# # ============================================================

# st.set_page_config(
#     page_title="PhishGuard | AI URL Security",
#     page_icon="🛡️",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )


# # ============================================================
# # CUSTOM CSS
# # ============================================================

# st.markdown(
#     """
#     <style>
#     .stApp {
#         background:
#             radial-gradient(circle at 15% 10%, rgba(70, 90, 140, 0.12), transparent 30%),
#             radial-gradient(circle at 85% 15%, rgba(120, 70, 150, 0.10), transparent 30%),
#             #080b12;
#         color: #e8edf5;
#     }

#     .block-container {
#         max-width: 1250px;
#         padding-top: 2rem;
#         padding-bottom: 3rem;
#     }

#     /* Header */
#     .hero {
#         padding: 2rem 0 1.2rem 0;
#     }

#     .hero-badge {
#         display: inline-block;
#         padding: 0.35rem 0.75rem;
#         border: 1px solid rgba(120, 140, 180, 0.25);
#         border-radius: 999px;
#         background: rgba(255,255,255,0.035);
#         color: #aebbd0;
#         font-size: 0.78rem;
#         letter-spacing: 0.08em;
#         text-transform: uppercase;
#         margin-bottom: 0.9rem;
#     }

#     .hero h1 {
#         font-size: 3.2rem;
#         line-height: 1.05;
#         margin: 0;
#         font-weight: 800;
#         letter-spacing: -0.04em;
#     }

#     .hero h1 span {
#         color: #79a8ff;
#     }

#     .hero p {
#         color: #9ba8bc;
#         font-size: 1.05rem;
#         max-width: 780px;
#         margin-top: 0.8rem;
#         line-height: 1.65;
#     }

#     /* Cards */
#     .card {
#         background: rgba(17, 22, 32, 0.78);
#         border: 1px solid rgba(130, 145, 170, 0.16);
#         border-radius: 16px;
#         padding: 1.2rem;
#         margin-bottom: 1rem;
#         box-shadow: 0 12px 35px rgba(0,0,0,0.18);
#     }

#     .card-title {
#         font-size: 0.82rem;
#         color: #8f9caf;
#         text-transform: uppercase;
#         letter-spacing: 0.08em;
#         margin-bottom: 0.55rem;
#     }

#     .card-value {
#         font-size: 1.7rem;
#         font-weight: 750;
#         color: #f0f4fa;
#     }

#     .card-sub {
#         color: #7f8b9d;
#         font-size: 0.82rem;
#         margin-top: 0.25rem;
#     }

#     /* Assessment */
#     .assessment {
#         padding: 1.35rem 1.5rem;
#         border-radius: 16px;
#         background: linear-gradient(
#             135deg,
#             rgba(30, 40, 58, 0.95),
#             rgba(15, 20, 30, 0.95)
#         );
#         border: 1px solid rgba(120, 145, 190, 0.2);
#         margin: 1.25rem 0 1.5rem 0;
#     }

#     .assessment-label {
#         color: #8f9caf;
#         text-transform: uppercase;
#         letter-spacing: 0.08em;
#         font-size: 0.75rem;
#     }

#     .assessment-verdict {
#         font-size: 2rem;
#         font-weight: 800;
#         margin-top: 0.25rem;
#     }

#     .assessment-description {
#         color: #a5b0c0;
#         margin-top: 0.4rem;
#     }

#     /* Section */
#     .section-header {
#         margin-top: 1.8rem;
#         margin-bottom: 0.8rem;
#     }

#     .section-header h2 {
#         font-size: 1.35rem;
#         margin-bottom: 0.15rem;
#     }

#     .section-header p {
#         color: #7f8b9d;
#         margin-top: 0;
#         font-size: 0.9rem;
#     }

#     /* Findings */
#     .finding {
#         padding: 0.9rem 1rem;
#         border-radius: 12px;
#         background: rgba(255,255,255,0.025);
#         border: 1px solid rgba(255,255,255,0.07);
#         margin-bottom: 0.6rem;
#     }

#     .finding-title {
#         font-weight: 650;
#     }

#     .finding-desc {
#         color: #8e9bad;
#         font-size: 0.84rem;
#         margin-top: 0.2rem;
#     }

#     /* Pills */
#     .pill {
#         display: inline-block;
#         padding: 0.35rem 0.65rem;
#         margin: 0.2rem;
#         border-radius: 999px;
#         background: rgba(121, 168, 255, 0.10);
#         border: 1px solid rgba(121, 168, 255, 0.18);
#         color: #b9d0ff;
#         font-size: 0.8rem;
#     }

#     /* URL box */
#     .url-box {
#         background: #0d121b;
#         border: 1px solid rgba(130,145,170,0.16);
#         border-radius: 12px;
#         padding: 0.85rem 1rem;
#         color: #b9c5d7;
#         word-break: break-all;
#         font-family: monospace;
#         font-size: 0.86rem;
#     }

#     /* Sidebar */
#     [data-testid="stSidebar"] {
#         background: #090d14;
#         border-right: 1px solid rgba(130,145,170,0.12);
#     }

#     /* Buttons */
#     .stButton > button {
#         border-radius: 10px;
#         font-weight: 650;
#     }

#     /* Footer */
#     .footer {
#         text-align: center;
#         color: #667286;
#         font-size: 0.78rem;
#         padding-top: 2.5rem;
#         line-height: 1.7;
#     }

#     /* Hide Streamlit branding */
#     #MainMenu {
#         visibility: hidden;
#     }

#     footer {
#         visibility: hidden;
#     }

#     header {
#         visibility: hidden;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )


# # ============================================================
# # SIDEBAR
# # ============================================================

# with st.sidebar:

#     st.markdown("## 🛡️ PhishGuard")

#     st.caption(
#         "AI-assisted phishing URL analysis"
#     )

#     st.divider()

#     st.markdown("### Detection Stack")

#     st.markdown(
#         """
#         **01 · ML Pattern Model**  
#         Character-level URL analysis

#         **02 · Structure Engine**  
#         URL and domain red flags

#         **03 · Brand Intelligence**  
#         Known-brand impersonation

#         **04 · Typosquatting Engine**  
#         Lookalike & leetspeak detection

#         **05 · Threat Fusion**  
#         Combined security assessment
#         """
#     )

#     st.divider()

#     st.markdown("### Privacy")

#     st.caption(
#         "PhishGuard analyzes the URL string locally "
#         "within the application. It does not visit "
#         "or download content from the submitted website."
#     )

#     st.divider()

#     st.caption(
#         "Built as a machine-learning security research project."
#     )


# # ============================================================
# # HERO
# # ============================================================

# st.markdown(
#     """
#     <div class="hero">
#         <div class="hero-badge">AI-Assisted URL Security</div>
#         <h1>Phish<span>Guard</span></h1>
#         <p>
#             Analyze suspicious URLs using machine-learning patterns,
#             structural security heuristics, brand impersonation and
#             typosquatting intelligence — without relying on external
#             threat-intelligence APIs.
#         </p>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )


# # ============================================================
# # HOW IT WORKS
# # ============================================================

# with st.expander("🧭 How to use PhishGuard", expanded=False):

#     st.markdown(
#         """
#         ### Scan a URL in three steps

#         **1. Paste a URL**  
#         Enter the complete URL you want to analyze.

#         **2. Run the security scan**  
#         PhishGuard evaluates the URL using multiple independent
#         detection layers.

#         **3. Review the evidence**  
#         Don't rely only on the final score. Check the detected
#         structural indicators, suspicious keywords, brand
#         impersonation and possible typosquatting.

#         **Example URLs**
#         """
#     )

#     demo_urls = [
#         "https://google.com",
#         "https://github.com/login",
#         "https://goggle.com",
#         "https://paypa1.com",
#         "http://paypal-login-verify.com",
#         "http://192.168.1.100/login",
#     ]

#     for demo in demo_urls:
#         st.code(demo)


# # ============================================================
# # INPUT
# # ============================================================

# st.markdown(
#     """
#     <div class="section-header">
#         <h2>🔎 URL Security Scanner</h2>
#         <p>Paste a URL to generate a multi-layer threat assessment.</p>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# url = st.text_input(
#     "URL",
#     placeholder="https://example.com/login",
#     label_visibility="collapsed",
# )

# scan = st.button(
#     "🔍 Analyze URL",
#     type="primary",
#     use_container_width=True,
# )


# # ============================================================
# # ANALYSIS
# # ============================================================

# if scan:

#     if not url.strip():

#         st.warning(
#             "Please enter a URL before starting the scan."
#         )
#         st.stop()

#     url = url.strip()

#     # Automatically add scheme when omitted.
#     analysis_url = url

#     if not analysis_url.lower().startswith(
#         ("http://", "https://")
#     ):
#         analysis_url = "https://" + analysis_url

#     try:
#         result = analyze_url(analysis_url)

#     except Exception as error:

#         st.error(
#             f"Unable to analyze this URL: {error}"
#         )
#         st.stop()

#     verdict = result["verdict"]
#     score = result["score"]
#     ml_score = result["ml_score"]
#     intelligence = result["intelligence_score"]

#     # ========================================================
#     # ASSESSMENT DESCRIPTION
#     # ========================================================

#     if verdict == "Verified Low Risk":

#         description = (
#             "The domain matches a known official domain in "
#             "PhishGuard's brand verification list."
#         )

#     elif verdict == "High Risk":

#         description = (
#             "Multiple signals indicate that this URL may "
#             "represent a phishing or deceptive destination."
#         )

#     elif verdict == "Suspicious":

#         description = (
#             "The URL contains signals associated with "
#             "potentially deceptive or suspicious behavior."
#         )

#     else:

#         description = (
#             "No strong phishing indicators were detected, "
#             "but this does not guarantee the website is safe."
#         )

#     # ========================================================
#     # THREAT ASSESSMENT
#     # ========================================================

#     st.markdown(
#         f"""
#         <div class="assessment">
#             <div class="assessment-label">Threat Assessment</div>
#             <div class="assessment-verdict">{verdict}</div>
#             <div class="assessment-description">
#                 {description}
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

#     # ========================================================
#     # SCORE CARDS
#     # ========================================================

#     c1, c2, c3, c4 = st.columns(4)

#     with c1:
#         st.markdown(
#             f"""
#             <div class="card">
#                 <div class="card-title">Threat Score</div>
#                 <div class="card-value">{score:.1f}/100</div>
#                 <div class="card-sub">Final fused assessment</div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#     with c2:
#         st.markdown(
#             f"""
#             <div class="card">
#                 <div class="card-title">ML Score</div>
#                 <div class="card-value">{ml_score:.1f}%</div>
#                 <div class="card-sub">URL pattern probability</div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#     with c3:
#         st.markdown(
#             f"""
#             <div class="card">
#                 <div class="card-title">Intelligence</div>
#                 <div class="card-value">{intelligence}/100</div>
#                 <div class="card-sub">Security heuristics</div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#     with c4:

#         if result["trusted_domain"]:
#             domain_status = "Recognized"
#         else:
#             domain_status = "Unverified"

#         st.markdown(
#             f"""
#             <div class="card">
#                 <div class="card-title">Domain Status</div>
#                 <div class="card-value">{domain_status}</div>
#                 <div class="card-sub">Brand verification layer</div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#     # ========================================================
#     # URL
#     # ========================================================

#     st.markdown(
#         """
#         <div class="section-header">
#             <h2>🌐 Scanned URL</h2>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

#     st.markdown(
#         f"""
#         <div class="url-box">{analysis_url}</div>
#         """,
#         unsafe_allow_html=True,
#     )

#     # ========================================================
#     # URL ANATOMY
#     # ========================================================

#     parsed = urlparse(analysis_url)

#     st.markdown(
#         """
#         <div class="section-header">
#             <h2>🧩 URL Anatomy</h2>
#             <p>Breakdown of the submitted address.</p>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

#     a1, a2, a3, a4 = st.columns(4)

#     with a1:
#         st.markdown(
#             f"""
#             <div class="card">
#                 <div class="card-title">Scheme</div>
#                 <div class="card-value">{parsed.scheme or "—"}</div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#     with a2:
#         st.markdown(
#             f"""
#             <div class="card">
#                 <div class="card-title">Hostname</div>
#                 <div class="card-value" style="font-size:1.05rem;word-break:break-all;">
#                     {parsed.hostname or "—"}
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#     with a3:
#         st.markdown(
#             f"""
#             <div class="card">
#                 <div class="card-title">Path</div>
#                 <div class="card-value" style="font-size:1.05rem;word-break:break-all;">
#                     {parsed.path or "/"}
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#     with a4:
#         st.markdown(
#             f"""
#             <div class="card">
#                 <div class="card-title">Query</div>
#                 <div class="card-value" style="font-size:1.05rem;word-break:break-all;">
#                     {parsed.query or "—"}
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#     # ========================================================
#     # BRAND INTELLIGENCE
#     # ========================================================

#     brands = result["brand_impersonation"]
#     typos = result["typosquatting"]

#     st.markdown(
#         """
#         <div class="section-header">
#             <h2>🎯 Brand & Typosquatting Intelligence</h2>
#             <p>
#                 Detects attempts to imitate known brands through
#                 deceptive domains and character substitutions.
#             </p>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

#     b1, b2 = st.columns(2)

#     with b1:

#         if brands:

#             st.markdown(
#                 """
#                 <div class="card">
#                     <div class="card-title">Brand Impersonation</div>
#                 """,
#                 unsafe_allow_html=True,
#             )

#             for brand in brands:
#                 st.markdown(
#                     f'<span class="pill">🚨 {brand}</span>',
#                     unsafe_allow_html=True,
#                 )

#             st.markdown("</div>", unsafe_allow_html=True)

#         else:

#             st.markdown(
#                 """
#                 <div class="card">
#                     <div class="card-title">Brand Impersonation</div>
#                     <div class="card-value">None detected</div>
#                     <div class="card-sub">
#                         No known brand was directly detected in the domain.
#                     </div>
#                 </div>
#                 """,
#                 unsafe_allow_html=True,
#             )

#     with b2:

#         if typos:

#             st.markdown(
#                 """
#                 <div class="card">
#                     <div class="card-title">Possible Typosquatting</div>
#                 """,
#                 unsafe_allow_html=True,
#             )

#             for item in typos[:5]:

#                 st.markdown(
#                     f"""
#                     <div style="margin-bottom:0.65rem;">
#                         <strong>⚠️ {item['brand']}</strong>
#                         <span style="color:#8f9caf;">
#                             — "{item['domain']}"
#                             ({item['similarity']}% similarity)
#                         </span>
#                     </div>
#                     """,
#                     unsafe_allow_html=True,
#                 )

#             st.markdown("</div>", unsafe_allow_html=True)

#         else:

#             st.markdown(
#                 """
#                 <div class="card">
#                     <div class="card-title">Possible Typosquatting</div>
#                     <div class="card-value">None detected</div>
#                     <div class="card-sub">
#                         No strong known-brand lookalike was identified.
#                     </div>
#                 </div>
#                 """,
#                 unsafe_allow_html=True,
#             )

#     # ========================================================
#     # SUSPICIOUS KEYWORDS
#     # ========================================================

#     keywords = result["suspicious_keywords"]

#     st.markdown(
#         """
#         <div class="section-header">
#             <h2>🔑 Suspicious Keywords</h2>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

#     if keywords:

#         pills = ""

#         for keyword in keywords:
#             pills += (
#                 f'<span class="pill">⚠️ {keyword}</span>'
#             )

#         st.markdown(
#             f"""
#             <div class="card">
#                 {pills}
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#     else:

#         st.markdown(
#             """
#             <div class="card">
#                 <div class="card-value">No suspicious keywords detected</div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#     # ========================================================
#     # STRUCTURAL ANALYSIS
#     # ========================================================

#     findings = result["security_findings"]

#     st.markdown(
#         """
#         <div class="section-header">
#             <h2>🔬 Structural Analysis</h2>
#             <p>Signals identified from the URL structure itself.</p>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

#     for icon, title, description in findings:

#         st.markdown(
#             f"""
#             <div class="finding">
#                 <div class="finding-title">
#                     {icon} {title}
#                 </div>
#                 <div class="finding-desc">
#                     {description}
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#     # ========================================================
#     # WHY THIS SCORE?
#     # ========================================================

#     with st.expander(
#         "🧠 Why did PhishGuard give this score?"
#     ):

#         st.markdown(
#             "### Detection reasoning"
#         )

#         reasons = result["intelligence_reasons"]

#         if reasons:

#             for reason in reasons:
#                 st.markdown(
#                     f"- **{reason}**"
#                 )

#         else:

#             st.markdown(
#                 "No additional deterministic intelligence signals."
#             )

#         st.divider()

#         st.markdown(
#             """
#             **How the final assessment works**

#             PhishGuard combines several independent signals:

#             **ML Pattern Model**  
#             A character-level TF-IDF + Logistic Regression model
#             learns suspicious URL patterns from the training dataset.

#             **Security Intelligence**  
#             Handcrafted rules examine structural properties such as
#             IP addresses, excessive subdomains, unusual numbers,
#             suspicious keywords and URL obfuscation.

#             **Brand / Typosquatting Intelligence**  
#             The engine compares domains against a curated list of
#             known brands and checks for lookalike character patterns.

#             These signals are fused into the final threat assessment.
#             """
#         )

#     # ========================================================
#     # LIMITATIONS
#     # ========================================================

#     with st.expander(
#         "⚠️ Limitations & responsible use"
#     ):

#         st.markdown(
#             """
#             ### Important

#             PhishGuard is an **ML-based research and educational
#             security tool**, not a replacement for a commercial
#             threat-intelligence platform.

#             **What it can do**
#             - Detect learned URL patterns associated with phishing.
#             - Identify common structural red flags.
#             - Detect known-brand impersonation.
#             - Identify many common typosquatting techniques.
#             - Explain the signals contributing to its assessment.

#             **What it cannot guarantee**
#             - It does not verify whether a website is currently online.
#             - It does not inspect the website's HTML or JavaScript.
#             - It does not query live domain reputation databases.
#             - It does not guarantee that a "Low Risk" URL is safe.
#             - Novel phishing domains without recognizable signals may
#               evade detection.
#             - The trusted-domain layer only covers brands in its
#               curated verification list.

#             **Best practice:** treat the result as one security signal,
#             not as proof that a website is safe or malicious.
#             """
#         )

#     # ========================================================
#     # FOOTER
#     # ========================================================

#     st.markdown(
#         """
#         <div class="footer">
#             <strong>PhishGuard</strong> · AI-Assisted Phishing URL Detection<br>
#             Machine Learning · Security Heuristics · Brand Intelligence · Explainability
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )
































# import streamlit as st
# from urllib.parse import urlparse
# from phishguard_engine import analyze_url


# # ============================================================
# # PAGE CONFIG
# # ============================================================

# st.set_page_config(
#     page_title="PhishGuard | AI URL Security",
#     page_icon="🛡️",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )


# # ============================================================
# # SESSION STATE
# # ============================================================

# if "theme" not in st.session_state:
#     st.session_state.theme = "dark"

# if "url_input" not in st.session_state:
#     st.session_state.url_input = ""


# # ============================================================
# # THEME
# # ============================================================

# dark_mode = st.session_state.theme == "dark"

# if dark_mode:
#     BG = "#080b12"
#     PANEL = "rgba(17, 22, 32, 0.82)"
#     PANEL_SOLID = "#111620"
#     TEXT = "#e8edf5"
#     MUTED = "#9ba8bc"
#     SUBTLE = "#7f8b9d"
#     BORDER = "rgba(130, 145, 170, 0.16)"
#     INPUT = "#20232d"
#     CODE_BG = "#0d121b"
#     ACCENT = "#79a8ff"
# else:
#     BG = "#f5f7fb"
#     PANEL = "rgba(255, 255, 255, 0.88)"
#     PANEL_SOLID = "#ffffff"
#     TEXT = "#172033"
#     MUTED = "#536176"
#     SUBTLE = "#718096"
#     BORDER = "rgba(40, 55, 80, 0.14)"
#     INPUT = "#ffffff"
#     CODE_BG = "#eef2f7"
#     ACCENT = "#356edb"


# # ============================================================
# # CUSTOM CSS
# # ============================================================

# st.markdown(
#     f"""
#     <style>

#     :root {{
#         --bg: {BG};
#         --panel: {PANEL};
#         --panel-solid: {PANEL_SOLID};
#         --text: {TEXT};
#         --muted: {MUTED};
#         --subtle: {SUBTLE};
#         --border: {BORDER};
#         --input: {INPUT};
#         --code-bg: {CODE_BG};
#         --accent: {ACCENT};
#     }}

#     .stApp {{
#         background:
#             radial-gradient(
#                 circle at 15% 8%,
#                 rgba(70, 100, 170, 0.10),
#                 transparent 30%
#             ),
#             radial-gradient(
#                 circle at 85% 12%,
#                 rgba(120, 70, 170, 0.08),
#                 transparent 30%
#             ),
#             var(--bg);

#         color: var(--text);
#     }}

#     .block-container {{
#         max-width: 1280px;
#         padding-top: 2.2rem;
#         padding-bottom: 3rem;
#     }}

#     /* ========================================================
#        SIDEBAR
#        ======================================================== */

#     [data-testid="stSidebar"] {{
#         background: var(--panel-solid);
#         border-right: 1px solid var(--border);
#     }}

#     .sidebar-brand {{
#         text-align: center;
#         padding: 1rem 0 1.4rem 0;
#     }}

#     .sidebar-brand-icon {{
#         font-size: 2.2rem;
#     }}

#     .sidebar-brand-name {{
#         font-size: 1.45rem;
#         font-weight: 800;
#         margin-top: 0.3rem;
#     }}

#     .sidebar-subtitle {{
#         color: var(--subtle);
#         font-size: 0.78rem;
#         margin-top: 0.3rem;
#     }}

#     .sidebar-section {{
#         font-size: 0.76rem;
#         text-transform: uppercase;
#         letter-spacing: 0.08em;
#         color: var(--subtle);
#         margin: 1.3rem 0 0.7rem 0;
#     }}

#     .stack-item {{
#         padding: 0.65rem 0;
#         border-bottom: 1px solid var(--border);
#     }}

#     .stack-number {{
#         color: var(--accent);
#         font-weight: 800;
#         font-size: 0.75rem;
#     }}

#     .stack-title {{
#         font-weight: 700;
#         margin-left: 0.35rem;
#     }}

#     .stack-desc {{
#         color: var(--subtle);
#         font-size: 0.76rem;
#         margin-top: 0.15rem;
#     }}

#     /* ========================================================
#        HERO
#        ======================================================== */

#     .hero {{
#         text-align: center;
#         padding: 1.1rem 0 1rem 0;
#     }}

#     .hero-badge {{
#         display: inline-block;
#         padding: 0.4rem 0.85rem;
#         border: 1px solid var(--border);
#         border-radius: 999px;
#         background: rgba(121, 168, 255, 0.05);
#         color: var(--muted);
#         font-size: 0.74rem;
#         letter-spacing: 0.1em;
#         text-transform: uppercase;
#     }}

#     .hero h1 {{
#         font-size: 4.1rem;
#         line-height: 1;
#         margin: 1.1rem 0 0.8rem 0;
#         font-weight: 850;
#         letter-spacing: -0.055em;
#         color: var(--text);
#     }}

#     .hero h1 span {{
#         color: var(--accent);
#     }}

#     .hero p {{
#         color: var(--muted);
#         font-size: 1.02rem;
#         max-width: 820px;
#         margin: auto;
#         line-height: 1.7;
#     }}

#     /* ========================================================
#        CARDS
#        ======================================================== */

#     .card {{
#         background: var(--panel);
#         border: 1px solid var(--border);
#         border-radius: 16px;
#         padding: 1.15rem;
#         margin-bottom: 1rem;
#         box-shadow: 0 12px 35px rgba(0,0,0,0.08);
#     }}

#     .card-title {{
#         font-size: 0.74rem;
#         color: var(--subtle);
#         text-transform: uppercase;
#         letter-spacing: 0.08em;
#         margin-bottom: 0.55rem;
#     }}

#     .card-value {{
#         font-size: 1.55rem;
#         font-weight: 780;
#         color: var(--text);
#     }}

#     .card-sub {{
#         color: var(--subtle);
#         font-size: 0.78rem;
#         margin-top: 0.25rem;
#     }}

#     /* ========================================================
#        SECTION HEADERS
#        ======================================================== */

#     .section-header {{
#         margin-top: 2rem;
#         margin-bottom: 0.8rem;
#     }}

#     .section-header h2 {{
#         font-size: 1.3rem;
#         margin-bottom: 0.15rem;
#         color: var(--text);
#     }}

#     .section-header p {{
#         color: var(--subtle);
#         margin-top: 0;
#         font-size: 0.86rem;
#     }}

#     /* ========================================================
#        ASSESSMENT
#        ======================================================== */

#     .assessment {{
#         padding: 1.4rem 1.5rem;
#         border-radius: 17px;
#         background: var(--panel);
#         border: 1px solid var(--border);
#         margin: 1.5rem 0;
#         text-align: center;
#     }}

#     .assessment-label {{
#         color: var(--subtle);
#         text-transform: uppercase;
#         letter-spacing: 0.09em;
#         font-size: 0.72rem;
#     }}

#     .assessment-verdict {{
#         font-size: 2.15rem;
#         font-weight: 850;
#         margin-top: 0.25rem;
#         color: var(--text);
#     }}

#     .assessment-description {{
#         color: var(--muted);
#         margin-top: 0.4rem;
#         font-size: 0.9rem;
#     }}

#     /* ========================================================
#        FINDINGS
#        ======================================================== */

#     .finding {{
#         padding: 0.85rem 1rem;
#         border-radius: 12px;
#         background: rgba(128, 145, 175, 0.035);
#         border: 1px solid var(--border);
#         margin-bottom: 0.6rem;
#     }}

#     .finding-title {{
#         font-weight: 680;
#         color: var(--text);
#     }}

#     .finding-desc {{
#         color: var(--subtle);
#         font-size: 0.82rem;
#         margin-top: 0.2rem;
#     }}

#     /* ========================================================
#        PILLS
#        ======================================================== */

#     .pill {{
#         display: inline-block;
#         padding: 0.34rem 0.62rem;
#         margin: 0.18rem;
#         border-radius: 999px;
#         background: rgba(121, 168, 255, 0.09);
#         border: 1px solid rgba(121, 168, 255, 0.18);
#         color: var(--accent);
#         font-size: 0.78rem;
#     }}

#     /* ========================================================
#        URL BOX
#        ======================================================== */

#     .url-box {{
#         background: var(--code-bg);
#         border: 1px solid var(--border);
#         border-radius: 12px;
#         padding: 0.85rem 1rem;
#         color: var(--muted);
#         word-break: break-all;
#         font-family: monospace;
#         font-size: 0.84rem;
#     }}

#     /* ========================================================
#        EMPTY STATE
#        ======================================================== */

#     .empty-state {{
#         text-align: center;
#         padding: 2rem 1rem;
#         border: 1px dashed var(--border);
#         border-radius: 16px;
#         margin-top: 1.2rem;
#         color: var(--subtle);
#     }}

#     .empty-icon {{
#         font-size: 2.2rem;
#     }}

#     .empty-title {{
#         color: var(--text);
#         font-size: 1.05rem;
#         font-weight: 700;
#         margin-top: 0.5rem;
#     }}

#     /* ========================================================
#        FOOTER
#        ======================================================== */

#     .footer {{
#         text-align: center;
#         color: var(--subtle);
#         font-size: 0.74rem;
#         padding-top: 2.5rem;
#         line-height: 1.7;
#     }}

#     /* ========================================================
#        STREAMLIT CLEANUP
#        ======================================================== */

#     #MainMenu {{
#         visibility: hidden;
#     }}

#     footer {{
#         visibility: hidden;
#     }}

#     /* IMPORTANT:
#        Do NOT hide Streamlit's header.
#        The sidebar open/close control lives there.
#     */

#     </style>
#     """,
#     unsafe_allow_html=True,
# )


# # ============================================================
# # SIDEBAR
# # ============================================================

# with st.sidebar:

#     st.markdown(
#         """
#         <div class="sidebar-brand">
#             <div class="sidebar-brand-icon">🛡️</div>
#             <div class="sidebar-brand-name">PhishGuard</div>
#             <div class="sidebar-subtitle">
#                 AI-assisted phishing URL analysis
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Theme toggle
#     if st.button(
#         "☀️ Light Mode" if dark_mode else "🌙 Dark Mode",
#         use_container_width=True,
#     ):
#         st.session_state.theme = (
#             "light" if dark_mode else "dark"
#         )
#         st.rerun()

#     st.divider()

#     st.markdown(
#         '<div class="sidebar-section">Detection Stack</div>',
#         unsafe_allow_html=True,
#     )

#     stack = [
#         (
#             "01",
#             "ML Pattern Model",
#             "Character-level URL analysis",
#         ),
#         (
#             "02",
#             "Structure Engine",
#             "URL and domain red flags",
#         ),
#         (
#             "03",
#             "Brand Intelligence",
#             "Known-brand impersonation",
#         ),
#         (
#             "04",
#             "Typosquatting Engine",
#             "Lookalike & leetspeak detection",
#         ),
#         (
#             "05",
#             "Threat Fusion",
#             "Combined security assessment",
#         ),
#     ]

#     for number, title, description in stack:

#         st.markdown(
#             f"""
#             <div class="stack-item">
#                 <span class="stack-number">{number}</span>
#                 <span class="stack-title">{title}</span>
#                 <div class="stack-desc">{description}</div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#     st.markdown(
#         '<div class="sidebar-section">Privacy</div>',
#         unsafe_allow_html=True,
#     )

#     st.caption(
#         "PhishGuard analyzes the URL string without "
#         "visiting or downloading the target website."
#     )

#     st.divider()

#     st.caption(
#         "ML security research project · No external threat-intelligence API"
#     )


# # ============================================================
# # HERO
# # ============================================================

# st.markdown(
#     """
#     <div class="hero">

#         <div class="hero-badge">
#             AI-ASSISTED URL SECURITY
#         </div>

#         <h1>
#             Phish<span>Guard</span>
#         </h1>

#         <p>
#             Analyze suspicious URLs using machine-learning patterns,
#             structural security heuristics, brand impersonation and
#             typosquatting intelligence — all without relying on
#             external threat-intelligence APIs.
#         </p>

#     </div>
#     """,
#     unsafe_allow_html=True,
# )


# # ============================================================
# # HOW TO USE
# # ============================================================

# with st.expander(
#     "🧭 How to use PhishGuard",
#     expanded=False,
# ):

#     st.markdown(
#         """
#         ### Scan a URL in three steps

#         **1. Paste a URL**  
#         Enter the complete URL you want to investigate.

#         **2. Start the scan**  
#         PhishGuard runs the URL through multiple detection layers.

#         **3. Inspect the evidence**  
#         Review the ML score, structural signals, brand intelligence,
#         typosquatting results and the final threat assessment.

#         > **Tip:** Don't judge a URL only by its final score.
#         > The individual findings explain *why* the system reached
#         > its assessment.
#         """
#     )


# # ============================================================
# # SCANNER
# # ============================================================

# st.markdown(
#     """
#     <div class="section-header">
#         <h2>🔎 URL Security Scanner</h2>
#         <p>
#             Paste a URL below or start with one of the examples.
#         </p>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )


# # Demo buttons
# d1, d2, d3, d4 = st.columns(4)

# with d1:
#     if st.button(
#         "🟢 Safe Example",
#         use_container_width=True,
#     ):
#         st.session_state.url_input = "https://google.com"
#         st.rerun()

# with d2:
#     if st.button(
#         "🟡 Typosquat",
#         use_container_width=True,
#     ):
#         st.session_state.url_input = "https://paypa1.com"
#         st.rerun()

# with d3:
#     if st.button(
#         "🔴 Phishing",
#         use_container_width=True,
#     ):
#         st.session_state.url_input = (
#             "http://paypal-login-verify.com"
#         )
#         st.rerun()

# with d4:
#     if st.button(
#         "🧪 Obfuscated",
#         use_container_width=True,
#     ):
#         st.session_state.url_input = (
#             "http://paypal.com@evil-site.com/login"
#         )
#         st.rerun()


# url = st.text_input(
#     "URL",
#     key="url_input",
#     placeholder="https://example.com/login",
#     label_visibility="collapsed",
# )


# scan = st.button(
#     "🔍 Analyze URL",
#     type="primary",
#     use_container_width=True,
# )


# # ============================================================
# # NO SCAN STATE
# # ============================================================

# if not scan:

#     st.markdown(
#         """
#         <div class="empty-state">
#             <div class="empty-icon">🛡️</div>
#             <div class="empty-title">
#                 Ready to inspect a URL
#             </div>
#             <div>
#                 Enter a URL above and PhishGuard will generate
#                 a multi-layer security assessment.
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

#     st.stop()


# # ============================================================
# # INPUT VALIDATION
# # ============================================================

# if not url.strip():

#     st.warning(
#         "Please enter a URL before starting the scan."
#     )

#     st.stop()


# url = url.strip()

# analysis_url = url

# if not analysis_url.lower().startswith(
#     ("http://", "https://")
# ):
#     analysis_url = "https://" + analysis_url


# # ============================================================
# # RUN ANALYSIS
# # ============================================================

# with st.spinner(
#     "Running ML and security intelligence checks..."
# ):

#     try:
#         result = analyze_url(analysis_url)

#     except Exception as error:

#         st.error(
#             f"Unable to analyze this URL: {error}"
#         )

#         st.stop()


# # ============================================================
# # RESULT VARIABLES
# # ============================================================

# verdict = result["verdict"]
# score = result["score"]
# ml_score = result["ml_score"]
# intelligence = result["intelligence_score"]

# trusted = result["trusted_domain"]
# brands = result["brand_impersonation"]
# typos = result["typosquatting"]
# keywords = result["suspicious_keywords"]
# findings = result["security_findings"]


# # ============================================================
# # DESCRIPTION
# # ============================================================

# if verdict == "Verified Low Risk":

#     description = (
#         "The domain matches a known official domain in "
#         "PhishGuard's curated verification list."
#     )

# elif verdict == "High Risk":

#     description = (
#         "Multiple signals indicate that this URL may represent "
#         "a phishing or deceptive destination."
#     )

# elif verdict == "Suspicious":

#     description = (
#         "The URL contains signals associated with potentially "
#         "deceptive or suspicious behavior."
#     )

# else:

#     description = (
#         "No strong phishing indicators were detected, but this "
#         "does not guarantee that the website is safe."
#     )


# # ============================================================
# # THREAT ASSESSMENT
# # ============================================================

# st.markdown(
#     f"""
#     <div class="assessment">

#         <div class="assessment-label">
#             Threat Assessment
#         </div>

#         <div class="assessment-verdict">
#             {verdict}
#         </div>

#         <div class="assessment-description">
#             {description}
#         </div>

#     </div>
#     """,
#     unsafe_allow_html=True,
# )


# # ============================================================
# # SCORE CARDS
# # ============================================================

# c1, c2, c3, c4 = st.columns(4)

# with c1:

#     st.markdown(
#         f"""
#         <div class="card">
#             <div class="card-title">Threat Score</div>
#             <div class="card-value">{score:.1f}/100</div>
#             <div class="card-sub">
#                 Final fused assessment
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

# with c2:

#     st.markdown(
#         f"""
#         <div class="card">
#             <div class="card-title">ML Score</div>
#             <div class="card-value">{ml_score:.1f}%</div>
#             <div class="card-sub">
#                 URL pattern probability
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

# with c3:

#     st.markdown(
#         f"""
#         <div class="card">
#             <div class="card-title">Intelligence</div>
#             <div class="card-value">{intelligence}/100</div>
#             <div class="card-sub">
#                 Security heuristics
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

# with c4:

#     domain_status = (
#         "Recognized"
#         if trusted
#         else "Unverified"
#     )

#     st.markdown(
#         f"""
#         <div class="card">
#             <div class="card-title">Domain Status</div>
#             <div class="card-value">
#                 {domain_status}
#             </div>
#             <div class="card-sub">
#                 Brand verification layer
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )


# # ============================================================
# # THREAT SCORE VISUAL
# # ============================================================

# st.markdown(
#     """
#     <div class="section-header">
#         <h2>📊 Threat Level</h2>
#         <p>Visual representation of the final fused score.</p>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# st.progress(
#     min(max(score / 100, 0.0), 1.0)
# )


# # ============================================================
# # SCANNED URL
# # ============================================================

# st.markdown(
#     """
#     <div class="section-header">
#         <h2>🌐 Scanned URL</h2>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# st.markdown(
#     f"""
#     <div class="url-box">
#         {analysis_url}
#     </div>
#     """,
#     unsafe_allow_html=True,
# )


# # ============================================================
# # URL ANATOMY
# # ============================================================

# parsed = urlparse(analysis_url)

# st.markdown(
#     """
#     <div class="section-header">
#         <h2>🧩 URL Anatomy</h2>
#         <p>Breakdown of the submitted address.</p>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# a1, a2, a3, a4 = st.columns(4)

# with a1:

#     st.markdown(
#         f"""
#         <div class="card">
#             <div class="card-title">Scheme</div>
#             <div class="card-value">
#                 {parsed.scheme or "—"}
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

# with a2:

#     st.markdown(
#         f"""
#         <div class="card">
#             <div class="card-title">Hostname</div>
#             <div class="card-value"
#                  style="font-size:1rem;word-break:break-all;">
#                 {parsed.hostname or "—"}
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

# with a3:

#     st.markdown(
#         f"""
#         <div class="card">
#             <div class="card-title">Path</div>
#             <div class="card-value"
#                  style="font-size:1rem;word-break:break-all;">
#                 {parsed.path or "/"}
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

# with a4:

#     st.markdown(
#         f"""
#         <div class="card">
#             <div class="card-title">Query</div>
#             <div class="card-value"
#                  style="font-size:1rem;word-break:break-all;">
#                 {parsed.query or "—"}
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )


# # ============================================================
# # BRAND + TYPOSQUATTING
# # ============================================================

# st.markdown(
#     """
#     <div class="section-header">
#         <h2>🎯 Brand & Typosquatting Intelligence</h2>
#         <p>
#             Detects attempts to imitate known brands through
#             deceptive domains and character substitutions.
#         </p>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# b1, b2 = st.columns(2)

# with b1:

#     if brands:

#         st.markdown(
#             """
#             <div class="card">
#                 <div class="card-title">
#                     Brand Impersonation
#                 </div>
#             """,
#             unsafe_allow_html=True,
#         )

#         for brand in brands:

#             st.markdown(
#                 f"""
#                 <span class="pill">
#                     🚨 {brand}
#                 </span>
#                 """,
#                 unsafe_allow_html=True,
#             )

#         st.markdown(
#             "</div>",
#             unsafe_allow_html=True,
#         )

#     else:

#         st.markdown(
#             """
#             <div class="card">
#                 <div class="card-title">
#                     Brand Impersonation
#                 </div>

#                 <div class="card-value">
#                     None detected
#                 </div>

#                 <div class="card-sub">
#                     No known brand was directly detected
#                     in the domain.
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )


# with b2:

#     if typos:

#         st.markdown(
#             """
#             <div class="card">
#                 <div class="card-title">
#                     Possible Typosquatting
#                 </div>
#             """,
#             unsafe_allow_html=True,
#         )

#         for item in typos[:5]:

#             st.markdown(
#                 f"""
#                 <div style="margin-bottom:0.65rem;">
#                     <strong>
#                         ⚠️ {item['brand']}
#                     </strong>

#                     <span style="color:var(--subtle);">
#                         — "{item['domain']}"
#                         ({item['similarity']}% similarity)
#                     </span>
#                 </div>
#                 """,
#                 unsafe_allow_html=True,
#             )

#         st.markdown(
#             "</div>",
#             unsafe_allow_html=True,
#         )

#     else:

#         st.markdown(
#             """
#             <div class="card">
#                 <div class="card-title">
#                     Possible Typosquatting
#                 </div>

#                 <div class="card-value">
#                     None detected
#                 </div>

#                 <div class="card-sub">
#                     No strong known-brand lookalike
#                     was identified.
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )


# # ============================================================
# # SUSPICIOUS KEYWORDS
# # ============================================================

# st.markdown(
#     """
#     <div class="section-header">
#         <h2>🔑 Suspicious Keywords</h2>
#         <p>
#             Authentication, payment and account-related
#             language detected in the URL.
#         </p>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# if keywords:

#     pills = ""

#     for keyword in keywords:

#         pills += (
#             f'<span class="pill">'
#             f'⚠️ {keyword}'
#             f'</span>'
#         )

#     st.markdown(
#         f"""
#         <div class="card">
#             {pills}
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

# else:

#     st.markdown(
#         """
#         <div class="card">
#             <div class="card-value">
#                 No suspicious keywords detected
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )


# # ============================================================
# # STRUCTURAL ANALYSIS
# # ============================================================

# st.markdown(
#     """
#     <div class="section-header">
#         <h2>🔬 Structural Analysis</h2>
#         <p>
#             Signals identified directly from the URL structure.
#         </p>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# for icon, title, description in findings:

#     st.markdown(
#         f"""
#         <div class="finding">

#             <div class="finding-title">
#                 {icon} {title}
#             </div>

#             <div class="finding-desc">
#                 {description}
#             </div>

#         </div>
#         """,
#         unsafe_allow_html=True,
#     )


# # ============================================================
# # WHY THIS SCORE?
# # ============================================================

# with st.expander(
#     "🧠 Why did PhishGuard give this score?"
# ):

#     st.markdown(
#         "### Detection reasoning"
#     )

#     reasons = result["intelligence_reasons"]

#     if reasons:

#         for reason in reasons:
#             st.markdown(
#                 f"- **{reason}**"
#             )

#     else:

#         st.markdown(
#             "No additional deterministic intelligence signals."
#         )

#     st.divider()

#     st.markdown(
#         """
#         ### How the assessment works

#         **ML Pattern Model**  
#         A character-level TF-IDF + Logistic Regression
#         model learns suspicious URL patterns from the
#         training dataset.

#         **Security Intelligence**  
#         Handcrafted rules examine structural properties
#         such as IP addresses, excessive subdomains,
#         unusual numbers, suspicious keywords and
#         URL obfuscation.

#         **Brand Intelligence**  
#         The engine checks whether the domain resembles
#         or impersonates a known brand.

#         **Typosquatting Detection**  
#         Character similarity and leetspeak normalization
#         are used to identify common lookalike domains.

#         **Threat Fusion**  
#         These signals are combined into the final
#         threat assessment.
#         """
#     )


# # ============================================================
# # LIMITATIONS
# # ============================================================

# with st.expander(
#     "⚠️ Limitations & responsible use"
# ):

#     st.markdown(
#         """
#         ### Important

#         PhishGuard is an **ML-based research and educational
#         security tool**, not a replacement for a commercial
#         threat-intelligence platform.

#         **What it can do**

#         - Detect learned URL patterns associated with phishing.
#         - Identify common structural red flags.
#         - Detect known-brand impersonation.
#         - Identify many common typosquatting techniques.
#         - Explain signals contributing to its assessment.

#         **What it cannot guarantee**

#         - It does not verify whether a website is currently online.
#         - It does not inspect the website's HTML or JavaScript.
#         - It does not query live domain reputation databases.
#         - A "Low Risk" result does not prove that a URL is safe.
#         - Novel phishing domains without recognizable signals may evade detection.
#         - The trusted-domain layer only covers brands in its curated list.

#         **Best practice:** treat PhishGuard as one security signal,
#         not as proof that a website is safe or malicious.
#         """
#     )


# # ============================================================
# # FOOTER
# # ============================================================

# st.markdown(
#     """
#     <div class="footer">

#         <strong>PhishGuard</strong>
#         · AI-Assisted Phishing URL Detection

#         <br>

#         Machine Learning · Security Heuristics ·
#         Brand Intelligence · Explainability

#     </div>
#     """,
#     unsafe_allow_html=True,
# )






































import streamlit as st
from urllib.parse import urlparse
from phishguard_engine import analyze_url


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="PhishGuard | AI URL Security",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# SESSION STATE
# ============================================================

if "theme" not in st.session_state:
    st.session_state.theme = "dark"

if "url_input" not in st.session_state:
    st.session_state.url_input = ""


# ============================================================
# THEME VARIABLES
# ============================================================

dark_mode = st.session_state.theme == "dark"

if dark_mode:
    BG = "#080b12"
    PANEL = "rgba(17, 22, 32, 0.86)"
    PANEL_SOLID = "#10151f"
    TEXT = "#e8edf5"
    MUTED = "#9ba8bc"
    SUBTLE = "#7f8b9d"
    BORDER = "rgba(130, 145, 170, 0.17)"
    INPUT = "#20232d"
    CODE_BG = "#0d121b"
    ACCENT = "#79a8ff"
    SHADOW = "rgba(0, 0, 0, 0.18)"
else:
    BG = "#f5f7fb"
    PANEL = "rgba(255, 255, 255, 0.92)"
    PANEL_SOLID = "#ffffff"
    TEXT = "#172033"
    MUTED = "#536176"
    SUBTLE = "#718096"
    BORDER = "rgba(40, 55, 80, 0.14)"
    INPUT = "#ffffff"
    CODE_BG = "#eef2f7"
    ACCENT = "#356edb"
    SHADOW = "rgba(40, 55, 80, 0.08)"


# ============================================================
# GLOBAL CSS
# ============================================================

st.html(
    f"""
    <style>

    :root {{
        --pg-bg: {BG};
        --pg-panel: {PANEL};
        --pg-panel-solid: {PANEL_SOLID};
        --pg-text: {TEXT};
        --pg-muted: {MUTED};
        --pg-subtle: {SUBTLE};
        --pg-border: {BORDER};
        --pg-input: {INPUT};
        --pg-code: {CODE_BG};
        --pg-accent: {ACCENT};
        --pg-shadow: {SHADOW};
    }}

    /* ========================================================
       APP BACKGROUND
       ======================================================== */

    .stApp {{
        background:
            radial-gradient(
                circle at 15% 5%,
                rgba(80, 120, 210, 0.09),
                transparent 28%
            ),
            radial-gradient(
                circle at 85% 8%,
                rgba(130, 80, 190, 0.07),
                transparent 28%
            ),
            var(--pg-bg);
        color: var(--pg-text);
    }}

    .block-container {{
        max-width: 1280px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }}

    /* ========================================================
       SIDEBAR
       ======================================================== */

    [data-testid="stSidebar"] {{
        background: var(--pg-panel-solid);
        border-right: 1px solid var(--pg-border);
    }}

    .pg-sidebar-brand {{
        text-align: center;
        padding: 0.9rem 0 1.2rem 0;
    }}

    .pg-sidebar-icon {{
        font-size: 2.4rem;
        line-height: 1;
    }}

    .pg-sidebar-name {{
        margin-top: 0.5rem;
        font-size: 1.45rem;
        font-weight: 800;
        color: var(--pg-text);
    }}

    .pg-sidebar-subtitle {{
        margin-top: 0.3rem;
        font-size: 0.78rem;
        color: var(--pg-subtle);
    }}

    .pg-sidebar-section {{
        margin: 1.35rem 0 0.75rem 0;
        color: var(--pg-subtle);
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        font-weight: 700;
    }}

    .pg-stack-item {{
        padding: 0.72rem 0;
        border-bottom: 1px solid var(--pg-border);
    }}

    .pg-stack-number {{
        color: var(--pg-accent);
        font-size: 0.74rem;
        font-weight: 800;
    }}

    .pg-stack-title {{
        color: var(--pg-text);
        font-size: 0.91rem;
        font-weight: 700;
        margin-left: 0.35rem;
    }}

    .pg-stack-desc {{
        margin-top: 0.2rem;
        color: var(--pg-subtle);
        font-size: 0.75rem;
        line-height: 1.4;
    }}

    /* ========================================================
       HERO
       ======================================================== */

    .pg-hero {{
        text-align: center;
        padding: 1.15rem 0 1rem 0;
    }}

    .pg-hero-badge {{
        display: inline-block;
        padding: 0.42rem 0.9rem;
        border: 1px solid var(--pg-border);
        border-radius: 999px;
        background: rgba(121, 168, 255, 0.045);
        color: var(--pg-muted);
        font-size: 0.72rem;
        letter-spacing: 0.11em;
        text-transform: uppercase;
        font-weight: 650;
    }}

    .pg-hero-title {{
        margin: 1rem 0 0.75rem 0;
        font-size: 4.15rem;
        line-height: 0.98;
        letter-spacing: -0.055em;
        font-weight: 850;
        color: var(--pg-text);
    }}

    .pg-hero-title span {{
        color: var(--pg-accent);
    }}

    .pg-hero-description {{
        max-width: 830px;
        margin: 0 auto;
        color: var(--pg-muted);
        font-size: 1rem;
        line-height: 1.72;
    }}

    /* ========================================================
       CARDS
       ======================================================== */

    .pg-card {{
        background: var(--pg-panel);
        border: 1px solid var(--pg-border);
        border-radius: 16px;
        padding: 1.1rem;
        margin-bottom: 0.9rem;
        box-shadow: 0 12px 35px var(--pg-shadow);
    }}

    .pg-card-label {{
        color: var(--pg-subtle);
        font-size: 0.69rem;
        text-transform: uppercase;
        letter-spacing: 0.09em;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }}

    .pg-card-value {{
        color: var(--pg-text);
        font-size: 1.5rem;
        line-height: 1.2;
        font-weight: 800;
    }}

    .pg-card-sub {{
        margin-top: 0.3rem;
        color: var(--pg-subtle);
        font-size: 0.76rem;
        line-height: 1.4;
    }}

    /* ========================================================
       SECTION HEADERS
       ======================================================== */

    .pg-section {{
        margin-top: 2rem;
        margin-bottom: 0.8rem;
    }}

    .pg-section-title {{
        color: var(--pg-text);
        font-size: 1.28rem;
        font-weight: 800;
        margin-bottom: 0.15rem;
    }}

    .pg-section-description {{
        color: var(--pg-subtle);
        font-size: 0.84rem;
        line-height: 1.5;
    }}

    /* ========================================================
       ASSESSMENT
       ======================================================== */

    .pg-assessment {{
        text-align: center;
        background: var(--pg-panel);
        border: 1px solid var(--pg-border);
        border-radius: 18px;
        padding: 1.4rem;
        margin: 1.5rem 0;
        box-shadow: 0 12px 35px var(--pg-shadow);
    }}

    .pg-assessment-label {{
        color: var(--pg-subtle);
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.11em;
        font-weight: 750;
    }}

    .pg-assessment-verdict {{
        color: var(--pg-text);
        font-size: 2.15rem;
        font-weight: 850;
        margin-top: 0.28rem;
    }}

    .pg-assessment-description {{
        color: var(--pg-muted);
        font-size: 0.86rem;
        margin-top: 0.35rem;
    }}

    /* ========================================================
       URL BOX
       ======================================================== */

    .pg-url-box {{
        background: var(--pg-code);
        border: 1px solid var(--pg-border);
        border-radius: 12px;
        padding: 0.9rem 1rem;
        color: var(--pg-muted);
        word-break: break-all;
        font-family: monospace;
        font-size: 0.82rem;
        line-height: 1.5;
    }}

    /* ========================================================
       FINDINGS
       ======================================================== */

    .pg-finding {{
        background: rgba(128, 145, 175, 0.035);
        border: 1px solid var(--pg-border);
        border-radius: 12px;
        padding: 0.82rem 1rem;
        margin-bottom: 0.58rem;
    }}

    .pg-finding-title {{
        color: var(--pg-text);
        font-weight: 700;
        font-size: 0.88rem;
    }}

    .pg-finding-description {{
        color: var(--pg-subtle);
        font-size: 0.79rem;
        line-height: 1.5;
        margin-top: 0.22rem;
    }}

    /* ========================================================
       PILLS
       ======================================================== */

    .pg-pill {{
        display: inline-block;
        padding: 0.34rem 0.62rem;
        margin: 0.16rem;
        border-radius: 999px;
        background: rgba(121, 168, 255, 0.09);
        border: 1px solid rgba(121, 168, 255, 0.18);
        color: var(--pg-accent);
        font-size: 0.76rem;
        font-weight: 650;
    }}

    /* ========================================================
       EMPTY STATE
       ======================================================== */

    .pg-empty {{
        text-align: center;
        border: 1px dashed var(--pg-border);
        border-radius: 16px;
        padding: 2rem 1rem;
        margin-top: 1.15rem;
        color: var(--pg-subtle);
    }}

    .pg-empty-icon {{
        font-size: 2.15rem;
    }}

    .pg-empty-title {{
        margin-top: 0.45rem;
        color: var(--pg-text);
        font-size: 1rem;
        font-weight: 750;
    }}

    .pg-empty-description {{
        margin-top: 0.25rem;
        font-size: 0.8rem;
    }}

    /* ========================================================
       FOOTER
       ======================================================== */

    .pg-footer {{
        text-align: center;
        color: var(--pg-subtle);
        font-size: 0.73rem;
        line-height: 1.7;
        padding-top: 2.5rem;
    }}

    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 768px) {{

        .block-container {{
            padding-top: 1.2rem;
        }}

        .pg-hero-title {{
            font-size: 3rem;
        }}

        .pg-hero-description {{
            font-size: 0.9rem;
        }}

        .pg-assessment-verdict {{
            font-size: 1.75rem;
        }}

    }}

    /* ========================================================
       IMPORTANT STREAMLIT FIX
       ======================================================== */

    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    /*
       DO NOT hide Streamlit's header.
       The sidebar open/close control lives there.
    */

    </style>
    """
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html(
        """
        <div class="pg-sidebar-brand">

            <div class="pg-sidebar-icon">
                🛡️
            </div>

            <div class="pg-sidebar-name">
                PhishGuard
            </div>

            <div class="pg-sidebar-subtitle">
                AI-assisted phishing URL analysis
            </div>

        </div>
        """
    )

    theme_label = "☀️ Light Mode" if dark_mode else "🌙 Dark Mode"

    if st.button(
        theme_label,
        use_container_width=True,
    ):
        st.session_state.theme = (
            "light" if dark_mode else "dark"
        )
        st.rerun()

    st.divider()

    st.html(
        """
        <div class="pg-sidebar-section">
            Detection Stack
        </div>
        """
    )

    stack = [
        (
            "01",
            "ML Pattern Model",
            "Character-level URL analysis",
        ),
        (
            "02",
            "Structure Engine",
            "URL and domain red flags",
        ),
        (
            "03",
            "Brand Intelligence",
            "Known-brand impersonation",
        ),
        (
            "04",
            "Typosquatting Engine",
            "Lookalike & leetspeak detection",
        ),
        (
            "05",
            "Threat Fusion",
            "Combined security assessment",
        ),
    ]

    for number, title, description in stack:

        st.html(
            f"""
            <div class="pg-stack-item">

                <span class="pg-stack-number">
                    {number}
                </span>

                <span class="pg-stack-title">
                    {title}
                </span>

                <div class="pg-stack-desc">
                    {description}
                </div>

            </div>
            """
        )

    st.html(
        """
        <div class="pg-sidebar-section">
            Privacy
        </div>
        """
    )

    st.caption(
        "PhishGuard analyzes the URL string without "
        "visiting or downloading the target website."
    )

    st.divider()

    st.caption(
        "ML security research project · "
        "No external threat-intelligence API"
    )


# ============================================================
# HERO
# ============================================================

st.html(
    """
    <div class="pg-hero">

        <div class="pg-hero-badge">
            AI-ASSISTED URL SECURITY
        </div>

        <div class="pg-hero-title">
            Phish<span>Guard</span>
        </div>

        <div class="pg-hero-description">
            Analyze suspicious URLs using machine-learning patterns,
            structural security heuristics, brand impersonation and
            typosquatting intelligence — all without relying on
            external threat-intelligence APIs.
        </div>

    </div>
    """
)


# ============================================================
# HOW TO USE
# ============================================================

with st.expander(
    "🧭 How to use PhishGuard",
    expanded=False,
):

    st.markdown(
        """
### Scan a URL in three steps

**1. Paste a URL**  
Enter the complete URL you want to investigate.

**2. Start the scan**  
PhishGuard runs the URL through multiple detection layers.

**3. Inspect the evidence**  
Review the ML score, structural signals, brand intelligence,
typosquatting results and the final threat assessment.

> **Tip:** Don't judge a URL only by its final score.
> The individual findings explain *why* the system reached
> its assessment.
        """
    )


# ============================================================
# SCANNER HEADER
# ============================================================

st.html(
    """
    <div class="pg-section">

        <div class="pg-section-title">
            🔎 URL Security Scanner
        </div>

        <div class="pg-section-description">
            Paste a URL below or start with one of the examples.
        </div>

    </div>
    """
)


# ============================================================
# DEMO BUTTONS
# ============================================================

d1, d2, d3, d4 = st.columns(4)

with d1:

    if st.button(
        "🟢 Safe Example",
        use_container_width=True,
    ):
        st.session_state.url_input = "https://google.com"
        st.rerun()

with d2:

    if st.button(
        "🟡 Typosquat",
        use_container_width=True,
    ):
        st.session_state.url_input = "https://paypa1.com"
        st.rerun()

with d3:

    if st.button(
        "🔴 Phishing",
        use_container_width=True,
    ):
        st.session_state.url_input = (
            "http://paypal-login-verify.com"
        )
        st.rerun()

with d4:

    if st.button(
        "🧪 Obfuscated",
        use_container_width=True,
    ):
        st.session_state.url_input = (
            "http://paypal.com@evil-site.com/login"
        )
        st.rerun()


# ============================================================
# URL INPUT
# ============================================================

url = st.text_input(
    "URL",
    key="url_input",
    placeholder="https://example.com/login",
    label_visibility="collapsed",
)


scan = st.button(
    "🔍 Analyze URL",
    type="primary",
    use_container_width=True,
)


# ============================================================
# EMPTY STATE
# ============================================================

if not scan:

    st.html(
        """
        <div class="pg-empty">

            <div class="pg-empty-icon">
                🛡️
            </div>

            <div class="pg-empty-title">
                Ready to inspect a URL
            </div>

            <div class="pg-empty-description">
                Enter a URL above and PhishGuard will generate
                a multi-layer security assessment.
            </div>

        </div>
        """
    )

    st.stop()


# ============================================================
# INPUT VALIDATION
# ============================================================

if not url.strip():

    st.warning(
        "Please enter a URL before starting the scan."
    )

    st.stop()


url = url.strip()

analysis_url = url

if not analysis_url.lower().startswith(
    ("http://", "https://")
):
    analysis_url = "https://" + analysis_url


# ============================================================
# ANALYSIS
# ============================================================

with st.spinner(
    "Running ML and security intelligence checks..."
):

    try:

        result = analyze_url(analysis_url)

    except Exception as error:

        st.error(
            f"Unable to analyze this URL: {error}"
        )

        st.stop()


# ============================================================
# RESULT VARIABLES
# ============================================================

verdict = result["verdict"]
score = result["score"]
ml_score = result["ml_score"]
intelligence = result["intelligence_score"]

trusted = result["trusted_domain"]
brands = result["brand_impersonation"]
typos = result["typosquatting"]
keywords = result["suspicious_keywords"]
findings = result["security_findings"]


# ============================================================
# VERDICT DESCRIPTION
# ============================================================

if verdict == "Verified Low Risk":

    description = (
        "The domain matches a known official domain in "
        "PhishGuard's curated verification list."
    )

elif verdict == "High Risk":

    description = (
        "Multiple signals indicate that this URL may represent "
        "a phishing or deceptive destination."
    )

elif verdict == "Suspicious":

    description = (
        "The URL contains signals associated with potentially "
        "deceptive or suspicious behavior."
    )

else:

    description = (
        "No strong phishing indicators were detected, but this "
        "does not guarantee that the website is safe."
    )


# ============================================================
# THREAT ASSESSMENT
# ============================================================

st.html(
    f"""
    <div class="pg-assessment">

        <div class="pg-assessment-label">
            Threat Assessment
        </div>

        <div class="pg-assessment-verdict">
            {verdict}
        </div>

        <div class="pg-assessment-description">
            {description}
        </div>

    </div>
    """
)


# ============================================================
# SCORE CARDS
# ============================================================

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.html(
        f"""
        <div class="pg-card">

            <div class="pg-card-label">
                Threat Score
            </div>

            <div class="pg-card-value">
                {score:.1f}/100
            </div>

            <div class="pg-card-sub">
                Final fused assessment
            </div>

        </div>
        """
    )

with c2:

    st.html(
        f"""
        <div class="pg-card">

            <div class="pg-card-label">
                ML Score
            </div>

            <div class="pg-card-value">
                {ml_score:.1f}%
            </div>

            <div class="pg-card-sub">
                URL pattern probability
            </div>

        </div>
        """
    )

with c3:

    st.html(
        f"""
        <div class="pg-card">

            <div class="pg-card-label">
                Intelligence
            </div>

            <div class="pg-card-value">
                {intelligence}/100
            </div>

            <div class="pg-card-sub">
                Security heuristics
            </div>

        </div>
        """
    )

with c4:

    domain_status = (
        "Recognized"
        if trusted
        else "Unverified"
    )

    st.html(
        f"""
        <div class="pg-card">

            <div class="pg-card-label">
                Domain Status
            </div>

            <div class="pg-card-value">
                {domain_status}
            </div>

            <div class="pg-card-sub">
                Brand verification layer
            </div>

        </div>
        """
    )


# ============================================================
# THREAT SCORE
# ============================================================

st.html(
    """
    <div class="pg-section">

        <div class="pg-section-title">
            📊 Threat Level
        </div>

        <div class="pg-section-description">
            Visual representation of the final fused score.
        </div>

    </div>
    """
)

st.progress(
    min(max(score / 100, 0.0), 1.0)
)


# ============================================================
# SCANNED URL
# ============================================================

st.html(
    """
    <div class="pg-section">

        <div class="pg-section-title">
            🌐 Scanned URL
        </div>

    </div>
    """
)

st.html(
    f"""
    <div class="pg-url-box">
        {analysis_url}
    </div>
    """
)


# ============================================================
# URL ANATOMY
# ============================================================

parsed = urlparse(analysis_url)

st.html(
    """
    <div class="pg-section">

        <div class="pg-section-title">
            🧩 URL Anatomy
        </div>

        <div class="pg-section-description">
            Breakdown of the submitted address.
        </div>

    </div>
    """
)


a1, a2, a3, a4 = st.columns(4)

with a1:

    st.html(
        f"""
        <div class="pg-card">

            <div class="pg-card-label">
                Scheme
            </div>

            <div class="pg-card-value">
                {parsed.scheme or "—"}
            </div>

        </div>
        """
    )

with a2:

    st.html(
        f"""
        <div class="pg-card">

            <div class="pg-card-label">
                Hostname
            </div>

            <div class="pg-card-value"
                 style="font-size:1rem;word-break:break-all;">
                {parsed.hostname or "—"}
            </div>

        </div>
        """
    )

with a3:

    st.html(
        f"""
        <div class="pg-card">

            <div class="pg-card-label">
                Path
            </div>

            <div class="pg-card-value"
                 style="font-size:1rem;word-break:break-all;">
                {parsed.path or "/"}
            </div>

        </div>
        """
    )

with a4:

    st.html(
        f"""
        <div class="pg-card">

            <div class="pg-card-label">
                Query
            </div>

            <div class="pg-card-value"
                 style="font-size:1rem;word-break:break-all;">
                {parsed.query or "—"}
            </div>

        </div>
        """
    )


# ============================================================
# BRAND + TYPOSQUATTING
# ============================================================

st.html(
    """
    <div class="pg-section">

        <div class="pg-section-title">
            🎯 Brand & Typosquatting Intelligence
        </div>

        <div class="pg-section-description">
            Detects attempts to imitate known brands through
            deceptive domains and character substitutions.
        </div>

    </div>
    """
)


b1, b2 = st.columns(2)


with b1:

    if brands:

        content = ""

        for brand in brands:

            content += (
                f'<span class="pg-pill">'
                f'🚨 {brand}'
                f'</span>'
            )

        st.html(
            f"""
            <div class="pg-card">

                <div class="pg-card-label">
                    Brand Impersonation
                </div>

                {content}

            </div>
            """
        )

    else:

        st.html(
            """
            <div class="pg-card">

                <div class="pg-card-label">
                    Brand Impersonation
                </div>

                <div class="pg-card-value">
                    None detected
                </div>

                <div class="pg-card-sub">
                    No known brand was directly detected
                    in the domain.
                </div>

            </div>
            """
        )


with b2:

    if typos:

        content = ""

        for item in typos[:5]:

            content += f"""
            <div style="margin-bottom:0.65rem;">
                <strong style="color:var(--pg-text);">
                    ⚠️ {item['brand']}
                </strong>

                <span style="color:var(--pg-subtle);">
                    — "{item['domain']}"
                    ({item['similarity']}% similarity)
                </span>
            </div>
            """

        st.html(
            f"""
            <div class="pg-card">

                <div class="pg-card-label">
                    Possible Typosquatting
                </div>

                {content}

            </div>
            """
        )

    else:

        st.html(
            """
            <div class="pg-card">

                <div class="pg-card-label">
                    Possible Typosquatting
                </div>

                <div class="pg-card-value">
                    None detected
                </div>

                <div class="pg-card-sub">
                    No strong known-brand lookalike
                    was identified.
                </div>

            </div>
            """
        )


# ============================================================
# SUSPICIOUS KEYWORDS
# ============================================================

st.html(
    """
    <div class="pg-section">

        <div class="pg-section-title">
            🔑 Suspicious Keywords
        </div>

        <div class="pg-section-description">
            Authentication, payment and account-related
            language detected in the URL.
        </div>

    </div>
    """
)


if keywords:

    pills = ""

    for keyword in keywords:

        pills += (
            f'<span class="pg-pill">'
            f'⚠️ {keyword}'
            f'</span>'
        )

    st.html(
        f"""
        <div class="pg-card">
            {pills}
        </div>
        """
    )

else:

    st.html(
        """
        <div class="pg-card">

            <div class="pg-card-value">
                No suspicious keywords detected
            </div>

        </div>
        """
    )


# ============================================================
# STRUCTURAL ANALYSIS
# ============================================================

st.html(
    """
    <div class="pg-section">

        <div class="pg-section-title">
            🔬 Structural Analysis
        </div>

        <div class="pg-section-description">
            Signals identified directly from the URL structure.
        </div>

    </div>
    """
)


for icon, title, explanation in findings:

    st.html(
        f"""
        <div class="pg-finding">

            <div class="pg-finding-title">
                {icon} {title}
            </div>

            <div class="pg-finding-description">
                {explanation}
            </div>

        </div>
        """
    )


# ============================================================
# WHY THIS SCORE?
# ============================================================

with st.expander(
    "🧠 Why did PhishGuard give this score?"
):

    st.markdown(
        "### Detection reasoning"
    )

    reasons = result["intelligence_reasons"]

    if reasons:

        for reason in reasons:

            st.markdown(
                f"- **{reason}**"
            )

    else:

        st.markdown(
            "No additional deterministic intelligence signals."
        )

    st.divider()

    st.markdown(
        """
### How the assessment works

**ML Pattern Model**  
A character-level TF-IDF + Logistic Regression model learns
suspicious URL patterns from the training dataset.

**Security Intelligence**  
Handcrafted rules examine structural properties such as
IP addresses, excessive subdomains, unusual numbers,
suspicious keywords and URL obfuscation.

**Brand Intelligence**  
The engine checks whether the domain resembles or impersonates
a known brand.

**Typosquatting Detection**  
Character similarity and leetspeak normalization are used
to identify common lookalike domains.

**Threat Fusion**  
These signals are combined into the final threat assessment.
        """
    )


# ============================================================
# LIMITATIONS
# ============================================================

with st.expander(
    "⚠️ Limitations & responsible use"
):

    st.markdown(
        """
### Important

PhishGuard is an **ML-based research and educational security
tool**, not a replacement for a commercial threat-intelligence
platform.

**What it can do**

- Detect learned URL patterns associated with phishing.
- Identify common structural red flags.
- Detect known-brand impersonation.
- Identify many common typosquatting techniques.
- Explain signals contributing to its assessment.

**What it cannot guarantee**

- It does not verify whether a website is currently online.
- It does not inspect the website's HTML or JavaScript.
- It does not query live domain reputation databases.
- A "Low Risk" result does not prove that a URL is safe.
- Novel phishing domains without recognizable signals may evade detection.
- The trusted-domain layer only covers brands in its curated list.

**Best practice:** treat PhishGuard as one security signal,
not as proof that a website is safe or malicious.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="pg-footer">

        <strong>PhishGuard</strong>
        · AI-Assisted Phishing URL Detection

        <br>

        Machine Learning · Security Heuristics ·
        Brand Intelligence · Explainability

    </div>
    """
)
