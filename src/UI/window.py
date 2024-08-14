import customtkinter as ctk
from tkinter import filedialog, colorchooser
from PIL import Image
from enum import Enum

from src.ImageReader import *
from src.Tiles import TilesRefsManager


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

        self.colorConfig = {"#00000000": TileSelector("Space")}
        self.colormap = {}
        self.fullColors = {} # #RRGGBB: #RRGGBBAA            
        self.tiles = list(TilesRefsManager().tileRefs.keys())


    def setup_colormap(self, color: str, selector):
        self.colormap[self.fullColors[color]] = selector


    def change_frame(self, value):
        # Delete current page
        [frame.pack_forget() for frame in self.frames.values() if frame.winfo_ismapped()]

        # Show selected frame
        self.frames[Frames(value)].pack(fill="both", expand=True)


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
            self.image_label.pack(pady=0, fill="x")

            # Choose image button
            self.select_image_button = ctk.CTkButton(self.right_frame, text="Choose image", command=self.select_image)
            self.select_image_button.pack(pady=0)

            # Choose out path button
            self.output_path_button = ctk.CTkButton(self.right_frame, text="Choose output path", command=self.select_output_path)
            self.output_path_button.pack(pady=10)

            self.output_path = ""

            self._initialized = True




    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
        if file_path:
            image = Image.open(file_path)

            width, height = image.size
            resize = min(self.image_label.winfo_height() / width, self.image_label.winfo_height() / height)
            
            ctk_image = ctk.CTkImage(image, size=(width * resize, height * resize))
            self.image_label.configure(image=ctk_image, text="")
            self.image_label.image = ctk_image

            # Update settings frame
            _settingsFrame = SettingsFrame(self.master)
            colormap = GetImageColormap(file_path)
            for color in colormap:
                self.master.fullColors[color[:7]] = color

            _settingsFrame.set_options([color[:7] for color in colormap if color[7:] != "00"])


    def select_output_path(self):
        self.output_path = filedialog.askdirectory()
        if self.output_path:
            print(f"Путь для сохранения: {self.output_path}")


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
            self.frames: list[ctk.CTkFrame] = []

            self.upper_frame = ctk.CTkFrame(self)
            self.upper_frame.pack(fill="x", padx=20, pady=5)

            self.scrollable_frame = ctk.CTkScrollableFrame(self)
            self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=15)


            # Autogenerate config button
            self.autogen_button = ctk.CTkButton(self.upper_frame, text="Autogenerate", command=self.autogenerate_config)
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


    def set_options(self, colormap: list[str]):
        [frame.pack_forget() for frame in self.frames]
        [self.create_option_row(color) for color in colormap]


    def create_option_row(self, color):
        row_frame = ctk.CTkFrame(self.scrollable_frame)
        row_frame.pack(fill="x", pady=5, padx=10)

        baseTile = "Plating"

        self.frames.append(row_frame)
        self.master.setup_colormap(color, TileSelector(baseTile))

        # Selectors option menu
        option_menu = ctk.CTkOptionMenu(row_frame, 
                                        values=[Selectors.Tile.value, Selectors.Entity.value], 
                                        command=lambda value: self.change_selector(value, entityEntry))
        option_menu.pack(side="left", padx=10, pady=10)
        option_menu.set(Selectors.Tile.value)

        # Entity protoName selector
        entityEntry = ctk.CTkEntry(row_frame, width=200)

        # TileName selector
        '''tileEntry = ctk.CTkEntry(row_frame, width=200)
        tileEntry.pack(side="left", padx=10, pady=10)
        tileEntry.insert(0, baseTile)'''
        tileOption = ctk.CTkOptionMenu(row_frame,
                                       values=self.master.tiles)
        tileOption.pack(side="left", padx=10, pady=10)

        # Color square
        color_label = ctk.CTkLabel(row_frame, width=30, height=30, text="", fg_color=color)
        color_label.pack(side="right", pady=10, padx=10)
    

    def autogenerate_config(self):
        pass


    def change_selector(self, value: str, entEntry: ctk.CTkEntry):
        if value == Selectors.Entity.value:
            entEntry.pack(side="left", padx=10, pady=10)
        elif value == Selectors.Tile.value:
            entEntry.pack_forget()