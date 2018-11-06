from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from user.FavoriteThread import get_user_favorites
from user.NotifThread import load_notifications
from dbtables.User import User
from dbtables.Favorite import Favorite


# Create your views here.
from django.contrib.auth.models import User as djangoUser

@login_required
def user_details(request, user_id):
    # We get the django user given the user_id
    intermediate = djangoUser.objects.get(id=user_id)
    # We then convert it to our customed user
    user = User(intermediate.id, intermediate.username, intermediate.password)
    # We get the list of user's friends
    friends = user.get_friends()

    notifs = load_notifications(request)
    # We call the multithreading to get the user's favorites
    favorites = get_user_favorites(user)

    return render(request, 'user/user_details.html', locals())

# Actions on favorite's display, to add or remove a tv show to the favorites
@login_required
def ajax_add_favorite(request):
    user_id = request.GET.get('user_id', None)
    tv_id = request.GET.get('tv_id', None)

    fav = Favorite(user_id, tv_id)
    # If the tv show is already into its favorites, we delete it and we get button transforms to "Add to favorites"
    if fav.is_in_db():
        fav.delete()
        return JsonResponse({'button_text': '<span style="font-size: 30px;"> + </span> <br/> Add to favorites', 'class': 'favorite-button'})

    # If not, we add it to favorites, and the button transforms to  "Added to favorites"
    fav.insert()
    return JsonResponse({'button_text': 'Added to favorites', 'class': 'favorite-button-added'})

@login_required
def ajax_remove_favorite(request):
    user_id = request.GET.get('user_id', None)
    tv_id = request.GET.get('tv_id', None)

    fav = Favorite(user_id, tv_id)

    intermediate = djangoUser.objects.get(id=user_id)
    user = User(intermediate.id, intermediate.username, intermediate.password)
    # We call the multithreading to get the user's favorites details,
    # # to change the page title adapted to the new number of favorites
    favorites = get_user_favorites(user)
    num_favorites = len(favorites)
    print(num_favorites)

    # We then delete the favorite from user's lsit and update the number of favorites
    fav.delete()
    num_favorites -= 1
    return JsonResponse({'num_favorites': num_favorites})

