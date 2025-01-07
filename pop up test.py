from tkinter import *
from PIL import ImageTk, Image

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("800x600")

        # List of images and current index
        self.images = [
            r'assets\Images\Hall 1 left.png', #left
            r'assets\Images\Hall 1.png', #Forward
            r'assets\Images\Hall 1 right.png', #Right
            r'assets\Images\Hall 2 left.png', #Left
        ]
        self.index = 0
        self.trigger_index = 2  # The index at which the button appears

        # Label to display images
        self.image_label = Label(self.root, bd=0)
        self.image_label.pack(expand=True)

        # Navigation buttons
        Button(self.root, text="Previous", command=self.previous_image).pack(side=LEFT, padx=20)
        Button(self.root, text="Next", command=self.next_image).pack(side=RIGHT, padx=20)

        # Button for the trigger (hidden initially)
        self.button_pic = ImageTk.PhotoImage(Image.open(r'assets\Images\Pop up arrow for tkinter.png'))
        self.trigger_button = Button(self.root, image=self.button_pic, command=self.show_popup)
        self.trigger_button.pack_forget()  # Hide initially

        # Display the first image
        self.display_image()
        
    def display_image(self):
        """Update the displayed image based on the current index."""
        image = Image.open(self.images[self.index])
        resized_image = image.resize((600, 400))
        tk_image = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image  # Prevent garbage collection

        # Check if the trigger condition is met
        self.check_trigger()

    def check_trigger(self):
        """Show or hide the trigger button based on the current index."""
        if self.index == self.trigger_index:
            self.trigger_button.pack(anchor = "center")  # Show the button
        else:
            self.trigger_button.pack_forget()  # Hide the button

    def previous_image(self):
        """Go to the previous image."""
        self.index = (self.index - 1) % len(self.images)
        self.display_image()

    def next_image(self):
        """Go to the next image."""
        self.index = (self.index + 1) % len(self.images)
        self.display_image()

    def show_popup(self):
        """Display a pop-up window with a message or image."""
        self.popup = Toplevel(self.root)
        self.popup.title("Pop-Up")
        self.popup.geometry("400x300")

        Label(self.popup, text="You triggered the pop-up!", font=("Arial", 16)).pack(pady=20)
        Button(self.popup, text="Close", command=self.popup.destroy).pack()

# Main application
root = Tk()
app = ImageViewer(root)
root.mainloop()
