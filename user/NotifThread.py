from dbtables.User import User
from threading import Thread
from series.APIClient import APIClient

from django.contrib.auth.models import User as djangoUser


class NotifThread(Thread):
    
    def __init__(self, notif):
        Thread.__init__(self)
        self.notif = notif
        self.details = {'image': None, 'title': None}

    def run(self):
         client = APIClient()
         show_details = client.get_tv_show_details(self.notif.tv_id)
         self.details['image'] = show_details['poster']
         self.details['title'] = show_details['name']


# Fonction destinée à être utilisée à chaque chargement de view, pour loader les notifications dans le header
def load_notifications(request):

    myuser = User(request.user.id, request.user.username, request.user.password)

    # PARTIE FRIEND REQUESTS
    friend_requests_query = myuser.get_friend_requests()
    friend_requests = []

    for request in friend_requests_query:
        from_user = djangoUser.objects.get(id=request[1])
        new_request = {'friend_request_id': request[0], 'from_user': from_user}
        friend_requests.append(new_request)


    # PARTIE NOTIFICATIONS NEW EPISODES
    notifs = myuser.get_notifications()

    alert = False

    # Threads pour charger les APIs pour l'image et le nom de la série
    threads = [NotifThread(notif) for notif in notifs]
    new_episodes = []

    for th in threads:
        th.start()

        # Détermine si il y a au moins une notif non lue
        if not th.notif.seen:
            alert = True

    for th in threads:
        th.join()
        ep = {'image': th.details['image'],
            'title': th.details['title'],
            'notif_id': th.notif.notification_id,
            'tv_id': th.notif.tv_id,
            'season': th.notif.season,
            'episode': th.notif.episode,
            'seen': th.notif.seen}
        new_episodes.append(ep)

    return {'alert': alert, 'friend_requests': friend_requests, 'new_episodes': new_episodes}