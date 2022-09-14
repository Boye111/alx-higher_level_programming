#!/usr/bin/python3
"""
a script that lists all states from the database
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ get states from database """
    db = MySQLd.connect(host="localhost", user=argv[1], port=3306, password=argv[2], db_name=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
