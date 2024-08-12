from .chunk import Chunk
from .tile import Tile

from src.Components import *
from src.EntitySystem import Entity


class Grid(Entity):
    def __init__(self, Map, chunks: list[Chunk], name: str, x: float, y: float):
        Entity.__init__(self)
        self.chunks = {f"{chunk.ind[0]},{chunk.ind[1]}": chunk for chunk in chunks}
        self.map = Map

        self.components: list[Component] = [
            MetaDataComponent(name),
            TransformComponent(x, y, "invalid"),
            MapGridComponent(self.chunks, self.map.tilemap),
            BroadphaseComponent(),
            PhysicsComponent(),
            FixturesComponent(),
            GravityComponent(),
            DecalGridComponent(),
            GridAtmosphereComponent(),
            OccluderTreeComponent(),
            ShuttleComponent(),
            GridPathfindingComponent(),
            SpreaderGridComponent(),
            GravityShakeComponent(),
            GasTileOverlayComponent(),
        ]
        self.map.addGrid(self)


    def SetTile(self, tile: Tile):
        ind = [int(tile.x / 16), int(tile.y / 16)]
        ind_str = f"{ind[0]},{ind[1]}"
        if ind_str in self.chunks:
            self.chunks[ind_str].setTile(tile)
        else:
            self.chunks[ind_str] = Chunk(ind)
            self.chunks[ind_str].setTile(tile)

