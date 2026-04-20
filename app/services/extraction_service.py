from app.core.extractor import extract
import time

def run_extraction(text: str, schema: dict | None, execution_mode: str = "fast"):

    start_time = time.time()
    schema = schema or {}

    mode = "schema" if schema else "auto"

    if execution_mode == "fast":
        data, suggested = extract(text, schema, include_suggested=True)

    else:
        data, _ = extract(text, schema)
        auto_data, _ = extract(text, None)

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

    return {
        "mode": mode,
        "execution_mode": execution_mode,
        "data": data,
        "missing": missing,
        "confidence": confidence,
        "suggested_schema": suggested,
        "processing_time": processing_time
    }


# def run_extraction(text: str, schema: dict | None, execution_mode: str = "fast"):

#     start_time = time.time()

#     mode = "schema" if schema else "auto"

#     if execution_mode == "fast":
#         data, suggested = extract(text, schema, include_suggested=True)

#     else:
#         data, _ = extract(text, schema)
#         auto_data, _ = extract(text, None)
#         suggested = {
#             k: "string"
#             for k in auto_data.keys()
#             if k not in schema
#         }

#         if schema:
#             suggested = {k: v for k, v in suggested.items() if k not in schema}

#     missing = [k for k, v in data.items() if v is None] if schema else []

#     confidence = {
#         k: 1.0 if v is not None else 0.0
#         for k, v in data.items()
#     }

#     processing_time = round(time.time() - start_time, 3)

#     return {
#         "mode": mode,
#         "execution_mode": execution_mode,
#         "data": data,
#         "missing": missing,
#         "confidence": confidence,
#         "suggested_schema": suggested,
#         "processing_time": processing_time
#     }