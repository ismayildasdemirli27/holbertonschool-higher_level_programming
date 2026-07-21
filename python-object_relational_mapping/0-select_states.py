#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Verilənlər bazasına qoşulma
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    # Kursor yaradılması və sorğunun icrası
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Nəticələrin ekrana yazdırılması
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
        
    # Əlaqələrin bağlanması
    cur.close()
    db.close()
