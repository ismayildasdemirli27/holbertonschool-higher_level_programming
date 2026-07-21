#!/usr/bin/python3
"""
this is global enviroment
"""


import sys
import MySQLdb

if __name__ == "__main__":
    """
        this is local enviroment
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = 'SELECT * FROM states WHERE BINARY name = "{}"'.format(name)
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
