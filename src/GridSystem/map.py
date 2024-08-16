from .grid import Grid
from src.EntitySystem import EntitySystem
from src.Tiles import TilesRefsManager


class Map:
    def __init__(self, formatId: int = 6, postmapinit: bool = False):
        self.grids = {} # uid: grid
        self.format = formatId
        self.postmapinit = postmapinit

        self.usedTiles = ["Space"]


    def addGrid(self, grid: Grid) -> bool:
        if grid.uid not in self.grids:
            self.grids[grid.uid] = grid
            return True
        return False


    def _serialize(self):
        _entityMan = EntitySystem()
        _tilesRefsManager = TilesRefsManager()
        return {
            "meta": {
                "format": self.format,
                "postmapinit": self.postmapinit
            },
            "tilemap": { # id: tileName
                _tilesRefsManager.tileRefs[tile]: tile for tile in self.usedTiles
            },
            "entities": _entityMan._serialize()
        }

