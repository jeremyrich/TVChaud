from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from user.FavoriteThread import get_user_favorites
from user.NotifThread import load_notifications

from dbtables.User import User
from dbtables.Favorite import Favorite
from dbtables.FriendRequest import FriendRequest

from django.contrib.auth.models import User as djangoUser

# Create your views here.

@login_required
def user_details(request, user_id):
    intermediate = djangoUser.objects.get(id=user_id)
    user = User(intermediate.id, intermediate.username, intermediate.password)
    friends = user.get_friends()

    notifs = load_notifications(request)

    # On appelle le multithreading pour obtenir les favoris du user
    favorites = get_user_favorites(user)


    return render(request, 'user/user_details.html', locals())


@login_required
def ajax_add_favorite(request):
    user_id = request.GET.get('user_id', None)
    tv_id = request.GET.get('tv_id', None)

    fav = Favorite(user_id, tv_id)

    # Si la série est déjà dans les favoris, on l'enlève et on reviendra au bouton "Add to favorites"
    if fav.is_in_db():
        fav.delete()
        return JsonResponse({'button_text': '<span style="font-size: 30px;"> + </span> <br/> Add to favorites', 'class': 'favorite-button'})

    # Sinon, on l'ajoute aux favoris, et le bouton deviendra "Added to favorites"
    fav.insert()
    return JsonResponse({'button_text': 'Added to favorites', 'class': 'favorite-button-added'})


@login_required
def ajax_remove_favorite(request):
    user_id = request.GET.get('user_id', None)
    tv_id = request.GET.get('tv_id', None)

    fav = Favorite(user_id, tv_id)

    intermediate = djangoUser.objects.get(id=user_id)
    user = User(intermediate.id, intermediate.username, intermediate.password)

    # On appelle le multithreading pour obtenir les favoris du user,
    # pour pouvoir changer le titre de la page (nouveau nombre de favoris)
    favorites = get_user_favorites(user)
    num_favorites = len(favorites)

    # On supprime le favori, et update le nombre de favoris
    fav.delete()
    num_favorites -= 1
    return JsonResponse({'num_favorites': num_favorites})


@login_required
def ajax_send_friend_request(request):
    to_username = request.GET.get('to_username', None)

    current_user = User(request.user.id, request.user.username, request.user.password)
    is_valid = True

    try:
        to_user = djangoUser.objects.get(username=to_username)
        current_user.send_friend_request(to_user.id)

    except djangoUser.DoesNotExist:
        print('no such user in the db')
        is_valid = False

    return JsonResponse({'valid_username': is_valid})


@login_required
def ajax_accept_friend_request(request):
    friend_request_id = request.GET.get('friend_request_id', None)

    friend_request = FriendRequest.get_friend_request(friend_request_id)

    friend_request.accept()
    friend_request.delete()

    return JsonResponse({'accepted': True})


@login_required
def ajax_decline_friend_request(request):
    friend_request_id = request.GET.get('friend_request_id', None)

    friend_request = FriendRequest.get_friend_request(friend_request_id)

    friend_request.delete()

    return JsonResponse({'accepted': False})

