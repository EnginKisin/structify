# 🚀 Structify

**AI-powered structured data extraction with schema enforcement and smart schema discovery.**

Structify transforms unstructured text into clean, structured JSON using LLMs.
A lightweight LLM-powered extraction engine with validation, caching, and confidence scoring.
It supports both **schema-based extraction** and **schema-less parsing**, with optional **automatic schema suggestions**.

---

## 🌐 API Overview

Structify exposes a REST API for structured data extraction.

### Endpoint
`POST /extract`

---

## ✨ Features

* 🧠 **Schema-based extraction**
* 🔍 **Schema-less smart parsing**
* 💡 **Suggested schema generation**
* ⚡ **Fast & Safe execution modes**
  * `fast` → single LLM call (low latency)
  * `safe` → multi-step extraction (higher accuracy)
* 📊 **Confidence & missing field detection**
* ⏱ **Processing time tracking**
* ⚙️ **Provider-based architecture (extensible LLM support)**
* 🧹 **Validation & normalization pipeline**
* 🧠 **Rule-based confidence scoring**
* 💾 **LRU caching layer**
* 🐛 **Debug mode for full extraction visibility**
* 🚨 **Global error handling**
* 📏 **Input validation (length limits)**
* 🚦 **Rate limiting (IP-based)**

---

## 🧠 How It Works

Structify operates in two dimensions:

### 1. Mode (Automatic)

| Mode     | Description                                       |
| -------- | ------------------------------------------------- |
| `auto`   | No schema provided → AI generates structured JSON |
| `schema` | Schema provided → AI fills only defined fields    |

---

### 2. Execution Mode

| Mode   | Description                                                        |
| ------ | ------------------------------------------------------------------ |
| `fast` | ⚡ Single LLM call (faster, cheaper)                                |
| `safe` | 🧠 Dual LLM calls (more accurate, especially for suggested fields) |

---

### 3. Architecture
Text → Prompt Builder → LLM Provider → JSON Parser → Validator → Confidence Engine → Response

---

## 📦 Installation

```bash
git clone https://github.com/EnginKisin/structify.git
cd structify
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

> ⚠️ Do not commit your `.env` file. Use `.env.example` instead.

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-2.5-flash
GEMINI_TEMPERATURE=0

RATE_LIMIT=5      # requests per window
RATE_WINDOW=60    # seconds

MAX_TEXT_LENGTH=5000
MAX_SCHEMA_FIELDS=50

CACHE_TTL=300
CACHE_SIZE=1000

LLM_TIMEOUT=10
```

---

## ▶️ Run the API

```bash
uvicorn app.main:app --reload
```

---

## 📌 Example Usage

### 🔹 Request

```json
{
  "text": "Merhaba ben Ahmet, ürün almak istiyorum. Email: ahmet@gmail.com, Telefon: 555 123 45 67",
  "schema": {
    "name": "string",
    "email": "string",
    "intent": ["buy", "sell", "question"]
  },
  "execution_mode": "safe",
  "provider": "gemini",
  "debug": true
}
```

---

### 🔹 Response

```json
{
  "mode": "schema",
  "execution_mode": "safe",
  "data": {
    "name": "Ahmet",
    "email": "ahmet@gmail.com",
    "intent": "buy"
  },
  "missing": [],
  "confidence": {...},
  "suggested_schema": {
    "phone": "string"
  },
  "processing_time": 0.842,
  "cached": false,
  "debug": {...}
}
```

---

## ⚖️ Fast vs Safe Mode

| Feature          | Fast        | Safe          |
| ---------------- | ----------- | ------------- |
| Speed            | ⚡           | 🐢            |
| Cost             | 💸 Low      | 💸💸 Higher   |
| Accuracy         | Good        | Better        |
| Suggested fields | Approximate | More reliable |

---

## 🛠 Tech Stack

* ⚡ FastAPI
* 🧠 Gemini (Google Generative AI)
* 🐍 Python

