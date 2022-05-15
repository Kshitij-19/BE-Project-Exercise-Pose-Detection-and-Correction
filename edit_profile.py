import User
import tkinter
import tkinter as tk
# from tkinter import filedialog
import tkinter as tk
import os
from tkinter import filedialog
from tkinter import ttk
from matplotlib import path
import pyrebase
import io
from tkinter import *
import os
import subprocess
from PIL import Image, ImageTk


def edit_profile(firebase, auth, db, storage,email,password):
    
    
    edit_profile_window = tkinter.Tk()
    edit_profile_window.config(bg='white')

    
    user = auth.sign_in_with_email_and_password(
        email=email, password=password)
    user_info = auth.get_account_info(user['idToken'])
    key = user_info['users'][0]['localId']

    name_label = tk.Label(
        edit_profile_window, text='Name:\t\t', bg='white')
    name_label.grid(column=0, sticky='w', padx=10, pady=10)
    
    email_label = tk.Label(
        edit_profile_window, text='Email:\t\t', bg='white')
    email_label.grid(column=0, sticky='w', padx=10, pady=10)

    mobno_label = tk.Label(
        edit_profile_window, text='Mob No:\t\t', bg='white')
    mobno_label.grid(column=0, sticky='w', padx=10, pady=10)

    name_var = tk.StringVar()
    email_var = tk.StringVar()
    mobno_var = tk.StringVar()

    name_entry = tk.Entry(edit_profile_window,textvariable=name_var)
    name_entry.grid(row=0, column=1, padx=8)
    email_entry = tk.Entry(edit_profile_window,textvariable=email_var)
    email_entry.grid(row=1, column=1, padx=8)
    mobno_entry = tk.Entry(edit_profile_window,textvariable=mobno_var)
    mobno_entry.grid(row=2, column=1, padx=8)

    path_to_profile_picture = ''


        
    def save_function():
        name = name_entry.get()
        print(name)
        email = email_entry.get()
        print(email)
        mobno = mobno_entry.get()
        print(mobno)

        user_dict = {
            "name": name,
            "email": email,
            "mobno": mobno,
            "password": password
        }
        key = auth.get_account_info(user['idToken'])['users'][0]['localId']

        db.child("users").child(key).set(user_dict)
        
        edit_profile_window.destroy()
        
    save_button  = ttk.Button(
    edit_profile_window,
    text='Save',
    command=save_function
    )
    save_button.grid(row=5,column=0,columnspan=2,pady=8)

    edit_profile_window.mainloop()

# edit_profile(firebase, auth, db, storage)