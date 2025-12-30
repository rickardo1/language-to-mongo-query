import json
from openai import AsyncOpenAI
from core.config import settings
from ..base_service import AIProvider

class OpenAIService(AIProvider):
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.OPENAI_MODEL

    async def convert_to_mongo_query(self, prompt: str) -> dict:
        system_prompt = (
            """Você é um tradutor especializado em MongoDB Query.
      Sua resposta deve ser estritamente um objeto JSON válido do MongoDB.
      Não inclua explicações ou markdown."""
        )

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Converta: {prompt}"}
            ],
            temperature=0,
            response_format={"type": "json_object"}
        )

        content = response.choices[0].message.content
        return json.loads(content) if content else {}
