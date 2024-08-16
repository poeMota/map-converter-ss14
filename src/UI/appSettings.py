from enum import Enum


class Selectors(Enum):
    Tile = "Tile"
    Entity = "Entity"


class Frames(Enum):
    Settings="Settings"
    Image="Image"


class GlobalSettings:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GlobalSettings, cls).__new__(cls)
            cls.instance._initialized = False
        return cls.instance


    def __init__(self):
        if not self._initialized:
            self.image = None
            self.outPath = None
            self.outFileName = None

            self.colorConfig = {} # color: selector

            self._initialized = True

