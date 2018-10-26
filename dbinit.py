import sqlite3

conn = sqlite3.connect('tvchaud.db')

cursor = conn.cursor()

# Table : FAVORITE
cursor.execute("""
    CREATE TABLE favorite (
        favorite_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        user_id INTEGER,
        tv_id INTEGER,
        insert_date DATETIME
    )
""")

# Table : FRIENDSHIP
cursor.execute("""
    CREATE TABLE friendship (
        friendship_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        user_id_1 INTEGER,
        user_id_2 INTEGER,
        insert_date DATETIME
    )
""")

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

# Table : NOTIFICATION_TYPE
cursor.execute("""
    CREATE TABLE notification_type (
        notification_type_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name VARCHAR(85),
        insert_date DATETIME,
        update_date DATETIME
    )
""")
cursor.execute("""
    INSERT INTO notification_type(name, insert_date, update_date) VALUES
    ('New episode', DATETIME(), DATETIME()),
    ('Friend Request', DATETIME(), DATETIME())
""")

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



conn.commit()
conn.close()
