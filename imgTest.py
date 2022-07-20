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

frame = Frame(gui, width=50,height=50)
frame.pack()
frame.place(anchor='center',relx=0.5, rely=0.5)

for images in os.listdir(folder_dir):

	# check if the image ends with png
	if (images.endswith(".jpg")):
          images = os.path.join(folder_dir,images) # opens the image
          i =  Image.open(images)
          i.thumbnail((100,100))
          img = ImageTk.PhotoImage(i)
          Label(frame, image=img).pack()       
          #i.show()
         #print(images)
         



gui.mainloop()