import hashlib
import json

class SimpleCache:
    def __init__(self):
        self.store = {}

    def make_key(self, text: str, schema: dict, execution_mode: str, provider: str):
        payload = {
            "text": text,
            "schema": schema,
            "execution_mode": execution_mode,
            "provider": provider,
        }

        raw = json.dumps(payload, sort_keys=True)
        return hashlib.md5(raw.encode()).hexdigest()

    def get(self, key: str):
        return self.store.get(key)

    def set(self, key: str, value: dict):
        self.store[key] = value