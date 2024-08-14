class EntitySelector:
    def __init__(self, protos: list[str], name: str = "", description: str = "", tileName: str = "Plating"):
        self.protos = protos
        self.name = name
        self.description = description
        self.tileName = tileName # Tile name under the entity


class TileSelector:
    def __init__(self, tileName):
        self.tileName = tileName

