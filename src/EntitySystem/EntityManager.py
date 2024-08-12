class EntitySystem:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(EntitySystem, cls).__new__(cls)
            cls.lastEntityUid = 1 # 0 For errors
            cls.entities = {}
        return cls.instance

    '''
    :argument entity: the entity that needs to be serialized
    :return no return
    '''
    def serialize_entity(self, entity) -> None:
        if entity not in self.entities.values():
            self.entities[self.lastEntityUid] = entity
            entity.uid = self.lastEntityUid

            self.lastEntityUid += 1
        else:
            raise Exception("Entity already registered")

    '''
    :argument entity: the entity that needs to be removed from entity system
    :return true if the entity has been removed
    '''
    def clear_entity(self, entity):
        if entity.uid in self.entities:
            del self.entities[entity.uid]
            return True
        return False

    '''
    :argument uid: the UID of the entity by which to get the entity object
    :return entity by id, false otherwise
    '''
    def get_entity(self, uid: int):
        if uid in self.entities:
            return self.entities[uid]
        return False


    def _serialize(self):
        protos = {}
        for entity in self.entities.values():
            if entity.proto not in protos:
                protos[entity.proto] = [entity._serialize()]
            else:
                protos[entity.proto].append(entity._serialize())

        return [{"proto": proto,
                  "entities": [ent for ent in protos[proto]]
                }for proto in protos]

