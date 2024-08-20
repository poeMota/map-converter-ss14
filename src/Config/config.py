from os import path
from pathlib import Path


def getConfigPath() -> str:
    configPath = Path(path.dirname(__file__) + '/../../.config/')
    configPath.mkdir(parents=True, exist_ok=True)

    return configPath

