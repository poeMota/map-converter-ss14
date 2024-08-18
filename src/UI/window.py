import customtkinter as ctk

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


    def change_frame(self, value):
        # Delete current page
        [frame.pack_forget() for frame in self.frames.values() if frame.winfo_ismapped()]

        # Show selected frame
        self.frames[Frames(value)].pack(fill="both", expand=True)

