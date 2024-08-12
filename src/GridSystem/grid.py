from .chunk import Chunk
from .tile import Tile


class MapGrid:
    def __init__(self, chunks: list[Chunk]):
        self.chunks: list[Chunk] = chunks


    def _serialize(self, tilemap: dict) -> dict:
        return {
            "type": "MapGrid",
            "chunks": {
                ",".join([str(i) for i in chunk.ind]): chunk._serialize(tilemap)
            for chunk in self.chunks}
        }

