import tkinter as tk
from tkinter import scrolledtext
import fnmatch
from smbprotocol.connection import Connection
from smbprotocol.session import Session
from smbprotocol.tree import TreeConnect
from smbprotocol.open import Open
from smbprotocol.file_info import FileAttributes

SERVER = "your_samba_server"
SHARE = "your_share"
USERNAME = "your_username"
PASSWORD = "your_password"
FILE_PATH = r"\path\to\file.txt"

def read_samba_file():
    conn = Connection(uuid="connection", server=SERVER, port=445)
    conn.connect()
    
    session = Session(conn, username=USERNAME, password=PASSWORD)
    session.connect()
    
    tree = TreeConnect(session, fr"\\{SERVER}\{SHARE}")
    tree.connect()
    
    file_open = Open(tree, FILE_PATH, desired_access=0x120089, file_attributes=FileAttributes.FILE_ATTRIBUTE_NORMAL)
    file_open.create()
    
    data = file_open.read(0, 0, 4096).decode('utf-8')
    
    file_open.close()
    tree.disconnect()
    session.disconnect()
    conn.disconnect()
    
    return data.splitlines()

def match_wildcard():
    pattern = entry.get()
    file_lines = ["*.example.com",]
    matches = fnmatch.filter(file_lines, pattern)
    
    output_text.delete(1.0, tk.END)
    if matches:
        output_text.insert(tk.END, "\n".join(matches))
    else:
        output_text.insert(tk.END, "No matches found.")

root = tk.Tk()
root.title("Wildcard String Matcher")

tk.Label(root, text="Enter wildcard pattern:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Match", command=match_wildcard).pack(pady=5)

output_text = scrolledtext.ScrolledText(root, width=60, height=15)
output_text.pack(pady=10)


https://www.tcl-lang.org/man/tcl8.6/TkCmd/grid.htm#M19
https://www.tcl-lang.org/man/tcl8.6/TkCmd/listbox.htm
https://tkdocs.com/tutorial/morewidgets.html#listbox


root.mainloop()
