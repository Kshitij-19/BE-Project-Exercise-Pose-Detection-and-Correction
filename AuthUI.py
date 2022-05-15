#import modules

# from asyncio import subprocess
from tkinter import *
import os
#import User
import json
import subprocess

# MY CODE

from ast import Try
from tkinter import messagebox
import pyrebase

email = "NULL"
password = "NULL"

firebaseConfig = {
    "databaseURL": "https://pose-corrector-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "apiKey": "AIzaSyAa0qidybVUqV_KQA4Bs-R4BflC8qnwWGU",
    "authDomain": "pose-corrector.firebaseapp.com",
    "projectId": "pose-corrector",
    "storageBucket": "pose-corrector.appspot.com",
    "messagingSenderId": "513768245537",
    "appId": "1:513768245537:web:86db905f39d9334cfe9660",
    "measurementId": "G-JGLL6NL6EZ"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def signup():
    email = input("Enter Email:")
    password = input("Enter Password:")
    try:
        user = auth.create_user_with_email_and_password(email,password)
        print(user)
    except:
        print("Email Already Exists")

def signin():
    email = input("Enter Email:")
    password = input("Enter Password:")
    try:
        user = auth.sign_in_with_email_and_password(email,password)
        print(user)
        print("sign in successfull")
    except:
        print("invalid email or password")

# Designing window for registration
def register():
    global register_screen
    register_screen = Toplevel(main_screen)

    register_screen.title("Register")
    register_screen.config(padx=120,pady=16,bg='white')
    # register_screen.geometry("500x500")
 
    global username
    global password
    global name
    global phoneno
    global weight
    global height
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    name = StringVar()
    phoneno = StringVar()
    weight = StringVar()
    height = StringVar()
 
    Label(register_screen, text="Please enter details below",  bg="blue", width="30", height="2", font=("Calibri", 13)).pack()
    Label(register_screen, text="",bg='white').pack()
    username_lable = Label(register_screen, text="Email * ",bg='white')
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    name_lable = Label(register_screen, text="Name * ",bg='white')
    name_lable.pack()
    name_entry = Entry(register_screen, textvariable=name)
    name_entry.pack()
    phone_lable = Label(register_screen, text="Phoneno * ",bg='white')
    phone_lable.pack()
    phoneno_entry = Entry(register_screen, textvariable=phoneno)
    phoneno_entry.pack()

    weight_label = Label(register_screen, text="Weight(in kg) * ",bg='white')
    weight_label.pack()
    weight_entry = Entry(register_screen, textvariable=weight)
    weight_entry.pack()

    height_label = Label(register_screen, text="Height(in cm) * ",bg='white')
    height_label.pack()
    height_entry = Entry(register_screen, textvariable=height)
    height_entry.pack()

    password_lable = Label(register_screen, text="Password * ",bg='white')
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="",bg='white').pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user,pady=8).pack()


# Designing window for login 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    # login_screen = Tk()
    login_screen.config(bg='white')
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login",bg='white').pack()
    Label(login_screen, text="",bg='white').pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Email * ",bg='white').pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="",bg='white').pack()
    Label(login_screen, text="Password * ",bg='white').pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="",bg='white').pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
    # main_screen.destroy()
# Implementing event on register button

class User(object):
    def __init__(self,email,password,name,mobno,weight,height):
        self.email = email
        self.password = password
        self.name = name
        self.mobno = mobno
        self.weight = weight
        self.height= height

    # method to create user from dictionary
    @staticmethod
    def from_dict(source):
        us = User(source['email'], source['password'], source['name'],source['mobno'],source['weight'],source['height'])
        return us
    def to_dict(self):
        dest = {
            'email':self.email,
            'password':self.password,
            'name' : self.name,
            'mobno' : self.mobno,
            'weight' : self.weight,
            'height' : self.height
        }
        return dest

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

