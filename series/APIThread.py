# Thread destined to call several times the popular_shows API

from threading import Thread

from .APIClient import APIClient

class APIThread(Thread):

    # constructor
    def __init__(self, clientAPI, page):
        Thread.__init__(self)
        self.clientAPI = clientAPI
        self.page = page
        self.shows_list = [] 

    
    # the run function is destined to call the API popular_shows on a specific page, and store the relevant info
    def run(self):

        url = 'https://api.themoviedb.org/3/tv/popular'
        result = self.clientAPI.call('GET', url, page=self.page)

        for resu in result['results']:
            tvshow = {'tv_id': resu['id'], 'name': resu['name'], 'poster_path': None if resu['poster_path'] is None else 'https://image.tmdb.org/t/p/w500' + resu['poster_path']}
            self.shows_list.append(tvshow)


# API Call : Returns the 400 most popular TV shows
def get_popular_shows():
    popular = []

    client = APIClient()

    # we are going to create 20 threads to get the 20 first pages of the API popular_shows
    threads = [APIThread(client, page) for page in range(20)]

    for th in threads:
        th.start()

    for th in threads:
        th.join()
        popular += th.shows_list

    return popular