from PIL import Image
from src.GridSystem import Map, Grid, Chunk, Tile


def GetImageColormap(path: str):
    img = Image.open(path).convert('RGB')
    pixels = img.load()
    width, height = img.size

    colormap = []
    for y in range(height):
        for x in range(width):
            color = rgbToHex(pixels[x, y])
            if color not in colormap:
                colormap.append(color)

    return colormap


def rgbToHex(rgb: list):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])


def ConvertImageToMap(path: str, colormap: dict):
    img = Image.open(path).convert('RGB')
    pixels = img.load()
    width, height = img.size

    chunkSize = 16
    chunksY = int(height / chunkSize)
    chunksX = int(width / chunkSize)

    centerChunkY = chunksY // 2
    centerChunkX = chunksX // 2
    centerX = centerChunkX * chunkSize + chunkSize // 2
    centerY = centerChunkY * chunkSize + chunkSize // 2

    _map = Map()
    _map.tilemap = {
            "Space": 0,
        }
    grid = Grid(_map, [], (centerX, centerY), "grid", 0, 0)

    for x in range(width):
        for y in range(height):
            ind = [int(x / chunkSize) - centerChunkX,
                   int(y / chunkSize) - centerChunkY]
            strInd = f"{ind[0]},{ind[1]}"
            if strInd not in grid.chunks:
                grid.AddChunk(Chunk(ind))
            color = rgbToHex(pixels[x, y])
            tile = Tile(x - centerX, y - centerY, colormap[color])
            grid.SetTile(tile)

    _map.addGrid(grid)
    return _map

