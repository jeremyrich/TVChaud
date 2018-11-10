from dbtables.User import User
from threading import Thread
from series.APIClient import APIClient

from django.contrib.auth.models import User as djangoUser

""" 
When NotifThread is launched, it will make the API call from the get_favorite_details 
function. Multithreading allows us to make multiple API calls simultaneously

"""

class NotifThread(Thread):
    
    def __init__(self, clientAPI, notif):
        Thread.__init__(self)
        self.clientAPI = clientAPI
        self.notif = notif
        self.details = {'image': None, 'title': None}

    def run(self):
         show_details = self.clientAPI.get_tv_show_details(self.notif.tv_id)
         self.details['image'] = show_details['poster']
         self.details['title'] = show_details['name']

# Function to be used every time the view is charged., to load notification into the header
def load_notifications(request):

    myuser = User(request.user.id, request.user.username, request.user.password)

    # PART FRIEND REQUESTS
    friend_requests_query = myuser.get_friend_requests()
    friend_requests = []

    for request in friend_requests_query:
        from_user = djangoUser.objects.get(id=request[1])
        new_request = {'friend_request_id': request[0], 'from_user': from_user}
        friend_requests.append(new_request)


    # PART NOTIFICATIONS NEW EPISODES
    notifs = myuser.get_notifications()

    client = APIClient()

    alert = False
    # Thread to load the API calls to get the image and title of the different tv shows
    threads = [NotifThread(client, notif) for notif in notifs]
    new_episodes = []

    for th in threads:
        th.start()
        # Determine if there is at least one unseen notification
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

    return {'alert': (alert or len(friend_requests) > 0), 'friend_requests': friend_requests, 'new_episodes': new_episodes}