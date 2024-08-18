import os
from pathlib import Path
import platform


def getConfigPath(folderName="map-converter-ss14") -> Path:
    system = platform.system()

    if system == "Windows":
        configDir = os.getenv('APPDATA')
    elif system in ["Linux", "Darwin"]:  # "Darwin" for macOS
        configDir = Path.home() / ".config"
    else:
        raise NotImplementedError(f"Unsupported operating system: {system}")

    configPath = Path(configDir) / folderName
    configPath.mkdir(parents=True, exist_ok=True)

    return configPath

