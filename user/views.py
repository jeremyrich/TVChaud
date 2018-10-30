from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import user.ThreadFavorites as ThreadFavorites
from dbtables.User import User
# Create your views here.
from django.contrib.auth.models import User as djangoUser

@login_required
def user_details(request, user_id):
    user = User(request.user.id, request.user.username, request.user.password)
    friends = user.get_friends()
    # Retourne une liste d'objets Favorite
    favorites = user.get_my_favorites()
    # on appelle le multithreading depuis les objets Favorites
    favorites_details = ThreadFavorites.get_user_favorites(favorites)
    output = {'user_id': user_id,
              'user': user,
              'details': favorites_details,
              'friends': friends
              }
    return render(request, 'user/user_details.html', output)
