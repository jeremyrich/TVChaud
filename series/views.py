from django.shortcuts import render, redirect
from .APIClient import APIClient
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from user.NotifThread import load_notifications

from dbtables.Notification import Notification


# Create your views here.

@login_required
def home(request):

    client = APIClient()
    movies = client.get_popular_shows()

    notifs = load_notifications(request)

    return render(request, 'series/home.html', locals())


@login_required
def series_details(request, tv_id):

    client = APIClient()
    details = client.get_tv_show_details(tv_id)
    cast = client.get_tv_show_cast(tv_id)
    reviews = client.get_tv_shows_reviews(tv_id)
    similar = client.get_tv_shows_similar(tv_id)

    notifs = load_notifications(request)

    return render(request, 'series/series_details.html', locals())


@login_required
def season_details(request, tv_id, season_number):

    client = APIClient()
    show_details = client.get_tv_show_details(tv_id)
    season_details = client.get_season_details(tv_id, season_number)

    notifs = load_notifications(request)

    return render(request, 'series/season_details.html', locals())


@login_required
def ajax_see_notif(request):
    notif_id = request.GET.get('notif_id', None)
    Notification.check_as_seen(notif_id)
    return JsonResponse({'notif_id': notif_id})


@login_required
def ajax_check_notif(request):
    notif_id = request.GET.get('notif_id', None)
    Notification.check_seen_unseen(notif_id)
    return JsonResponse({'notif_id': notif_id})