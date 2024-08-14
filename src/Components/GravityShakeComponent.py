from .base import Component


class GravityShakeComponent(Component):
    def __init__(self, shakeTimes: int):
        Component.__init__(self)
        self.shakeTimes = shakeTimes

