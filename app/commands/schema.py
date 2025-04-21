from enum import Enum

from pydantic import BaseModel, IPvAnyAddress

from app.devices.schema import IPWithPortModel, Platform


# IMPORTANT: If you add or remove commands in `Command`, update `CommandSet` fields to match.
class Command(Enum):
    ping = "ping"
    traceroute = "traceroute"
    bgp = "bgp_route"
    config = "config"


class CommandSet(BaseModel):
    ping: str
    traceroute: str
    bgp_route: str
    config: str | None = None

    def get_command(self, command: Command) -> str | None:
        """
        Retrieve the command string corresponding to a given Command enum.
        Assumes the field names in the model are the same as the enum values.
        """
        return getattr(self, command.value, None)


class RunCommand(BaseModel):
    from_device: IPWithPortModel
    target: IPvAnyAddress | None = None
    command: Command


class CommandsFile(BaseModel):
    commands: dict[Platform, CommandSet]
