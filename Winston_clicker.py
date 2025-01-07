from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

counter = 0

def Clicked():
    global counter
    counter +=1
    clicks.set(counter)

root = Tk()
frame = ttk.Frame(width=400, height=200)

root.title("Winston Clicker")
content = ttk.Frame(root)

image = ImageTk.PhotoImage(Image.open('winston.png'))
button = ttk.Button(root, image=image, command=Clicked)
ttk.Label(root, text='$Winston$')

clicks = IntVar()
ttk.Label(root, textvariable=clicks)

for child in root.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()