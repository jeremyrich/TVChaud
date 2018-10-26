from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import user.ThreadFavorites as ThreadFavorites
# Create your views here.

@login_required
def user_details(request, user_id):

    output = {'user_id': user_id}

    return render(request, 'user/details.html', output)

@login_required
def my_favorites(request):
    # Retourne une liste d'objets Favorite
    favorites = request.User.get_my_favorites()
    # on appelle le multithreading depuis les objets Favorites
    favorites_details = ThreadFavorites.get_user_favorites(favorites)
    hey = "hey"
    return (request, 'series/my_favorites.html', locals())


