import customtkinter as ctk
from PIL import Image
from tkinter import filedialog

from .settingsFrame import SettingsFrame
from src.ColorHelper import *
from .appSettings import *
from .optionMenu import OptionEntry


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
            self.convert_button = ctk.CTkButton(self.right_frame, text="Convert to map", command=master.convert_image)
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
            settings = GlobalSettings()
            image = Image.open(file_path)

            if '.png' in file_path:
                settings.image = image.convert("RGBA")
            else:
                settings.image = image.convert("RGB")

            width, height = image.size
            resize = min(self.image_label.winfo_height() / width, self.image_label.winfo_height() / height)

            ctk_image = ctk.CTkImage(image, size=(width * resize, height * resize))
            self.image_label.configure(image=ctk_image, text="")
            self.image_label.image = ctk_image

            # Update settings frame
            _settingsFrame = SettingsFrame(self.master)
            _settingsFrame.set_options(GetImageColormap(file_path))

            print(f"Open image from {file_path}")


    def select_output_path(self):
        path = filedialog.askdirectory() + '/'
        if path:
            GlobalSettings().outPath = path
            print(f"Output path selected: {path}")

