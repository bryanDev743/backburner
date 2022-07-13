# SEARCHES THROUGH FOLDERS/DIRECTORIES
import os
from os import listdir
import tkinter
from tkinter import filedialog
from PIL import Image


# get the path/directory

tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

folder_path = filedialog.askdirectory()
x=0 #counter of images in folder
q=0 #resolution to be reduced to
#folder_dir = "/home/bryan/Projects/backburner/test"

for images in os.listdir(folder_path):
    # check if the image ends with png
    if (images.endswith(".jpg")):
        a = Image.open(images)
        a.save(str(x+1)+".jpg",quality=1)

# OPENS FILE EXPLORER
# import tkinter
# from tkinter import filedialog

# tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

# folder_path = filedialog.askdirectory()
#file_path = filedialog.askopenfile()#s()
