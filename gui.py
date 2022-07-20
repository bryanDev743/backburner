from distutils.cmd import Command
from tkinter import *
from PIL import ImageTk, Image

top = Tk()

top.title('Gui')
top.geometry('400x220')

# frame = Frame(top, width=50,height=50)
# frame.pack()
# frame.place(anchor='center',relx=0.5, rely=0.5)

i = Image.open('resources/fire.png')
i.thumbnail((100,100))
img = ImageTk.PhotoImage(i)


Label(top, image=img).pack()

exitB = Button(top,text='exit',command=lambda:top.destroy())
exitB.pack(pady=20)

top.mainloop()

# to do later
# image = Image.open('demo_image.jpg')
# image.thumbnail((400, 400))
# image.save('image_thumbnail.jpg')
