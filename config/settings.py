from pydantic import BaseSettings

class Settings(BaseSettings):
    LINE_CHANNEL_ACCESS_TOKEN: str
    LINE_CHANNEL_SECRET: str
    TRANSLATION_ENABLED: bool = True
    TARGET_LANGUAGE: str = "en"

    class Config:
        env_file = ".env"

settings = Settings()
