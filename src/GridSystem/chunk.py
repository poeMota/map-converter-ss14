from .tile import Tile
import base64


class Chunk:
    def __init__(self, ind: list[int], version: int = 6):
        self.chunksize: int = 16

        self.ind = ind # [x, y]
        self.tiles = [[None for _ in range(self.chunksize)] for _ in range(self.chunksize)]
        self.version = version
        self._filled_tiles = 0

        for y in range(self.chunksize):
            for x in range(self.chunksize):
                self.tiles[y][x] = Tile(
                        x= self.ind[0] * self.chunksize + x,
                        y= self.ind[1] * self.chunksize + y,
                        tile= "Space",
                        tileId= 0
                    )


    def _serialize(self) -> dict:
        return {
                "ind": ",".join([str(i) for i in self.ind]),
                "tiles": self._serialize_tiles(),
                "version": self.version
                }


    def _serialize_tiles(self):
        barr = bytes()
        for y in range(self.chunksize):
            for x in range(self.chunksize):
                tile = self.tiles[y][x]
                barr += tile.id.to_bytes(2)
                barr += tile.metadata.to_bytes(2)
                barr += tile.variation.to_bytes(2)
        return base64.b64encode(barr).decode('utf-8')


    def setTile(self, tile: Tile):
        y, x = tile.y % self.chunksize, tile.x % self.chunksize
        if tile.id != 0 and self.tiles[y][x].id == 0:
            self._filled_tiles += 1
        elif tile.id == 0 and self.tiles[y][x].id != 0:
            self._filled_tiles -= 1

        self.tiles[y][x] = tile


    def strInd(self):
        return f"{self.ind[0]},{self.ind[1]}"

