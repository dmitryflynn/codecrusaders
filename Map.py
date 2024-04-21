import tkinter as tk
from PIL import Image, ImageTk

def display_images(image_paths):
    root = tk.Tk()
    root.title("Digipen Map")
    
    for i, image_path in enumerate(image_paths):
        img = Image.open(image_path)
        img.thumbnail((300, 300))  # Resizing the image to have a maximum size of 300x300
        photo = ImageTk.PhotoImage(img)
        
        label = tk.Label(root, image=photo)
        label.image = photo
        label.grid(row=0, column=i, padx=10, pady=10)
    
    root.mainloop()
    
if __name__ == "__main__":
    image_paths = ["digipen-building-map-floor-1.jpg", 
                   "digipen-building-map-floor-2.jpg",
                   "digipen-building-map-floor-3.jpg"]  # Change these to your image paths
    display_images(image_paths)
