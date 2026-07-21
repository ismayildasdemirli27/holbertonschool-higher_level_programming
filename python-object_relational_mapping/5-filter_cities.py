#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa. Safe from SQL injections.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = db.cursor()
    
    # Cədvəlləri JOIN edirik və parametrlə inyeksiyadan qoruyuruq
    query = ("SELECT cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s ORDER BY cities.id ASC")
    cur.execute(query, (sys.argv[4],))
    
    # Yalnız şəhər adlarını alıb, vergül və boşluqla bir sətirdə birləşdiririk
    print(", ".join([row[0] for row in cur.fetchall()]))
    
    cur.close()
    db.close()
