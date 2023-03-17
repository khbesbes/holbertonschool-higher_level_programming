#!/usr/bin/python3
"""
connect to database
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # Open database connection
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch all rows using fetchall() method.
    data = cursor.fetchall()
    # loop through the data and print results
    for row in data:
        print(row)
    # disconnect from server
    db.close()