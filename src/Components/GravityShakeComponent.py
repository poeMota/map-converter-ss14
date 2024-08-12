from .base import Component


class GravityShakeComponent(Component):
    def __init__(self, shakeTimes: int = 10):
        Component.__init__(self)
        self.shakeTimes = shakeTimes

