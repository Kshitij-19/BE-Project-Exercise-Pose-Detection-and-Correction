from logging import PlaceHolder
import time
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
# from tkinter import filedialog
from turtle import width
import User
import pyautogui
import cv2 as cv
import subprocess
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
import os
import pyrebase
# from asyncio import subprocess
import io
from tkinter import *
import os
import subprocess
from PIL import Image, ImageTk
import urllib.request
from firebase import *
import sys
import edit_profile as ep
import display_profile as dp

print(len(sys.argv))
if len(sys.argv) == 3:
    global email
    global password 
    email = sys.argv[1]
    password = sys.argv[2]


width = ''
height = ''
cap = ''
root = tk.Tk()
root.config(background='white')
lmain = ''
label_frame = ''
# label_hello_world = Label(root, text="Hello World")
# label_hello_world.grid(row=0,column=0)



class gui:
    filename = ""
    exercise = ""

    def browseFiles(self):
        self.filename = filedialog.askopenfilename(initialdir="./",
                                                   title="Select a File",
                                                   filetypes=(("Text files",
                                                               "*.mp4*"),
                                                              ("all files",
                                                               "*.*")))

    def process_function(self):
        destoy_all_side_frames()
        # filename = filedialog.askopenfilename(initialdir="./",
        #                                       title="Select a File",
        #                                       filetypes=(("Text files",
        #                                                   "*.mp4*"),
        #                                                  ("all files",
        #                                                   "*.*")))

        # # Change label contents
        # label_file_explorer.configure(text="File Opened: "+filename)

        # set exercise variable
        self.exercise = exercise_dict[clicked.get()]

        # command = f'py main.py --mode evaluate --video sample_bicep_curl.mp4'

        # uncomment start
        

        
        command = f'py main.py --mode evaluate --video {self.filename} --exercise {self.exercise}'
        print(command)
        # command = "dir"
        command_list = command.split()
        # subprocess.Popen(command,shell=True)


        # pb = ttk.Progressbar(
        #     imageFrame,
        #     orient='horizontal',
        #     mode='indeterminate',
        #     length=280
        # )
        # # place the progressbar
        # pb.grid(column=0, row=5,padx=10, pady=20)
        # pb.start(20)

        output = '''
OpenPose demo successfully finished. Total time: 187.908795 seconds.
processing video file...
Exercise arm detected as: right.
Upper arm and torso angle range: 12.91638852310736
Upper arm and forearm minimum angle: 28.69665215047628
Exercise performed correctly!
Exercise performed correctly! Weight was lifted fully up, and upper arm did not move significantly.'''


        # out = subprocess.check_output(command, shell=True)
        # print(out.decode("utf-8"))

        process = subprocess.Popen(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, code = process.communicate()


        output = out.decode("utf-8")


        global lmain
        # Capture video frames
        lmain = tk.Label(imageFrame, width=600, height=700,bg='white')
        # lmain.grid(row=0, column=0)
        lmain.grid()
        
        global width
        global height
        global cap
        cap = cv.VideoCapture('result.avi')
        width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

        # uncomment end

        # stream = os.popen(command)
        # label_hello_world = Label(
        #     root, text=out.decode("utf-8"), justify="left")
        # label_hello_world.pack(fill='both')
        cap = cv.VideoCapture('result.avi')
        show_frame()



        # pyautogui code
        # print("call Finished")
        # pyautogui.alert(out.decode("utf-8"))

        # Output Window
#         output = '''
# OpenPose demo successfully finished. Total time: 237.896797 seconds.
# Exercise arm detected as: right.
# Upper arm and torso angle range: 12.91638852310736
# Upper arm and forearm minimum angle: 28.69665215047628
# Exercise performed correctly!
# Exercise performed correctly! Weight was lifted fully up, and upper arm did not move significantly.'''
        global label_frame
        label_frame = tk.Frame(root, width=500, height=700,bg='white')
        label_frame.grid(row=0, column=2, rowspan=5, padx=50, pady=70)
        output_text = tk.Text(label_frame,border=0)
        output_text.insert(tk.END,output)
        output_text.pack()
        label_frame.grid_propagate(0)



guiInstance = gui()


# def on_click_process():
#     pb = ttk.Progressbar(
#         imageFrame,
#         orient='horizontal',
#         mode='indeterminate',
#         length=280
#     )
#     # place the progressbar
#     pb.grid(column=0, row=5,padx=10, pady=20)
#     pb.start(20)
#     # time.sleep(7)
#     guiInstance.process_function()

# Change the label text

# select_exercise_optionmenudown menu options
exercise_dict = {
    "             BICEP CURL             ": "bicep_curl",
    "           SHOULDER PRESS           ": "shoulder_press",
    "            FRONT  RAISE            ": "front_raise",
    "           SHOULDER SHRUG           ": "shoulder_shrug",
}

options = [
    "             BICEP CURL             ",
    "           SHOULDER PRESS           ",
    "            FRONT  RAISE            ",
    "           SHOULDER SHRUG           ",
]


# datatype of menu text
clicked = tk.StringVar()

# initial menu text
clicked.set("-- SELECT AN EXERCISE --")

# edit profile start
def edit_profile():
    ep.edit_profile(firebase, auth, db, storage,email,password)
# edit profile end

# edit profile start
def display_profile():
    destoy_all_side_frames()
    dp.display_profile(firebase, auth, db, storage,email,password,root)
# edit profile end



# display Diet Plan start
def display_diet_plan():
    diet_plan_window = tk.Tk()
    diet_plan_window.config(bg='white')
    diet_plan_window.mainloop()
# display Diet Plan end


# Diet Plan Button start
# diet_plan_button = tk.Button(
#     root, text="DIET PLAN", command=display_diet_plan, width=30, height=1, background='white')
# diet_plan_button.grid(row=4, column=0, pady=60, padx=10)
# Diet Plan Button end

profile_button = tk.Button(root, text="SEE PROFILE",
                           command=display_profile, width=30, height=1, background='white')
profile_button.grid(row=0, column=0, pady=60, padx=10)

# Create select_exercise_optionmenudown menu
select_exercise_optionmenu = tk.OptionMenu(root, clicked, *options,)
select_exercise_optionmenu.configure(
    width=25, height=1, fg='black', bg='white')
select_exercise_optionmenu.grid(row=1, column=0, pady=60, padx=10)
select_exercise_optionmenu['menu'].config(
    fg='black', bg='white', activebackground='black', activeforeground='white')


browse_button = tk.Button(root, text="SELECT VIDEO",
                          command=guiInstance.browseFiles, width=30, height=1, background='white')
browse_button.grid(row=2, column=0, pady=60, padx=10)


process_button = tk.Button(
    root, text="PROCESS", command=guiInstance.process_function, width=30, height=1, background='white')
process_button.grid(row=3, column=0, pady=60, padx=10)


# capture video with opencv
# cap = cv.VideoCapture('shoulder_press.mp4')
# width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

imageFrame = tk.Frame(root, width=600, height=600,bg='white')
imageFrame.grid(row=0, column=1, rowspan=5, padx=50, pady=70)
# imageFrame.grid_propagate(0)


# cap = cv.VideoCapture(0)


def show_frame():
    
    _, frame = cap.read()
    # frame = cv.flip(frame, 1)
    if not _:
        print("Can't receive frame (stream end?). Exiting ...")
        return
                   
    cv2image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    img = img.resize((width, height), Image.NEAREST)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)


