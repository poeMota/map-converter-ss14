from .chunk import Chunk
from .tile import Tile
from src.Components import *


class Grid:
    def __init__(self, uid: int, chunks: list[Chunk], name: str, x: float, y: float):
        self.uid = uid
        self.chunks: list[Chunk] = chunks
        self.tilemap = {}

        self.components: list[Component] = [
            MetaDataComponent(name),
            TransformComponent(x, y, "invalid"),
            MapGridComponent(self),
            BroadphaseComponent(),
            PhysicsComponent(),
            FixturesComponent(),
            GravityComponent(),
            OccluderTreeComponent(),
            ShuttleComponent(),
            GridPathfindingComponent(),
            SpreaderGridComponent(),
            GravityShakeComponent(),
            GasTileOverlayComponent(),
        ]


    def _serialize(self) -> dict:
        return {
            "uid": self.uid,
            "components": [comp._serialize() for comp in self.components]
        }


    def AddComponent(self, comp: Component) -> bool:
        for _comp in self.components:
            if type(_comp) is type(comp):
                return False

        self.components.append(comp)
        return True

