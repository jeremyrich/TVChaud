from threading import Thread, RLock, BoundedSemaphore
import random
import time

class ThreadFavorites(Thread):

    def __init__(self, Favorite):
        Thread.__init__(self)
        self.Favorite = Favorite

    def run(self):
        self.Favorite.get_favorite_details()


def get_user_favorites(Favorites):
    Threads = []
    for Favorite in Favorites:
        Threads.append(ThreadFavorites(Favorite))
    for k in range(0, len(Favorites)):
        Threads[k].start()
    for l in range(0, len(Threads)):
        Threads[l].join()