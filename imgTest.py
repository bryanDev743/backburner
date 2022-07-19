import os
from os import listdir

from tkinter import filedialog

# get the path/directory 
folder_dir = filedialog.askdirectory()
for images in os.listdir(folder_dir):

	# check if the image ends with png
	if (images.endswith(".png")):
		print(images)
