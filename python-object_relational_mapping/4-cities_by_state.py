#!/usr/bin/python3
"""safe from injection
script that lists states that match the argument supplied by user"""


if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    cursor = db.cursor()

    cursor.execute('SELECT c.id, c.name, s.name\
                   FROM cities AS c\
                   INNER JOIN states AS s ON s.id = c.state_id\
                   ORDER BY c.id ASC')

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
