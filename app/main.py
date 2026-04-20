from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def root():
    return {
        "name": "Structify",
        "status": "running",
        "version": "1.0.0"
    }