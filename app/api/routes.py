from fastapi import APIRouter
from app.schemas.base import ExtractionRequest, ExtractionResponse
from fastapi import Request, HTTPException
from app.core.rate_limiter import RateLimiter
from app.core.config import RATE_LIMIT, RATE_WINDOW
from app.services.extraction_service import run_extraction

router = APIRouter()

limiter = RateLimiter(max_requests=RATE_LIMIT, window_seconds=RATE_WINDOW)

@router.post("/extract", response_model=ExtractionResponse)
def extract_endpoint(req: ExtractionRequest, request: Request):

    client_ip = request.client.host

    if not limiter.is_allowed(client_ip):
        raise HTTPException(
            status_code=429,
            detail={
                "error": "rate_limit_exceeded",
                "message": "Too many requests. Try again later."
            }
        )

    result = run_extraction(req.text, req.schema, req.execution_mode, req.provider, req.debug)

    return result
