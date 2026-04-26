import time

class RateLimiter:
    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window = window_seconds
        self.store = {}

    def is_allowed(self, key: str) -> bool:
        now = time.time()

        if key not in self.store:
            self.store[key] = []

        self.store[key] = [
            t for t in self.store[key]
            if now - t < self.window
        ]

        if len(self.store[key]) >= self.max_requests:
            return False

        self.store[key].append(now)
        return True
