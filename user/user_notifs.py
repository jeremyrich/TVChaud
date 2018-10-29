# une seule fonction destinée à être utilisée à chaque chargement de view, pour loader les notifications dans le header

from dbtables.User import User
from threading import Thread
from series.APIClient import APIClient

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


def load_notifications(request):

    myuser = User(request)
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

    return {'alert': alert, 'new_episodes': new_episodes}