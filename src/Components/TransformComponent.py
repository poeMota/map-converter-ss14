from .base import Component


class TransformComponent(Component):
    def __init__(self, x: float, y: float, parent: int | str):
        Component.__init__(self)
        self.pos = [x, y]
        self.parent = parent

