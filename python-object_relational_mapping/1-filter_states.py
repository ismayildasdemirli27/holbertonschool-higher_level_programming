<<<<<<< HEAD
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

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = 'SELECT * FROM states WHERE BINARY name LIKE "N%";'
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
=======
#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    cur = db.cursor()
    # BINARY açar sözü yalnız böyük N hərfi ilə başlayanları tapmağı təmin edir
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
        
    cur.close()
    db.close()
>>>>>>> 2fdd82f (Task 1: Filter states strictly starting with upper N)
