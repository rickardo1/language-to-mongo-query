from services.openai.openai_service import OpenAIService
from services.gemini.gemini_service import GeminiService
from services.claude.claude_service import ClaudeService

_openai_service = OpenAIService()
_gemini_service = GeminiService()
_claude_service = ClaudeService()

strategy_map = {
    "openai": _openai_service,
    "gemini": _gemini_service,
    "claude": _claude_service
}
