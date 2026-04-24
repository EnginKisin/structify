from app.core.engine import ExtractionEngine


def run_extraction(text: str, schema: dict | None, execution_mode: str = "fast", provider: str = "gemini", debug: bool = False):

    engine = ExtractionEngine(provider_name=provider)

    return engine.run(text, schema, execution_mode, debug)