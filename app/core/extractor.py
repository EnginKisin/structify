from app.core.prompt_builder import build_prompt
from app.core.parser import safe_parse_json
from app.core.validator import validate_and_normalize

def extract(text: str, schema: dict | None, include_suggested: bool = False, provider_instance=None):

    prompt = build_prompt(text, schema, include_suggested)

    response_text = provider_instance.generate(prompt)


    try:
        parsed = safe_parse_json(response_text)

        if parsed is None:
            if schema:
                return {k: None for k in schema.keys()}, {}
            return {}, {}
        
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

    data = validate_and_normalize(data, schema)

    return data, suggested


