from src.GridSystem import Chunk, Tile
from .base import Component


class MapGridComponent(Component):
    def __init__(self, chunks, tilemap):
        Component.__init__(self)
        self.chunks: dict[Chunk] = chunks
        self.tilemap = tilemap


    def _serialize(self) -> dict:
        return {
            "type": type(self).__name__.replace("Component", ""),
            "chunks": {
                ind: self.chunks[ind]._serialize(self.tilemap)
                for ind in self.chunks if self.chunks[ind]._filled_tiles > 0
            }
        }

