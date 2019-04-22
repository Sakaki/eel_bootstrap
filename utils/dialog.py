from tkinter import filedialog, Tk, Frame
import platform
from pathlib import Path


class Dialogs(Frame):
    def __init__(self):
        self.root = Tk()
        super().__init__(self.root)
        self.root.geometry("0x0")
        self.root.overrideredirect(1)
        self.root.withdraw()
        self.system = platform.system()
        self.pack()

    def open_dialog(self, dialog_open_method=filedialog.askopenfilename, options=None):
        if self.system == "Windows":
            self.root.deiconify()
        self.root.update()
        self.root.lift()
        self.root.focus_force()
        path_str = dialog_open_method(**(options or {}))
        self.root.update()
        if self.system == "Windows":
            self.root.withdraw()
        return Path(path_str)
