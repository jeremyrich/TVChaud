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

def details(request):

    return render(request, 'series/details.html', locals())