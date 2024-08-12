from src.GridSystem import *
from src import yaml
from pprint import pprint
from src.EntitySystem import EntitySystem
import os


if __name__ == '__main__':
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

    yaml.write(os.getcwd() + "/test.yml", _map._serialize())

