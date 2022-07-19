import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
USER_INP = simpledialog.askinteger(title="Test",
                                  prompt="What's your Name?:")

# check it out
print("Hello", USER_INP)
print(int(USER_INP))
print(type(USER_INP))