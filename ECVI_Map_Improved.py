###By Jack Whaley, special thanks to Jack Clements and Chatty G. for helping me with this fucking nightmare###
###ICS4U1, P.Hanna###
###October 24, 2024###
from tkinter import *
from PIL import ImageTk, Image
class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pictures Project")
        self.root.state('zoomed')
        
        
        #Test for info pop ups within the school
        
        # Configure grid
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        # Initialize image list and index
        self.images = [
            '',
            r'assets\Images\Hall 1 left.png', #left
            r'assets\Images\Hall 1.png', #Forward
            r'assets\Images\Hall 1 right.png', #Right
            r'assets\Images\Hall 2 left.png', #Left
            r'assets\Images\Hall 2.png', #Forward
            r'assets\Images\Hall 2 right.png', #Right
            r'assets\Images\Hall 3 left.png', #Left
            r'assets\Images\Hall 3.png', #Forward
            r'assets\Images\Hall 3 right.png', #Right
            r'assets\Images\Hall 4 left.png', #Left
            r'assets\Images\Hall 4.png', #Forward
            r'assets\Images\Hall 4 right.png', #Right
            ]
        self.index = 2

        # Display the initial image
        self.image_label = Label(self.root, bd=0)
        self.image_label.grid(column=1, row=1, sticky="nsew")
        self.display_image()

        # Navigation buttons
        self.left_image = ImageTk.PhotoImage(Image.open(r'assets/images/left (2).png'))
        self.right_image = ImageTk.PhotoImage(Image.open(r'assets/images/right (2).png'))
        up_image_big = Image.open(r'assets/images/up.png').resize((200, 200))
        self.up_image = ImageTk.PhotoImage(up_image_big)

        Button(self.root, image=self.left_image, command=self.previous_image, bd=0).grid(column=0, row=2, sticky="nsew")
        Button(self.root, image=self.right_image, command=self.next_image, bd=0).grid(column=2, row=2, sticky="nsew")
        Button(self.root, image=self.up_image, command=self.forward_image, bd=0).grid(column=1, row=2, sticky="nsew")
        Button(self.root, text="back", command=self.back_image, bd=0).grid(column=1, row=3, sticky="nsew")

    def display_image(self):
        """Displays the current image based on the index."""
        main_image = Image.open(self.images[self.index])
        resized_image = main_image.resize((1000, 800))
        tk_image = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image  # Prevent garbage collection

    def previous_image(self):
        """Turns the camera left."""
        if (self.index + 2) % 3 == 0:
            return
        self.index = (self.index - 1 ) % len(self.images)
        if self.index == 0:
            self.index = 1
        if self.index == 4:
            self.pop_up()
        self.display_image()

    def next_image(self):
        """Turns the camera right."""
        if self.index % 3 == 0:
            return
        self.index = (self.index + 1) % len(self.images)
        if self.index == 0:
            self.index = 2
        if self.index == 4:
            self.pop_up()
        self.display_image()

    def forward_image(self):
        """Moves forward one image."""
        self.index = (self.index + 3) % len(self.images)
        if self.index == 1:
            self.index = 2
        if self.index == 4:
            self.pop_up()
        print(self.index)
        self.display_image()

    def back_image(self):
        """Moves back one image."""
        self.index = (self.index - 3) % len(self.images)
        

    def pop_up(self):
        if self.index == 4:
            print('image')
            hi = Image.open(self.pop_up_image)
            bye = ImageTk.PhotoImage(hi)
            self.pop_up_label.config(image=bye)


# Main application
root = Tk()
app = ImageViewer(root)
root.mainloop()