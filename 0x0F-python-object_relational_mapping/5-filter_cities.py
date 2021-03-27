#!/usr/bin/python3
'''
Script that lists all cities from the database hbtn_0e_4_usa
'''
import MySQLdb
from sys import argv


def mysqlconnect():
    '''
    Script that lists all cities from the database hbtn_0e_4_usa
    '''
    db_connection = MySQLdb.connect('localhost', argv[1], argv[2],
                                    argv[3], port=3306)
    cursor = db_connection.cursor()
    cursor.execute("SELECT DISTINCT cities.name FROM cities INNER JOIN \
                    states ON cities.state_id = states.id WHERE \
                    states.name = %s", (argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        if (row[0] != rows[0][0]):
            print(", ", end='')
        print(row[0], end='')
    print()
    cursor.close()
    db_connection.close()


if __name__ == '__main__':
    mysqlconnect()
