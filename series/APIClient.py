"""API Client for the The Movie DB api
All functions are stored here and API calls made with the API key stored in settings.py"""

"""
Je veux :
- image
- noms des acteurs
- réalisateur
- pays
- duration
- categories (drame, comedy...)
- date de sortie
- rating
- synopsis
- saisons et épisodes       
- reviews   
- Others ?
- id

"""
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
        popular = result['results']
        for movie in popular:
            movie['id'] = 'http://localhost:8000/series/details/' + str(movie['id'])
            movie['poster_path'] = 'https://image.tmdb.org/t/p/w500' + movie['poster_path']
        return popular

    def get_tv_show_details(self, tv_id):
        url = 'https://api.themoviedb.org/3/tv/' + str(tv_id)

        details = self.call('GET', url)
        real = []
        if details['created_by'] == []:
            real = ['non renseigné']
        else:
            for realisateur in details['created_by']:
                real.append(realisateur['name'])
        realisateur = ', '.join(real)


        genres = []
        if details['genres'] == []:
            genres = ['Not identified']
        else:
            for g in details['genres']:
                genres.append(g['name'])
        genre = ', '.join(genres)

        details_useful = {'realisateur': realisateur,
                          'genres': genre,
                          'name': details['name'],
                          'number_of_episodes': details['number_of_episodes'],
                          'origin_country': details['origin_country'][0],
                          'language': details['original_language'],
                          'overview': details['overview'],
                          'popularity': details['popularity'],
                          'poster': 'https://image.tmdb.org/t/p/w500' + details['poster_path'],
                          'first_air_date': details['first_air_date'],
                          'next_episode_to_air': details['next_episode_to_air'],
                          'vote_average': details['vote_average'],
                          }

        return details_useful

    def get_tv_show_season_cast(self, tv_id, season_number = 1):
        url = 'https://api.themoviedb.org/3/tv/' + str(tv_id) + '/season/' +str(season_number) +'/credits'

        details = self.call('GET', url)
        actors = details['cast']
        crew = details['crew']
        cast = {'actors': actors, 'crew': crew}
        for actor in cast['actors']:
            actor['profile_path'] = 'https://image.tmdb.org/t/p/w200' + str(actor['profile_path'])
        return cast

    def get_tv_show_cast(self, tv_id):
        url = 'https://api.themoviedb.org/3/tv/' + str(tv_id) + '/credits'

        details = self.call('GET', url)
        actors = details['cast']
        crew = details['crew']
        cast = {'actors': actors, 'crew': crew}
        for actor in cast['actors']:
            actor['profile_path'] = 'https://image.tmdb.org/t/p/w200' + str(actor['profile_path'])
        return cast

    def get_tv_shows_reviews(self, tv_id):
        url = 'https://api.themoviedb.org/3/tv/' + str(tv_id) + '/reviews'

        reviews = self.call('GET', url)
        if reviews['results'] == []:
            return [{'author': "", 'content': "Sorry, this TV show doesn't have any reviews yet. It's not bad though."}]
        else:
            return reviews['results'] # return a list of reviews contained in dictionaries


    def get_tv_shows_similar(self, tv_id):
        url = 'https://api.themoviedb.org/3/tv/' + str(tv_id) + '/similar'

        similar = self.call('GET', url)
        if similar['results'] == []:
            return [{'name': "No similar movies"}]
        else:
            for result in similar['results']:
                result['poster_path'] = 'https://image.tmdb.org/t/p/w500' + result['poster_path']
                result['id'] = 'http://localhost:8000/series/details/' + str(result['id'])

            return similar['results'][:12]
