from series.APIClient import APIClient

class Favorite():
    def __init__(self, user_id, tv_id):
        self.user_id = user_id
        self.tv_id = tv_id

    def get_favorite_details(self):
        client = APIClient()
        details = client.get_tv_show_details(self.tv_id)
        return details