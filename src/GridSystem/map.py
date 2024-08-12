from .grid import Grid
from src.EntitySystem import EntitySystem


class Map:
    def __init__(self, tilemap, formatId: int = 6, postmapinit: bool = False):
        self.grids = {} # uid: grid
        self.format = formatId
        self.postmapinit = postmapinit

        self.tilemap = tilemap # tileName: id


    def addGrid(self, grid: Grid) -> bool:
        if grid.uid not in self.grids:
            self.grids[grid.uid] = grid
            return True
        return False


    def _serialize(self):
        _entityMan = EntitySystem()
        return {
            "meta": {
                "formap": self.format,
                "postmapinit": self.postmapinit
            },
            "tilemap": {self.tilemap[tile]: tile for tile in self.tilemap}, # id: tileName
            "enities": _entityMan._serialize()
        }

