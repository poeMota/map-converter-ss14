import customtkinter as ctk


class PopupWindow(ctk.CTkToplevel):
    def __init__(self, master, title: str, message: str, width=300, height=150, buttlonLabel: str = "Close"):
        super().__init__(master)
        self.title(title)
        self.geometry(f"{width}x{height}")

        self.grab_set()
        self.attributes("-topmost", True)

        # Message label
        self.label = ctk.CTkLabel(self, text=message, wraplength=250)
        self.label.pack(pady=20, padx=20)

        # Close buttom
        self.close_button = ctk.CTkButton(self, text=buttlonLabel, command=self.close_window)
        self.close_button.pack(pady=10)


    def close_window(self):
        self.grab_release()
        self.destroy()

