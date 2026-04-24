import os
import re
import google.generativeai as genai
from app.providers.base import BaseLLM

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class GeminiProvider(BaseLLM):

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate(self, prompt: str) -> str:
        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature": 0
            }
        )

        text = response.text or ""

        text = re.sub(r"```json\s*|\s*```", "", text, flags=re.IGNORECASE).strip()

        return text
