import sqlite3

conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
cursor = conn.cursor()

def query(command, data=None):
    """
    :param command: SQL query
    :type command: string
    """
    if data == None:
        my_query = cursor.execute(command)
    else:
        my_query = cursor.execute(command, data)

    conn.commit()
    return my_query.fetchall()
