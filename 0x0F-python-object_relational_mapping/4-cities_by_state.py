#!/usr/bin/python3
"""
lists all cities in a database
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ lists cities in the db """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         password=argv[2], db=argv[3])
    with db.cursor() as cur:
        cur.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            ORDER BY
                cities.id ASC
        """)

        rows = cur.fetchall()

        if rows is not None:
            for row in rows:
                print(row)
