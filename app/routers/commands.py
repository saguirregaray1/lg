from fastapi import APIRouter

from ..core.config import settings
from ..schemas.commands import CommandsFile
from ..schemas.devices import Platform
from ..utils import read_yaml_file

router = APIRouter()


@router.get("/")
async def read_commands(device: Platform | None = None):
    commands_file = read_yaml_file(settings.commands_path, CommandsFile)
    return commands_file.commands
