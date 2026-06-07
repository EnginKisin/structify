import time
import asyncio
from collections import defaultdict, deque

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window = window_seconds
        self.store = defaultdict(deque)
        self.lock = asyncio.Lock()

    async def is_allowed(self, key: str) -> bool:
        now = time.time()

        async with self.lock:
            q = self.store[key]

            while q and now - q[0] > self.window:
                q.popleft()

            if len(q) >= self.max_requests:
                return False

            q.append(now)
            return True

