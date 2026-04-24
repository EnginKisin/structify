class BaseLLM:
    def generate(self, prompt: str) -> str:
        raise NotImplementedError("LLM provider must implement generate()")
