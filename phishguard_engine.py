
import re
import joblib
from difflib import SequenceMatcher
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

LEET_MAP = str.maketrans({
    "0": "o",
    "1": "l",
    "3": "e",
    "4": "a",
    "5": "s",
    "7": "t",
    "8": "b"
})


def normalize_text(text):
    return text.translate(LEET_MAP)


def is_trusted_domain(url):
    hostname = (urlparse(url).hostname or "").lower()

    if hostname.startswith("www."):
        hostname = hostname[4:]

    for domains in KNOWN_BRANDS.values():
        for domain in domains:
            if hostname == domain or hostname.endswith("." + domain):
                return True

    return False


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


def detect_typosquatting(url):
    hostname = (urlparse(url).hostname or "").lower()

    if hostname.startswith("www."):
        hostname = hostname[4:]

    domain_name = hostname.split(".")[0]

    candidates = [domain_name]
    candidates.extend(domain_name.split("-"))

    matches = []

    for brand, official_domains in KNOWN_BRANDS.items():

        if any(
            hostname == domain or hostname.endswith("." + domain)
            for domain in official_domains
        ):
            continue

        best_similarity = 0
        best_candidate = ""

        for candidate in candidates:
            similarity = SequenceMatcher(
                None,
                normalize_text(candidate),
                brand
            ).ratio()

            if similarity > best_similarity:
                best_similarity = similarity
                best_candidate = candidate

        if best_similarity >= 0.80:
            matches.append({
                "brand": brand.title(),
                "domain": best_candidate,
                "similarity": round(best_similarity * 100, 2)
            })

    return sorted(
        matches,
        key=lambda x: x["similarity"],
        reverse=True
    )


def detect_suspicious_keywords(url):
    return sorted({
        keyword
        for keyword in SUSPICIOUS_KEYWORDS
        if keyword in url.lower()
    })


def explain_url(url):
    parsed = urlparse(url)
    hostname = parsed.netloc.lower()
    findings = []

    if len(url) > 75:
        findings.append((
            "⚠️",
            "Very long URL",
            "Long URLs can hide suspicious components."
        ))

    if len(hostname) > 30:
        findings.append((
            "⚠️",
            "Long domain name",
            "Unusually long domains can disguise phishing links."
        ))

    if re.search(r"(?:\d{1,3}\.){3}\d{1,3}", hostname):
        findings.append((
            "🚨",
            "IP address detected",
            "The URL uses an IP instead of a normal domain."
        ))

    if "@" in url:
        findings.append((
            "🚨",
            "@ symbol detected",
            "The @ symbol can obscure the actual destination."
        ))

    if hostname.count(".") >= 3:
        findings.append((
            "⚠️",
            "Multiple subdomains",
            "Deep subdomains can make domains harder to recognize."
        ))

    if url.count("-") >= 3:
        findings.append((
            "⚠️",
            "Many hyphens",
            "Excessive hyphens can indicate deceptive domains."
        ))

    if sum(c.isdigit() for c in url) >= 5:
        findings.append((
            "⚠️",
            "Many numbers",
            "Unusual numbers can indicate deceptive domains."
        ))

    if not url.lower().startswith("https://"):
        findings.append((
            "⚠️",
            "No HTTPS",
            "The URL does not use HTTPS."
        ))

    if not findings:
        findings.append((
            "✅",
            "No obvious structural red flags",
            "No common structural indicators were detected."
        ))

    return findings


def intelligence_score(url):
    score = 0
    reasons = []

    parsed = urlparse(url)
    hostname = parsed.netloc.lower()

    if is_trusted_domain(url):
        return 0, ["Official domain recognized"]

    checks = [
        (len(url) > 75, 10, "Long URL"),
        (len(hostname) > 30, 10, "Long domain"),
        (
            bool(re.search(
                r"(?:\d{1,3}\.){3}\d{1,3}",
                hostname
            )),
            25,
            "IP address used"
        ),
        ("@" in url, 20, "@ symbol detected"),
        (hostname.count(".") >= 3, 10, "Multiple subdomains"),
        (url.count("-") >= 3, 10, "Excessive hyphens"),
        (
            sum(c.isdigit() for c in url) >= 5,
            5,
            "Many numbers"
        ),
        (
            not url.lower().startswith("https://"),
            10,
            "No HTTPS"
        )
    ]

    for condition, points, reason in checks:
        if condition:
            score += points
            reasons.append(reason)

    brands = detect_brand_impersonation(url)
    typos = detect_typosquatting(url)
    keywords = detect_suspicious_keywords(url)

    if brands:
        score += 25
        reasons.append("Brand impersonation detected")

    if typos:
        score += 30
        reasons.append(
            "Possible typosquatting: "
            + ", ".join(x["brand"] for x in typos)
        )

    if len(keywords) >= 2:
        score += 10
        reasons.append("Multiple suspicious keywords")

    return min(score, 100), reasons


def analyze_url(url):
    ml_probability = float(
        url_model.predict_proba([url])[0][1]
    )

    ml_score = ml_probability * 100

    trusted = is_trusted_domain(url)

    if trusted:
        combined = 0
        verdict = "Verified Low Risk"
        intel_score = 0
        intel_reasons = ["Official domain recognized"]
    else:
        intel_score, intel_reasons = intelligence_score(url)

        brands = detect_brand_impersonation(url)
        typos = detect_typosquatting(url)

        if typos:
            best_similarity = max(
                item["similarity"]
                for item in typos
            )

            if best_similarity >= 95:
                combined = max(
                    85,
                    ml_score * 0.35 + 85 * 0.65
                )
            else:
                combined = max(
                    70,
                    ml_score * 0.45 + 70 * 0.55
                )

        elif brands:
            combined = max(
                75,
                ml_score * 0.45 + 75 * 0.55
            )

        else:
            combined = (
                ml_score * 0.7
                + intel_score * 0.3
            )

        if combined >= 75:
            verdict = "High Risk"
        elif combined >= 40:
            verdict = "Suspicious"
        else:
            verdict = "Low Risk"

    return {
        "verdict": verdict,
        "score": round(float(combined), 2),
        "ml_score": round(float(ml_score), 2),
        "intelligence_score": intel_score,
        "trusted_domain": trusted,
        "brand_impersonation": detect_brand_impersonation(url),
        "typosquatting": detect_typosquatting(url),
        "suspicious_keywords": detect_suspicious_keywords(url),
        "security_findings": explain_url(url),
        "intelligence_reasons": intel_reasons
    }


print("PhishGuard engine upgraded successfully.")
