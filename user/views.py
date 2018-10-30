from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from user.FavoriteThread import get_user_favorites
from dbtables.User import User
from dbtables.Favorite import Favorite


# Create your views here.

@login_required
def user_details(request, user_id):

    user = User(request.user.id, request.user.username, request.user.password)

    # On appelle le multithreading pour obtenir les favorites du user
    favorites = get_user_favorites(user)

    print(favorites)

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
    return JsonResponse({'button_text': 'Added in favorites', 'class': 'favorite-button-added'})