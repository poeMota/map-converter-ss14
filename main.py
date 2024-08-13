from src.GridSystem import *
from src import yaml
from pprint import pprint
from src.EntitySystem import EntitySystem
from src.ImageReader import *
import os


if __name__ == '__main__':
    '''
    _entityMan = EntitySystem()
    _map = Map()

    chunk1 = Chunk([0, 0])
    chunk2 = Chunk([0, 1])
    grid = Grid(_map, [chunk1, chunk2], "grid", 0, 0)
    tile = Tile(10, 10, "Test")
    tile2 = Tile(5, 22, "Test")
    grid.SetTile(tile)
    grid.SetTile(tile2)
    _map.addGrid(grid)
    '''
    _map = ConvertImageToMap(
            path=os.getcwd() + "/test.png",
            colormap={
                      '#000000': "Space",
                      '#007f7f': "Plating",
                      '#c6c6c6': "Plating",
                      '#7f6a00': "Plating",
                      '#404040': "Plating",
                      '#808080': "Plating",
                      '#7f6e6b': "Plating",
                      '#5c9035': "Plating",
                      '#ffdc6b': "Plating",
                      '#2f7b8b': "Plating",
                      '#93774b': "Plating"
                    }
        )
    print(_map.tilemap)
    yaml.write(os.getcwd() + "/test.yml", _map._serialize())


    print(GetImageColormap(os.getcwd() + "/test.png"))

