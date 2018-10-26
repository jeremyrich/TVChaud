from django.shortcuts import render
import requests
from .APIClient import APIClient
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def home(request):

    client = APIClient()
    movies = client.get_popular_shows()

    output = {'movies': movies}

    return render(request, 'series/home.html', output)


@login_required
def series_details(request, tv_id):

    client = APIClient()
    details = client.get_tv_show_details(tv_id)
    reviews = client.get_tv_shows_reviews(tv_id)
    cast = client.get_tv_show_cast(tv_id)
    season_cast = client.get_tv_show_season_cast(tv_id)
    similar = client.get_tv_shows_similar(tv_id)

    output = {'client': client, 'details': details, 'reviews': reviews, 'cast': cast, 'season_cast': season_cast,
              'similar': similar}
    return render(request, 'series/series_details.html', output)

@login_required
def season_details(request, tv_id, season_number):

    client = APIClient()

    season_details = client.get_season_details(tv_id, season_number)
    show_details = client.get_tv_show_details(tv_id)

    output = {'season_details': season_details, 'show_details': show_details}
    return render(request, 'series/season_details.html', output)

@login_required
def test(request, tv_id):
    client = APIClient()
    details = client.get_tv_show_details(tv_id)
    reviews = client.get_tv_shows_reviews(tv_id)
    cast = client.get_tv_show_cast(tv_id)
    season_cast = client.get_tv_show_season_cast(tv_id)

    output = {'client': client, 'details': details, 'reviews': reviews, 'cast': cast, 'season_cast': season_cast}
    return render(request, 'series/test.html', output)
