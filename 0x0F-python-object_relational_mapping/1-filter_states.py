#!/usr/bin/python3
"""
Filter states
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':

    data_base = MySQLdb.connect(host="localhost",
                                port=3306,
                                user=argv[1],
                                passwd=argv[2],
                                db=argv[3],
                                charset="utf8")
    cur = data_base.cursor()
    cur.execute(""" SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id
    ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    data_base.close()
