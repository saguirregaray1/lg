from dotenv import load_dotenv
from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    config_path: DirectoryPath

    model_config = SettingsConfigDict(env_prefix="")


settings = Settings()  # noqa
