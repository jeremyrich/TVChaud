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
    intermediate = djangoUser.objects.get(id=user_id)
    user = User(intermediate.id, intermediate.username, intermediate.password)
    friends = user.get_friends()

    notifs = load_notifications(request)

    # On appelle le multithreading pour obtenir les favorites du user
    favorites = get_user_favorites(user)

    return render(request, 'user/user_details.html', locals())


@login_required
def ajax_add_favorite(request):
    user_id = request.GET.get('user_id', None)
    tv_id = request.GET.get('tv_id', None)

    fav = Favorite(user_id, tv_id)
    if fav.is_in_db():
        fav.delete()
        return JsonResponse({'button_text': '<span style="font-size: 30px;"> + </span> <br/> Add to favorites', 'class': 'favorite-button'})

    fav.insert()
    return JsonResponse({'button_text': 'Added to favorites', 'class': 'favorite-button-added'})
