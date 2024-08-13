from src.GridSystem import *
from src import yaml
from pprint import pprint
from src.EntitySystem import EntitySystem
from src.ImageReader import *
import os


if __name__ == '__main__':
    print(GetImageColormap(os.getcwd() + "/.debug/test.png"))
    _map = ConvertImageToMap(
            path=os.getcwd() + "/.debug/test.png",
            colormap={
                      '#00000000': "Space",
                      '#000000fe01': "Plating",
                      '#007f7ffe01': "Plating",
                      '#c6c6c6fe01': "Plating",
                      '#7f6a00fe01': "Plating",
                      '#404040fe01': "Plating",
                      '#808080fe01': "Plating",
                      '#7f6e6bfe01': "Plating",
                      '#5c9035fe01': "Plating",
                      '#ffdc6bfe01': "Plating",
                      '#2f7b8bfe01': "Plating",
                      '#93774bfe01': "Plating"
                    }
        )
    print(_map.tilemap)
    yaml.write(os.getcwd() + "/.debug/test.yml", _map._serialize())

