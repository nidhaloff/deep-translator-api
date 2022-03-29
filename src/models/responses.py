from typing import Optional
from pydantic import BaseModel


class TranslationResponse(BaseModel):
    """class that represents the response api."""

    translation: Optional[str] = None
    error: Optional[str] = None
