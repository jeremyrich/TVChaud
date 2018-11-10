class Friendship:

    # constructor
    def __init__(self, user_id_1, user_id_2):
        self.__user_id_1 = user_id_1
        self.__user_id_2 = user_id_2


    # getters
    def _get_user_id_1(self):
        return self.__user_id_1

    def _get_user_id_2(self):
        return self.__user_id_2


    # properties
    user_id_1 = property(_get_user_id_1)
    user_id_2 = property(_get_user_id_2)

