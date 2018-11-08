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
        command = """SELECT * FROM notification WHERE user_id = ? ORDER BY notification_id DESC LIMIT 10"""
        data = (self.__user_id,)
        notif_query = query(command, data)
        notifications = []
        for notif in notif_query:
        # We create the Notification object with the needed arguments
            n = Notification(notif[0], notif[1], notif[2], notif[3], notif[4], notif[5])
            notifications.append(n)
        return notifications

    # methods for friend requests
    def get_friend_requests(self):
        command = """SELECT * FROM friend_request WHERE to_user=? GROUP BY from_user, to_user"""
        data = (self.__user_id,)
        return query(command, data)

    def send_friend_request(self, to_user):
        command = """INSERT INTO friend_request(from_user, to_user) VALUES(?, ?)"""
        data = (self.__user_id, to_user)
        query(command, data)


    # Returns the list of friends for the current user
    def get_friends(self):
        command = """SELECT DISTINCT user_id_2 FROM friendship WHERE user_id_1=? UNION SELECT DISTINCT user_id_1 FROM friendship WHERE user_id_2=?"""
        data = (self.__user_id, self.__user_id)
        friends = query(command, data)

        list_friends = []
        for friend in friends:
            intermediate = djangoUser.objects.get(id=friend[0])
            list_friends.append(User(intermediate.id, intermediate.username, intermediate.password))

        return list_friends


