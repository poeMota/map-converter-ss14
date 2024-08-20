from os import listdir, path
from PIL import Image
from pathlib import Path

import src.yaml as yaml
from src.ColorHelper import *


class TilesRefsManager:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TilesRefsManager, cls).__new__(cls)
            cls.instance._initialized = False
        return cls.instance


    def __init__(self):
        if not self._initialized:
            self.tilesDataPath = path.dirname(__file__) + '/../../Tiles/'
            self.texturesPath = path.dirname(__file__) + '/../../'

            self.prototypes = []
            self.tileRefs = {} # TileName: tileID
            self.colorRefs = {} # color: TileName

            self.getPrototypes(self.tilesDataPath)
            self.getTileRefs()

            self._initialized = True


    def getPrototypes(self, dirPath):
        for filename in listdir(dirPath):
            if '.yml' in filename:
                data = yaml.read(dirPath + filename)
                if type(data) is list:
                    [self.prototypes.append(i) for i in data]
                else:
                    self.prototypes.append(data)
            elif path.isdir(dirPath + filename):
                self.getPrototypes(f"{dirPath}{filename}/")


    def getTileRefs(self):
        tileRefs = {"Space": 0} # Space tile should be only 0 id

        for proto in self.prototypes:
            if (proto["type"] == "tile"
                and proto["id"] != "Space"):
                tileRefs[proto["id"]] = len(tileRefs.values())

        self.tileRefs = tileRefs


    def getColorRefs(self):
        for proto in self.prototypes:
            if "sprite" in proto:
                if Path(self.texturesPath + proto["sprite"]).is_file():
                    image = Image.open(self.texturesPath + proto["sprite"]).convert("RGBA")
                    colors = GetImageColormap(image, None)
                    self.colorRefs[rgbaToHex(AvargeColor(colors))] = proto["id"]
                else:
                    print(f"WARNING: No sprite found for the tile {proto['id']} on the path: {proto['sprite']}")

