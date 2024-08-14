from src.GridSystem import *
from src import yaml
from pprint import pprint
from src.EntitySystem import EntitySystem
from src.ImageReader import *
from src.Tiles import TilesRefsManager
import os


if __name__ == '__main__':
    _tilesRefsManager = TilesRefsManager()
    _map = ConvertImageToMap(
            path=os.getcwd() + "/.debug/test.png",
            colormap={
                      '#00000000': ["tile", "Space"],
                      '#000000fe01': ["tile", "Plating"],
                      '#007f7ffe01': ["tile", "Plating"],
                      '#c6c6c6fe01': ["tile", "Plating"],
                      '#7f6a00fe01': ["tile", "Plating"],
                      '#404040fe01': ["tile", "Plating"],
                      '#808080fe01': ["tile", "Plating"],
                      '#7f6e6bfe01': ["tile", "Plating"],
                      '#5c9035fe01': ["tile", "Plating"],
                      '#ffdc6bfe01': ["tile", "Plating"],
                      '#2f7b8bfe01': ["tile", "Plating"],
                      '#93774bfe01': ["tile", "Plating"]
                    }
        )
    yaml.write(os.getcwd() + "/.debug/test.yml", _map._serialize())

