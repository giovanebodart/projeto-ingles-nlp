from pydantic import BaseModel

class TranscribeRequest(BaseModel):
    language: str
    url: str
