#!/usr/bin/python3
"""Lists all states with a name starting with N from the database hbtn_0e_0_usa
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    with db.cursor() as cur:
        cur.execute("SELECT * FROM states \
            WHERE name LIKE BINARY 'N%' \
            ORDER BY id ASC")
        [print(row) for row in cur.fetchall()]
