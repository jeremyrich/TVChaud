from database_helper import query
from datetime import datetime

class User:

    def __init__(self, first_name, last_name, email, password=None, user_id=None):
        if user_id is not None:
            self.__user_id = user_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        if password is not None:
            self.__password = password

    # getters
    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    #setters
    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password


    # methods for db
    def insert(self):
        data = {'first_name': self.__first_name, 'last_name': self.__last_name, 'email': self.__email, 'password': self.__password, 'insert_date': datetime.now()}
        script = """INSERT INTO user(first_name, last_name, email, password, insert_date) VALUES (:first_name, :last_name, :email, :password, :insert_date)"""
        query(script, data)

    def add_favorite(self, tv_id):
        command = """INSERT INTO favorite(user_id, tv_id) VALUES(?, ?)"""
        data = (self.__user_id, tv_id)
        query(command, data)

    def get_my_favorites(self):
        command = """SELECT * FROM favorite WHERE """
        my_favorite = query(command)
        my_favorite = Favorite(my_favorite['favorite_id'], my_favorite['user_id'], my_favorite['tv_id'])
        return my_favorite

    def accept_friend_request():
        # Ajouter l'ami aux 2 users
        pass

    def send_friend_request(self, to_user, text=None):
        if text == None:
            command = """INSERT INTO friend_request(from_user, to_user) VALUES(?, ?)"""
            data = (self.__user_id, to_user)
        else:
            command = """INSERT INTO friend_request(from_user, to_user, message) VALUES(?, ?, ?)"""
            data = (self.__user_id, to_user, text)
        query(command, data)


    # static methods
    @staticmethod
    def get_user_by_email(email):
        print(User.get_all_users())
        script = """SELECT * FROM user WHERE email='""" + email + """'"""
        qresult = query(script)[0]
        user = User(qresult[1], qresult[2], qresult[3], qresult[4], qresult[0])
        return user

    @staticmethod
    def get_all_users():
        script = """SELECT * FROM user"""
        users = query(script)
        return users
