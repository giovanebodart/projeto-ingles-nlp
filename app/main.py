from fastapi import FastAPI, HTTPException
from app.models.request import AnalyzeRequest
from app.services.pipeline import analyze_text

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    try:
        return analyze_text(request.texts, request.language)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))    