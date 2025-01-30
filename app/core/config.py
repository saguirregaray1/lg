from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import FilePath
from dotenv import load_dotenv
import os

load_dotenv(".env")  # Manually load env file

print("DEVICES_PATH:", os.getenv("DEVICES_PATH"))
print("COMMANDS_PATH:", os.getenv("COMMANDS_PATH"))


class Settings(BaseSettings):
    devices_path: FilePath
    commands_path: FilePath

    model_config = SettingsConfigDict(env_prefix="")


settings = Settings()
