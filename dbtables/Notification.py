class Notification():
    def __init__(self, user_id, text=None, notification_type_id):
        if text is not None:
            self.text = text
        self.user_id = user_id
        self.seen = 0
        self.notification_type_id = notification_type_id

    def read_notification(self):
        self.seen = 1
