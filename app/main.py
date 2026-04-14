from fastapi import FastAPI
from services.pipeline import analyze_text

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(payload: dict): 
    texts = payload.get("texts", [])
    return analyze_text(texts)
    