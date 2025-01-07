###By Jack Whaley, special thanks to Jack Clements for helping me with this fucking nightmare###
###ICS4U1, P.Hanna###
###October 24, 2024###
from tkinter import *
from PIL import ImageTk, Image

x=0

def left():
    global x
    x -= 1
    global displayed_image
    global main_image
    global images
    global resized_image
    global tk_image
    if x < 0:
        x= len(images) - 1
    main_image = Image.open(images[x])
    resized_image = main_image.resize((1000, 800))
    tk_image = ImageTk.PhotoImage(resized_image)
    displayed_image = Label(root, image=tk_image, bd=0).grid(column=1, row=1, sticky="")
   

def right():
    global x
    x += 1
    global displayed_image
    global main_image
    global images
    global resized_image
    global tk_image
    if x > (len(images)-1):
        x = 0
    main_image = Image.open(images[x])
    resized_image = main_image.resize((1000, 800))
    tk_image = ImageTk.PhotoImage(resized_image)
    displayed_image = Label(root, image=tk_image, bd=0).grid(column=1, row=1, sticky="")

def forward():
    global x
    x += 1
    global displayed_image
    global main_image
    global images
    global resized_image
    global tk_image
    if x > (len(images)-1):
        x = 0
    main_image = Image.open(images[x])
    resized_image = main_image.resize((1000, 800))
    tk_image = ImageTk.PhotoImage(resized_image)
    displayed_image = Label(root, image=tk_image, bd=0).grid(column=1, row=1, sticky="")
    


images = ('assets\images\\test_4.jpg', 'assets\images\\test_3.jpg', 'assets\images\\test_2.jpg', 'assets\images\\test_1(hall end).jpg')

root = Tk()
root.title("Pictures Project")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


main_image = Image.open(images[x])
resized_image = main_image.resize((1000, 800))
tk_image = ImageTk.PhotoImage(resized_image)
displayed_image = Label(root, image=tk_image, bd=0).grid(column=1, row=1)


left_image = ImageTk.PhotoImage(Image.open('assets\images\left (2).png'))
left_arrow = Button(root, image=left_image, command=left, bd=0).grid(column=0, row=2, sticky=W)
right_image = ImageTk.PhotoImage(Image.open('assets\images\\right (2).png'))
right_arrow = Button(root, image=right_image, command=right, bd=0).grid(column=2, row=2, sticky=W)
up_image_big = Image.open('assets\images\\up.png')
up_image_small = up_image_big.resize((200, 200))
up_image = ImageTk.PhotoImage(up_image_small)
up_arrow = Button(root, image=up_image, command=forward, bd=0).grid(column=1, row=2, sticky=W, padx=165)


root.state('zoomed') 

root.mainloop()