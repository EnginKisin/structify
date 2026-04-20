import json

def build_prompt(text: str, schema: dict | None) -> str:

    if not schema:
        return f"""
Analyze the following text and extract structured information as JSON.

Identify relevant entities such as name, email, intent, or any other meaningful information.
Create a clean and minimal JSON structure based on the content of the text.

Text:
{text}

Example:
Text: "Hello, I'm Ahmet and I want to buy a product. My email is ahmet@gmail.com"
Output:
{{
  "name": "Ahmet",
  "email": "ahmet@gmail.com",
  "intent": "buy"
}}

Rules:
1. Return ONLY valid JSON.
2. Do NOT include explanations or extra text.
3. Use clear and meaningful field names.
4. If a value is uncertain, you may omit the field or set it to null.
5. Keep the JSON structure simple and relevant.

JSON:
"""

    return f"""
Analyze the following text and extract structured data according to the given schema.
Extract all relevant information such as person name, email, intent, or other fields, and map them to the schema fields.

Text:
{text}

Schema:
{json.dumps(schema)}

Example:
Text: "Hello, I'm Ahmet and I want to buy a product. My email is ahmet@gmail.com"  
Schema: {{"name": "string", "email": "string", "intent": ["buy","sell","question"]}}  
Output:
{{
  "name": "Ahmet",
  "email": "ahmet@gmail.com",
  "intent": "buy"
}}

Rules:
1. Return ONLY valid JSON.
2. Use the exact keys from the schema.
3. If a value is missing, set it to null.
4. Do NOT add extra fields.
5. For list fields (e.g. intent), choose the closest matching value from the list.

JSON:
"""

def build_prompt(text: str, schema: dict | None, include_suggested: bool = False) -> str:

    if not schema:
        return f"""
Analyze the following text and extract structured information as JSON.

Identify relevant entities such as name, email, intent, phone, or any other meaningful information.
Create a clean and minimal JSON structure based on the content of the text.

Text:
{text}

Example:
Text: "Hello, I'm Ahmet and I want to buy a product. My email is ahmet@gmail.com"
Output:
{{
  "name": "Ahmet",
  "email": "ahmet@gmail.com",
  "intent": "buy"
}}

Rules:
1. Return ONLY valid JSON.
2. Do NOT include explanations or extra text.
3. Use clear and meaningful field names.
4. If a value is uncertain, you may omit the field or set it to null.
5. Keep the JSON structure simple and relevant.

JSON:
"""

    if include_suggested:
        return f"""
Analyze the following text and extract structured data according to the given schema.
Extract all relevant information such as person name, email, intent, phone, or other fields.

Text:
{text}

Schema:
{json.dumps(schema)}

Example:
Text: "Hello, I'm Ahmet and I want to buy a product. My email is ahmet@gmail.com, phone: 555 555 55 55"  
Schema: {{"name": "string", "email": "string", "intent": ["buy","sell","question"]}}  

Output:
{{
  "data": {{
    "name": "Ahmet",
    "email": "ahmet@gmail.com",
    "intent": "buy"
  }},
  "suggested_schema": {{
    "phone": "string"
  }}
}}

Rules:
1. Return ONLY valid JSON.
2. Use the exact keys from the schema inside "data".
3. If a value is missing, set it to null.
4. Do NOT add extra fields inside "data".
5. Extract additional fields NOT in schema under "suggested_schema".
6. For list fields (e.g. intent), choose the closest matching value from the list.

JSON:
"""

    return f"""
Analyze the following text and extract structured data according to the given schema.
Extract all relevant information such as person name, email, intent, or other fields, and map them to the schema fields.

Text:
{text}

Schema:
{json.dumps(schema)}

Example:
Text: "Hello, I'm Ahmet and I want to buy a product. My email is ahmet@gmail.com"  
Schema: {{"name": "string", "email": "string", "intent": ["buy","sell","question"]}}  

Output:
{{
  "name": "Ahmet",
  "email": "ahmet@gmail.com",
  "intent": "buy"
}}

Rules:
1. Return ONLY valid JSON.
2. Use the exact keys from the schema.
3. If a value is missing, set it to null.
4. Do NOT add extra fields.
5. For list fields (e.g. intent), choose the closest matching value from the list.

JSON:
"""