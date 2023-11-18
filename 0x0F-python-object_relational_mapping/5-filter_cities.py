#!/usr/bin/python3
"""
    A script that takes in the name of a state as
    an argument and lists all cities of that state,
    using the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb as db

if __name__ == "__main__":
    connection = db.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    cursor = connection.cursor()

    query = "SELECT cities.name FROM cities \
            INNER JOIN states ON cities.state_id = states.id \
            WHERE states.name = %(search_state)s \
            ORDER BY cities.id ASC"

    cursor.execute(query, {'search_state': argv[4]})

    selected_row = cursor.fetchall()

    if selected_row is not None:
        print(", ".join([row[0] for row in selected_row]))
