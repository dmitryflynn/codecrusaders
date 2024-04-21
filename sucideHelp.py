import tkinter as tk

def open_link(url):
    import webbrowser
    webbrowser.open(url)

def main():
    root = tk.Tk()
    root.title("Sucide Help Resources")
    root.configure(bg='#ADD8E6')

    label = tk.Label(root, text="Sucide Help Resources", font=("Helvetica", 16), bg='#ADD8E6')
    label.pack(pady=10)

    # Add some time management tips or resources
    tip1 = tk.Label(root, text="1. Call a helpline at 988 .", bg='#ADD8E6')
    tip1.pack(anchor="w", padx=20)

    tip2 = tk.Label(root, text="2. Remember you are not alone talk to someone", bg='#ADD8E6')
    tip2.pack(anchor="w", padx=20)

    tip3 = tk.Label(root, text="3. Don't suffer from your depression in silence.", bg='#ADD8E6')
    tip3.pack(anchor="w", padx=20)

    # Add a button to open external resources
    external_button = tk.Button(root, text="Talk to someone here", command=lambda: open_link("https://www.mayoclinic.org/diseases-conditions/suicide/in-depth/suicide/art-20048230"),
                                bg='#61cefe', fg='black', relief=tk.FLAT, activebackground='#61cefe', activeforeground='black',
                                borderwidth=0, highlightthickness=0)
    external_button.pack(pady=10)

    # Set button border color to #61cefe
    external_button.configure(highlightbackground="#61cefe")

    root.mainloop()

if __name__ == "__main__":
    main()
