import os

RATE_LIMIT = int(os.getenv("RATE_LIMIT", 5))
RATE_WINDOW = int(os.getenv("RATE_WINDOW", 60))

MAX_TEXT_LENGTH = int(os.getenv("MAX_TEXT_LENGTH", 5000))
MAX_SCHEMA_FIELDS = int(os.getenv("MAX_SCHEMA_FIELDS", 50))

CACHE_TTL = int(os.getenv("CACHE_TTL", 300))
CACHE_SIZE = int(os.getenv("CACHE_SIZE", 1000))

GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
GEMINI_TEMPERATURE=int(os.getenv("GEMINI_TEMPERATURE", 0))

LLM_TIMEOUT = int(os.getenv("LLM_TIMEOUT", 10))
