from dotenv import load_dotenv
from pydantic import FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    devices_path: FilePath
    commands_path: FilePath

    model_config = SettingsConfigDict(env_prefix="")


settings = Settings()  # noqa
