import re


def normalize_string(val):
    if not isinstance(val, str):
        return val
    return val.strip()


def normalize_email(val):
    if not isinstance(val, str):
        return None

    val = val.strip().lower()

    if re.match(r"^[^@]+@[^@]+\.[^@]+$", val):
        return val

    return None


def normalize_number(val):
    try:
        return float(val)
    except:
        return None


def normalize_enum(val, options: list):
    if not isinstance(val, str):
        return None

    val_lower = val.lower()

    for opt in options:
        if val_lower == opt.lower():
            return opt

    for opt in options:
        if opt.lower() in val_lower:
            return opt

    return None


def validate_and_normalize(data: dict, schema: dict | None) -> dict:

    if not schema:
        return data

    cleaned = {}

    for key, rule in schema.items():
        val = data.get(key)

        if val is None:
            cleaned[key] = None
            continue

        if isinstance(rule, list):
            cleaned[key] = normalize_enum(val, rule)
            continue

        if isinstance(rule, dict):
            t = rule.get("type")

            if t == "string":
                cleaned[key] = normalize_string(val)

            elif t == "number":
                cleaned[key] = normalize_number(val)

            elif t == "email":
                cleaned[key] = normalize_email(val)

            else:
                cleaned[key] = val

            continue

        if rule == "string":
            cleaned[key] = normalize_string(val)

        elif rule == "number":
            cleaned[key] = normalize_number(val)

        elif rule == "email":
            cleaned[key] = normalize_email(val)

        else:
            cleaned[key] = val

    return cleaned