def register_user():
 
    # username_info = username.get()
    # password_info = password.get()
 
    # file = open(username_info, "w")
    # file.write(username_info + "\n")
    # file.write(password_info)
    # file.close()
 
    # username_entry.delete(0, END)
    # password_entry.delete(0, END)
 
    # Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

    # My Implementation

    email = username.get()
    password_ = password.get()
    nname = name.get()
    mobno = phoneno.get()
    weight_ = weight.get()
    height_ = height.get()


    try:
        user = auth.create_user_with_email_and_password(email,password_)
        print(user)

        print("email verification start")
        auth.send_email_verification(user['idToken'])
        print("email verification end")
        db = firebase.database()
       # data = {"email": user['email'],"name":nname,"mobno":mobno,"password":password}
      #  db.child("users").child(user['idToken']).set(data)
        u = User(email , password_ , nname , mobno, weight_, height_)
        print(u.to_dict())
        db.child("users").child(user['localId']).set(u.to_dict())
        print("Data added to real time database ")
        # success_window = Tk()
        # Label(success_window, text="Registration Successfull", fg="green", font=("calibri", 11)).pack()
        # Label(success_window, text="Email verification link has\n been sent to your email account", fg="green", font=("calibri", 11)).pack()
        register_screen.destroy()
        messagebox.showinfo("Registration Successfull", "Email verification link has been sent to your email account")
        # success_window.mainloop()
    except Exception as e:

        print(e)
        print("Email Already Exists")
        Label(register_screen, text="Email Already Exists", fg="red", font=("calibri", 11),bg='white').pack()
 
# Implementing event on login button 
 
def login_verify_():

    # username1 = username_verify.get()
    # password1 = password_verify.get()
    # username_login_entry.delete(0, END)
    # password_login_entry.delete(0, END)
 
    # list_of_files = os.listdir()
    # if username1 in list_of_files:
    #     file1 = open(username1, "r")
    #     verify = file1.read().splitlines()
    #     if password1 in verify:
    #         process_login()
 
    #     else:
    #         password_not_recognised()
 
    # else:
    #     user_not_found()
 
    # MY IMPLEMENTATION
    global email
    global password
    email = username_verify.get()
    password = password_verify.get()
    
    try:
        user = auth.sign_in_with_email_and_password(email,password)
        # print(user)
        account_info = auth.get_account_info(user['idToken'])
        print(account_info)
        emailVerified = account_info.users[0].emailVerified
        if emailVerified:
            print("sign in successfull")
            process_login()
        else:
            print("email not verified")
    except Exception as e:
        print(e)
        user_not_found()

def login_verify():
    global email
    global password
    email = username_verify.get()
    password = password_verify.get()
    
    user = auth.sign_in_with_email_and_password(email,password)
    # print(user)
    account_info = auth.get_account_info(user['idToken'])
    print(account_info)
    emailVerified = account_info["users"][0]["emailVerified"]
    process_login(emailVerified)

# Designing popup for login success

def process_login(emailVerified):
    global login_success_screen

    login_success_screen = Toplevel(login_screen)
    if emailVerified:
        # login_success_screen.title("Success")
        # login_success_screen.geometry("150x100")
        # Label(login_success_screen, text="Login Success").pack()
        # print("email verified","Inside process login")
        # print(auth.current_user)
        global email
        global password
        print(email,password)
        main_screen.destroy()
        subprocess.call((f'py gui.py {email} {password}').split())
    else:

        login_success_screen.title("Unverifies Email")
        login_success_screen.geometry("150x100")
        Label(login_success_screen, text="Email is not verified",bg='white').pack()
    # Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ",bg='white').pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found",bg='white').pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups
def delete_login_success():
    login_success_screen.destroy()
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.config(bg='white')
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="",bg='white').pack()
    Button(text="Login", height="2", width="30", command = login,bg='white').pack()
    Label(text="",bg='white').pack()
    Button(text="Register", height="2", width="30", command=register,bg='white').pack()
 
    main_screen.mainloop()
 
 
main_account_screen()
