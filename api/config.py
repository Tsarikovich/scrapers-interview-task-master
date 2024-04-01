from pydantic import BaseSettings


class Settings(BaseSettings):
    redis_url: str = "redis://redis:6379/0"


settings = Settings()
