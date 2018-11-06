from database_helper import query
from datetime import datetime

from django.contrib.auth.models import User as djangoUser

from dbtables.Favorite import Favorite
from dbtables.Notification import Notification

# Customed user class based on django user, to add specific methods
class User:

    # constructeur
    def __init__(self, id, username, password):
        self.__user_id = id
        self.__username = username
        self.__password = password

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


    # method that returns every favorites of current user
    def get_favorites(self):
        command = """SELECT * FROM favorite WHERE user_id=?"""
        data = (self.__user_id,)
        fav_query = query(command, data)
        
        favorites = []
        for fav in fav_query:
        # We create the Favorite object from user_id and tv_id
            favorites.append(Favorite(fav[1], fav[2]))
        return favorites


    # method to get notification of current user
    def get_notifications(self):
        command = """SELECT * FROM notification WHERE user_id = ?"""
        data = (self.__user_id,)
        notif_query = query(command, data)
        notifications = []
        for notif in notif_query:
        # We create the Notification object with the needed arguments
            n = Notification(notif[0], notif[1], notif[2], notif[3], notif[4], notif[5])
            notifications.append(n)
        return notifications


    # method to send friend request to another user
    def send_friend_request(self, to_user, text=None):
        command = """INSERT INTO friend_request(from_user, to_user, message) VALUES(?, ?, ?)"""
        data = (self.__user_id, to_user, text)
        query(command, data)

    # Returns the list of friends for the current user
    def get_friends(self):
        command = """SELECT * FROM friendship WHERE user_id_1=? OR user_id_2=?"""
        data = (self.__user_id, self.__user_id)
        friends = query(command, data)
        list_friends = []
        for friend in friends:
    # two possible cases : current user is either user_1 or user_2 is the friendship table
            if friend[1] == self.__user_id:
            # We first fetch the dango user given user_id
                intermediate = djangoUser.objects.get(id=friend[2])
            # Then we convert it into our customed user object
                list_friends.append(User(intermediate.id, intermediate.username, intermediate.password))
            elif friend[2] == self.__user_id:
                intermediate = djangoUser.objects.get(id=friend[1])
                list_friends.append(User(intermediate.id, intermediate.username, intermediate.password))
        return list_friends


