from .base import Component


class GravityComponent(Component):
    def __init__(self):
        Component.__init__(self)
        self.gravityShakeSound = {
            "!type": "SoundPathSpecifier",
            "path": "Audio/Effects/alert.ogg"
        }

