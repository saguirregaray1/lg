from pydantic import BaseModel, IPvAnyAddress
from .devices import Platform, IPv4WithPortModel
from typing import Dict
from enum import Enum


class Command(Enum):
    ping = "ping"
    traceroute = "traceroute"
    bgp = "bgp_route"


class RunPing(BaseModel):
    from_device: IPv4WithPortModel
    target: IPvAnyAddress


class CommandSet(BaseModel):
    ping: str
    traceroute: str
    bgp_route: str

    def get_command(self, command: Command) -> str:
        field_name = command.value
        return getattr(self, field_name)


class CommandsFile(BaseModel):
    commands: Dict[Platform, CommandSet]
