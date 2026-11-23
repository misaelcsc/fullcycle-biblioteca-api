from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Biblioteca API"
    DATABASE_URL: str = "sqlite:///./biblioteca.db"
    DEBUG: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
