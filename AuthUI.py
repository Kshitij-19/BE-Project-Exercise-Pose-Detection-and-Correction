#import modules

from asyncio import subprocess
from logging import root
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk, ImageSequence
import time
import os
#import User
import json
import subprocess
import tkinter

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



splash_win= Tk()

# # #Set the title of the window
splash_win.title("Splash Screen Example")

# # #Define the size of the window or frame
splash_win.geometry("1360x780")
splash_win.resizable(False,False)
screen_width = splash_win.winfo_screenwidth()
screen_height = splash_win.winfo_screenheight()

x_cordinate = int((screen_width/2) - (1360/2))
y_cordinate = int((screen_height/2) - (780/2))  

splash_win.geometry("{}x{}+{}+{}".format(1360, 780, x_cordinate, y_cordinate))



#Remove border of the splash Window

#splash_win.overrideredirect(True)

#Define the label of the window

path = "splash2.png"

    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img2 = (Image.open(path))

resize_image = img2.resize((1360, 780),Image.ANTIALIAS)
img = ImageTk.PhotoImage(resize_image)


#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(splash_win, image = img).place(x=0,y=0,relwidth=1,relheight=1)





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

def play():

    global img1

    img1 = Image.open("gym2.gif")

    lbl1 = Label(register_screen)
    lbl1.place(x=700,y=150)


    for img1 in ImageSequence.Iterator(img1):
        img1 = img1.resize((500,500))
        img1 = ImageTk.PhotoImage(img1)
        lbl1.config(image=img1)
        register_screen.update()
        time.sleep(0.075)

    register_screen.after(0,play)
    

def register(e):
    global register_screen
    register_screen = Toplevel(main_screen)



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

    main_screen.withdraw()

    
    register_screen.title("Register")
    register_screen.config(bg='#a3d3fe')
    #register_screen.config(padx=120,pady=16,bg='white')
    # register_screen.geometry("500x500")

    

    register_screen.geometry("1360x780")
    register_screen.resizable(False,False)


    screen_width = register_screen.winfo_screenwidth()
    screen_height = register_screen.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (1360/2))
    y_cordinate = int((screen_height/2) - (780/2))

    register_screen.geometry("{}x{}+{}+{}".format(1360, 780, x_cordinate, y_cordinate))


    # img = Image.open("gym.gif")

    # lbl1 = Label(register_screen)
    # lbl1.place(x=0,y=0)

    # for img in ImageSequence.Iterator(img):
    #     img = ImageTk.PhotoImage(img)
    #     lbl1.config(image=img)
    #     register_screen.update()
    
    register_screen.after(0,play)




 
    # Label(register_screen, text="Please enter details below",  bg="blue", width="30", height="2", font=("Calibri", 13)).pack()
    # Label(register_screen, text="",bg='white').pack()
    # username_lable = Label(register_screen, text="Email * ",bg='white')
    # username_lable.pack()
    # username_entry = Entry(register_screen, textvariable=username)
    # username_entry.pack()
    # name_lable = Label(register_screen, text="Name * ",bg='white')
    # name_lable.pack()
    # name_entry = Entry(register_screen, textvariable=name)
    # name_entry.pack()
    # phone_lable = Label(register_screen, text="Phoneno * ",bg='white')
    # phone_lable.pack()
    # phoneno_entry = Entry(register_screen, textvariable=phoneno)
    # phoneno_entry.pack()

    # weight_label = Label(register_screen, text="Weight(in kg) * ",bg='white')
    # weight_label.pack()
    # weight_entry = Entry(register_screen, textvariable=weight)
    # weight_entry.pack()

    # height_label = Label(register_screen, text="Height(in cm) * ",bg='white')
    # height_label.pack()
    # height_entry = Entry(register_screen, textvariable=height)
    # height_entry.pack()

    # password_lable = Label(register_screen, text="Password * ",bg='white')
    # password_lable.pack()
    # password_entry = Entry(register_screen, textvariable=password, show='*')
    # password_entry.pack()
    # Label(register_screen, text="",bg='white').pack()
    # Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user,pady=8).pack()



    def my_fun(*args):
        my_w_child = Toplevel(login)


    lbl1 = Label(register_screen,text="Email",font=("times new roman",13),fg="#686869",bg='#a3d3fe').place(x=210,y=150)
    username = Entry(register_screen,font=("Goudy old style",13), textvariable=username).place(x=210,y=180)

    lbl1 = Label(register_screen,text="Name",font=("times new roman",13),fg="#686869",bg='#a3d3fe').place(x=210,y=220)
    name = Entry(register_screen,font=("Goudy old style",13), textvariable=username).place(x=210,y=250)

    lbl1 = Label(register_screen,text="Phone No. ",font=("times new roman",13),fg="#686869",bg='#a3d3fe').place(x=210,y=290)
    phoneno = Entry(register_screen,font=("Goudy old style",13), textvariable=username).place(x=210,y=320)

    lbl1 = Label(register_screen,text="Weight",font=("times new roman",13),fg="#686869",bg='#a3d3fe').place(x=210,y=360)
    weight = Entry(register_screen,font=("Goudy old style",13), textvariable=username).place(x=210,y=390)

    lbl1 = Label(register_screen,text="Height",font=("times new roman",13),fg="#686869",bg='#a3d3fe').place(x=210,y=430)
    height = Entry(register_screen,font=("Goudy old style",13), textvariable=username).place(x=210,y=460)


    lbl2 = Label(register_screen,text="Password",font=("times new roman",13),fg="#686869",bg='#a3d3fe').place(x=210,y=500)
    password = Entry(register_screen,font=("Goudy old style",13), textvariable=password,show= '*').place(x=210,y=530)


    Button(register_screen,text="Register", height="2", width="25",command = register_user,bg="#0925DB",fg='white').place(x=210,y=600)

    lbl3 = Label(register_screen,text="Already Have an Account, ",font=("Goudy old style",10,"bold"),fg="#686869",bg="#a3d3fe").place(x=210,y=655)
    lbl4 = Label(register_screen,text="Click Here",font=("Goudy old style",10,"bold","underline"),fg="#0925DB",bg="#a3d3fe")
    lbl4.place(x=353,y=655)
    
    lbl4.bind("<Button-1>",login)
    
    




    # register_screen.mainloop()


