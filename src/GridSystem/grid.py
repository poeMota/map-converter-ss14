from .chunk import Chunk
from .tile import Tile

from src.Components import *
from src.EntitySystem import Entity


class Grid(Entity):
    def __init__(self, Map, chunks: list[Chunk], center: list, name: str, x: float, y: float):
        Entity.__init__(self)
        self.chunks = {chunk.strInd(): chunk for chunk in chunks}
        self.map = Map
        self.center = center

        self.components: list[Component] = [
            MetaDataComponent(name),
            TransformComponent(x, y, "invalid"),
            MapGridComponent(self.chunks),
            BroadphaseComponent(),
            PhysicsComponent(),
            FixturesComponent(),
            GravityComponent(),
            DecalGridComponent(),
            #GridAtmosphereComponent(),
            OccluderTreeComponent(),
            ShuttleComponent(),
            GridPathfindingComponent(),
            SpreaderGridComponent(),
            GravityShakeComponent(),
            GasTileOverlayComponent(),
        ]
        self.map.addGrid(self)


    def AddChunk(self, chunk: Chunk):
        self.chunks[chunk.strInd()] = chunk


    def SetTile(self, tile: Tile):
        if tile.name not in self.map.tilemap:
            tile.id = len(self.map.tilemap.values())
            self.map.tilemap[tile.name] = len(self.map.tilemap.values())
        else:
            tile.id = self.map.tilemap[tile.name]

        ind = [int((tile.x - self.center[0]) / 16), int((tile.y - self.center[1]) / 16)]
        ind_str = f"{ind[0]},{ind[1]}"
        if ind_str in self.chunks:
            self.chunks[ind_str].setTile(tile)
        else:
            self.AddChunk(Chunk(ind))
            self.chunks[ind_str].setTile(tile)

