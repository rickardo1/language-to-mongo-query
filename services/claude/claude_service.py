import json
from anthropic import AsyncAnthropic
from core.config import settings
from ..base_service import AIProvider

class ClaudeService(AIProvider):
    def __init__(self):
        self.client = AsyncAnthropic(api_key=settings.CLAUDE_API_KEY)
        self.model = settings.CLAUDE_MODEL

    async def convert_to_mongo_query(self, prompt: str) -> dict:
        response = await self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            system=("""Você é um tradutor especializado em MongoDB Query.
      Sua resposta deve ser estritamente um objeto JSON válido do MongoDB.
      Não inclua explicações ou markdown.
      Texto para converter:"""),
            messages=[
                {"role": "user", "content": f"Converta para query MongoDB: {prompt}"}
            ],
            temperature=0
        )

        content = response.content[0].text
        return json.loads(content)
