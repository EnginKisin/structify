import re

def score_email(value: str, text: str) -> float:
    if not value:
        return 0.0

    score = 0.0

    if re.match(r"^[^@]+@[^@]+\.[^@]+$", value):
        score += 0.6

    if value.lower() in text.lower():
        score += 0.4

    return min(score, 1.0)


def score_string(value: str, text: str) -> float:
    if not value:
        return 0.0

    score = 0.5

    if value.lower() in text.lower():
        score += 0.5

    return min(score, 1.0)


def score_enum(value: str, options: list) -> float:
    if not value:
        return 0.0

    if value in options:
        return 1.0

    return 0.5


def compute_confidence(data: dict, schema: dict | None, text: str) -> dict:
    scores = {}

    for key, value in data.items():

        if not schema:
            scores[key] = 0.7 if value else 0.0
            continue

        rule = schema.get(key)

        if rule == "email":
            scores[key] = score_email(value, text)

        elif rule == "string":
            scores[key] = score_string(value, text)

        elif isinstance(rule, list):
            scores[key] = score_enum(value, rule)

        else:
            scores[key] = 0.6 if value else 0.0

    return scores
