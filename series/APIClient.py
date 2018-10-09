"""API Client for the The Movie DB api
All functions are stored here and API calls made with the API key stored in settings.py"""

from django.conf import settings
import requests

class APIClient:

    def __init__(self):
        self.api_key = settings.TMDB_API_KEY


    def call(self, method, url, *args):
        
        if method == 'GET':
            url += '?api_key=' + str(self.api_key)
            response = requests.get(url)

        return response.json()


    def get_popular_shows(self):
        url = 'https://api.themoviedb.org/3/tv/popular'

        result = self.call('GET', url)
        return result
