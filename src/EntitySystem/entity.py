from src.Components import *
from .EntityManager import EntitySystem


class Entity:
    def __init__(self, proto: str, pos: list, parent: int | str, name: str, description: str = ""):
        _entityMan = EntitySystem()
        self.uid = 0
        self.proto = proto
        self.parent = parent
        self.components: list[Component] = [
            TransformComponent(pos[0], pos[1], self.parent),
            MetaDataComponent(name, description)
        ]

        _entityMan.serialize_entity(self)


    def AddComponent(self, comp: Component) -> bool:
        for _comp in self.components:
            if type(_comp) is type(comp):
                return False

        self.components.append(comp)
        return True


    def _serialize(self) -> dict:
        return {
            "uid": self.uid,
            "components": [cmp for cmp in
                            [comp._serialize() for comp in self.components]
                          if cmp]
        }

