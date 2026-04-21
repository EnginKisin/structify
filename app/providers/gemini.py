import os
import re
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def call_gemini(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0,
        }
    )

    text = response.text or ""

    text = re.sub(r"```json\s*|\s*```", "", text, flags=re.IGNORECASE).strip()

    return text