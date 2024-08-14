from src.GridSystem import *
from src import yaml
from pprint import pprint
from src.EntitySystem import EntitySystem
from src.ImageReader import *
from src.Tiles import TilesRefsManager
from src.UI import Window
import os


if __name__ == '__main__':
    app = Window()
    app.mainloop()
    #_tilesRefsManager = TilesRefsManager()
    #_map = ConvertImageToMap(
    #        path=os.getcwd() + "/.debug/test.png",
    #        colormap={
    #                  '#00000000': TileSelector("Space"),
    #                  '#000000fe01': EntitySelector(["WallReinforced"]),
    #                  '#007f7ffe01': EntitySelector(["Window", "Grille"]),
    #                  '#c6c6c6fe01': TileSelector("Plating"),
    #                  '#7f6a00fe01': TileSelector("Plating"),
    #                  '#404040fe01': TileSelector("Plating"),
    #                  '#808080fe01': TileSelector("Lattice"),
    #                  '#7f6e6bfe01': TileSelector("Plating"),
    #                  '#5c9035fe01': TileSelector("Plating"),
    #                  '#ffdc6bfe01': TileSelector("Plating"),
    #                  '#2f7b8bfe01': TileSelector("Plating"),
    #                  '#93774bfe01': TileSelector("Plating")
    #                }
    #    )
    #yaml.write(os.getcwd() + "/.debug/test.yml", _map._serialize())

