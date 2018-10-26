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

        details['id'] = 'http://localhost:8000/series/details/' + str(details['id'])
        real = []
        if details['created_by'] == []:
            real = ['not in the database']
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

        if details['seasons'] == []:
            details['seasons'] = {'name': "This TV show doesn't have any seasons yet. It'll come soon ;)",
                                  'poster_path': "None"}
        else:
            for season in details['seasons']:
                season['id'] = str(details['id']) + "/" + str(season['season_number'])
                if season['poster_path'] == None:
                    season['poster_path'] = \
                        "https://wingslax.com/wp-content/uploads/2017/12/no-image-available.png"
                else:
                    season['poster_path'] = 'https://image.tmdb.org/t/p/w500' + season['poster_path']
                if season['episode_count'] == 1:
                    season['episode_count'] = "1 episode"
                else:
                    season['episode_count'] = str(season['episode_count']) + " episodes"

        details_useful = {'link': details['id'],
                          'realisateur': realisateur,
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
                          'seasons': details['seasons'],
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

    def get_season_details(self, tv_id, season_number):
        url = 'https://api.themoviedb.org/3/tv/' + str(tv_id) + '/season/' + str(season_number)

        details = self.call('GET', url)

        url = 'https://api.themoviedb.org/3/tv/' + str(tv_id)

        show_details = self.call('GET', url)

        if details['season_number'] == 0:
            details['season_number'] = "Specials"
        else:
            details['season_number'] = "Season " + str(details['season_number'])

        if details['poster_path'] is None:
            details['poster_path'] = 'https://image.tmdb.org/t/p/w500' + show_details['poster_path']
        else:
            details['poster_path'] = 'https://image.tmdb.org/t/p/w500' + details['poster_path']

        details['number_of_episodes'] = len(details['episodes'])

        for episode in details['episodes']:
            episode['name'] = "Episode " + str(episode['episode_number']) + " - " + episode['name']

            if episode['overview'] == "":
                episode['overview'] = "There's currently no description for this episode. It's probably " \
                                      "not one of the best..."

            episode['vote_average'] = round(episode['vote_average'], 1)

            stars = []
            if episode['guest_stars'] != []:

                for actor in episode['guest_stars']:
                    actor['profile_path'] = 'https://image.tmdb.org/t/p/w200' + str(actor['profile_path'])
                    stars.append(actor['name'])
                stars = ', '.join(stars)

            episode['stars'] = stars


        return details
