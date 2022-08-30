import os
import tkinter.filedialog

def select_folder(title="Select folder", folder=".", master=None):

    if not os.path.isdir(folder):
        folder = "."
    
    return tkinter.filedialog.askdirectory(title=title, initialdir=folder, parent=None if master is None else master.tk)