from .base import Component


class PhysicsComponent(Component):
    def __init__(self):
        Component.__init__(self)
        self.bodyStatus = "InAir"
        self.angularDamping = 0.05
        self.linearDamping = 0.05
        self.fixedRotation = False
        self.bodyType = "Dynamic"

