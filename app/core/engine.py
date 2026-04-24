import time
from app.core.extractor import extract
from app.providers.factory import get_provider, list_providers
from app.core.cache import SimpleCache

cache = SimpleCache()

class ExtractionEngine:

    def __init__(self, provider_name: str = "gemini"):
        self.provider_name = provider_name

        try:
            self.provider = get_provider(provider_name)
        except ValueError:
            self.provider = None

    def run(self, text: str, schema: dict | None, execution_mode: str = "fast"):

        start_time = time.time()
        schema = schema or {}

        cache_key = cache.make_key(text, schema, execution_mode, self.provider_name)

        cached = cache.get(cache_key)
        if cached:
            cached["cached"] = True
            return cached

        if not self.provider:
            return {
                "error": "unsupported_provider",
                "message": f"Provider '{self.provider_name}' desteklenmiyor",
                "available_providers": list_providers()
            }

        mode = "schema" if schema else "auto"

        if execution_mode == "fast":
            data, suggested = extract(
                text,
                schema,
                include_suggested=True,
                provider_instance=self.provider
            )
        else:
            data, _ = extract(
                text,
                schema,
                provider_instance=self.provider
            )

            auto_data, _ = extract(
                text,
                None,
                provider_instance=self.provider
            )

            suggested = {
                k: "string"
                for k in auto_data.keys()
                if k not in schema
            }

        missing = [k for k, v in data.items() if v is None] if schema else []

        confidence = {
            k: 1.0 if v is not None else 0.0
            for k, v in data.items()
        }

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

        cache.set(cache_key, result)

        return result