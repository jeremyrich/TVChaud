from database_helper import query

class FriendRequest():

    # constructeur
    def __init__(self, friend_request_id, from_user, to_user):
        self.__friend_request_id = friend_request_id
        self.__from_user = from_user
        self.__to_user = to_user


    # getters
    def _get_friend_request_id(self):
        return self.__friend_request_id

    def _get_from_user(self):
        return self.__from_user

    def _get_to_user(self):
        return self.__to_user

    # properties
    friend_request_id = property(_get_friend_request_id)
    from_user = property(_get_from_user)
    to_user = property(_get_to_user)


    # methods
    # Creates the friendship objects resulting from the friend request
    def accept(self):
        command = """INSERT INTO friendship(user_id_1, user_id_2) VALUES(?, ?)"""
        data = (self.__from_user, self.__to_user)
        query(command, data)

    # Deletes a friend request (when either accepter or declined)
    def delete(self):
        command = """DELETE FROM friend_request WHERE friend_request_id = ?"""
        data = (self.__friend_request_id,)
        query(command, data)


    # class methods
    @classmethod
    def get_friend_request(cls, friend_request_id):
        command = """SELECT * FROM friend_request WHERE friend_request_id = ?"""
        data = (friend_request_id,)
        result = query(command, data)[0]
        return FriendRequest(result[0], result[1], result[2])
