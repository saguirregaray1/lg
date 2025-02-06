from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.commands.schema import RunPing
from app.devices.schema import Platform
from app.commands.service import (
    get_commands_by_platform,
    run_ping_command,
)

router = APIRouter()


@router.get("/")
async def read_commands(platform: Platform | None = None):
    return await get_commands_by_platform(platform)


@router.post("/", response_class=StreamingResponse)
async def run_ping(
    command_data: RunPing,
):
    return await run_ping_command(command_data)
