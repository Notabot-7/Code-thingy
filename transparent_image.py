from tkinter import Tk, Canvas
from PIL import Image, ImageTk

# Initialize Tkinter
root = Tk()

# Load the background image
background_image = Image.open("winston.png")  # Replace with your background image path
background_photo = ImageTk.PhotoImage(background_image)

# Load the arrow image directly without convert("RGBA")
arrow_image = Image.open("Cool Crow.png")  # Replace with your arrow image path
arrow_photo = ImageTk.PhotoImage(arrow_image)  # Tkinter should handle the transparency natively

# Create a Canvas widget to layer images
canvas = Canvas(root, width=background_image.width, height=background_image.height)
canvas.pack()

# Display the background image on the canvas
canvas.create_image(0, 0, anchor="nw", image=background_photo)

# Overlay the transparent PNG (arrow image) on top
canvas.create_image(50, 50, anchor="nw", image=arrow_photo)  # Adjust the coordinates as needed

root.mainloop()
