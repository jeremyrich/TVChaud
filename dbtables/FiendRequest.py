class FriendReques():



# Table : FRIEND_REQUEST
cursor.execute("""
    CREATE TABLE friend_request (
        friend_request_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        from_user INTEGER,
        to_user INTEGER,
        message TEXT,
        insert_date DATETIME
    )
""")