
import re
import joblib
import pandas as pd
from urllib.parse import urlparse

url_model = joblib.load("phishguard_url_model.pkl")

KNOWN_BRANDS = {
    "paypal": ["paypal.com"],
    "google": ["google.com"],
    "microsoft": ["microsoft.com", "live.com", "outlook.com"],
    "amazon": ["amazon.com"],
    "apple": ["apple.com", "icloud.com"],
    "facebook": ["facebook.com", "fb.com"],
    "instagram": ["instagram.com"],
    "linkedin": ["linkedin.com"],
    "netflix": ["netflix.com"],
    "github": ["github.com"],
    "dropbox": ["dropbox.com"],
    "adobe": ["adobe.com"]
}

SUSPICIOUS_KEYWORDS = {
    "login", "signin", "verify", "verification", "secure",
    "account", "update", "confirm", "password", "bank",
    "wallet", "credential", "authenticate", "billing",
    "payment", "unlock", "suspend", "recover"
}

def detect_brand_impersonation(url):
    hostname = (urlparse(url).hostname or "").lower()
    return [
        brand.title()
        for brand, domains in KNOWN_BRANDS.items()
        if brand in hostname and not any(
            hostname == domain or hostname.endswith("." + domain)
            for domain in domains
        )
    ]

def detect_suspicious_keywords(url):
    url_lower = url.lower()
    return sorted({
        keyword for keyword in SUSPICIOUS_KEYWORDS
        if keyword in url_lower
    })

def explain_url(url):
    parsed = urlparse(url)
    hostname = parsed.netloc.lower()
    findings = []

    if len(url) > 75:
        findings.append(("⚠️", "Very long URL", "Long URLs can hide suspicious components."))
    if len(hostname) > 30:
        findings.append(("⚠️", "Long domain name", "Unusually long domains can disguise phishing links."))
    if re.search(r"(?:\d{1,3}\.){3}\d{1,3}", hostname):
        findings.append(("🚨", "IP address detected", "The URL uses an IP instead of a normal domain."))
    if "@" in url:
        findings.append(("🚨", "@ symbol detected", "The @ symbol can obscure the actual destination."))
    if hostname.count(".") >= 3:
        findings.append(("⚠️", "Multiple subdomains", "Deep subdomains can make domains harder to recognize."))
    if url.count("-") >= 3:
        findings.append(("⚠️", "Many hyphens", "Excessive hyphens can indicate deceptive domains."))
    if sum(c.isdigit() for c in url) >= 5:
        findings.append(("⚠️", "Many numbers", "Unusual numbers can indicate deceptive URLs."))
    if not url.lower().startswith("https://"):
        findings.append(("⚠️", "No HTTPS", "The URL does not use HTTPS."))

    if not findings:
        findings.append(("✅", "No obvious structural red flags", "No common structural indicators were detected."))

    return findings

def intelligence_score(url):
    score = 0
    reasons = []
    parsed = urlparse(url)
    hostname = parsed.netloc.lower()

    checks = [
        (len(url) > 75, 10, "Long URL"),
        (len(hostname) > 30, 10, "Long domain"),
        (bool(re.search(r"(?:\d{1,3}\.){3}\d{1,3}", hostname)), 25, "IP address used"),
        ("@" in url, 20, "@ symbol detected"),
        (hostname.count(".") >= 3, 10, "Multiple subdomains"),
        (url.count("-") >= 3, 10, "Excessive hyphens"),
        (sum(c.isdigit() for c in url) >= 5, 5, "Many numbers"),
        (not url.lower().startswith("https://"), 10, "No HTTPS")
    ]

    for condition, points, reason in checks:
        if condition:
            score += points
            reasons.append(reason)

    if detect_brand_impersonation(url):
        score += 25
        reasons.append("Brand impersonation detected")

    if len(detect_suspicious_keywords(url)) >= 2:
        score += 10
        reasons.append("Multiple suspicious keywords")

    return min(score, 100), reasons

def analyze_url(url):
    ml_probability = float(url_model.predict_proba([url])[0][1])
    intel_score, intel_reasons = intelligence_score(url)

    combined = (ml_probability * 100 * 0.7) + (intel_score * 0.3)

    if combined >= 75:
        verdict = "High Risk"
    elif combined >= 40:
        verdict = "Suspicious"
    else:
        verdict = "Low Risk"

    return {
        "verdict": verdict,
        "score": round(combined, 2),
        "ml_score": round(ml_probability * 100, 2),
        "intelligence_score": intel_score,
        "brand_impersonation": detect_brand_impersonation(url),
        "suspicious_keywords": detect_suspicious_keywords(url),
        "security_findings": explain_url(url),
        "intelligence_reasons": intel_reasons
    }

print("PhishGuard engine saved successfully.")
