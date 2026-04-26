import time
from app.core.extractor import extract
from app.providers.factory import get_provider, list_providers
from app.core.cache import LRUCache
from app.core.confidence import compute_confidence
from fastapi import HTTPException
from app.core.config import MAX_TEXT_LENGTH, MAX_SCHEMA_FIELDS

cache = LRUCache()

class ExtractionEngine:

    def __init__(self, provider_name: str = "gemini"):
        self.provider_name = provider_name

        try:
            self.provider = get_provider(provider_name)
        except ValueError:
            self.provider = None

    def run(self, text: str, schema: dict | None, execution_mode: str = "fast", debug: bool = False):

        if len(text) > MAX_TEXT_LENGTH:
            raise HTTPException(
                status_code=400,
                detail={
                    "error": "text_too_long",
                    "message": "Text exceeds maximum length of {MAX_TEXT_LENGTH} characters",
                }
            )
        
        if schema and len(schema) > MAX_SCHEMA_FIELDS:
            raise HTTPException(
                status_code=400,
                detail={
                    "error": "schema_too_long",
                    "message": "Schema exceeds maximum of {MAX_SCHEMA_FIELDS} fields",
                }
            )

        start_time = time.time()
        schema = schema or {}

        cache_key = cache.make_key(text, schema, execution_mode, self.provider_name)

        cached = cache.get(cache_key)
        if cached:
            cached["cached"] = True
            cached["processing_time"] = 0
            if debug:
                cached["debug"] = {
                    "cache_hit": True,
                    "note": "debug limited: served from cache"
                }
            return cached
        
        if not self.provider:
            raise HTTPException(
                status_code=400,
                detail={
                    "error": "unsupported_provider",
                    "message": f"Provider '{self.provider_name}' desteklenmiyor",
                    "available_providers": list_providers()
                }
            )

        mode = "schema" if schema else "auto"

        if execution_mode == "fast":
            data, suggested, debug_info = extract(
                text,
                schema,
                include_suggested=True,
                provider_instance=self.provider,
                debug=debug
            )
        else:
            data, _, debug_info = extract(
                text,
                schema,
                provider_instance=self.provider,
                debug=debug
            )

            auto_data, _, _ = extract(
                text,
                None,
                provider_instance=self.provider,
                debug=debug
            )

            suggested = {
                k: "string"
                for k in auto_data.keys()
                if k not in schema
            }

        missing = [k for k, v in data.items() if v is None] if schema else []

        confidence = compute_confidence(data, schema, text)


        processing_time = round(time.time() - start_time, 3)

        result = {
            "mode": mode,
            "execution_mode": execution_mode,
            "data": data,
            "missing": missing,
            "confidence": confidence,
            "suggested_schema": suggested,
            "processing_time": processing_time,
            "cached": False
        }

        if debug:
            result["debug"] = {
                **debug_info,
                "cache_hit": False
            }

        cache.set(cache_key, {k: v for k, v in result.items() if k != "debug"})

        return result
