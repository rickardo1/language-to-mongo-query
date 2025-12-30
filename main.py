from fastapi import FastAPI, HTTPException
from dto.translate_dto import TranslateQueryDTO
from services.strategy import strategy_map
from core.logging import logger

app = FastAPI(title="AI Query Translator")

@app.post("/chat/translate-query")
async def translate(dto: TranslateQueryDTO):
    logger.info(f"Recebendo requisição para o provider: {dto.provider}")

    service = strategy_map.get(dto.provider.lower())

    if not service:
        logger.error(f"Provider {dto.provider} não encontrado no map")
        raise HTTPException(status_code=400, detail="Provider não suportado")

    result = await service.convert_to_mongo_query(dto.prompt)

    logger.info("Tradução concluída com sucesso")
    return result
