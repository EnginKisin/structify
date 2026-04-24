from app.providers.gemini import GeminiProvider


AVAILABLE_PROVIDERS = {
    "gemini": GeminiProvider,
}

def get_provider(name: str = "gemini"):
    provider_cls = AVAILABLE_PROVIDERS.get(name)

    if not provider_cls:
        raise ValueError(name)

    return provider_cls()


def list_providers():
    return list(AVAILABLE_PROVIDERS.keys())