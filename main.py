import tkinter as tk
from synthesizer import Synthesizer
from gui import GUI

if __name__ == "__main__":
    synthesizer = Synthesizer()
    root = tk.Tk()
    gui = GUI(root, synthesizer)
    gui.create_gui()
    root.mainloop()


