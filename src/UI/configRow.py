import customtkinter as ctk

from .appSettings import *
from .optionMenu import OptionEntry
from src.ColorHelper import *
from src.ImageReader.selectors import *
from src.Tiles import TilesRefsManager


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
        self.entityEntry.insert(0, "")

        # TileName selector
        self.tileEntry = OptionEntry(self, TilesRefsManager().tileRefs.keys(), width=200)
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

