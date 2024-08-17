import customtkinter as ctk
import tkinter as tk


# FIXME - Yep, i hate frontend
class OptionEntry(ctk.CTkFrame):
    def __init__(self, master, options, **kwargs):
        super().__init__(master, **kwargs)
        self.options = options

        self.entry = ctk.CTkEntry(self, width=200)
        self.entry.pack(fill='x')
        self.entry.bind("<KeyRelease>", self.update_listbox)
        self.entry.bind("<Return>", lambda _: self.master.focus())
        self.entry.bind("<FocusOut>", lambda _: self.listFrame.place_forget())

        self.listFrame = ctk.CTkFrame(master.master,
                                      border_color="#565b5e",
                                      fg_color="#343638",
                                      border_width=2)

        self.listbox = HoverListbox(self.listFrame,
                                  fg="white",
                                  bg="#343638",
                                  highlightbackground="#343638",
                                  selectbackground="#565b5e",
                                  font=("Arial", 9),
                                  relief="flat",
                                  bd=0)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        self.listbox.pack(fill="both", padx=3, pady=3, expand=True)


    def get(self):
        return self.entry.get()


    def insert(self, index, string):
        self.entry.insert(index, string)
    

    def delete(self, first_index, last_index):
        self.entry.delete(first_index, last_index)


    def update_listbox(self, _):
        search_term = self.entry.get().lower()
        self.listbox.delete(0, tk.END)

        matching_options = [option for option in self.options if search_term in option.lower()]

        if matching_options:
            for option in matching_options:
                self.listbox.insert(tk.END, option)
            self.find_place()
        else:
            self.listFrame.place_forget()


    def find_place(self):
        win_height = self.master.master.master.winfo_height()
        list_height = self.listFrame.winfo_height()
        x = self.master.winfo_x() + self.winfo_x()
        y = self.master.winfo_y() + self.winfo_y() + self.entry.winfo_height() + 2

        if y + list_height > win_height:
            y = self.master.winfo_y() + self.winfo_y() - list_height - 2

        self.listFrame.place_configure(x=x, y=y, width=self.entry.winfo_width())
        self.listFrame.lift()


    def on_select(self, _):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_option = self.listbox.get(selected_index)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, selected_option)
            self.listFrame.place_forget()
            self.master.focus()


class HoverListbox(tk.Listbox):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<Motion>", self.on_hover)
        self.bind("<Leave>", self.on_leave)


    def on_hover(self, event):
        index = self.nearest(event.y)
        self.selection_clear(0, tk.END)
        self.selection_set(index)
        self.activate(index)


    def on_leave(self, _):
        self.selection_clear(0, tk.END)