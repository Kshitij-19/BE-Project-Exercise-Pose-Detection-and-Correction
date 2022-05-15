from asyncio import subprocess
import io
from tkinter import *
import os
import subprocess
from tkinter import messagebox
from PIL import Image, ImageTk
import urllib.request


mainWindow = Tk()

# images = []


# raw_data = urllib.request.urlopen("https://upload.wikimedia.org/wikipedia/en/4/4c/GokumangaToriyama.png").read()
# im = Image.open(io.BytesIO(raw_data))
# image = ImageTk.PhotoImage(im)
# label1 = Label(mainWindow, image=image)
# label1.grid(row=0, sticky=W)

# # append to list in order to keep the reference
# images.append(image)
messagebox.showinfo("Registration Successfull", "Email verification link has been sent to your email account")

mainWindow.mainloop()