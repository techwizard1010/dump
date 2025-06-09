import fnmatch
import tkinter as tk  # Import Tkinter module

# Create a Button widget
def greet():
    i=0
    for s in urlList:
        if fnmatch.fnmatch(entry.get(), s):
            print(f"'{s}' matches the pattern '{entry.get()}'")
        else:
            print(f"'{s}' does NOT match the pattern '{entry.get()}'") 
    i = i+1

#get list from network drive
urlList=["example.com", "*.example.com"]


# Create the main window
root = tk.Tk()
root.title("URL Match")  # Set the title of the window
root.geometry("700x1000")  # Set the size of the window

# Create a Label widget
label = tk.Label(root, text="Enter URL to match:")
label.grid(row=0, column=1)  # Use pack() to add the label to the window

# Create an Entry field (textbox) for user input
entry = tk.Entry(root)
entry.grid(row=5, column=6)

listboxList = tk.StringVar(value=urlList)
listbox = tk.Listbox(root, height=10, listvariable=listboxList)
listbox.grid(row=55, column=7, sticky="we")

scroll_bar = tk.Scrollbar(root, command=listbox.yview)
scroll_bar.grid(column=1, row=0, sticky='ns')
listbox['yscrollcommand'] = scroll_bar.set


button = tk.Button(root, text="Greet", command=greet)
button.grid(row=10, column=6) # Add the button to the window

identifiedLabel = tk.Label(root, text="AO Identified Block List")
identifiedLabel.grid(row=13, column=6)



# Keep the window open and listen for events
root.mainloop()