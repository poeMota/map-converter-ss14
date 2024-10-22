from .chunk import Chunk

from src.Components import *
from src.EntitySystem import Entity
from math import floor


class Grid(Entity):
    def __init__(self, Map, chunks: list[Chunk], name: str, x: float, y: float):
        Entity.__init__(self, proto="", pos=[x, y], parent="invalid", name=name)
        self.chunks = {chunk.strInd(): chunk for chunk in chunks}
        self.map = Map

        [self.AddComponent(comp) for comp in [
            MapGridComponent(self.chunks),
            BroadphaseComponent(),
            PhysicsComponent(),
            FixturesComponent({}),
            GravityComponent(),
            DecalGridComponent(),
            #GridAtmosphereComponent(),
            OccluderTreeComponent(),
            ShuttleComponent(),
            GridPathfindingComponent(),
            SpreaderGridComponent(),
            GravityShakeComponent(10),
            GasTileOverlayComponent(),
        ]]
        self.map.addGrid(self)


    def AddChunk(self, chunk: Chunk):
        self.chunks[chunk.strInd()] = chunk


    def SetTile(self, tile, _tilesRefsMan):
        if tile.name not in _tilesRefsMan.tileRefs:
            _tilesRefsMan.tileRefs[tile.name] = len(_tilesRefsMan.tileRefs)
        tile.id = _tilesRefsMan.tileRefs[tile.name]

        ind = [floor(tile.x / 16), floor(tile.y / 16)]
        ind_str = f"{ind[0]},{ind[1]}"
        if ind_str in self.chunks:
            self.chunks[ind_str].setTile(tile)
        else:
            self.AddChunk(Chunk(ind))
            self.chunks[ind_str].setTile(tile)

        if tile.name not in self.map.usedTiles:
            self.map.usedTiles.append(tile.name)

