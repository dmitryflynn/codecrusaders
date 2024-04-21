import tkinter as tk #Import tkinter under alias of tk
import subprocess #Import subproccess to allow you to open processes

def open_file(file_path):  #create a function that takes a filepath as a pararemeter
    subprocess.Popen(['python', file_path]) #use default python process to run files

def main():
    root = tk.Tk() #New instance of main window
    root.title("Student ")
    root.configure(bg='#ADD8E6')  # Set background color to light blue

    # Define a function to open a specific file when a button is clicked
    
    def open_file1():
        open_file("productivitymenu.py")

    def open_file2():
        open_file("gamemenu.py")

    # Create buttons to open different files with flat appearance and light blue color scheme
    button1 = tk.Button(root, text="Productivity", command=open_file1, bg='#ADD8E6', fg='white', relief=tk.FLAT, activebackground='#61cefe', activeforeground='white', borderwidth=0, highlightthickness=0)
    button1.pack(pady=10)

    button2 = tk.Button(root, text="Game", command=open_file2, bg='#ADD8E6', fg='white', relief=tk.FLAT, activebackground='#61cefe', activeforeground='white', borderwidth=0, highlightthickness=0)
    button2.pack(pady=10)

    root.mainloop() #Starts event loop

if __name__ == "__main__":
    main()
