import asyncssh
from fastapi import HTTPException
from fastapi.responses import StreamingResponse

from app.commands.db import read_commands_by_platform
from app.commands.schema import RunCommand
from app.devices.schema import Device, Platform
from app.devices.service import get_devices
from app.utils import read_stream


async def get_commands_by_platform(platform: Platform | None = None):
    commands = read_commands_by_platform(platform)
    if not commands:
        raise HTTPException(
            status_code=404, detail="No commands found for the given platform"
        )
    return commands


async def execute_command(command_data: RunCommand):
    device = await get_devices(command_data.from_device)

    if not device:
        raise HTTPException(status_code=404, detail="Device not found")

    platform_comms = await get_commands_by_platform(device.platform)

    command = platform_comms.get_command(command_data.command)

    if command_data.target:
        command = command.format(target=command_data.target)

    return StreamingResponse(generate_stream(device, command), media_type="text/plain")


async def generate_stream(device: Device, command: str):
    try:
        async with asyncssh.connect(
            str(device.address),
            username=device.credentials.username,
            password=device.credentials.password,
            port=device.port,
            options=asyncssh.SSHClientConnectionOptions(known_hosts=None),
        ) as conn:
            process = await conn.create_process(command)

            async for chunk in read_stream(process.stdout):
                yield chunk

            async for chunk in read_stream(process.stderr):
                yield chunk

            exit_status = await process.wait()
            if exit_status != 0:
                yield f"\nProcess exited with status {exit_status}".encode()

    except (OSError, asyncssh.Error) as exc:
        yield f"SSH connection failed: {str(exc)}".encode()
