#!/usr/bin/python3
"""script that selects states from database"""


if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    cursor = db.cursor()

    cursor.execute('SELECT * FROM states')

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
