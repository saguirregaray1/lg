from app.commands.schema import CommandsFile
from app.core.config import settings
from app.devices.schema import Platform
from app.utils import read_yaml_file


def load_commands():
    commands_file = read_yaml_file(
        settings.config_path.name + "/commands.yaml", CommandsFile
    )

    return commands_file.commands


commands_db = load_commands()


def read_commands_by_platform(platform: Platform | None = None):
    if platform:
        return commands_db.get(platform)
    return commands_db
