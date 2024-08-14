import customtkinter as ctk


class Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("SS14 Map Converter -- Image to YAML")
        self.geometry("1080x780")

        self.mainloop()

