from fastapi import FastAPI, HTTPException
from app.models.analyze.request import AnalyzeRequest
from app.models.transcribe.request import TranscribeRequest
from app.services.nlp.pipeline import analyze_text
from app.services.transcribe.pipeline import execute

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    try:
        return analyze_text(request.language)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))    
    
@app.post
def transcribe(request: TranscribeRequest):
    try:
        return execute(request.audio_url)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))