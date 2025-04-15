from app.commands.schema import CommandSet, CommandsFile
from app.core.config import settings
from app.devices.schema import Platform
from app.utils import read_yaml_file


def load_commands() -> dict[Platform, CommandSet]:
    commands_file = read_yaml_file(settings.config_path / "commands.yaml", CommandsFile)

    return commands_file.commands


commands_db = load_commands()


def read_commands_by_platform(
    platform: Platform,
) -> CommandSet | None:
    return commands_db.get(platform)


def read_commands() -> dict[Platform, CommandSet]:
    return commands_db
