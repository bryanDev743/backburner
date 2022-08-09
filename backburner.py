
from genericpath import exists
import os
from os import listdir
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import askyesno, askyesnocancel
from PIL import Image, ImageTk
from tkinter import simpledialog

x=0 #counter of images in folder
q=0 #resolution to be reduced to

image_path = ''
jpgDir=''

#changepic=''

def selecr_folder(x):

    image_path=filedialog.askdirectory()
    jpgDir = os.path.join(image_path,"jpg")
    os.mkdir(jpgDir)
    os.chdir(jpgDir)
    
    X.pack()

    #return filedialog.askdirectory()

    # return simpledialog.askstring(title="Test",
    #                               prompt="What resolution do you wnat?: ")

    # USER_INP = simpledialog.askstring(title="Test",
    #                               prompt="What resolution do you wnat?: ")


def changePic():
    USER_INP = simpledialog.askstring(title="Test",
                                  prompt="What resolution do you wnat?: ")
    for images in os.listdir(image_path):
    # check if the image ends with png
        if (images.endswith(".jpg")):
            images = os.path.join(image_path,images)
            a = Image.open(images)
            if os.path.exists(image_path):
                ans = askyesnocancel(title='Error: jpg folder already exists',
                                message="Folder 'jpg' already exists. Do you wish to override it?")
                if ans:
                    print("fuck, working on it")

            a.save(f'{str(x)}.jpg',quality=USER_INP)
            x+=1


#image_path = selecr_folder()

#print(image_path)


if __name__ == '__main__':
    gui = Tk()
    gui.title('backburner')
    gui.geometry('400x200')
    gui.resizable(False,False)

    frame = Frame(gui, width=100,height=10z0)
    frame.pack()
    frame.place(anchor='center',relx=0.5, rely=0.5)

    i = Image.open('resources/fire.png')
    i.thumbnail((100,100))
    img = ImageTk.PhotoImage(i)


    #Label(gui, image=img).pack()

    
    changepic = Button(frame, text='Resize',command=changePic).pack()
    selectpic = Button(frame, text='Search',command=selecr_folder(changepic)).pack()


    gui.mainloop()




# OPENS FILE EXPLORER
# import tkinter
# from tkinter import filedialog

# tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

# folder_path = filedialog.askdirectory()
#file_path = filedialog.askopenfile()#s()

#a.save(image_path+"/jpg/"+str(x)+".jpg",quality=USER_INP)


    # for images in os.listdir(image_path):
    # # check if the image ends with png
    #     if (images.endswith(".jpg")):
    #         images = os.path.join(image_path,images)
    #         a = Image.open(images)
    #         a.save(f'{str(x)}.jpg',quality=USER_INP)
    #         x+=1

