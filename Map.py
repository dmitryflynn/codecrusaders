import tkinter as tk
from tkinter import PhotoImage

def open_link(url):
    import webbrowser
    webbrowser.open(url)

def main():
    root = tk.Tk()
    root.title("DigiPen Campus Map")
    root.configure(bg='#ADD8E6')

    label = tk.Label(root, text="DigiPen Campus Map", font=("Helvetica", 16), bg='#ADD8E6')
    label.pack(pady=10)

    # Add some time management tips or resources
    img1 = PhotoImage(file='codecrusaders\digipen-building-map-floor-1.jpg')
    label(tk ,image = img1).pack()


    # Add a button to open external resources
    external_button = tk.Button(root, text="DigiPen Website", command=lambda: open_link("https://www.digipen.edu/"),
                                bg='#61cefe', fg='black', relief=tk.FLAT, activebackground='#61cefe', activeforeground='black',
                                borderwidth=0, highlightthickness=0)
    external_button.pack(pady=10)

    # Set button border color to #61cefe
    external_button.configure(highlightbackground="#61cefe")

    root.mainloop()

if __name__ == "__main__":
    main()
