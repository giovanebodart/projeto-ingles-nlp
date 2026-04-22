from pydantic import BaseModel
from typing import Optional

class AnalyzeRequest(BaseModel):
    texts: list[str]
    language: str = "EN"   