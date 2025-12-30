import json
import google.generativeai as genai
from core.config import settings
from ..base_service import AIProvider

class GeminiService(AIProvider):
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(settings.GEMINI_MODEL)
        self.model_config = {
            "temperature": 0,
            "system": ("""Você é um tradutor especializado em MongoDB Query.
      Sua resposta deve ser estritamente um objeto JSON válido do MongoDB.
      Não inclua explicações ou markdown.""")
        }

    async def convert_to_mongo_query(self, prompt: str) -> dict:
        response = await self.model.generate_content_async(
            f"Converta para JSON de query MongoDB: {prompt}",
            generation_config={"response_mime_type": "application/json"}
        )
        return json.loads(response.text) if response.text else {}
