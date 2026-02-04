from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # API
    DEBUG: bool = False
    API_TITLE: str = "Multimodal AI Assistant"
    API_VERSION: str = "1.0.0"
    
    # Hugging Face
    HF_API_TOKEN: str = "dummy"
    HF_MODEL_ID: str = "llava-1.5-7b"
    
    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost/multimodal"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # JWT
    JWT_SECRET: str = "dev-secret-do-not-use-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24
    
    # WebSocket
    WEBSOCKET_URL: str = "ws://localhost:8000/ws"
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
