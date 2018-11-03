from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from user.FavoriteThread import get_user_favorites
from dbtables.User import User
from dbtables.Favorite import Favorite


# Create your views here.
from django.contrib.auth.models import User as djangoUser

@login_required
def user_details(request, user_id):
    intermediate = djangoUser.objects.get(id=user_id)
    user = User(intermediate.id, intermediate.username, intermediate.password)
    friends = user.get_friends()

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
    print(num_favorites)

    # On supprime le favori, et update le nombre de favoris
    fav.delete()
    num_favorites -= 1
    return JsonResponse({'num_favorites': num_favorites})

