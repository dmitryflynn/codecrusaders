import tkinter as tk
from PIL import Image, ImageTk

def display_images(image_paths):
    root = tk.Tk()
    root.title("Digipen Map")
    
    for i, image_path in enumerate(image_paths):  #iterates over each image path and gets their index using enumerate
        img = Image.open(image_path)  #opens image 
        img.thumbnail((300, 300))  # Resizing the image to have a maximum size of 300x300
        photo = ImageTk.PhotoImage(img) #craetes a tk compatible image
        
        label = tk.Label(root, image=photo) #creates label
        label.image = photo #sets labels image to a photo
        label.grid(row=0, column=i, padx=10, pady=10) #place label in grid with the column padding and row
    
    root.mainloop()

if __name__ == "__main__":
    image_paths = ["digipen-building-map-floor-1.jpg", 
                   "digipen-building-map-floor-2.jpg",
                   "digipen-building-map-floor-3.jpg"]  #this shows the images 
    display_images(image_paths)