# Slider window (slider controls stage position)
# sliderFrame = tk.Frame(root, width=900, height=100)
# sliderFrame.grid(row=0, column=0,columnspan=1,rowspan=4)
# show_frame()
# video end


# hover effect start
def on_enter(e):
    e.widget['background'] = 'black'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = 'white'
    e.widget['foreground'] = 'black'


profile_button.bind("<Enter>", on_enter)
profile_button.bind("<Leave>", on_leave)

select_exercise_optionmenu.bind("<Enter>", on_enter)
select_exercise_optionmenu.bind("<Leave>", on_leave)

browse_button.bind("<Enter>", on_enter)
browse_button.bind("<Leave>", on_leave)

process_button.bind("<Enter>", on_enter)
process_button.bind("<Leave>", on_leave)

# diet_plan_button.bind("<Enter>", on_enter)
# diet_plan_button.bind("<Leave>", on_leave)

# hover effect end

def destoy_all_side_frames():
    dp.destroy_display_profile_frame()
    if label_frame != '':
        label_frame.destroy()
root.mainloop()


# =========================================================================

# # import required modules
# import os
# import pyautogui

# # prompts message on screen and gets the command
# # value in val variable
# # value = pyautogui.prompt("Enter Shell Command")
# # value = "py main.py --mode evaluate --video sample_bicep_curl.mp4"
# def click():
#     value = "dir"

#     # executes the command and returns
#     # the output in stream variable
#     stream = os.popen(value)

#     # reads the output from stream variable
#     out = stream.read()
#     print(out)

# # pyautogui.alert(out)
