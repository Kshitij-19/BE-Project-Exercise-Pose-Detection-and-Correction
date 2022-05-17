from logging import PlaceHolder
import time
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import font
# from tkinter import filedialog
from turtle import width
import User
# import pyautogui
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
import threading
from PIL import ImageTk, Image

if len(sys.argv) == 3:
    global email
    global password
    email = sys.argv[1]
    password = sys.argv[2]


width = ''
height = ''
cap = ''
root = tk.Tk()
root.title('EXERCISE POSE DETECTION AND CORRECTION')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = -10, 0
root.geometry('%dx%d+%d+%d' % (w, h, x, y))


heading_label = tk.Label(root,
                            text='EXERCISE POSE DETECTION AND CORRECTION',
                            font=('MS Serif', 25, 'bold'),
                            foreground='#FFED41',
                            background='#36AFEC',
                            justify=CENTER)

#heading_label.place(relx = 0.5, rely = 0.05, anchor = 'center')
heading_label.grid(columnspan=4,ipadx=500)
#heading_label.place(anchor=CENTER)
#heading_label.place(relx = 0.5, rely = 0.05, anchor = 'center')

root.config(background='#66CCFF') #41EDFF
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
        # pb.grid(column=0, row=5,padx=10, pady=30)
        # pb.start(20)

        output = '''Starting OpenPose demo...
Configuring OpenPose...
Starting thread(s)...
---------------------------------- WARNING ----------------------------------
We have introduced an additional boost in accuracy in the CUDA version of about 0.2% with respect to the CPU/OpenCL versions. We will not port this to CPU given the considerable slow down in speed it would add to it. Nevertheless, this accuracy boost is almost insignificant so the CPU/OpenCL versions can be safely used.
-------------------------------- END WARNING --------------------------------
OpenPose demo successfully finished. Total time: 218.085159 seconds.
processing video file...
Exercise arm detected as: right.
Upper arm and torso angle range: 12.91638852310736
Upper arm and forearm minimum angle: 28.69665215047628
Exercise performed correctly!
Exercise performed correctly! Weight was lifted fully up, and upper arm did not move significantly.'''

        # process = subprocess.Popen(
        #     command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        # out, code = process.communicate()

        out = subprocess.check_output(command,shell=True)

        global pb
        pb.destroy()

        output = out.decode("utf-8")
        #output = output[output.find('OpenPose demo successfully'):]
        ind = output.find("Feedback")
        feedback2 =  output[output.find("Feedback")+8:]
        feedback3 = output[output.find('OpenPose demo successfully'):ind]

        # opData = feedback2.splitlines()
        # n=len(opData)
        # feedback ="FeedBack:- \n\n\t"
        # for i in range(n):
        #     feedback+=opData[i] + '\n\t'

        opData = feedback3.splitlines()
        n=len(opData)
        feedback ="FeedBack:- \n\n\t" + feedback2
        opDetails = "Details:- \n\n\t"
        for i in range(2,n):
            opDetails+=opData[i] + '\n\t'
        res = feedback + " \n\n\n\n" + opDetails
        print(res)
        
        #if(output.find('Exercise performed')==-1):
        #    feedback='Exercise could be Improved' + output
        #feedback = output.find('Exercise performed')


        global lmain
        # Capture video frames
        lmain = tk.Label(imageFrame, width=600, height=700, bg='#66CCFF')
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
        label_frame = tk.Frame(root, width=500, height=700, bg='#66CCFF')
        label_frame.grid(row=2, column=2, rowspan=5, padx=50, pady=70)
        output_text = tk.Text(label_frame, border=0,fg='red',bg='#66CCFF',font=('MS Serif', 10, 'bold'),pady=5)
        output_text.insert(tk.END, res)
        output_text.pack()
        # output_text2 = tk.Text(label_frame, border=0,fg='red',bg='#66CCFF')
        # output_text2.insert(tk.END, feedback)
        # output_text2.pack()
        label_frame.grid_propagate(0)


guiInstance = gui()


def on_click_process():
    global pb
    pb = ttk.Progressbar(
        imageFrame,
        orient='horizontal',
        mode='indeterminate',
        length=500
    )
    # place the progressbar
    pb.grid(column=0, row=5, padx=10, pady=30)
    pb.start(20)
    # time.sleep(7)
    threading.Thread(target=guiInstance.process_function).start()

def on_click_exercises():
    root.destroy()
    subprocess.call(f'py exercise_details.py {email} {password} '.split())

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
    ep.edit_profile(firebase, auth, db, storage, email, password)
# edit profile end

# edit profile start


def display_profile():
    destoy_all_side_frames()
    dp.display_profile(firebase, auth, db, storage, email, password, root)
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

# photo = PhotoImage(file = r"Gold's_Gym_logo.png")
# img = ImageTk.PhotoImage(Image.open("Gold's_Gym_logo.png"))
img = Image.open("gym_logo2.png")
#img = img.resize((100, 100), Image.ANTIALIAS)
factor = 130/img.height
img = img.resize((int(img.width*factor), int(img.height*factor)), Image.ANTIALIAS)
image = ImageTk.PhotoImage( image=img)
label6 = Label( image=image)
label6.grid(row=1, column=1, pady=30, padx=10)

profile_button = tk.Button(root, text="SEE PROFILE",
                           command=display_profile, width=30, height=1, background='#0080FF')
profile_button.grid(row=2, column=0, pady=(0,45), padx=10)

# Create select_exercise_optionmenudown menu
select_exercise_optionmenu = tk.OptionMenu(root, clicked, *options,)
select_exercise_optionmenu.configure(
    width=25, height=1, fg='black', bg='#0080FF')
select_exercise_optionmenu.grid(row=3, column=0, pady=45, padx=10)
select_exercise_optionmenu['menu'].config(
    fg='white', bg='black', activebackground='black', activeforeground='#0080FF')


browse_button = tk.Button(root, text="SELECT VIDEO",
                          command=guiInstance.browseFiles, width=30, height=1, background='#0080FF')
browse_button.grid(row=4, column=0, pady=45, padx=10)


process_button = tk.Button(
    root, text="PROCESS", command=on_click_process, width=30, height=1, background='#0080FF')
process_button.grid(row=5, column=0, pady=45, padx=10)

exercises_button = tk.Button(
    root, text="EXERCISES", command=on_click_exercises, width=30, height=1, background='#0080FF')
exercises_button.grid(row=6, column=0, pady=45, padx=10)


# capture video with opencv
# cap = cv.VideoCapture('shoulder_press.mp4')
# width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

imageFrame = tk.Frame(root, width=600, height=500, bg='#66CCFF')#41EDFF
imageFrame.grid(row=2, column=1, rowspan=5, padx=50, pady=0)
#imageFrame.place(x=600,y=250)
#imageFrame.grid_propagate(0)


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
    e.widget['background'] = '#0080FF'
    e.widget['foreground'] = 'black'


profile_button.bind("<Enter>", on_enter)
profile_button.bind("<Leave>", on_leave)

select_exercise_optionmenu.bind("<Enter>", on_enter)
select_exercise_optionmenu.bind("<Leave>", on_leave)

browse_button.bind("<Enter>", on_enter)
browse_button.bind("<Leave>", on_leave)

process_button.bind("<Enter>", on_enter)
process_button.bind("<Leave>", on_leave)

exercises_button.bind("<Enter>", on_enter)
exercises_button.bind("<Leave>", on_leave)

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
