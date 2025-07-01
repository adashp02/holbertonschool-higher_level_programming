#!/usr/bin/python3
"""script that lists states that match the argument supplied by user"""


if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    cursor = db.cursor()

    cursor.execute('SELECT * FROM states ORDER BY id')

    for state in cursor.fetchall():
        if state[1] == argv[4]:
            print(state)

    cursor.close()
    db.close()
