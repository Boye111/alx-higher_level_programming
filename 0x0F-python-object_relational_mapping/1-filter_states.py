#!/usr/bin/python3
"""
lists all states with a name starting with N
"""


import MySQLdb
from sys import argv

if __name__ = '__main__':
    """ filter states by letter """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         password=argv[2], db_name=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
            WHERE name LIKE BINARY 'N%'")

    rows = cur.fetchall()

    for row in rows:
        print(row)
