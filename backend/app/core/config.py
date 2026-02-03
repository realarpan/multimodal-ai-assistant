from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    backend_url: str = "http://localhost:8000"
    database_url: str
    redis_url: str = "redis://redis:6379/0"
    jwt_secret: str
    hf_api_token: str
    chroma_dir: str = "/data/chroma"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache
def get_settings() -> Settings:
    return Settings()
