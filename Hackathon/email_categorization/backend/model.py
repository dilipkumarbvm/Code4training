import re
from typing import Dict, List, Tuple
from collections import defaultdict

LABELS = [
    "Urgent",
    "Finance/Invoice",
    "Support",
    "Sales/Lead",
    "HR/Recruiting",
    "Security/IT",
    "Newsletter/Marketing",
    "Personal",
    "Spam",
]

KEYWORDS = {
    "Urgent": ["urgent", "asap", "immediately", "critical", "prod down", "sev1", "sev-1", "p1"],
    "Finance/Invoice": ["invoice", "payment", "po ", "purchase order", "remittance", "wire", "accounting", "bill", "due"],
    "Support": ["issue", "bug", "error", "not working", "broken", "support", "ticket", "outage", "fails"],
    "Sales/Lead": ["pricing", "quote", "demo", "trial", "subscribe", "licensing", "lead", "sow", "proposal", "renewal"],
    "HR/Recruiting": ["resume", "cv", "interview", "offer", "benefit", "payroll", "onboarding", "recruit", "career"],
    "Security/IT": ["password", "mfa", "vpn", "phishing", "compromised", "ransomware", "patch", "security", "okta", "single sign-on"],
    "Newsletter/Marketing": ["unsubscribe", "newsletter", "campaign", "webinar", "blog", "event", "marketing", "ebook"],
    "Personal": ["birthday", "party", "family", "vacation", "dinner", "lunch"],
    "Spam": ["winner", "free", "claim now", "bitcoin", "crypto", "adult", "casino", "viagra"],
}

ROUTING = {
    "Urgent": ("#incidents", 4, 4),
    "Finance/Invoice": ("#fin-ops", 3, 48),
    "Support": ("#support", 3, 72),
    "Sales/Lead": ("#sales", 2, 72),
    "HR/Recruiting": ("#people-ops", 2, 72),
    "Security/IT": ("#secops", 3, 24),
    "Newsletter/Marketing": ("#marketing", 1, 168),
    "Personal": ("(skip/low)", 1, 168),
    "Spam": ("(junk)", 1, 0),
}

AMOUNT_RE = re.compile(r"(?:usd\s*)?\$?\b(\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\d+(?:\.\d{2})?)\b")
PO_RE = re.compile(r"\b(?:po|purchase\s*order)\s*[:#]?\s*([a-z0-9\-]{4,})", re.I)
INVOICE_RE = re.compile(r"\b(?:inv|invoice)\s*(?:no\.?|#|number)?\s*[:#]?\s*([a-z0-9\-]{4,})", re.I)
DUE_RE = re.compile(r"\b(?:net\s*(\d+)|due\s*(?:by|on)?\s*([a-z]{3,9}\s*\d{1,2}|\d{1,2}/\d{1,2}/\d{2,4}))", re.I)
PRIORITY_RE = re.compile(r"\b(sev\s*[-]?(\d)|p(\d))\b", re.I)

NEGATIONS = ["no ", "not ", "without ", "never ", "cannot ", "can't "]

def tokenize(text: str) -> List[str]:
    return re.findall(r"[a-z0-9']+", text.lower())

def negated(text: str, kw: str) -> bool:
    idx = text.lower().find(kw.lower())
    if idx < 0: return False
    window = text[max(0, idx-12):idx].lower()
    return any(n in window for n in NEGATIONS)

def keyword_scores(text: str) -> Dict[str, float]:
    lower = text.lower()
    tokens = tokenize(lower)
    counts = defaultdict(int)
    for t in tokens:
        counts[t] += 1
    scores = {}
    for label, kws in KEYWORDS.items():
        s = 0.0
        for kw in kws:
            parts = kw.lower().split()
            if len(parts) == 1:
                c = counts.get(parts[0], 0)
                if c and not negated(lower, parts[0]): s += c
            else:
                hit = (kw.lower() in lower) and (not negated(lower, kw))
                if hit: s += 2.0
        scores[label] = s
    # de-boost Newsletter vs Spam clashes
    if scores.get("Newsletter/Marketing",0) and ("unsubscribe" in lower and "invoice" not in lower):
        scores["Spam"] += 0.5
    return scores

def normalize(scores: Dict[str, float]) -> Dict[str, float]:
    total = sum(scores.values()) + 1e-9
    return {k: v/total for k, v in scores.items()}

def topk(d: Dict[str, float], k=3):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)[:k]

def extract_entities(text: str) -> Dict[str, str]:
    out = {}
    m = INVOICE_RE.search(text)
    if m: out["invoice_number"] = m.group(1)
    m = PO_RE.search(text)
    if m: out["po_number"] = m.group(1)
    m = AMOUNT_RE.search(text.replace(",", ""))
    if m: out["amount"] = m.group(1)
    m = DUE_RE.search(text)
    if m: out["terms_or_due"] = m.group(0)
    sev = PRIORITY_RE.search(text)
    if sev: out["declared_priority"] = sev.group(0)
    return out

def priority_boost(text: str) -> int:
    t = text.lower()
    if any(w in t for w in ["sev1", "sev-1", "p1", "critical", "prod down", "outage"]): return 1
    return 0

def classify(subject: str, body: str):
    text = f"{subject}\n{body}"
    scores = keyword_scores(text)
    for lbl in LABELS: scores[lbl] = scores.get(lbl, 0.0) + 0.01
    norm = normalize(scores)
    best_label, best_score = max(norm.items(), key=lambda x: x[1])
    entities = extract_entities(text)
    routed_queue, base_priority, sla_hours = ROUTING.get(best_label, ("#inbox", 2, 72))
    priority = min(5, base_priority + priority_boost(text))
    actions = []
    if best_label == "Finance/Invoice":
        actions.append("Create AP entry and start 2-way match" if ("invoice_number" in entities and "amount" in entities) else "Request missing invoice details")
    if best_label == "Support": actions.append("Open/append to ticket")
    if best_label == "Security/IT": actions.append("Notify SecOps on-call")
    if best_label == "Sales/Lead": actions.append("Push to CRM as Lead")
    if best_label == "Urgent": actions.append("Escalate to incident channel")
    if best_label == "Newsletter/Marketing": actions.append("Consider auto-archive")
    if best_label == "Spam": actions.append("Move to Junk")
    if not actions: actions.append("Route to owner")
    return {
        "label": best_label,
        "confidence": round(float(best_score), 4),
        "reasons": [f"Keyword match score = {round(float(scores[best_label]),2)}"],
        "suggested_actions": actions,
        "priority": priority,
        "sla_hours": sla_hours,
        "routed_queue": routed_queue,
        "extracted": entities,
        "alt_labels": [{k: round(float(v),4)} for k, v in topk(norm, k=3)],
    }
