from django.shortcuts import render
import requests
from .APIClient import APIClient
from django.contrib.auth.decorators import login_required
import series.Multithreading as Multithreading
import dbtables.User as User
# Create your views here.

@login_required
def home(request):

    client = APIClient()
    movies = client.get_popular_shows()

    output = {'movies': movies}

    return render(request, 'series/home.html', output)


@login_required
def details(request, tv_id):

    client = APIClient()
    details = client.get_tv_show_details(tv_id)
    reviews = client.get_tv_shows_reviews(tv_id)
    cast = client.get_tv_show_cast(tv_id)
    season_cast = client.get_tv_show_season_cast(tv_id)
    similar = client.get_tv_shows_similar(tv_id)

    output = {'client': client, 'details': details, 'reviews': reviews, 'cast': cast, 'season_cast': season_cast,
              'similar': similar}
    return render(request, 'series/details.html', output)

@login_required
def test(request, tv_id):
    client = APIClient()
    details = client.get_tv_show_details(tv_id)
    reviews = client.get_tv_shows_reviews(tv_id)
    cast = client.get_tv_show_cast(tv_id)
    season_cast = client.get_tv_show_season_cast(tv_id)

    output = {'client': client, 'details': details, 'reviews': reviews, 'cast': cast, 'season_cast': season_cast}
    return render(request, 'series/test.html', output)

@login_required
def my_favorites(request):
    # Retourne une liste d'objets Favorite
    #Favorites = request.User.get_my_favorites()
    # on appelle le multithreading depuis les objets Favorites
    #favorites_details = Multithreading.get_user_favorites(Favorites)
    hey = "hey"
    return (request, 'series/my_favorites.html', locals())



