from PIL import Image
from src.GridSystem import Map, Grid, Chunk, Tile
from src.Tiles import TilesRefsManager
from math import floor


def GetImageColormap(path: str):
    img = Image.open(path).convert('RGBA')
    pixels = img.load()
    width, height = img.size

    colormap = []
    for y in range(height):
        for x in range(width):
            color = rgbaToHex(pixels[x, y])
            if color not in colormap:
                colormap.append(color)

    return colormap


def rgbToHex(rgb: list):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])


def rgbaToHex(rgba):
    r, g, b, a = rgba
    return "#{:02x}{:02x}{:02x}{:02x}".format(r, g, b, int(a * 255))


def ConvertImageToMap(path: str, colormap: dict):
    _tilesRefsMan = TilesRefsManager()

    img = Image.open(path).convert('RGBA')
    pixels = img.load()
    width, height = img.size

    chunkSize = 16
    chunksY = floor(height / chunkSize)
    chunksX = floor(width / chunkSize)

    _map = Map()
    grid = Grid(_map, [], "grid", 0, 0)

    for x in range(width):
        for y in range(height):
            inv_y = height - y - 1
            ind = [floor(x / chunkSize),
                   floor(inv_y / chunkSize)]
            strInd = f"{ind[0]},{ind[1]}"
            if strInd not in grid.chunks:
                grid.AddChunk(Chunk(ind))
            color = rgbaToHex(pixels[x, y])
            tile = Tile(x, inv_y, colormap[color])
            grid.SetTile(tile, _tilesRefsMan)

    _map.addGrid(grid)
    return _map
