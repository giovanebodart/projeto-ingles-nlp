from pydantic import BaseModel


class TranscribeRequest(BaseModel):
    language: str
    audio_url: str
