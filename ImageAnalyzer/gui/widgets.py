import tkinter as tk

class LabeledEntry(tk.Frame):
    """A custom widget combining a label and an entry field."""
    def __init__(self, master, label_text, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.label = tk.Label(self, text=label_text)
        self.label.pack(side=tk.LEFT)
        self.entry = tk.Entry(self)
        self.entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)

    def get_value(self):
        """Returns the value entered in the entry field."""
        return self.entry.get()

class StatusBar(tk.Frame):
    """A custom status bar widget."""
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.label = tk.Label(self, text="", anchor="w")
        self.label.pack(fill=tk.X)

    def set_message(self, message):
        """Sets a message in the status bar."""
        self.label.config(text=message)