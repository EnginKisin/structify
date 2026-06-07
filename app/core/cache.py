import time
import asyncio
import json
import hashlib
from collections import OrderedDict
from app.core.config import CACHE_TTL, CACHE_SIZE

class LRUCache:
    def __init__(self, ttl_seconds: int = CACHE_TTL, max_size: int = CACHE_SIZE):
        self.store = OrderedDict()
        self.ttl = ttl_seconds
        self.max_size = max_size
        self.lock = asyncio.Lock()

    def make_key(self, text: str, schema: dict, execution_mode: str, provider: str):
        payload = {
            "text": text,
            "schema": schema,
            "execution_mode": execution_mode,
            "provider": provider,
        }

        raw = json.dumps(payload, sort_keys=True)
        return hashlib.md5(raw.encode()).hexdigest()

    async def get(self, key: str):
        async with self.lock:
            if key not in self.store:
                return None

            entry = self.store[key]

            if time.time() - entry["time"] > self.ttl:
                del self.store[key]
                return None

            self.store.move_to_end(key)

            return entry["value"]

    async def set(self, key: str, value: dict):
        async with self.lock:
            if key in self.store:
                self.store.move_to_end(key)

            self.store[key] = {
                "value": value,
                "time": time.time()
            }

            if len(self.store) > self.max_size:
                self.store.popitem(last=False)
