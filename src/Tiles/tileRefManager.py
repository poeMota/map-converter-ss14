import os

import src.yaml as yaml
from src.ColorHelper import *


class TilesRefsManager:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TilesRefsManager, cls).__new__(cls)
            cls.tilesDataPath = os.path.dirname(__file__) + '/data/'
            cls.texturesPath = os.path.dirname(__file__) + '/../../'

            cls.prototypes = []
            cls.tileRefs = {} # TileName: tileID
            cls.colorRefs = {} # color: TileName

            cls.getPrototypes(cls)
            cls.getTileRefs(cls)
        return cls.instance


    def getPrototypes(self):
        for filename in os.listdir(self.tilesDataPath):
            if '.yml' in filename:
                data = yaml.read(self.tilesDataPath + filename)
                if type(data) is list:
                    [self.prototypes.append(i) for i in data]
                else:
                    self.prototypes.append(data)


    def getTileRefs(self):
        tileRefs = {"Space": 0} # Space tile should bo only 0 id

        for proto in self.prototypes:
            if (proto["type"] == "tile"
                and proto["id"] != "Space"):
                tileRefs[proto["id"]] = len(tileRefs.values())

        self.tileRefs = tileRefs


    def getColorRefs(self):
        for proto in self.prototypes:
            if "sprite" in proto:
                colors = GetImageColormap(self.texturesPath + proto["sprite"], None)
                self.colorRefs[rgbaToHex(AvargeColor(colors))] = proto["id"]