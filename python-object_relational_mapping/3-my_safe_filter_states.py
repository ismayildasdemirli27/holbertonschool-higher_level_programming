#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
Safe from MySQL injections!
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
    
    # %s istifadə etməklə kodu SQL İnyeksiyalarından qoruyuruq
    # Dəyişəni isə ikinci parametr kimi tuple şəklində (sys.argv[4],) göndəririk
    cur.execute("SELECT * FROM states WHERE name = %s "
                "ORDER BY states.id ASC", (sys.argv[4],))
    
    for row in cur.fetchall():
        print(row)
        
    cur.close()
    db.close()
