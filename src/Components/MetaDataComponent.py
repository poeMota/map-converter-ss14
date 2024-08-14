from .base import Component


class MetaDataComponent(Component):
    def __init__(self, name: str = "", description: str = ""):
        Component.__init__(self, dontShowOnDefault = True)
        self.name = name
        self.description = description

