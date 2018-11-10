from django.shortcuts import render, redirect
from .APIClient import APIClient
from .APIThread import get_popular_shows
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# in each view we need to load the notifications of the connected user
from user.NotifThread import load_notifications

from dbtables.Notification import Notification
from dbtables.Favorite import Favorite


# View of the home page. We make an API call to get the most popular tv shows
@login_required
def home(request):

    client = APIClient()
    movies = get_popular_shows()

    notifs = load_notifications(request)

    return render(request, 'series/home.html', locals())


# View for one specific tv show given its id
@login_required
def series_details(request, tv_id):
    # API calls to get the tv show information
    client = APIClient()
    details = client.get_tv_show_details(tv_id)
    cast = client.get_tv_show_cast(tv_id)
    reviews = client.get_tv_shows_reviews(tv_id)
    similar = client.get_tv_shows_similar(tv_id)

    # Check if the show is among the user's favorites
    is_fav = Favorite(request.user.id, tv_id).is_in_db()

    notifs = load_notifications(request)

    return render(request, 'series/series_details.html', locals())


# View of one specific season of one specific tv show given the tv_id and season number
@login_required
def season_details(request, tv_id, season_number):

    client = APIClient()
    show_details = client.get_tv_show_details(tv_id)
    season_details = client.get_season_details(tv_id, season_number)

    # Check if the show is among the user's favorites
    is_fav = Favorite(request.user.id, tv_id).is_in_db()

    notifs = load_notifications(request)

    return render(request, 'series/season_details.html', locals())



# Actions on notification's display

# This function simply checks a notif as seen (used when the user clicks on a notif to open the corresponding page)
@login_required
def ajax_see_notif(request):
    notif_id = request.GET.get('notif_id', None)
    Notification.check_as_seen(notif_id)
    return JsonResponse({'notif_id': notif_id})


# This function checks a seen notif as unseen, and reciprocally (used when clicking on the eye icon in notifs)
@login_required
def ajax_check_notif(request):
    notif_id = request.GET.get('notif_id', None)
    Notification.check_seen_unseen(notif_id)
    return JsonResponse({'notif_id': notif_id})