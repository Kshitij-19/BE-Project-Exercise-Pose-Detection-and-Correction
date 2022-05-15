import subprocess
import sys
import threading
import tkinter as tk
from tkinter import ttk
from turtle import bgcolor
import cv2 as cv
import pyrebase
from PIL import Image, ImageTk

if len(sys.argv) == 3:
    global email
    global password
    email = sys.argv[1]
    password = sys.argv[2]


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
# cap=''



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        

        self.shared_data = {'Balance': tk.IntVar()}

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MenuPage")

    def show_frame(self, page_name, name="back"):
        '''Show a frame for the given page name'''

        frame = self.frames[page_name]
        frame.change_exercise_details(name)
        print("Hello this is show frame", name)
        frame.tkraise()


def show_frame():
    _, frame = cap.read()
    # frame = cv.flip(frame, 1)
    if not _:

        print("Can't receive frame (stream end?). Exiting ...")
        return
    cv2image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)


class StartPage(tk.Frame):

    def __init__(self, parent, controller, bg='#66CCFF', name="u"):
        tk.Frame.__init__(self, parent, bg='#66CCFF',height=500,width=500)
        self.controller = controller

        self.controller.title('EXERCISE DETAILS')
        self.controller.state('normal')
        #self.controller.iconphoto(False,tk.PhotoImage(file='C:/Users/urban boutique/Documents/atm tutorial/atm.png'))
        print('this is class', name)

    def change_exercise_details(self, exercise_name):
        Exercise_label = tk.Label(self,
                                  text=exercise_name,
                                  font=('MS Serif', 30, 'bold'),
                                  fg='#FFED41',bg='#66CCFF')
        Exercise_label.pack()
        firebase = pyrebase.initialize_app(firebaseConfig)

        db = firebase.database()
        try:
            d = db.child('exercise').child(exercise_name).get()
            for p in d.each():

                print(p.key(), p.val())
                exercise_no = tk.Label(self,
                                       text=p.key(),
                                       font=('orbitron', 15),
                                       fg='black',bg='#66CCFF')
                exercise_no.pack(pady=15)
                z = 0
                imageFrame = tk.Frame(self, width=600, height=500)
                #imageFrame.pack()
                lmain = tk.Label(imageFrame)
                # lmain.grid(row=0, column=0)
                #lmain.pack()
                cap = cv.VideoCapture('Male-Barbell-BicepCurl-Front.mp4')

                def show_frame():
                    _, frame = cap.read()
                    # frame = cv.flip(frame, 1)
                    if not _:

                        print("Can't receive frame (stream end?). Exiting ...")
                        return
                    cv2image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
                    img = Image.fromarray(cv2image)
                    imgtk = ImageTk.PhotoImage(image=img)
                    lmain.imgtk = imgtk
                    lmain.configure(image=imgtk)
                    lmain.after(300, show_frame)

                # filename = 'Male-Barbell-BicepCurl-Front.gif'
                # frame2 = ImageTk.PhotoImage(file=filename, format="gif -index 3")
                # lmain.imgtk = frame2
                # lmain.configure(image=frame2)

                show_frame()

                # def play_repeat():
                #     for i in range(5):
                #         global cap
                #         cap = cv.VideoCapture('Male-Barbell-BicepCurl-Front.mp4')

                #         def show_frame():
                #                 _, frame = cap.read()
                #                 # frame = cv.flip(frame, 1)
                #                 if not _:

                #                     print("Can't receive frame (stream end?). Exiting ...")
                #                     return
                #                 cv2image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
                #                 img = Image.fromarray(cv2image)
                #                 imgtk = ImageTk.PhotoImage(image=img)
                #                 lmain.imgtk = imgtk
                #                 lmain.configure(image=imgtk)
                #                 lmain.after(10, show_frame)

                #         show_frame()

                # play_repeat()

                button_frame = tk.Frame(self,bg='#66CCFF')
                button_frame.pack(fill='both', expand=True)
                for c, v in p.val().items():
                    exercise_step = tk.Label(button_frame,
                                             text=c,
                                             font=12,
                                             fg='#2A2084',bg='#66CCFF')
                    exercise_step.grid(row=z, column=0, padx=10)
                    exercise_det = tk.Label(button_frame,
                                            text=v,
                                            font=12,
                                            fg='#2A2084',bg='#66CCFF')#FFED41
                    exercise_det.grid(row=z, column=1, sticky='w')
                    z = z+1
        except Exception as e:
            print(e)

        def exit():
            for widget in self.winfo_children():
                widget.destroy()
            self.controller.show_frame('MenuPage')

        exit_button = ttk.Button(self,
                                 text='Back',
                                 command=exit,
                                 )
        exit_button.pack(anchor='center',pady=16)

        print("Hello World ", exercise_name)


