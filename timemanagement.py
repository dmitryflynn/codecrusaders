import tkinter as tk

def open_link(url):  #open the url function
    import webbrowser 
    webbrowser.open(url)

def main():
    root = tk.Tk() #new instance of main window
    root.title("Time Management Resources")
    root.configure(bg='#ADD8E6')

    label = tk.Label(root, text="Time Management Resources", font=("Helvetica", 16), bg='#ADD8E6')
    label.pack(pady=10)

    # Add some time management tips or resources

    #first tip
    tip1 = tk.Label(root, text="1. Use a planner or calendar to organize your tasks.", bg='#ADD8E6')
    tip1.pack(anchor="w", padx=20)

    #second tip
    tip2 = tk.Label(root, text="2. Break tasks into smaller, manageable chunks.", bg='#ADD8E6')
    tip2.pack(anchor="w", padx=20)

    #third tip
    tip3 = tk.Label(root, text="3. Prioritize tasks based on deadlines and importance.", bg='#ADD8E6')
    tip3.pack(anchor="w", padx=20)

    #add a button to open external resources
    external_button = tk.Button(root, text="Find more time management tips online", command=lambda: open_link("https://www.mindtools.com/arb6j5a/what-is-time-management"),
                                 bg='#61cefe', fg='black', relief=tk.FLAT, activebackground='#61cefe', activeforeground='black',
                                 borderwidth=0, highlightthickness=0)
    external_button.pack(pady=10)

    #set button border color to #61cefes
    external_button.configure(highlightbackground="#61cefe")

    root.mainloop() #runs main tkinter function

if __name__ == "__main__":
    main()
