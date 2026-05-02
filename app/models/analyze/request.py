from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    language: str    