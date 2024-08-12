from .base import Component


class MetaDataComponent(Component):
    def __init__(self, name: str):
        Component.__init__(self)
        self.name = name

