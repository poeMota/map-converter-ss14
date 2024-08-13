class Tile:
    def __init__(self, x: float, y: float, tile: str, tileId: int = 0):
        self.id = tileId

        self.x = x
        self.y = y
        self.name = tile
        self.metadata = 0
        self.variation = 0

