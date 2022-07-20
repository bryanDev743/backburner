
import os
from os import listdir
from tkinter import *
from tkinter import filedialog
from PIL import Image
from tkinter import simpledialog

# get the path/directory

#tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

image_path = filedialog.askdirectory()
x=0 #counter of images in folder
q=0 #resolution to be reduced to


ROOT = Tk()

ROOT.withdraw()
# the input dialog
USER_INP = simpledialog.askstring(title="Test",
                                  prompt="What resolution do you wnat?: ")

USER_INP = int(USER_INP)

jpgDir = os.path.join(image_path,"jpg")
os.mkdir(jpgDir)
os.chdir(jpgDir)

print(image_path)

for images in os.listdir(image_path):
    # check if the image ends with png
    if (images.endswith(".jpg")):
        images = os.path.join(image_path,images)
        a = Image.open(images)
        a.save(f'{str(x)}.jpg',quality=USER_INP)
        x+=1

# OPENS FILE EXPLORER
# import tkinter
# from tkinter import filedialog

# tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

# folder_path = filedialog.askdirectory()
#file_path = filedialog.askopenfile()#s()



#a.save(image_path+"/jpg/"+str(x)+".jpg",quality=USER_INP)