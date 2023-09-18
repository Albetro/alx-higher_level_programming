#!/usr/bin/python3
"""
Writing a safe SQL injection by use of placeholders makes user
input to be treated as data and not as sql code
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    state = sys.argv[4]
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name = %s\
              ORDER BY states.id ASC", (state,))
    mydata = c.fetchall()
    for row in mydata:
        print(row)

    c.close()
    db.close()
