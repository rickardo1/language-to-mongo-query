# AI Query Translator

This project is a natural language translator for **MongoDB** queries using multiple AIs (OpenAI, Gemini, and Claude) through the **Strategy** pattern. Developed with FastAPI to ensure high performance and asynchronous operations.

## Prerequisites

* **Python 3.10+**
* API keys for the desired providers (OpenAI, Google Gemini, or Anthropic Claude).

## How to Run the Project

Follow the steps below to configure and start the API locally:

### 1. Clone and Access the Directory
```bash
git clone <repository-url>
cd dws-challenge

# Create the virtual environment
python -m venv venv

# Activate the environment (Windows)
.\venv\Scripts\activate

# Activate the environment (Linux/Mac)
source venv/bin/activate

pip install -r requirements.txt

# API Keys
OPENAI_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
CLAUDE_API_KEY=your_key_here

# Models
OPENAI_MODEL=gpt-4-turbo
GEMINI_MODEL=gemini-flash-latest
CLAUDE_MODEL=claude-3-5-sonnet-20240620

# API Settings
PORT=8000

python -m uvicorn main:app --reload --port 8000

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

POST /chat/translate-query HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Content-Length: 188

{
  "prompt": "Users who are Brazilians and whose occupation are Software Engineer or Systems Analyst, and who are between 18 and 40 years old.",
  "provider": "gemini"
}       


