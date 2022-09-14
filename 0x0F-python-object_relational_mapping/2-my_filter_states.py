#!/usr/bin/python3
"""
displays values of states
"""


import MySQLdb
from sys import argv

if __name__ = '__main__':
    """ displays states that me match arguement """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         password=argv[2], db_name=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
            WHERE name LIKE BINARY '{}' \
            ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)
