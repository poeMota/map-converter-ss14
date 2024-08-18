import customtkinter as ctk


class LoadingScreen(ctk.CTkFrame):
    def __init__(self, master, text="Loading..."):
        super().__init__(master, width=master.winfo_width(), height=master.winfo_height())
        self.place(x=0, y=0)
        self.configure(bg_color='transparent')

        # Loading label
        self.label = ctk.CTkLabel(self, text=text, text_color="white", font=("Arial", 18))
        self.label.place(relx=0.5, rely=0.4, anchor='center')
        self.lift()

        # Grab all events
        self.after(1, self.grab_set)


    def close(self):
        self.grab_release()
        self.destroy()

