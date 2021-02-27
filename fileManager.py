import tkinter
from tkinter import filedialog


def openFile():
    root = tkinter.Tk()
    root.withdraw()
    openFilePath = filedialog.askopenfilename()

    return openFilePath


def saveFile():
    root = tkinter.Tk()
    root.withdraw()
    outputFilePath = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                  filetypes=(("mp3 file", "*.mp3"), ("All Files", "*.*")))

    return outputFilePath
