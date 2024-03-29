#!/usr/bin/python3

"""
script that takes in an argument
and displays all values in the states
table of hbtn_0e_0_usa where
name matches the argument.
(Safe from SQL injections)
"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cur = db.cursor()
    name = sys.argv[4]
    cur.execute(
        "SELECT * FROM states WHERE\
          states.name LIKE BINARY %s\
            ORDER BY states.id ASC", (name,)
    )
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
