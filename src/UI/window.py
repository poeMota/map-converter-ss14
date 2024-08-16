import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
from enum import Enum

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

        self.colorConfig = None
        self.tiles = list(TilesRefsManager().tileRefs.keys())


    def setup_colormap(self):
        settingsFrame = SettingsFrame(self)
        self.colorConfig = {"#0000000": TileSelector("Space")}
        for color in settingsFrame.frames:
            self.colorConfig[color] = settingsFrame.frames[color].getOutput()


    def change_frame(self, value):
        # Delete current page
        [frame.pack_forget() for frame in self.frames.values() if frame.winfo_ismapped()]

        # Show selected frame
        self.frames[Frames(value)].pack(fill="both", expand=True)


    def autogen_config(self):
        _tilesRefsManager = TilesRefsManager()
        settingsFrame = SettingsFrame(self)
        for color in settingsFrame.frames:
            row: ConfigRow = settingsFrame.frames[color]
            tileColor = FindClosestColor(color, _tilesRefsManager.colorRefs.keys())
            row.setValues(Selectors.Tile, tile=_tilesRefsManager.colorRefs[tileColor])
        self.setup_colormap()


    def convert_image(self):
        imageFrame = ImageFrame(self)
        self.setup_colormap()

        if not imageFrame.image:
            print("ERROR: image not selected")
            return

        if not imageFrame.output_path:
            print("ERROR: output path not selected")
            return

        _map = ConvertImageToMap(imageFrame.image, self.colorConfig)
        yaml.write(imageFrame.output_path + imageFrame.fileName, _map._serialize())
        print("Image converted to path: " + imageFrame.output_path + imageFrame.fileName)

