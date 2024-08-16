import customtkinter as ctk
from PIL import Image

import src.yaml as yaml
from src.ImageReader import *
from src.Tiles import TilesRefsManager
from src.ColorHelper import *

from .settingsFrame import SettingsFrame
from .imageFrame import ImageFrame
from .appSettings import *



class Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("SS14 Map Converter -- Image to YAML")
        self.geometry("800x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Pages frames
        self.frames = {
            Frames.Image: ImageFrame(self),
            Frames.Settings: SettingsFrame(self)
        }

        # Segment button for switching pages
        self.segmented_button = ctk.CTkSegmentedButton(self, values=[frame.value for frame in self.frames], command=self.change_frame)
        self.segmented_button.pack(fill="x")

        # Show firt frame
        self.frames[Frames.Image].pack(fill="both", expand=True)

        self.tiles = list(TilesRefsManager().tileRefs.keys())


    def setup_colormap(self):
        settingsFrame = SettingsFrame(self)

        settings = GlobalSettings()
        settings.colorConfig = {"#0000000": TileSelector("Space")}
        for color in settingsFrame.frames:
            settings.colorConfig[color] = settingsFrame.frames[color].getOutput()


    def change_frame(self, value):
        # Delete current page
        [frame.pack_forget() for frame in self.frames.values() if frame.winfo_ismapped()]

        # Show selected frame
        self.frames[Frames(value)].pack(fill="both", expand=True)


    def autogen_config(self):
        _tilesRefsManager = TilesRefsManager()
        settingsFrame = SettingsFrame(self)
        for color in settingsFrame.frames:
            row = settingsFrame.frames[color]
            tileColor = FindClosestColor(color, _tilesRefsManager.colorRefs.keys())
            row.setValues(Selectors.Tile, tile=_tilesRefsManager.colorRefs[tileColor])
        self.setup_colormap()


    def convert_image(self):
        imageFrame = ImageFrame(self)
        settings = GlobalSettings()
        settings.outFileName = imageFrame.filename_entry.get().removesuffix('.yml') + '.yml'
        self.setup_colormap()

        if not settings.image:
            print("ERROR: image not selected")
            return

        if not settings.outPath:
            print("ERROR: output path not selected")
            return

        if not settings.outFileName.strip():
            print("ERROR: output filename not selected")
            return

        _map = ConvertImageToMap(settings.image, settings.colorConfig)
        yaml.write(settings.outPath + settings.outFileName, _map._serialize())
        print("Image converted to path: " + settings.outPath + settings.outFileName)

