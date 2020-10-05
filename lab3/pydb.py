#!/usr/bin/env python3
import sqlite3

# Create temporary database
connection = sqlite3.connect('mydb.db')

# Create cursor
c = connection.cursor()

#
c.execute(""" CREATE TABLE IF NOT EXISTS temps(
    tdate DATE,
    ttime TIME,
    zone TEXT,
    temperature NUMERIC
                    )""")

data = [
                ("date('now', '-1 day')", "time('now')", "kitchen", 20.6),
                ("date('now', '-1 day')", "time('now')", "greenhouse", 26.3),
                ("date('now', '-1 day')", "time('now')", "garage", 18.6),
                ("date('now')", "time('now', '-12 hours')", "kitchen", 19.5),
                ("date('now')", "time('now', '-12 hours')", "greenhouse", 15.1),
                ("date('now')", "time('now', '-12 hours')", "kitchen", 18.1),
                ("date('now')", "time('now')", "kitchen", 21.2),
                ("date('now')", "time('now')", "greenhouse", 27.1),
                ("date('now')", "time('now')", "garage", 19.1)
                ]

# Execute multiple commands
c.executemany("INSERT INTO temps VALUES(?, ?, ?,? ) ; ", data)

# Query the database
c.execute("SELECT * FROM temps")

# Commit our commands
connection.commit()

# Print the results
print(c.fetchall())






# ----------------------- PART 4 --------------------------------------

c.execute(""" CREATE TABLE IF NOT EXISTS sensors( 
    sensorID INTEGER PRIMARY KEY ,
    type TEXT,
    zone TEXT
                    )""")

data = [
                (1, "door", "kitchen"),
                (2, "temperature", "kitchen"),
                (3, "door", "garage"),
                (4, "motion", "garage"),
                (5, "temperature", "garage"),
                ]



# Execute multiple commands
c.executemany("INSERT INTO sensors VALUES(?, ?, ? ) ; ", data)


# Query the database
c.execute("SELECT * FROM sensors")

# Commit our commands
connection.commit()

# Print the results
print(c.fetchall())



# Close our connection
connection.close()
