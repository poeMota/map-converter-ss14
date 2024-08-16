from src.GridSystem import *
from src import yaml
from pprint import pprint
from src.EntitySystem import EntitySystem
from src.ImageReader import *
from src.Tiles import TilesRefsManager
from src.UI import Window
import os


if __name__ == '__main__':
    _tilesRefsMan = TilesRefsManager()
    _tilesRefsMan.getColorRefs()

    app = Window()
    app.mainloop()