class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#66CCFF',height=500,width=500)
        self.controller = controller
        title_frame = tk.Frame(self)
        title_frame.pack()
        heading_label = tk.Label(self,
                                 text='Exercise Details',
                                 font=('MS Serif', 25, 'bold'),
                                 foreground='#FFED41',
                                 background='#36AFEC')
        heading_label.pack(pady=25)


        selection_label = tk.Label(self,
                                   text='Please make a selection',
                                   font=('orbitron', 13),
                                   fg='#66CCFF',
                                   bg='#66CCFF',
                                   anchor='w')
        selection_label.pack(fill='x')

        button_frame = tk.Frame(self, bg='#66CCFF')
        button_frame.pack( expand=True,anchor='center',padx=260)

        def withdraw(exercise_name):
            controller.show_frame('StartPage', exercise_name)

        withdraw_button = tk.Button(button_frame,
                                    text='Biceps', height=1,width=10, font=('MS Serif', 10, 'bold'), bg='#0080FF',foreground='#FFED41',
                                    command=lambda: withdraw('Biceps'),
                                    )
        withdraw_button.grid(padx=0,row=0, column=0, pady=0)
        leg_button = tk.Button(button_frame,
                               text='legs', height=1,width=10, font=('MS Serif', 10, 'bold'), bg='#0080FF',foreground='#FFED41',
                               command=lambda: withdraw('legs'),
                               )
        leg_button.grid(padx=8,row=0, column=1, pady=5)

        def deposit():
            controller.show_frame('DepositPage')

        deposit_button = tk.Button(button_frame,
                                   text='Shoulder', height=1,width=10, font=('MS Serif', 10, 'bold'), bg='#0080FF',foreground='#FFED41',
                                   command=lambda: withdraw('Shoulder'))
        deposit_button.grid(padx=8,row=1, column=0, pady=5)
        triceps_button =tk.Button(button_frame,
                                   text='Triceps', height=1,width=10, font=('MS Serif', 10, 'bold'), bg='#0080FF',foreground='#FFED41',
                                   command=lambda: withdraw('Triceps'),
                                   )
        triceps_button.grid(padx=8,row=2, column=1, pady=5)

        def balance():
            controller.show_frame('BalancePage')

        balance_button =tk.Button(button_frame,
                                   text='Chest', height=1,width=10, font=('MS Serif', 10, 'bold'), bg='#0080FF',foreground='#FFED41',
                                   command=lambda: withdraw('Chest')
                                   )
        balance_button.grid(padx=8,row=2, column=0, pady=5)
        back_button =tk.Button(button_frame,
                                text='Back', height=1,width=10, font=('MS Serif', 10, 'bold'), bg='#0080FF',foreground='#FFED41',
                                command=lambda: withdraw('Back'),
                                )
        back_button.grid(padx=8,row=1, column=1, pady=5)


            # controller.show_frame('StartPage')

        def exit():
            controller.destroy()
            subprocess.call(f'py gui.py {email} {password}'.split())


        exit_button =tk.Button(button_frame,
                                text='Exit', height=1,width=10, font=('MS Serif', 10, 'bold'), bg='#0080FF',foreground='#FFED41',
                                command=exit,
                                )
        exit_button.grid(padx=8,row=3, column=0,columnspan=2, pady=5,)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
        ttk.Style().configure("TButton", padding=6, relief="flat", background="#000")


    def change_exercise_details(self, exercise_name):
        print("Hello World ", exercise_name)


class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='SECURITEX ATM',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='white')
        heading_label.pack(pady=25)

        choose_amount_label = tk.Label(self,
                                       text='Choose the amount you want to withdraw',
                                       font=('orbitron', 13),
                                       fg='white',
                                       bg='white')
        choose_amount_label.pack()

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        def withdraw(amount):
            global current_balance
            current_balance -= amount
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')


if __name__ == "__main__":
    app = SampleApp()
    app.tk.call("source", "azure.tcl")
    app.tk.call("set_theme", "light")

        
    app.mainloop()
