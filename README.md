# 🚀 Structify

**AI-powered structured data extraction with schema enforcement and smart schema discovery.**

Structify transforms unstructured text into clean, structured JSON using LLMs.
It supports both **schema-based extraction** and **schema-less parsing**, with optional **automatic schema suggestions**.

---

## ✨ Features

* 🧠 **Schema-based extraction**
  Define your own JSON schema and extract structured data accordingly.

* 🔍 **Schema-less smart parsing**
  Provide only text, and Structify generates a meaningful JSON automatically.

* 💡 **Suggested schema generation**
  Automatically detects missing fields (e.g. phone, address) and suggests them.

* ⚡ **Fast & Safe execution modes**

  * `fast` → single LLM call (low latency)
  * `safe` → multi-step extraction (higher accuracy)

* 📊 **Confidence & missing field detection**
  Know which fields are missing and how reliable the output is.

* ⏱ **Processing time tracking**

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

## 📦 Installation

```bash
git clone https://github.com/your-username/structify.git
cd structify
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
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
  "execution_mode": "safe"
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
  "confidence": {
    "name": 1.0,
    "email": 1.0,
    "intent": 1.0
  },
  "suggested_schema": {
    "phone": "string"
  },
  "processing_time": 0.842
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

