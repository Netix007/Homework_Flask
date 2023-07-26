from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str

    NAME_MAX_LENGTH: int = 32
    EMAIL_MAX_LENGTH: int = 128
    PASSWORD_MAX_LENGTH: int = 128

    class Config:
        env_file = ".env"


settings = Settings()
