import customtkinter as ctk


class PopupWindow(ctk.CTkToplevel):
    def __init__(self, master, title: str, message: str, width=300, height=150, buttlonLabel: str = "Close"):
        super().__init__(master)

        self.title(title)
        self.center_window(height, width)

        self.attributes("-topmost", True)
        self.resizable(False, False)

        # Message label
        self.label = ctk.CTkLabel(self, text=message, wraplength=250)
        self.label.pack(pady=20, padx=20)

        # Close buttom
        self.close_button = ctk.CTkButton(self, text=buttlonLabel, command=self.close_window)
        self.close_button.pack(pady=10)

        self.after(1, self.grab_set) # the window may not have time to initialise


    def center_window(self, height, width):
        self.update_idletasks()

        parent_x = self.master.winfo_x()
        parent_y = self.master.winfo_y()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()

        x = parent_x + (parent_width // 2) - (width // 2)
        y = parent_y + (parent_height // 2) - (height // 2)

        self.geometry(f'{width}x{height}+{x}+{y}')


    def close_window(self):
        self.grab_release()
        self.destroy()

