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
    [
        ["kitchen", 20.6],
        ["greenhouse", 26.3],
        ["garage", 18.6]
    ],
    [
        ["kitchen", 19.5],
        ["greenhouse", 15.1],
        ["kitchen", 18.1]
    ],
    [
        ["kitchen", 21.2],
        ["greenhouse", 27.1],
        ["garage", 19.1]
    ]
]

# Execute multiple commands

c.executemany("INSERT INTO temps VALUES(date('now', '-1 day'), time('now'), ?,? ) ; ", data[0])

c.executemany("INSERT INTO temps VALUES(date('now'), time('now', '-12 hours'), ?,? ) ; ", data[1])

c.executemany("INSERT INTO temps VALUES(date('now'), time('now'), ?,? ) ; ", data[2])

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
