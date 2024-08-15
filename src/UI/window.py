import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
from enum import Enum

import src.yaml as yaml
from src.ImageReader import *
from src.Tiles import TilesRefsManager
from src.ColorHelper import *


class Frames(Enum):
    Settings="Settings"
    Image="Image"


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

        self.colorConfig = {"#0000000": TileSelector("Space")}
        self.tiles = list(TilesRefsManager().tileRefs.keys())


    def setup_colormap(self):
        settingsFrame = SettingsFrame(self)
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


class ImageFrame(ctk.CTkFrame):
    def __new__(cls, master):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ImageFrame, cls).__new__(cls)
            cls.instance._initialized = False
        return cls.instance


    def __init__(self, master):
        if not self._initialized:
            super().__init__(master)
            self.left_frame = ctk.CTkFrame(self)
            self.left_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

            self.right_frame = ctk.CTkFrame(self)
            self.right_frame.pack(side="right", fill="y", padx=20, pady=20)

            # Image frame
            self.image_label = ctk.CTkLabel(self.left_frame, text="Select the image you want to convert", height=600, fg_color="gray", corner_radius=10)
            self.image_label.pack(fill="x")

            # Choose image button
            self.select_image_button = ctk.CTkButton(self.right_frame, text="Choose image", command=self.select_image)
            self.select_image_button.pack(pady=10)

            # Choose out path button
            self.output_path_button = ctk.CTkButton(self.right_frame, text="Choose output path", command=self.select_output_path)
            self.output_path_button.pack(pady=0)

            # Convert button
            self.convert_button = ctk.CTkButton(self.right_frame, text="Convert to map", command=master.convert_image)
            self.convert_button.pack(pady=10, padx=5, side="bottom")

            self.image = None
            self.fileName = ""
            self.output_path = ""

            self._initialized = True


    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
        if file_path:
            image = Image.open(file_path)
            self.image = image.convert("RGBA")

            width, height = image.size
            resize = min(self.image_label.winfo_height() / width, self.image_label.winfo_height() / height)
            
            ctk_image = ctk.CTkImage(image, size=(width * resize, height * resize))
            self.image_label.configure(image=ctk_image, text="")
            self.image_label.image = ctk_image

            # Update settings frame
            _settingsFrame = SettingsFrame(self.master)
            _settingsFrame.set_options(GetImageColormap(file_path))

            self.fileName = '/' + file_path.split('/')[-1].split('.')[0] + ".yml"


    def select_output_path(self):
        path = filedialog.askdirectory()
        if path: self.output_path = path


class Selectors(Enum):
    Tile = "Tile"
    Entity = "Entity"


class SettingsFrame(ctk.CTkFrame):
    def __new__(cls, master):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SettingsFrame, cls).__new__(cls)
            cls.instance._initialized = False
        return cls.instance


    def __init__(self, master):
        if not self._initialized:
            super().__init__(master)
            self.frames: dict = {}

            self.upper_frame = ctk.CTkFrame(self)
            self.upper_frame.pack(fill="x", padx=20, pady=5)

            self.scrollable_frame = ctk.CTkScrollableFrame(self)
            self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=15)


            # Autogenerate config button
            self.autogen_button = ctk.CTkButton(self.upper_frame, text="Autogenerate", command=master.autogen_config)
            self.autogen_button.pack(side="right")

            # Labels
            self.tileTitle = ctk.CTkLabel(
                self.upper_frame, 
                text="Title name", 
                fg_color="#4a4a4a",
                width=200)
            self.tileTitle.pack(side="left", padx=(185, 0))

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


class ConfigRow(ctk.CTkFrame):
    def __init__(self, master, color):
        super().__init__(master)
        self.color = color
        baseTile = "Plating"

        # Selectors option menu
        self.optionMenu = ctk.CTkOptionMenu(self, 
                                        values=[Selectors.Tile.value, Selectors.Entity.value], 
                                        command=lambda value: self.change_selector(value))
        self.optionMenu.pack(side="left", padx=10, pady=10)
        self.optionMenu.set(Selectors.Tile.value)

        # Entity protoName selector
        self.entityEntry = ctk.CTkEntry(self, width=200)

        # TileName selector
        self.tileEntry = ctk.CTkEntry(self, width=200)
        self.tileEntry.pack(side="left", padx=10, pady=10)
        self.tileEntry.insert(0, baseTile)

        # Color square
        self.colorLabel = ctk.CTkLabel(self, width=30, height=30, text="", fg_color=HEX8ToHEX6(self.color))
        self.colorLabel.pack(side="right", pady=10, padx=10)


    def change_selector(self, value: str):
        if value == Selectors.Entity.value:
            self.entityEntry.pack(side="left", padx=10, pady=10)
        elif value == Selectors.Tile.value:
            self.entityEntry.pack_forget()


    def setValues(self, option: Selectors = None, tile: str = None, proto: str = None, color = None):
        if option:
            self.optionMenu.set(option.value)
        if tile:
            self.tileEntry.delete(0, ctk.END)
            self.tileEntry.insert(0, tile)
        if proto:
            self.entityEntry.delete(0, ctk.END)
            self.entityEntry.insert(0, proto)
        if color:
            self.colorLabel.configure(fg_color=color)
    

    def getOutput(self):
        if self.optionMenu.get() == Selectors.Entity.value:
            if not self.entityEntry.get():
                return

            protos = self.entityEntry.get().strip().split(' ')
            tile = self.tileEntry.get().strip()

            return EntitySelector(protos, tileName=tile)
        elif self.optionMenu.get() == Selectors.Tile.value:
            if not self.tileEntry.get():
                return

            tile = self.tileEntry.get().strip()
            return TileSelector(tile)
