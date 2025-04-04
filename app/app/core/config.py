from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env",
    )

    DB_PATH: str = "sqlite:///../matrix.db"


settings = Settings()
