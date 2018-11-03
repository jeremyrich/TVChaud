from series.APIClient import APIClient
from database_helper import query

class Favorite():

    # constructeur
    def __init__(self, user_id, tv_id):
        self.__user_id = user_id
        self.__tv_id = tv_id
    
    # getters
    def _get_user_id(self):
        return self.__user_id

    def _get_tv_id(self):
        return self.__tv_id
    
    # properties
    user_id = property(_get_user_id)
    tv_id = property(_get_tv_id)

    # Methods to work on the Favorite object

    #  API call : Returns the tv show's details of the current favorite
    def get_favorite_details(self):
        client = APIClient()
        details = client.get_tv_show_details(self.tv_id)
        return details

    # method to check if a tv show is in the favorites of the current user
    def is_in_db(self):
        command = """SELECT * FROM favorite WHERE user_id = :user_id AND tv_id = :tv_id"""
        data = (self.__user_id, self.__tv_id)
        result = query(command, data)
        return len(result) > 0

    # Add tv show from the user's favorites
    def insert(self):
        command = """INSERT INTO favorite(user_id, tv_id) VALUES(?, ?)"""
        data = (self.__user_id, self.__tv_id)
        query(command, data)

    # Delete tv show from the user's favorites
    def delete(self):
        command = """DELETE FROM favorite WHERE user_id = :user_id AND tv_id = :tv_id"""
        data = {'user_id': self.__user_id, 'tv_id': self.__tv_id}
        query(command, data)