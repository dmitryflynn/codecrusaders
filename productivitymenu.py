import tkinter as tk
import subprocess

def open_file(file_path):
    subprocess.Popen(['python', file_path])

def main():
    root = tk.Tk()
    root.title("Button Demo")
    root.configure(bg='#ADD8E6')  # Set background color to light blue

    # Define a function to open a specific file when a button is clicked
    def open_file1():
        open_file("timemanagement.py")

    def open_file2():
        open_file("calculator.py")
    
    def open_file3():
        open_file("hourstracker.py")

    # Create buttons to open different files with flat appearance and light blue color scheme
    button1 = tk.Button(root, text="Time Management", command=open_file1, bg='#ADD8E6', fg='white', relief=tk.FLAT, activebackground='#61cefe', activeforeground='white', borderwidth=0, highlightthickness=0)
    button1.pack(pady=10)

    button2 = tk.Button(root, text="Calculator", command=open_file2, bg='#ADD8E6', fg='white', relief=tk.FLAT, activebackground='#61cefe', activeforeground='white', borderwidth=0, highlightthickness=0)
    button2.pack(pady=10)

    button3 = tk.Button(root, text="Honor Society Tracker", command=open_file3, bg='#ADD8E6', fg='white', relief=tk.FLAT, activebackground='#61cefe', activeforeground='white', borderwidth=0, highlightthickness=0)
    button3.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
