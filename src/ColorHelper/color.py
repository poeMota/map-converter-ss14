import math
from PIL import Image


def rgbToHex(rgb: list):
    return '#{:01x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])


def rgbaToHex(rgba):
    r, g, b, a = rgba
    return "#{:01x}{:02x}{:02x}{:02x}".format(r, g, b, int(a * 255))


def hexToRgba(hex_color):
    hex_color = hex_color.lstrip('#')

    if len(hex_color) == 6:  # RRGGBB
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        a = 255
    else:  # #RRGGBBAA
        r, g, b, a = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16), int(hex_color[6:8], 16)

    return (r, g, b, a)


def HEX8ToHEX6(hex8: str):
    if hex8.startswith("#"): return hex8[:7]
    return hex8[:6]


def euclideanDistance(color1, color2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(color1, color2)))


def FindClosestColor(target_color: str, color_list: list[str]):
    closest_color = None
    min_distance = float('inf')

    for color in color_list:
        distance = euclideanDistance(hexToRgba(target_color), hexToRgba(color))
        if distance < min_distance:
            min_distance = distance
            closest_color = color

    return closest_color


def AvargeColor(colors: list[list]) -> str:
    rgba = [0, 0, 0, 0]

    for i in range(len(rgba)):
        rgba[i] = sum([color[i] for color in colors]) // len(colors)
    return rgba


def GetImageColormap(path: Image, convert = rgbaToHex):
    pixels = img.load()
    width, height = img.size

    colormap = []
    for y in range(height):
        for x in range(width):
            if convert:
                color = convert(pixels[x, y])
            else:
                color = pixels[x, y]

            if color not in colormap:
                colormap.append(color)

    return colormap

