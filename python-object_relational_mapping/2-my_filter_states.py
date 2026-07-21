#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
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
    # Şərtə uyğun olaraq BINARY və .format() istifadə edirik
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
    cur.execute(query.format(sys.argv[4]))
    
    for row in cur.fetchall():
        print(row)
        
    cur.close()
    db.close()
