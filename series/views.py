from django.shortcuts import render
import requests
from .APIClient import APIClient
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def home(request):

    client = APIClient()
    result = client.get_popular_shows()

    images = []
    for movies in result['results']:
        images += ['https://image.tmdb.org/t/p/w500' + movies['poster_path']]

    output = {'images': images}

    return render(request, 'series/home.html', output)


@login_required
def details(request):
    return render(request, 'series/details.html', locals())

@login_required
def test(request, tv_id):
    client = APIClient()
    details = client.get_tv_show_details(tv_id)
    reviews = client.get_tv_shows_reviews(tv_id)
    cast = client.get_tv_show_cast(tv_id)
    return render(request, 'series/test.html', locals())
