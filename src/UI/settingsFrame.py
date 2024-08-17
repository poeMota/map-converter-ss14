import customtkinter as ctk
from .appSettings import *
from .configRow import ConfigRow
from src.ColorHelper import *
from src.ImageReader.selectors import *


class SettingsFrame(ctk.CTkFrame):
    def __new__(cls, master):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SettingsFrame, cls).__new__(cls)
            cls.instance._initialized = False
        return cls.instance


    def __init__(self, master):
        if not self._initialized:
            super().__init__(master)
            self.frames: dict = {} # color: row frame

            self.upper_frame = ctk.CTkFrame(self)
            self.upper_frame.pack(fill="x", padx=20, pady=5)

            self.scrollable_frame = ctk.CTkScrollableFrame(self)
            self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=15)


            # Autogenerate config button
            self.autogen_button = ctk.CTkButton(self.upper_frame, text="Autogenerate", command=master.autogen_config)
            self.autogen_button.pack(side="right")

            # Labels
            self.typeLabel = ctk.CTkLabel(
                self.upper_frame,
                text="Type",
                fg_color="#4a4a4a",
                width=140)
            self.typeLabel.pack(side="left", padx=(25, 0))

            self.tileTitle = ctk.CTkLabel(
                self.upper_frame,
                text="Title name",
                fg_color="#4a4a4a",
                width=200)
            self.tileTitle.pack(side="left", padx=(20, 0))

            self.entityTitle = ctk.CTkLabel(
                self.upper_frame,
                text="Entity proto",
                fg_color="#4a4a4a",
                width=200)
            self.entityTitle.pack(side="left", padx=(21, 0)) # Pixelhunting

            self._initialized = True


    def set_options(self, colormap: list[str]):
        [frame.pack_forget() for frame in self.frames.values()]
        for color in colormap:
            if color[7:] != '0':
                row_frame = ConfigRow(self.scrollable_frame, HEX8ToHEX6(color))
                row_frame.pack(fill="x", pady=5, padx=10)

                self.frames[color] = row_frame
        print(f"Settings frame has been set up for {len(colormap)} colors")


    def setup_colormap(self):
        settings = GlobalSettings()
        settings.colorConfig = {"#0000000": TileSelector("Space")} # For PNG's
        for color in self.frames:
            settings.colorConfig[color] = self.frames[color].getOutput()

