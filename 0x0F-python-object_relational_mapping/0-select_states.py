#!/usr/bin/python3
''' Script that lists all states from the database hbtn_0e_0_usa '''
import MySQLdb
from sys import argv


def mysqlconnect():
    ''' Script that lists all states from the database hbtn_0e_0_usa '''
    db_connection = MySQLdb.connect('localhost', argv[1], argv[2],
                                    argv[3], port=3306)
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM states;')
    for x in cursor:
        print(x)
    db_connection.close()


if __name__ == '__main__':
    mysqlconnect()
