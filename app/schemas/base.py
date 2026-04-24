from pydantic import BaseModel
from typing import Dict, Any, Optional


class ExtractionRequest(BaseModel):
    text: str
    schema: Dict[str, Any] | None = None
    execution_mode: Optional[str] = "fast"  # "fast" | "safe"
    provider: Optional[str] = "gemini"
    debug: bool = False


class ExtractionResponse(BaseModel):
    mode: str
    execution_mode: str
    data: Dict[str, Any]
    missing: list[str]
    confidence: Dict[str, float]
    suggested_schema: Dict[str, Any]
    processing_time: float
    cached: bool
    debug: Optional[Dict[str, Any]] = None


class ErrorResponse(BaseModel):
    error: str
    message: str
    available_providers: list[str]
