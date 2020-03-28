#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities JOIN states ON cities.state_id=states.id \
                ORDER BY cities.id;")
    myresult = cur.fetchall()
    for x in myresult:
        print(x)
    cur.close()
    db.close()
