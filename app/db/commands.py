from app.core.config import settings
from ..schemas.commands import CommandsFile
from ..schemas.devices import Platform
from ..utils import read_yaml_file


def load_commands():
    commands_file = read_yaml_file(settings.commands_path, CommandsFile)

    return commands_file.commands


commands_db = load_commands()


def read_commands_by_platform(platform: Platform | None = None):
    if platform:
        return commands_db.get(platform)
    return commands_db
