from src.GridSystem import Chunk, Tile
from .base import Component


class MapGridComponent(Component):
    def __init__(self, grid):
        Component.__init__(self)
        self.grid = grid
        self.chunks: list[Chunk] = grid.chunks


    def _serialize(self) -> dict:
        return {
            "type": type(self).__name__,
            "chunks": {
                ",".join([str(i) for i in chunk.ind]): chunk._serialize(self.grid.tilemap)
            for chunk in self.chunks}
        }

