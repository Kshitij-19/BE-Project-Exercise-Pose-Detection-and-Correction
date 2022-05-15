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
db = firebase.database()
storage = firebase.storage()