from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from ..schemas.commands import RunPing, Command
from ..schemas.devices import Platform
from ..services.commands import get_commands_by_platform
from ..services.devices import get_devices
import asyncssh

router = APIRouter()


@router.get("/")
async def read_commands(platform: Platform | None = None):
    return await get_commands_by_platform(platform)


@router.post("/", response_class=StreamingResponse)
async def run_ping(
    command_data: RunPing,
):
    from_device = await get_devices(command_data.from_device)

    if not from_device:
        raise HTTPException(status_code=404, detail="Device not found")

    platform_comms = await get_commands_by_platform(from_device.platform)

    ping_command = platform_comms.get_command(Command.ping)

    async def generate_stream():
        try:
            async with asyncssh.connect(
                "localhost", username="root", password="ffr", port=2222
            ) as conn:
                process = await conn.create_process("ping -w 3 8.8.8.8")

                async def read_stream(stream):
                    while True:
                        line = await stream.readline()
                        if not line:
                            break
                        yield line.encode()

                async for chunk in read_stream(process.stdout):
                    yield chunk

                async for chunk in read_stream(process.stderr):
                    yield chunk

                exit_status = await process.wait()
                if exit_status != 0:
                    yield f"\nProcess exited with status {exit_status}".encode()

        except (OSError, asyncssh.Error) as exc:
            yield f"SSH connection failed: {str(exc)}".encode()

    return StreamingResponse(generate_stream(), media_type="text/plain")
