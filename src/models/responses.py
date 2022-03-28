from typing import Optional
from pydantic import BaseModel


class TranslationResponse(BaseModel):
    translation: Optional[str] = None
    error: Optional[str] = None
