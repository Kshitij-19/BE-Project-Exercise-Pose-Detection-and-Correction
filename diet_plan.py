import pyrebase
import json

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


class diet_plan(object):
    def __init__(self, breakfast, lunch, snack, dinner):
        self.breakfast = breakfast
        self.lunch = lunch
        self.snack = snack
        self.dinner = dinner

    @staticmethod
    def from_dict(source):
        diet = diet_plan(source['breakfast'], source['lunch'], source['snack'], source['dinner'])
        return diet

    def to_dict(self):
        dest = {
            'breakfast': self.breakfast,
            'lunch': self.lunch,
            'snack': self.snack,
            'dinner': self.dinner
        }
        return dest

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()


db = firebase.database()
try:
    #data = diet_plan('break', 'lunch', 'pre', 'post')
    #print(data.to_dict())
    #data = diet_plan("Oatmeal with Greek Yogurt & Seasonal fruits Mango Juice","Multigrain roti, fish curry, vegetable salad","Toast with Jam","Broken wheat khichidi along with carrot raita, egg white, and vegetable salad")
    #db.child('diet_plan').child('sun').set(data.to_dict())
    #die = db.child('diet_plan').child('wed').get()

    #print(die.val()['dinner'])
    d = db.child('diet_plan').get()
    for p in d.each():
        print(p.val())

    print("data added successfully")
except Exception as e:
    print(e)
