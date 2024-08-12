from .chunk import Chunk
from .tile import Tile
from src.Components import *


class Grid:
    def __init__(self, uid: int, chunks: list[Chunk]):
        self.uid = uid
        self.chunks: list[Chunk] = chunks

        self.components: list[Component] = [
            MapGridComponent(self.chunks)
        ]


    def _serialize(self, tilemap: dict) -> dict:
        return {
            "uid": self.uid,
            "components": [comp._serialize(tilemap) for comp in self.components]
        }

