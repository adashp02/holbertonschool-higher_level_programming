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

    cursor.execute("SELECT * FROM `states`\
                   WHERE BINARY `name` = '{}'\
                    ORDER BY id".format(argv[4]))

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
