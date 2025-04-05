from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env",
    )
    PROJECT_NAME: str = "Template FastAPI"
    API_V1_STR: str = "/api/v1"
    DB_PATH: str = "localhost"


settings = Settings()
