import sqlite3

conn = sqlite3.connect('tvchaud.db')

cursor = conn.cursor()

# Table : FAVORITE
cursor.execute("""
    CREATE TABLE favorite (
        favorite_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        user_id INTEGER,
        tv_id INTEGER
    )
""")

# Table : FRIENDSHIP
cursor.execute("""
    CREATE TABLE friendship (
        friendship_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        user_id_1 INTEGER,
        user_id_2 INTEGER
    )
""")

# Table : FRIEND_REQUEST
cursor.execute("""
    CREATE TABLE friend_request (
        friend_request_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        from_user INTEGER,
        to_user INTEGER,
        message TEXT,
        seen TINYINT(1)
    )
""")

# Table : EPISODE_SEEN
# table pour stocker les épisodes déjà vus par un user (utilisé seulement pour ses favoris), permet de créer des notifications à la sortie d'un nouvel épisode
cursor.execute("""
    CREATE TABLE episode_seen (
        episode_seen_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        user_id INTEGER,
        tv_id INTEGER,
        season INTEGER,
        episode INTEGER
    )
""")

# Table : NOTIFICATION
cursor.execute("""
    CREATE TABLE notification (
        notification_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        user_id INTEGER,
        tv_id INTEGER,
        season INTEGER,
        episode INTEGER,
        seen TINYINT(1)
    )
""")

# insert into notification for example
cursor.execute("""
    INSERT INTO notification(user_id, tv_id, season, episode, seen) VALUES
    (1, 60735, 5, 4, 0),
    (1, 1402, 9, 8, 1)
""")



conn.commit()
conn.close()
