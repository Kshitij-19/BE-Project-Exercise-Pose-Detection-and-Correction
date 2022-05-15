#import modules

from asyncio import subprocess
import io
from tkinter import *
import os
import subprocess
from PIL import Image, ImageTk

# MY CODE

from ast import Try
import pyrebase
import urllib.request
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
db = firebase.database()
auth = firebase.auth()

email = "abhishekdhamgunde@gmail.com"
password = '123456'
user = auth.sign_in_with_email_and_password(email, password)

data = {
    "name": "Abhishek Dhamgunde",
    "height": "165",
    "weight": []
}
users_email = auth.get_account_info(user['idToken'])['users'][0]['email']
# Pass the user's idToken to the push method
# results = db.child("users").push(data, user['idToken'])
results = db.child('user/'+ auth.get_account_info(user['idToken'])['users'][0]['localId']).push(data, user['idToken'])
# print(db.child("users").get().val().popitem())

# print(user)
print(auth.get_account_info(user['idToken']))

# UI start

# window = Tk()
# name = 'Abhishek Dhamgunde'
# age = 22
# height = 165
# weight = 55
# name_label = Label(window, text='Name     -\t' + name)
# name_label.grid(row=0, column=0, sticky='W')

# age_label = Label(window, text='Age         -\t' + str(age) + ' years')
# age_label.grid(row=1, column=0, sticky='W')

# height_label = Label(window, text='Height    -\t' +
#                      str(height) + ' cm')
# height_label.grid(row=2, column=0, sticky='W')

# weight_label = Label(window, text='Weight   -\t' +
#                      str(weight) + ' Kg')
# weight_label.grid(row=3, column=0, sticky='W')

# window.mainloop()
# UI end

