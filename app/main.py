from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.api.routes import router
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

app.include_router(router)


@app.get("/")
def root():
    return {
        "name": "Structify",
        "status": "running",
        "version": "1.0.0"
    }

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):

    if isinstance(exc.detail, dict):
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.detail
        )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": "http_error",
            "message": str(exc.detail)
        }
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "internal_server_error",
            "message": "Something went wrong"
        }
    )
