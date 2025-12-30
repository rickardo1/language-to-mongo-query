from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    DEBUG: bool = False

    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4o-mini"

    GEMINI_API_KEY: str
    GEMINI_MODEL: str = "gemini-flash-latest"

    CLAUDE_API_KEY: str
    CLAUDE_MODEL: str = "claude-3-5-sonnet-20240620"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore")

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
