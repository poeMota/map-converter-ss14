from src.GridSystem import *
from src import yaml
from pprint import pprint
import os


if __name__ == '__main__':
    chunk1 = Chunk([0, 0])
    chunk2 = Chunk([0, 1])
    grid = Grid(1, [chunk1, chunk2], "grid", 10, 1.3242)
    grid.tilemap = {"Space": 0}

    yaml.write(os.getcwd() + "/test.yml", grid._serialize())

