from src.Components import Component
from .EntityManager import EntitySystem


class Entity:
    def __init__(self, proto: str = ""):
        _entityMan = EntitySystem()
        self.uid = 0
        self.proto = "\"\""
        self.components: list[Component] = []

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
            "components": [comp._serialize() for comp in self.components]
        }

