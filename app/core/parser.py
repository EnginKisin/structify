import json
import re


def clean_json_text(text: str) -> str:
    text = re.sub(r"```json\s*|\s*```", "", text, flags=re.IGNORECASE)

    text = re.sub(r",\s*}", "}", text)
    text = re.sub(r",\s*]", "]", text)

    return text.strip()


def safe_parse_json(text: str) -> dict | None:
    try:
        return json.loads(text)
    except Exception:
        cleaned = clean_json_text(text)
        try:
            return json.loads(cleaned)
        except Exception:
            return None