from pydantic import BaseModel, Field
from enum import Enum

class ProviderEnum(str, Enum):
    OPENAI = "openai"
    GEMINI = "gemini"
    CLAUDE = "claude"

class TranslateQueryDTO(BaseModel):
    prompt: str = Field(..., min_length=3, description="Prompt")
    provider: ProviderEnum = Field(..., description="Which provider to use")

    class Config:
        use_enum_values = True
