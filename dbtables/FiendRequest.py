class FriendRequest():
    def __init__(self, from_user, to_user, text=None):
        self.user_id = from_user
        self.to_user = to_user
        if text is not None:
            self.text = text
        self.request = 0



