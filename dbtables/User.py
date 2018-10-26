from database_helper import query
from datetime import datetime

from dbtables.Favorite import Favorite

class User:

    def __init__(self, request):
        self.__user_id = request.user.id
        self.__username = request.user.username
        self.__password = request.user.password

    # getters
    def _get_user_id(self):
        return self.__user_id

    def _get_username(self):
        return self.__username

    def _get_password(self):
        return self.__password

    # properties
    user_id = property(_get_user_id)
    username = property(_get_username)
    password = property(_get_password)


    # methods
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
