from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import user.ThreadFavorites as ThreadFavorites
from dbtables.User import User
# Create your views here.

@login_required
def user_details(request, user_id):
    user = User(request)
    # Retourne une liste d'objets Favorite
    """favorites = user.get_my_favorites()
    # on appelle le multithreading depuis les objets Favorites
    favorites_details = ThreadFavorites.get_user_favorites(favorites)"""
    output = {'user_id': user_id,
              'user': user,
              }

    return render(request, 'user/details.html', output)
