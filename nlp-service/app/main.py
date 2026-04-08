from fastapi import FastAPI
from app.services.pipeline import analyze_text

app = FastAPI()

@app.post("/analyze")
def analyze(payload: dict): 
    texts = payload.get("texts", [])
    return analyze_text(texts)
    