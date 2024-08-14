class EntitySelector:
    def __init__(self, proto: str, name: str = "", description: str = "", tileName: str = "Plating"):
        self.proto = proto
        self.name = name
        self.description = description
        self.tileName = tileName # Tile name under the entity


class TileSelector:
    def __init__(self, tileName):
        self.tileName = tileName

