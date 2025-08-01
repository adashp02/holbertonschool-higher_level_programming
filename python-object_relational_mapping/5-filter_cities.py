#!/usr/bin/python3
"""lists all cities that match state supplied as an arg - inner join"""


if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    cursor = db.cursor()

    cursor.execute('SELECT c.name, s.name\
                   FROM cities AS c\
                   INNER JOIN states AS s\
                   ON s.id = c.state_id')

    cities = []
    for city in cursor.fetchall():
        if city[1] == argv[4]:
            cities.append(city[0])
    print(", ".join(cities))

    cursor.close()
    db.close()
