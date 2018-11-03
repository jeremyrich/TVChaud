"""API Client for the The Movie DB api
All functions are stored here and API calls made with the API key stored in settings.py"""


from django.conf import settings
import requests

class APIClient:

    def __init__(self):
        self.api_key = settings.TMDB_API_KEY

    # Fonction d'appel de l'API TheMovieDB : elle permet de rajouter l'API Key à la suite de l'url et de lancer la requête
    def call(self, method, url, *args):
        
        if method == 'GET':
            url += '?api_key=' + str(self.api_key)
            response = requests.get(url)

        return response.json()


    # API Call : Retourne les 20 TV shows les plus populaires
    def get_popular_shows(self):
        url = 'https://api.themoviedb.org/3/tv/popular'
        result = self.call('GET', url)

        popular = []

        for resu in result['results']:
            tvshow = {'tv_id': resu['id'], 'poster_path': 'https://image.tmdb.org/t/p/w500' + resu['poster_path']}
            popular.append(tvshow)

        return popular


    # API Call : Retourne la fiche détail d'un TV show en particulier
    def get_tv_show_details(self, tv_id):
        url = 'https://api.themoviedb.org/3/tv/' + str(tv_id)
        details = self.call('GET', url)

        realisateurs = 'Unknown' if len(details['created_by']) == 0 else ', '.join([real['name'] for real in details['created_by']])
        genres = 'Not identified' if len(details['genres']) == 0 else ', '.join([g['name'] for g in details['genres']])

        show_seasons = []

        for se in details['seasons']:

            image = 'https://wingslax.com/wp-content/uploads/2017/12/no-image-available.png' if se['poster_path'] is None else 'https://image.tmdb.org/t/p/w500' + se['poster_path']

            episode_count = '1 episode' if se['episode_count'] == 1 else str(se['episode_count']) + ' episodes'

            season = {'season_name': se['name'], 'season_number': se['season_number'], 'poster_path': image, 'episode_count': episode_count}
            show_seasons.append(season)

        details_useful = {'tv_id' : details['id'],
                          'realisateur': realisateurs,
                          'genres': genres,
                          'name': details['name'],
                          'number_of_episodes': details['number_of_episodes'],
                          'origin_country': details['origin_country'][0],
                          'overview': details['overview'],
                          'poster': 'https://image.tmdb.org/t/p/w500' + details['poster_path'],
                          'first_air_date': details['first_air_date'],
                          'vote_average': details['vote_average'],
                          'seasons': show_seasons}

        return details_useful


    # API Call : Retourne le casting du TV show en argument
    def get_tv_show_cast(self, tv_id):
        url = 'https://api.themoviedb.org/3/tv/' + str(tv_id) + '/credits'
        credits = self.call('GET', url)

        for actor in credits['cast']:
            actor['profile_path'] = 'https://image.tmdb.org/t/p/w200' + str(actor['profile_path'])

        return credits['cast']


    # API Call : Retourne les reviews du TV show en argument
    def get_tv_shows_reviews(self, tv_id):
        url = 'https://api.themoviedb.org/3/tv/' + str(tv_id) + '/reviews'
        reviews = self.call('GET', url)

        if reviews['results'] == []:
            return [{'author': '', 'content': "Sorry, this TV show doesn't have any reviews yet. It's not bad though."}]
        return reviews['results']


    # API Call : Retourne les recommandations de shows similaires (dans la limite de 12 shows)
    def get_tv_shows_similar(self, tv_id):
        url = 'https://api.themoviedb.org/3/tv/' + str(tv_id) + '/similar'
        similar = self.call('GET', url)

        if similar['results'] == []:
            return [{'name': 'No similar movies'}]

        for result in similar['results']:
            result['poster_path'] = 'https://image.tmdb.org/t/p/w500' + result['poster_path']

        return similar['results'][:12]


    # API Call : Retourne les détails de la saison d'un TV show donnés en argument
    def get_season_details(self, tv_id, season_number):
        url = 'https://api.themoviedb.org/3/tv/' + str(tv_id) + '/season/' + str(season_number)
        season_details = self.call('GET', url)

        image = 'https://wingslax.com/wp-content/uploads/2017/12/no-image-available.png' if season_details['poster_path'] is None \
            else 'https://image.tmdb.org/t/p/w500' + season_details['poster_path']

        episodes = []
        for ep in season_details['episodes']:
            name = 'Episode ' + str(ep['episode_number']) + ' - ' + ep['name']

            overview = "There's currently no description for this episode. It's probably not one of the best..." if ep['overview'] == '' else ep['overview']
            vote_average = round(ep['vote_average'], 1)

            stars = 'None' if len(ep['guest_stars']) == 0 else ', '.join([actor['name'] for actor in ep['guest_stars']])

            ep['still_path'] = 'https://wingslax.com/wp-content/uploads/2017/12/no-image-available.png' if ep['still_path'] is None \
                else 'https://image.tmdb.org/t/p/w500' + ep['still_path']

            episode = {'name': name, 'overview': overview, 'vote_average': vote_average, 'stars': stars,
                       'air_date': ep['air_date'], 'still_path': ep['still_path']}
            episodes.append(episode)



        output = {'season_name': season_details['name'],
                'poster_path': image,
                'overview': season_details['overview'],
                'air_date': season_details['air_date'],
                'number_of_episodes': len(season_details['episodes']),
                'episodes': episodes}

        return output
