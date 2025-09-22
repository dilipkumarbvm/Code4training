from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List
from schemas import EmailIn, ClassificationOut, BulkIn, FeedbackIn
from model import classify, LABELS
import json, os, datetime

app = FastAPI(title="Email Triage & Categorization Agent", version="0.2.0")  # enhanced

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok", "version": "0.2.0"}

@app.get("/labels")
def labels() -> Dict[str, list]:
    return {"labels": LABELS}

@app.post("/classify", response_model=ClassificationOut)
def classify_email(email: EmailIn) -> ClassificationOut:
    data = classify(email.subject or "", email.body or "")
    return ClassificationOut(**data)

@app.post("/bulk_classify")
def bulk_classify(bulk: BulkIn):
    out = []
    for e in bulk.emails:
        out.append(classify(e.subject or "", e.body or ""))
    return {"results": out, "count": len(out)}

FEEDBACK_FILE = os.environ.get("FEEDBACK_FILE", "feedback.jsonl")

@app.post("/feedback")
def feedback(fb: FeedbackIn):
    rec = {
        "ts": datetime.datetime.utcnow().isoformat() + "Z",
        "subject": fb.subject, "body": fb.body,
        "predicted": fb.predicted, "correct": fb.correct,
    }
    with open(FEEDBACK_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")
    return {"ok": True}
