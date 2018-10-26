import sqlite3

conn = sqlite3.connect('tvchaud.db', check_same_thread=False)
cursor = conn.cursor()

def query(command, data=None):
    """
    :param command: SQL query
    :type command: string
    """
    if data == None:
        my_query = cursor.execute(command)
        my_query = my_query.fetchall()
    else:
        my_query = cursor.execute(command, data)

    conn.commit()
    return my_query
