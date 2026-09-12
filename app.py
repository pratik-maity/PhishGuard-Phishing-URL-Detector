import streamlit as st
from urllib.parse import urlparse
from phishguard_engine import analyze_url

st.set_page_config(
    page_title="PhishGuard",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
.main {
    padding-top: 2rem;
}
.hero {
    padding: 2rem;
    border-radius: 20px;
    background: linear-gradient(135deg, #111827, #1f2937);
    color: white;
    margin-bottom: 2rem;
}
.hero h1 {
    font-size: 3rem;
    margin-bottom: 0.3rem;
}
.hero p {
    color: #cbd5e1;
    font-size: 1.1rem;
}
.result-card {
    padding: 1.5rem;
    border-radius: 18px;
    border: 1px solid #334155;
    background: #111827;
    color: white;
}
.badge {
    display: inline-block;
    padding: 0.35rem 0.8rem;
    border-radius: 999px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🛡️ PhishGuard</h1>
    <p>AI-powered phishing URL risk analysis with explainable security intelligence.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("🔎 Analyze a URL")

url = st.text_input(
    "Enter a website URL",
    placeholder="https://example.com/login"
)

analyze = st.button("🚀 Analyze URL", use_container_width=True)

if analyze:
    if not url.strip():
        st.warning("Please enter a URL.")
    else:
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        try:
            parsed = urlparse(url)

            if not parsed.netloc:
                st.error("Please enter a valid URL.")
            else:
                result = analyze_url(url)

                st.divider()

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Overall Risk",
                    f"{result['score']}%"
                )

                col2.metric(
                    "ML Score",
                    f"{result['ml_score']}%"
                )

                col3.metric(
                    "Security Intelligence",
                    f"{result['intelligence_score']}/100"
                )

                st.subheader(f"🎯 Verdict: {result['verdict']}")

                st.progress(min(result["score"] / 100, 1.0))

                st.divider()

                left, right = st.columns(2)

                with left:
                    st.subheader("🧠 Security Intelligence")

                    if result["brand_impersonation"]:
                        st.error(
                            "Brand impersonation: "
                            + ", ".join(result["brand_impersonation"])
                        )

                    if result["suspicious_keywords"]:
                        st.warning(
                            "Suspicious keywords: "
                            + ", ".join(result["suspicious_keywords"])
                        )

                    for reason in result["intelligence_reasons"]:
                        st.write("•", reason)

                with right:
                    st.subheader("🔍 URL Analysis")

                    for icon, title, description in result["security_findings"]:
                        st.write(f"{icon} **{title}**")
                        st.caption(description)

                st.divider()

                st.caption(
                    "PhishGuard analyzes URL characteristics and does not visit or execute the target website."
                )

        except Exception as e:
            st.error(f"Unable to analyze this URL: {e}")
