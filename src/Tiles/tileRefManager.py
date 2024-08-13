import os
import src.yaml as yaml


class TilesRefsManager:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TilesRefsManager, cls).__new__(cls)
            cls.tilesDataPath = os.path.dirname(__file__) + '/data/'
            cls.tileRefs = {} # TileName: tileID
            cls.getTileRefs(cls)
        return cls.instance


    def getTileRefs(self):
        tileRefs = {"Space": 0} # Space tile should bo only 0 id
        prototypes = []
        for filename in os.listdir(self.tilesDataPath):
            if '.yml' in filename:
                data = yaml.read(self.tilesDataPath + filename)
                if type(data) is list:
                    [prototypes.append(i) for i in data]
                else:
                    prototypes.append(data)

        for proto in prototypes:
            if (proto["type"] == "tile"
                and proto["id"] != "Space"):
                tileRefs[proto["id"]] = len(tileRefs.values())

        self.tileRefs = tileRefs

