import tkinter as tk
from tkinter import messagebox, Button, LEFT, RIGHT


root = tk.Tk()
root.geometry("200x100+300+300")

def disp_slogan():
    messagebox.showinfo("our message", "Hello World")

slogan = Button(root, text="Hello World", command=disp_slogan)

slogan.pack(side=LEFT, padx=10)

button = Button(root, text="QUIT", fg="red", command=quit)

button.pack(side=RIGHT, padx=10)

root.mainloop()
