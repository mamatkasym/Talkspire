from typing import Optional

from pydantic import PostgresDsn, field_validator
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 5
    ALGORITHM: str
    API_V1_STR: str = '/api/v1'
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_PORT: int
    PROJECT_NAME: str = 'Talkspire'
    SECRET_KEY: str
    DATABASE_URL: Optional[PostgresDsn] = None
    ASYNC_DATABASE_URL: Optional[PostgresDsn] = None

    @field_validator("ASYNC_DATABASE_URL", mode='before')
    def assemble_db_connection(cls, v: Optional[str], values: ValidationInfo) -> any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=values.data.get("POSTGRES_USER"),
            password=values.data.get("POSTGRES_PASSWORD"),
            host=values.data.get("POSTGRES_HOST"),
            port=values.data.get('POSTGRES_PORT'),
            path=f"{values.data.get('POSTGRES_DB') or ''}",
        )

    model_config = SettingsConfigDict(env_file="../.env")


settings = Settings()
