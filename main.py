from src.GridSystem import *
from pprint import pprint


if __name__ == '__main__':
    chunk1 = Chunk([0, 0])
    chunk2 = Chunk([0, 1])
    grid = MapGrid([chunk1, chunk2])

    pprint(grid._serialize({"Space": 0}))

