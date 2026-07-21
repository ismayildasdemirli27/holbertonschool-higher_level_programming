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
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = """
        SELECT cities.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
    cursor.execute(query, (state, ))

    states = cursor.fetchall()
    states_new = []
    for state in states:
        states_new.append(state[0])
    print(", ".join(states_new))

    cursor.close()
    db.close()
