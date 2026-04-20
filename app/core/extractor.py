import json
from app.providers.gemini import call_gemini
from app.core.prompt_builder import build_prompt

def validate(data: dict) -> dict:
    if "email" in data and data["email"]:
        if "@" not in data["email"]:
            data["email"] = None

    return data

def extract(text: str, schema: dict | None, include_suggested: bool = False):

    prompt = build_prompt(text, schema, include_suggested)
    response_text = call_gemini(prompt)

    try:
        parsed = json.loads(response_text)
    except Exception:
        if schema:
            return {k: None for k in schema.keys()}, {}
        return {}, {}

    if include_suggested and schema:
        data = parsed.get("data", {})
        suggested = parsed.get("suggested_schema", {})
    else:
        data = parsed
        suggested = {}

    if schema:
        for k, v in schema.items():
            if isinstance(v, list) and k in data:
                if data[k] not in v:
                    data[k] = None

    data = validate(data)

    return data, suggested


