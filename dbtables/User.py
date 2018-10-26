from database_helper import query
from datetime import datetime

from dbtables.Favorite import Favorite

class User:

    def __init__(self, request):
        self.__user_id = request.user.id
        self.__username = request.user.username
        self.__password = request.user.password

    # getters
    def get_user_id(self):
        return self.__user_id

    def get_password(self):
        return self.__password

    #setters
    def set_password(self, password):
        self.__password = password


    # methods for db
    def add_favorite(self, tv_id):
        command = """INSERT INTO favorite(user_id, tv_id) VALUES(?, ?)"""
        data = (self.__user_id, tv_id)
        query(command, data)

    def get_my_favorites(self):
        command = """SELECT * FROM favorite WHERE user_id=?"""
        my_favorite = query(command, self.__user_id)
        favorites = []
        for fav in my_favorite:
            favorites.append(Favorite(fav[1], fav[2]))
        return favorites

    def accept_friend_request(self):
        # Ajouter l'ami aux 2 users
        pass

    def send_friend_request(self, to_user, text=None):
        command = """INSERT INTO friend_request(from_user, to_user, message) VALUES(?, ?, ?)"""
        data = (self.__user_id, to_user, text)
        query(command, data)
