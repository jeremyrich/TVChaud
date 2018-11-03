from threading import Thread
from dbtables.Favorite import Favorite

""" 
When Thread is launched, it will make the API call from the get_favorite_details 
function. Multithreading allows us to make multiple API calls simultaneously

"""
class FavoriteThread(Thread):

    def __init__(self, favorite):
        Thread.__init__(self)
        self.favorite = favorite
        self.details = {'tv_id': None, 'name': None, 'poster': None, 'overview': None, 'vote_average': None}

    def run(self):
        result = self.favorite.get_favorite_details()
        self.details['tv_id'] = result['tv_id']
        self.details['name'] = result['name']
        self.details['poster'] = result['poster']
        self.details['overview'] = result['overview']
        self.details['vote_average'] = result['vote_average']


# Fonction pour récuperer la liste des favorites d'un user
def get_user_favorites(user):

    favs = user.get_favorites()

    # Threads pour charger les APIs pour les détails des favorites
    threads = [FavoriteThread(fav) for fav in favs]
    fav_details = []

    for th in threads:
        th.start()

    for th in threads:
        th.join()
        favorite = {'tv_id': th.details['tv_id'],
            'name': th.details['name'],
            'poster': th.details['poster'],
            'overview': th.details['overview'],
            'vote_average': th.details['vote_average']}
        fav_details.append(favorite)

    return fav_details