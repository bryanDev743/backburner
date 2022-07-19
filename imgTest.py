import os
from os import listdir
from tkinter import filedialog
from distutils.cmd import Command
from tkinter import *
from PIL import ImageTk, Image


# get the path/directory 
folder_dir = filedialog.askdirectory()

gui = Tk()
gui.title('imgTest')
gui.geometry('500x300')


for images in os.listdir(folder_dir):

	# check if the image ends with png
	if (images.endswith(".png")):
          images = os.path.join(folder_dir,images)
          i =  Image.open(images)       
          i.show()
         #print(images)
         



gui.mainloop()