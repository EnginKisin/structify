from app.core.prompt_builder import build_prompt
from app.core.parser import safe_parse_json
from app.core.validator import validate_and_normalize

async def extract(text: str, schema: dict | None, include_suggested: bool = False, provider_instance=None, debug: bool = False):

    prompt = build_prompt(text, schema, include_suggested)

    debug_info = {}

    if debug:
        debug_info["prompt"] = prompt

    response_text = await provider_instance.generate(prompt)

    if debug:
        debug_info["raw_response"] = response_text

    try:
        parsed = safe_parse_json(response_text)

        if parsed is None:
            if debug:
                debug_info["parse_error"] = True

            if schema:
                return {k: None for k in schema.keys()}, {}, debug_info
            return {}, {}, debug_info
        
    except Exception:
        if debug:
            debug_info["parse_error"] = True

        if schema:
            return {k: None for k in schema.keys()}, {}, debug_info
        return {}, {}, debug_info

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

    if debug:
        debug_info["parsed"] = data

    return data, suggested, debug_info
