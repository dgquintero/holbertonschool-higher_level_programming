#!/usr/bin/python3
""" script that lists all states from the database
hbtn_0e_0_usa starting with N"""

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
	cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
	myresult = cur.fetchall()

	for x in myresult:
		if x[1][0] == 'N':
			print(x)
	cur.close()
	db.close()
