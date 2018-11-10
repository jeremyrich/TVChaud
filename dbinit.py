import sqlite3

try:

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    ########################
    ######## PART 1 ########
    ########################

    # We are going to create a few users to populate the database
    cursor.execute("""
        INSERT INTO auth_user(password, is_superuser, username, first_name, email, is_staff, is_active, date_joined, last_name) VALUES
        ('pbkdf2_sha256$120000$Tr2zPMf80uil$Pb93LIje8eKuzniey2zGi/KMnxJgXPhzB43rZiPJ+dk=', 0, 'user1', '', '', 0, 1, DATETIME(), ''),
        ('pbkdf2_sha256$120000$Tr2zPMf80uil$Pb93LIje8eKuzniey2zGi/KMnxJgXPhzB43rZiPJ+dk=', 0, 'user2', '', '', 0, 1, DATETIME(), ''),
        ('pbkdf2_sha256$120000$Tr2zPMf80uil$Pb93LIje8eKuzniey2zGi/KMnxJgXPhzB43rZiPJ+dk=', 0, 'user3', '', '', 0, 1, DATETIME(), ''),
        ('pbkdf2_sha256$120000$Tr2zPMf80uil$Pb93LIje8eKuzniey2zGi/KMnxJgXPhzB43rZiPJ+dk=', 0, 'user4', '', '', 0, 1, DATETIME(), ''),
        ('pbkdf2_sha256$120000$Tr2zPMf80uil$Pb93LIje8eKuzniey2zGi/KMnxJgXPhzB43rZiPJ+dk=', 0, 'user5', '', '', 0, 1, DATETIME(), '')
    """)


    ########################
    ######## PART 2 ########
    ########################

    # We create our custom tables in the database

    # Table : FAVORITE
    cursor.execute("""
        CREATE TABLE favorite (
            favorite_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            user_id INTEGER,
            tv_id INTEGER
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
            to_user INTEGER
        )
    """)


    ########################
    ######## PART 3 ########
    ########################

    # We insert in the tables some rows for examples
    cursor.execute("""
        INSERT INTO favorite(user_id, tv_id) VALUES
        (1, 60735),
        (1, 1402),
        (2, 456),
        (3, 1425),
        (4, 1622)
    """)

    cursor.execute("""
        INSERT INTO notification(user_id, tv_id, season, episode, seen) VALUES
        (1, 60735, 5, 4, 1),
        (1, 1402, 9, 8, 0),
        (2, 456, 30, 6, 0)
    """)

    cursor.execute("""
        INSERT INTO friendship(user_id_1, user_id_2) VALUES
        (1, 2),
        (1, 3)
    """)

    cursor.execute("""
        INSERT INTO friend_request(from_user, to_user) VALUES
        (2, 5),
        (3, 5)
    """)

    conn.commit()
    conn.close()

    print('Database created with success !')

except sqlite3.OperationalError as exce:

    print('Error while creating the database')
    print(exce)

