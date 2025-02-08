from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.commands.schema import RunCommand
from app.commands.service import (
    execute_command,
    get_commands_by_platform,
)
from app.devices.schema import Platform

router = APIRouter()


@router.get("/")
async def read_commands(platform: Platform | None = None):
    return await get_commands_by_platform(platform)


@router.post("/", response_class=StreamingResponse)
async def run_command(
    command_data: RunCommand,
):
    return await execute_command(command_data)
