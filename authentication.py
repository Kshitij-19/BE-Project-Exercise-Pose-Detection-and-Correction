from ast import Try
import pyrebase

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
        print("sign in successfull")
        print(user)
    except:
        print("invalid email or password")

ans = input("are you a new user? y/n")

if ans == 'y':
    signup()
else: 
    signin()