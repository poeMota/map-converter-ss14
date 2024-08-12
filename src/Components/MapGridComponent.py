from src.GridSystem import Chunk, Tile
from .base import Component


class MapGridComponent(Component):
    def __init__(self, chunks: list[Chunk]):
        Component.__init__(self)
        self.chunks: list[Chunk] = chunks


    def _serialize(self, tilemap: dict) -> dict:
        return {
            "type": "MapGrid",
            "chunks": {
                ",".join([str(i) for i in chunk.ind]): chunk._serialize(tilemap)
            for chunk in self.chunks}
        }

