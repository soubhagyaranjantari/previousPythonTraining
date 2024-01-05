from cProfile import label
from msilib.schema import File
from Tkinter import *
two=Tk()
two.geometry()
img=PhotoImage(file="five.png")

img1=Label(text="This Is A GUI")
img1.pack()
img2=Label(image=img)
img2.pack()
two.mainloop()