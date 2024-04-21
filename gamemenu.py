import tkinter as tk
import subprocess

def open_file(file_path):
    subprocess.Popen(['python', file_path]) #uses the subprocess library to open files using the process python, and takes the file path as a parameter

def main():
    root = tk.Tk()
    root.title("Game Menu")
    root.configure(bg='#ADD8E6')

    root.attributes('-fullscreen', True)

    custom_font = ("Helvetica", 36)

    def on_enter(e):
        e.widget.config(bg="#61cefe")  #change background color to active color on hover

    def on_leave(e):
        e.widget.config(bg='#ADD8E6')  #change background color back to original color on leave

    def open_file1():
        open_file("PongGame.py") #create a function that opens the productivity menu, used in the button command

    def open_file2():
        open_file("SnakeGame.py")

    button1 = tk.Button(root, text="Pong", command=open_file1, width=20, height=5, bg='#ADD8E6', fg='white', relief=tk.FLAT, activebackground='#61cefe', activeforeground='white', borderwidth=0, highlightthickness=0, font=custom_font)
    button1.pack(side='top', fill='both', expand=True)
    button1.bind("<Enter>", on_enter)  #bind the enter event to on_enter function
    button1.bind("<Leave>", on_leave)  #bind the leave event to on_leave function

    button2 = tk.Button(root, text="Snake", command=open_file2, width=20, height=5, bg='#ADD8E6', fg='white', relief=tk.FLAT, activebackground='#61cefe', activeforeground='white', borderwidth=0, highlightthickness=0, font=custom_font)
    button2.pack(side='top', fill='both', expand=True)
    button2.bind("<Enter>", on_enter)  #bind the enter event to on_enter function
    button2.bind("<Leave>", on_leave)  #bind the leave event to on_leave function

    root.mainloop()

if __name__ == "__main__":
    main()
