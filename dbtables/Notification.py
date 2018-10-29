from database_helper import query

class Notification:

    def __init__(self, notification_id, user_id, tv_id, season, episode, seen):
        self.__notification_id = notification_id
        self.__user_id = user_id
        self.__tv_id = tv_id
        self.__season = season
        self.__episode = episode
        self.__seen = seen

    # getters
    def _get_notification_id(self):
        return self.__notification_id

    def _get_user_id(self):
        return self.__user_id

    def _get_tv_id(self):
        return self.__tv_id

    def _get_season(self):
        return self.__season

    def _get_episode(self):
        return self.__episode

    def _is_seen(self):
        return self.__seen

    # setters
    def _change_seen(self):
        self.__seen = not self.__seen

    # properties
    notification_id = property(_get_notification_id)
    user_id = property(_get_user_id)
    tv_id = property(_get_tv_id)
    season = property(_get_season)
    episode = property(_get_episode)
    seen = property(_is_seen, _change_seen)


    # static methods
    @staticmethod
    def check_as_seen(notif_id):
        command = """UPDATE notification SET seen = 1 WHERE notification_id = ?"""
        data = (notif_id,)
        query(command, data)

    @staticmethod
    def check_seen_unseen(notif_id):
        command = """UPDATE notification SET seen = (CASE WHEN seen = 1 THEN 0 ELSE 1 END) WHERE notification_id = ?"""
        data = (notif_id,)
        query(command, data)