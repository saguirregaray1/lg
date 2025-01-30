from fastapi import HTTPException

from app.db.commands import read_commands_by_platform
from app.schemas.devices import Platform
import asyncio
import asyncssh
import sys
from app.utils import read_stream


async def get_commands_by_platform(platform: Platform | None = None):
    commands = read_commands_by_platform(platform)
    if not commands:
        raise HTTPException(
            status_code=404, detail="No commands found for the given platform"
        )
    return commands


async def run_command(command: str) -> None:
    async with asyncssh.connect(
        "localhost", username="root", password="ffr", port=2222
    ) as conn:
        try:
            process = await conn.create_process("ping -w 3 8.8.8.8")

            stdout_task = asyncio.create_task(read_stream(process.stdout, sys.stdout))
            stderr_task = asyncio.create_task(read_stream(process.stderr, sys.stderr))

            await asyncio.gather(stdout_task, stderr_task)

            process_exit: asyncssh.SSHClientProcess = await process.wait()
            if process_exit != 0:
                if process_exit.exit_status != 0:
                    print(
                        f"\nProcess exited with status {process_exit.exit_status}",
                        file=sys.stderr,
                    )
        except asyncssh.ProcessError as exc:
            print(f"\nProcess exited with status {exc.exit_status}", file=sys.stderr)
        except Exception as e:
            print(f"An error occurred: {e}", file=sys.stderr)
