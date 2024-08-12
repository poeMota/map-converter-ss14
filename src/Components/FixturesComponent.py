from .base import Component


class FixturesComponent(Component):
    def __init__(self, fixtures: dict = {}):
        Component.__init__(self)
        self.fixtures = fixtures

