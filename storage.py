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
user = auth.sign_in_with_email_and_password(email="abhishekdhamgunde@gmail.com",password='123456')
user_info = auth.get_account_info(user['idToken'])
key = user_info['users'][0]['localId']
download_token = storage.child('profile_pictures/goku_dp.jpg').put('goku.jpg',key)['downloadTokens']
# storage.child('profile_pictures/goku_dp.jpg').put('goku.jpg',user["idToken"])
url = storage.child("profile_pictures/goku_dp.jpg").get_url(token=download_token)
print(url)
# storage.child('profile_pictures/goku_dp.jpg').download('./','goku_downloaded.jpg')

