from .base import Component


class GridAtmosphereComponent(Component):
    def __init__(self, version: int = 2):
        Component.__init__(self)
        self.version = version
        self.data = {
                # tiles: {}, # TODO
                "uniqueMixes": [{
                    "volume": 2500,
                    "temperature": 293.15,
                    "moles": [
                        21.824879,
                        82.10312,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0
                    ]}],
                "chunkSize": 4
                }

