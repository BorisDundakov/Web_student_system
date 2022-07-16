from tkinter import *
from PIL import ImageTk, Image
import os

# 1. Creating a Window

window = Tk()
window.title("WebStudent Login")
window.geometry("900x900")
# username label and text entry box
usernameLabel = Label(window, text="Username").grid(row=0, column=0, padx=10, pady=10)
username = StringVar()
usernameEntry = Entry(window, textvariable=username).grid(row=0, column=1)

# password label and password entry box
passwordLabel = Label(window, text="Password").grid(row=1, column=0, padx=10, pady=10)
password = StringVar()
passwordEntry = Entry(window, textvariable=password, show='*').grid(row=1, column=1)

# adding an image

from PIL import ImageTk, Image

path = 'F:\Projects archive- for Github\Python\Webstudent System\Interface\student-login.png'

img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

# img = ImageTk.PhotoImage(Image.open("student-login.png"))
img = Image.open(r)
panel = Label(window, image=img).grid(row=5, column=5, padx=10, pady=10)

# creating a button
b = Button(window, text="Log in")
b.grid(row=2, column=0, columnspan=5)

window.mainloop()
