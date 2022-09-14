#!/usr/bin/python3
"""
list all cities in a state
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ all cities in a state """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         password=argv[2], db=argv[3])
    with db.cursor as cur:
        cur.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
            })

        rows = cur.fetchall()

        if row is not None:
            print(", ".join([row[1] for row in rows]))
