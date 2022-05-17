from threading import local
import tkinter as tk

import urllib
from logging import PlaceHolder
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
# from tkinter import filedialog
from turtle import width

from matplotlib.pyplot import prism
import User
import pyautogui
import cv2 as cv
import subprocess
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
import os
import pyrebase
from asyncio import subprocess
import io
from tkinter import *
import os
import subprocess
from PIL import Image, ImageTk
import urllib.request
from firebase import *
import sys
import edit_profile as ep

global_firebase  = ''
global_auth = ''
global_db = ''
global_storage = ''
global_email = ''
global_password  = ''
global_url = ''
path_to_profile_picture = ''
localID = ''
frame = ''

def edit_profile():
    ep.edit_profile(global_firebase, global_auth, global_db, global_storage,global_email,global_password)

def edit_dp():
    global path_to_profile_picture
    path_to_profile_picture = filedialog.askopenfilename(initialdir="./",
                                                            title="Select an image",
                                                            )
    filename = path_to_profile_picture.split('/')[-1]
    print(filename)
    # below line uploads image to storage
    download_token = global_storage.child(
        'profile_pictures/'+filename).put(path_to_profile_picture, localID)['downloadTokens']
        

    # storage.child('profile_pictures/goku_dp.jpg').put('goku.jpg',user["idToken"])

    # below lines get url from storage and write it to the file
    url = storage.child(
        "profile_pictures/"+filename).get_url(token=download_token)

    with open("dp_urls.txt", "r") as f:
        lines = f.readlines()
    with open("dp_urls.txt", "w") as f:
        for line in lines:
            if line.strip("\n").split(',')[0] != localID:
                f.write(line)
    
    f = open("dp_urls.txt","a")
    f.write(localID + ',' + url + '\n')
    f.close()
    print('done')

    

# display profile start
def display_profile(firebase, auth, db, storage,email,password,root):
    global frame
    frame = tk.Frame(root, width=600, height=700,bg='white')
    frame.grid(row=2, column=1, rowspan=7,columnspan=1, padx=50, pady=0)
    frame.grid_propagate(0)

    # global lmain
    # # Capture video frames
    # lmain = tk.Label(frame, width=700, height=700,bg='white')
    # # lmain.grid(row=0, column=0)
    # lmain.grid(row=5, column=0)
    
    global global_firebase
    global global_auth
    global global_db
    global global_storage
    global global_email
    global global_password

    global_firebase = firebase
    global_auth = auth
    global_db = db
    global_storage = storage
    global_email = email
    global_password = password

    # profile_window = tk.Tk()
    profile_window = frame
    profile_window.config(bg='#a3d3fe')

    user = auth.sign_in_with_email_and_password(
        email, password)
    user_info = auth.get_account_info(user['idToken'])
    global localID
    key = user_info['users'][0]['localId']
    localID = user_info['users'][0]['localId']

    # below line uploads image to storage
    # download_token = storage.child(
    #     'profile_pictures/goku_dp.jpg').put('goku.jpg', key)['downloadTokens']
        

    # storage.child('profile_pictures/goku_dp.jpg').put('goku.jpg',user["idToken"])

    # below lines get url from storage and write it to the file
    # url = storage.child(
    #     "profile_pictures/goku_dp.jpg").get_url(token=download_token)
    # f = open("dp_urls.txt","a")
    # f.write(key + ',' + url + '\n')
    # f.close()
    # print(url)
    
    f = open('dp_urls.txt')
    url_list = f.readlines()
    global global_url
    for url in url_list:
        if url.split(',')[0] == key:
            global_url = url.split(',')[1]
            break;
    else:
        global_url = 'https://pbs.twimg.com/media/BtFUrp6CEAEmsml.jpg'



    raw_data = urllib.request.urlopen(global_url).read()
    im = Image.open(io.BytesIO(raw_data))
    factor = 400/im.height
    # print(im.width,im.height,factor)
    im = im.resize((int(im.width*factor), int(im.height*factor)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(master=profile_window, image=im)
    label1 = Label(profile_window, image=image)
    label1.grid(row=1,column=1,columnspan=2,padx=10, pady=0)


    user = auth.sign_in_with_email_and_password(
        email=email, password=password)
    user_info = auth.get_account_info(user['idToken'])
    localID = user_info['users'][0]['localId']


    users = db.child('users').get()
    for user in users.each():
        # print(user.val()['email'])
        # print(type(user.val()))
        if user.key() == localID:
            name_label = tk.Label(
                profile_window, text='Name:\t\t' + user.val()['name'], bg='#a3d3fe')
            name_label.grid(row=2,column=1,sticky='w', padx=10, pady=4,columnspan=2)
            email_label = tk.Label(
                profile_window, text='Email:\t\t' + user.val()['email'], bg='#a3d3fe')
            email_label.grid(row=3,column=1,sticky='w', padx=10, pady=4,columnspan=2)
            mobno_label = tk.Label(
                profile_window, text='Mob No:\t\t' + user.val()['mobno'], bg='#a3d3fe')
            mobno_label.grid(row=4,column=1,sticky='w', padx=10, pady=4,columnspan=2)
            weight_label = tk.Label(
                profile_window, text='Weight (kg):\t' + user.val()['weight'], bg='#a3d3fe')
            weight_label.grid(row=5,column=1,sticky='w', padx=10, pady=4,columnspan=2)
            height_label = tk.Label(
                profile_window, text='Height (cm):\t' + user.val()['height'], bg='#a3d3fe')
            height_label.grid(row=6,column=1,sticky='w', padx=10, pady=4,columnspan=2)
            break

    edit_button = ttk.Button(profile_window, text='Edit', command=edit_profile)
    edit_button.grid(row=7,column=1,pady=8)

    edit_dp_button = ttk.Button(profile_window, text='Edit DP', command=edit_dp)
    edit_dp_button.grid(row=7,column=2,pady=8)

    profile_window.mainloop()
# display profile end

def destroy_display_profile_frame():
    if frame != '':
        frame.destroy()
