from threading import Thread, RLock, BoundedSemaphore
import random
import time

class ThreadFavorites(Thread):

    def __init__(self, favorite):
        Thread.__init__(self)
        self.favorite = favorite

    def run(self):
        self.favorite.get_favorite_details()


def get_user_favorites(favorites):
    Threads = []
    for favorite in favorites:
        Threads.append(ThreadFavorites(favorite))
    for k in range(0, len(favorites)):
        Threads[k].start()
    for l in range(0, len(Threads)):
        Threads[l].join()