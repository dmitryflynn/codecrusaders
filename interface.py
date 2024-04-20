import tkinter as tk
import subprocess

def open_file(file_path):
    subprocess.Popen(['python', file_path])

def main():
    root = tk.Tk()
    root.title("Button Demo")

    # Define a function to open a specific file when a button is clicked
    def open_file1():
        open_file("calculator.py")

    def open_file2():
        open_file("hourstracker.py")

    def open_file3():
        open_file("SnakeGame.py")

    # Create buttons to open different files
    button1 = tk.Button(root, text="Calculator", command=open_file1)
    button1.pack()

    button2 = tk.Button(root, text="Snake", command=open_file2)
    button2.pack()

    button3 = tk.Button(root, text="hourstracker", command=open_file3)
    button3.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
