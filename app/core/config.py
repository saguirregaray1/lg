from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import FilePath

load_dotenv()


class Settings(BaseSettings):
    devices_path: FilePath
    commands_path: FilePath

    model_config = SettingsConfigDict(env_prefix="")


settings = Settings()  # noqa
