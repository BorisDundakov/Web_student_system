from tkinter import *
from PIL import ImageTk, Image
import os

# 1. Creating a Window

window = Tk()
window.title("WebStudent Login")
window.geometry("900x900")
window.configure(bg='#e67300')
# username label and text entry box
usernameLabel = Label(window, text="Username:", bg="#e67300").grid(row=0, column=0, padx=10, pady=10, sticky=NW)
username = StringVar()
usernameEntry = Entry(window, textvariable=username).grid(row=0, column=1, padx=10, pady=10, sticky=NW)

# password label and password entry box
passwordLabel = Label(window, text="Password:", bg="#e67300").grid(row=1, column=0, padx=10, pady=10, sticky=NW)
password = StringVar()
passwordEntry = Entry(window, textvariable=password, show='*').grid(row=1, column=1, padx=10, pady=10, sticky=NW)

# adding an image
path = 'F:\Projects archive- for Github\Python\Webstudent System\Interface\student-login.png'

img = ImageTk.PhotoImage(Image.open(path))

panel = Label(window, image=img, bg="#e67300")
panel.grid(row=6, column=6, sticky=SW)
# img = ImageTk.PhotoImage(Image.open("student-login.png"))
# img = Image.open(r"F:\Projects archive- for Github\Python\Webstudent System\Interface\student-login.png")
# panel = Label(window, image=img).grid(row=5, column=5, padx=10, pady=10)

# creating a button
b = Button(window, text="Log in")
b.grid(row=2, column=0, columnspan=2)

window.mainloop()
