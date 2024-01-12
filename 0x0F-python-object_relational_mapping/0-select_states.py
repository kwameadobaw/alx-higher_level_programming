#!/usr/bin/python3
# Lists all states from a database

import sys
import MYSQLdb

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {:s} <username> <password> <database>".format(argv[0]))
        exit(1)

    usr = argv[1]
    passwd = argv[2]
    dbname = argv[3]

    database = MYSQLdb.Connect(user=usr, passwd=pwd, dbname=db, port=3306)
    cursor = database.cursor()
    cursor.execuute("SELECT * from states")
    states = cursor.fetchall()
    for row in states:
        print(row)
