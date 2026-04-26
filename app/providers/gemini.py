import os
import re
import google.generativeai as genai
from app.providers.base import BaseLLM
from app.core.config import GEMINI_MODEL, GEMINI_TEMPERATURE, LLM_TIMEOUT

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiProvider(BaseLLM):

    def __init__(self):
        self.model = genai.GenerativeModel(GEMINI_MODEL)
    
    def generate(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(
                prompt,
                generation_config={
                    "temperature": GEMINI_TEMPERATURE
                },
                request_options={
                    "timeout": LLM_TIMEOUT
                }
            )

            text = response.text or ""

        except Exception as e:
            raise Exception(f"Gemini generation failed: {str(e)}")

        text = re.sub(r"```json\s*|\s*```", "", text, flags=re.IGNORECASE).strip()

        return text
