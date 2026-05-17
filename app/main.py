from fastapi import FastAPI, HTTPException
from app.models.transcribe.request import TranscribeRequest
from app.services.pipeline import execute

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/transcribe")
def transcribe(request: TranscribeRequest):
    try:
        print("URL RECEBIDA:", request.url)
        print("TIPO:", type(request.url))
        return execute(request.url, request.language)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))