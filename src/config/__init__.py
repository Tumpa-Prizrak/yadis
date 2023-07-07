import json
from enum import Enum
from typing import Any, Union

from src.config import pyconfig


class Configs(Enum):
    """Enum representing the available config files."""

    bot_info = "src/config/bot_info.json"
    logger = "src/config/logger.json"


def load_config(file: Union[Configs, str]) -> dict:
    """Load a config file.

    Args:
        file (Configs | str): The config file to load. Either a Configs enum member or the file path.

    Returns:
        dict[str, Any]: The loaded config data.
    """
    return json.load(open(file if isinstance(file, str) else file.value, "r"))
