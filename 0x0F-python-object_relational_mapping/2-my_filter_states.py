#!/usr/bin/python3
""" Write a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument."""

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
    cur.execute("SELECT * FROM states WHERE name = '{:s}' \
    ORDER BY id ASC".format(argv[4]))
    myresult = cur.fetchall()

    for x in myresult:
        if x[1] == argv[4]:
            print(x)
    cur.close()
    db.close()