def quit_file():
    root.quit()


# # Designing window for login 
def login(e):
    global login_screen
    login_screen = Toplevel(main_screen)
    register_screen.withdraw()
    # login_screen = Tk()
    #login_screen.config(bg='white')
    login_screen.title("Login")
    login_screen.geometry("1360x780")

    login_screen.resizable(False,False)

    screen_width = login_screen.winfo_screenwidth()
    screen_height = login_screen.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (1360/2))
    y_cordinate = int((screen_height/2) - (780/2))

    login_screen.geometry("{}x{}+{}+{}".format(1360, 780, x_cordinate, y_cordinate))



    # Label(login_screen, text="Please enter details below to login").pack()
    # Label(login_screen, text="",bg='white').pack()

    path = "login_background.png"

    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    img = ImageTk.PhotoImage(Image.open(path))

    #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    panel = Label(login_screen, image = img).place(x=0,y=0,relwidth=1,relheight=1)


    
 

    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    # Label(login_screen, text="Email * ",bg='white').pack()
    # username_login_entry = Entry(login_screen, textvariable=username_verify)
    # username_login_entry.pack()
    # Label(login_screen, text="",bg='white').pack()
    # Label(login_screen, text="Password * ",bg='white').pack()
    # password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    # password_login_entry.pack()
    # Label(login_screen, text="",bg='white').pack()
    # Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()


    def my_fun(*args):
        my_w_child = Toplevel(register_screen)


    Frame_login = Frame(login_screen,bg="white")
    Frame_login.place(x=740,y=230,height=300,width=250)
    Label(Frame_login,text="Please Login to Continue",bg='white', font=("bold", 13)).place(x=30,y=20)

    lbl1 = Label(Frame_login,text="Email",font=("times new roman",13),fg="#686869",bg="white").place(x=15,y=70)
    username_login_entry = Entry(Frame_login,font=("Goudy old style",13), textvariable=username_verify).place(x=15,y=100)

    lbl2 = Label(Frame_login,text="Password",font=("times new roman",13),fg="#686869",bg="white").place(x=15,y=140)
    username_login_entry = Entry(Frame_login,font=("Goudy old style",13), textvariable=password_verify,show= '*').place(x=15,y=170)


    Button(Frame_login,text="Login", height="2", width="25",command = login_verify,bg="#0925DB",fg='white').place(x=15,y=225)
    #Button(Frame_login,text="Register", height="2", width="30", command=register,bg="#0925DB",fg='white').place(x=15,y=125)
    
    lbl3 = Label(Frame_login,text="Don't Have an Account, ",font=("Goudy old style",10,"bold"),fg="#686869",bg="white").place(x=30,y=280)
    lbl4 = Label(Frame_login,text="Click Here",font=("Goudy old style",10,"bold","underline"),fg="#0925DB",bg="white")
    lbl4.place(x=160,y=280)
    
    lbl4.bind("<Button-1>",register)
    

    login_screen.mainloop()


    

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
        main_screen.deiconify()
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

    # login_success_screen = Toplevel(login_screen)
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

        # login_success_screen.title("Unverifies Email")
        # login_success_screen.geometry("150x100")
        # Label(login_success_screen, text="Email is not verified",bg='white').pack()
        messagebox.showerror("Unverified Email", "Email is not verified")


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

    splash_win.destroy()
    

    main_screen = Tk()


    #main_screen.config(bg='white')
    #main_screen.geometry("1200x1050")

    path = "login_background.png"

    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    img = ImageTk.PhotoImage(Image.open(path))

    #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    panel = Label(main_screen, image = img).place(x=0,y=0,relwidth=1,relheight=1)

    #The Pack geometry manager packs widgets in rows or columns.
    #panel.pack(side = "bottom", fill = "both", expand = "yes")

    
    #register_screen.config(padx=120,pady=16,bg='white')
    main_screen.geometry("1360x780")





    # width= main_screen.winfo_screenwidth()
    # heightt= main_screen.winfo_screenheight()
    #setting tkinter window size
    #main_screen.geometry("%dx%d" % (width, heightt))

    main_screen.resizable(False,False)





    main_screen.title("Account Login")
    screen_width = main_screen.winfo_screenwidth()
    screen_height = main_screen.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (1360/2))
    y_cordinate = int((screen_height/2) - (780/2))

    main_screen.geometry("{}x{}+{}+{}".format(1360, 780, x_cordinate, y_cordinate))




    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    #Label(login_screen, text="Email * ",bg='white').pack()
    #username_login_entry = Entry(login_screen, textvariable=username_verify)
    #username_login_entry.pack()

    def my_fun(*args):
        my_w_child = Toplevel(register_screen)


    Frame_login = Frame(main_screen,bg="white")
    Frame_login.place(x=740,y=230,height=300,width=250)
    Label(Frame_login,text="Please Login to Continue",bg='white', font=("bold", 13)).place(x=30,y=20)

    lbl1 = Label(Frame_login,text="Email",font=("times new roman",13),fg="#686869",bg="white").place(x=15,y=70)
    username_login_entry = Entry(Frame_login,font=("Goudy old style",13), textvariable=username_verify).place(x=15,y=100)

    lbl2 = Label(Frame_login,text="Password",font=("times new roman",13),fg="#686869",bg="white").place(x=15,y=140)
    username_login_entry = Entry(Frame_login,font=("Goudy old style",13), textvariable=password_verify,show= '*').place(x=15,y=170)


    Button(Frame_login,text="Login", height="2", width="25",command = login_verify,bg="#0925DB",fg='white').place(x=15,y=225)
    #Button(Frame_login,text="Register", height="2", width="30", command=register,bg="#0925DB",fg='white').place(x=15,y=125)
    
    lbl3 = Label(Frame_login,text="Don't Have an Account, ",font=("Goudy old style",10,"bold"),fg="#686869",bg="white").place(x=30,y=280)
    lbl4 = Label(Frame_login,text="Click Here",font=("Goudy old style",10,"bold","underline"),fg="#0925DB",bg="white")
    lbl4.place(x=160,y=280)
    
    lbl4.bind("<Button-1>",register)
    main_screen.mainloop()
    


    

splash_win.after(5000,main_account_screen)
mainloop()


# main_account_screen()
