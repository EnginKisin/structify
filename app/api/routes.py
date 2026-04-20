from fastapi import APIRouter
from app.schemas.base import ExtractionRequest, ExtractionResponse
from app.services.extraction_service import run_extraction

router = APIRouter()


@router.post("/extract", response_model=ExtractionResponse)
def extract_endpoint(req: ExtractionRequest):
    result = run_extraction(req.text, req.schema, req.execution_mode)
    return result