from enum import Enum

from pydantic import BaseModel, IPvAnyAddress, create_model

from app.devices.schema import IPv4WithPortModel, Platform


class Command(Enum):
    ping = "ping"
    traceroute = "traceroute"
    bgp = "bgp_route"
    config = "config"


class RunCommand(BaseModel):
    from_device: IPv4WithPortModel
    target: IPvAnyAddress | None = None
    command: Command


class CommandSetBase(BaseModel):
    def get_command(self, command: Command) -> str:
        """
        Retrieve the command string corresponding to a given Command enum.
        Assumes the field names in the model are the same as the enum values.
        """
        return getattr(self, command.value)


CommandSet = create_model(
    "CommandSet",
    __base__=CommandSetBase,
    **{cmd.value: (str | None, None) for cmd in Command},
)


class CommandsFile(BaseModel):
    commands: dict[Platform, CommandSet]
