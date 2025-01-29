# gacha_system/main.py
import tkinter as tk
from gacha_system.interface.gui import GachaGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = GachaGUI(root)
    root.mainloop()