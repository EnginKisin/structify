from fastapi import APIRouter
from typing import Union
from app.schemas.base import ExtractionRequest, ExtractionResponse
from app.schemas.base import ExtractionResponse, ErrorResponse
from app.services.extraction_service import run_extraction

router = APIRouter()


@router.post("/extract", response_model=Union[ExtractionResponse, ErrorResponse])
def extract_endpoint(req: ExtractionRequest):
    result = run_extraction(req.text, req.schema, req.execution_mode, req.provider)
    return result
