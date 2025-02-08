from typing import TypeVar

import yaml
from fastapi import HTTPException
from pydantic import BaseModel, FilePath

T = TypeVar("T", bound=BaseModel)


def read_yaml_file(path: FilePath, model_class: type[T]) -> T:
    try:
        with open(path) as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError:
        raise HTTPException(
            status_code=500,
            detail="Could not read configuration file",
        )
    except OSError:
        raise HTTPException(
            status_code=500,
            detail=f"Could not open file {path}",
        )

    try:
        return model_class(**data)
    except ValueError as exc:
        raise HTTPException(
            status_code=422,
            detail=f"Invalid configuration data: {exc}",
        )


async def read_stream(stream):
    """Read lines from a stream and write them to the output in real-time."""
    while True:
        line = await stream.readline()
        if not line:
            break
        yield line.encode()
