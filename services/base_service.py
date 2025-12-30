from abc import ABC, abstractmethod
from typing import Any

class AIProvider(ABC):
    @abstractmethod
    async def convert_to_mongo_query(self, prompt: str) -> dict:
        """Método específico para o Challenge."""
        pass
