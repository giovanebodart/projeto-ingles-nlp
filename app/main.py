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
        return execute(str(request.url), str(request.language))
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))