# Email Triage & Categorization Agent – Hackathon Kit

This kit contains:
- **frontend/** – Single‑file `index.html` for demo UI (vanilla JS)
- **backend/** – FastAPI service with `/classify`, `/bulk_classify`, `/feedback`

## Run backend

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

## Open frontend
Just open `frontend/index.html` in a browser. (If CORS blocks on file://, serve it: `python -m http.server 8080` and visit http://localhost:8080)

Optional: pass a custom API URL with `?api=http://localhost:8000`

## Feedback loop
Click **Thumbs‑up / Fix Label** in the UI to send records to `/feedback` (stored in `feedback.jsonl`). You can use these to tune rules or train ML later.

## Bulk classify
Use the **Bulk** tab to stress‑test with multiple emails at once.

