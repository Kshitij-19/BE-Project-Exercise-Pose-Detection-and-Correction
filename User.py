class User(object):
    def __init__(self,email,password,name,mobno):
        self.email = email
        self.password = password
        self.name = name
        self.mobno = mobno

    # method to create user from dictionary
    @staticmethod
    def from_dict(source):
        us = User(source['email'], source['password'], source['name'],source['mobno'])
        return us
    def to_dict(self):
        dest = {
            'email':self.email,
            'password':self.password,
            'name' : self.name,
            'mobno' : self.mobno
        }
        return dest

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()