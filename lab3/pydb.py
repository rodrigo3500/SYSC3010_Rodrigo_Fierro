#!/usr/bin/env python3
import sqlite3
# connect to database file
dbconnect = sqlite3.connect("mydb.db")

# If we want to access columns by name we need to set
# row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row

#  we create a cursor to work with db
cursor = dbconnect.cursor()

# execute insert statement
cursor.execute('''insert into temps values ('2013-10-09',time('now'),"kitchen",2.1 )''')
dbconnect.commit()

# execute simple select statement
cursor.execute('SELECT * FROM temps')

# print data
for row in cursor:
    print(row['tdate'], row['ttime'], row['zone'], row['temperature'])
# close the connection
dbconnect.close()
