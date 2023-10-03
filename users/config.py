from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    secret_key: str

    class Config:
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


settings: Settings = Settings()
