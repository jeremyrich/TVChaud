class Notification():
    def __init__(self, user_id, text=None):
        self.user_id = user_id
        self.seen = 0



# Table : NOTIFICATION
cursor.execute("""
    CREATE TABLE notification (
        notification_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        user_id INTEGER,
        message TEXT,
        notification_type_id INTEGER,
        seen TINYINT(1),
        insert_date DATETIME,
        update_date DATETIME
    )
""")
