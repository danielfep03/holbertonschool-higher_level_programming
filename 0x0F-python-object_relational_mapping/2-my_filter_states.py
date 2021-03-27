#!/usr/bin/python3
'''
Script that lists all states with a name
starting with N from the database hbtn_0e_0_usa
'''
import MySQLdb
from sys import argv


def mysqlconnect():
    '''
    Script that lists all states with a name
    starting with N from the database hbtn_0e_0_usa
    '''
    db_connection = MySQLdb.connect('localhost', argv[1], argv[2],
                                    argv[3], port=3306)
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
        id ASC".format(argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db_connection.close()

if __name__ == '__main__':
    mysqlconnect()
