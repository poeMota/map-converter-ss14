import customtkinter as ctk
from PIL import Image
from tkinter import filedialog

import src.yaml as yaml
from src.EntitySystem import EntitySystem
from src.ImageReader import ConvertImageToMap
from .settingsFrame import SettingsFrame
from src.ColorHelper import *
from .appSettings import *
from .optionMenu import OptionEntry
from .popup import PopupWindow, ColorsWarningPopup


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
            self.image_label = ctk.CTkLabel(self.left_frame, text="Select the image you want to convert", height=600, corner_radius=10)
            self.image_label.pack(fill="x")

            # Choose image button
            self.select_image_button = ctk.CTkButton(self.right_frame, text="Choose image", command=self.select_image)
            self.select_image_button.pack(pady=10)

            # Choose out path button
            self.output_path_button = ctk.CTkButton(self.right_frame, text="Choose output path", command=self.select_output_path)
            self.output_path_button.pack(pady=0)

            # Convert button
            self.convert_button = ctk.CTkButton(self.right_frame, text="Convert to map", command=self.convert_image)
            self.convert_button.pack(pady=10, padx=5, side="bottom")

            # Filename entry
            self.filename_entry = ctk.CTkEntry(self.right_frame)
            self.filename_entry.pack(pady=0, side="bottom")
            self.filename_entry.insert(0, "")

            self.filename_label = ctk.CTkLabel(self.right_frame, text="Enter out file name")
            self.filename_label.pack(side="bottom")

            GlobalSettings().outFileEntry = self.filename_entry

            self._initialized = True


    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("PNG", ".png"), ("JPEG", ".jpg")])
        if file_path:
            image = Image.open(file_path)

            if '.png' in file_path:
                image = image.convert("RGBA")
                imageColormap = GetImageColormap(image)
            else:
                image = image.convert("RGB")
                imageColormap = GetImageColormap(image, rgbToHex)


            colorsLimit = 256 # TODO - move this to config
            if len(imageColormap) > colorsLimit:
                print(f"WARNING: to many colors in image - {len(imageColormap)}")
                ColorsWarningPopup(self,
                                   "Warning",
                                   "The image contains too many colors, the program will work unstably, it is recommended to convert the image to a format with fewer bits.",
                                   lambda value: self._select_image(quantize(image, 2**value)))
            else:
                self._select_image(image, imageColormap)
                print(f"Open image from {file_path}")


    def _select_image(self, image: Image, imageColormap = None):
        settings = GlobalSettings()
        settings.image = image

        if not imageColormap:
            imageColormap = GetImageColormap(image)

        width, height = image.size
        resize = min(self.image_label.winfo_height() / width, self.image_label.winfo_height() / height)

        ctk_image = ctk.CTkImage(image, size=(width * resize, height * resize))
        self.image_label.configure(image=ctk_image, text="")
        self.image_label.image = ctk_image

        # Update settings frame
        _settingsFrame = SettingsFrame(self.master)
        _settingsFrame.set_options(imageColormap)


    def select_output_path(self):
        path = filedialog.askdirectory() + '/'
        if path:
            GlobalSettings().outPath = path
            print(f"Output path selected: {path}")


    def convert_image(self):
        settings = GlobalSettings()
        settings.outFileName = settings.outFileEntry.get().strip().removesuffix('.yml') + '.yml'
        SettingsFrame(self.master).setup_colormap()

        if not settings.image:
            print("ERROR: image not selected")
            PopupWindow(self, "Error", "Image is not selected.")
            return

        if not settings.outPath:
            print("ERROR: output path not selected")
            PopupWindow(self, "Error", "Output folder is not selected.")
            return

        if not settings.outFileName:
            print("ERROR: output filename not selected")
            PopupWindow(self, "Error", "Name for the output file is not selected.")
            return

        _map = ConvertImageToMap(settings.image, settings.colorConfig)
        yaml.write(settings.outPath + settings.outFileName, _map._serialize())
        print("Image converted to path: " + settings.outPath + settings.outFileName)

        EntitySystem().clean()
        print("Cleanup all entities")

