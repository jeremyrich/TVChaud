from threading import Thread, RLock, BoundedSemaphore
from dbtables.Favorite import Favorite
import random
import time

class ThreadFavorites(Thread):

    def __init__(self, favorite):
        Thread.__init__(self)
        self.favorite = favorite

    def run(self):
        self.favorite.get_favorite_details()


def get_user_favorites(favorites):
    """
    :param favorites: list of objects favorite from the class Favorite
    :type favorites: oject
    """
    favorite_test = Favorite(1, 1402)
    favorite_test_2 = Favorite(1, 60735)
    favorite_test_bobby = Favorite(2, 1418)
    Threads = []
    for favorite in favorites:
        Threads.append(ThreadFavorites(favorite))
    for k in range(0, len(favorites)):
        Threads[k].start()
    for l in range(0, len(Threads)):
        Threads[l].join()
    Threads.append(favorite_test.get_favorite_details())
    Threads.append(favorite_test_2.get_favorite_details())
    Threads.append(favorite_test_bobby.get_favorite_details())
    return Threads