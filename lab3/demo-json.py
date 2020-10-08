#!/usr/bin/env python3
import sqlite3
import json
from urllib.parse import urlencode
from urllib.request import urlopen

# The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa
# As of October 2015, you need an API key.
# I have registered under my Carleton email.

apiKey = "a808bbf30202728efca23e099a4eecc7" # If it doesn’t work, get your own.
# Query the user for a city
city = input("Enter the name of a city whose weather you want: ")
# Build the URL parameters
params = {"q":city, "units":"imperial", "APPID":apiKey }
arguments = urlencode(params)
# Get the weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments
print (url)
webData = urlopen(url)
results = webData.read().decode('utf-8')
# results is a JSON string
webData.close()
print("JSON: " + results)

# Convert the json result to a dictionary
# See http://openweathermap.org/current#current_JSON for the API
data = json.loads(results)
# Print the results
current = data["main"]
degreeSym = chr(176)

# Connect to database
connection = sqlite3.connect('mydb.db')

# Create cursor
c = connection.cursor()

#
c.execute(""" CREATE TABLE IF NOT EXISTS meteomatics(
    city TEXT,
    temperature_in_F NUMERIC,
    humidity_percentage NUMERIC,
    pressure NUMERIC,
    wind TEXT
                    )""")

db_data = (city, current["temp"], current["humidity"], current["pressure"], str(data["wind"]["speed"]))


c = connection.cursor()
# print(db_data)

# Add data to database
c.execute("INSERT INTO meteomatics VALUES(?, ?, ?,?,? ) ; ", db_data)

# Commit our commands
connection.commit()

# Close our connection
connection.close()

print("Temperature: %d%sF" % (current["temp"], degreeSym))
print("Humidity: %d%%" % current["humidity"])
print("Pressure: %d" % current["pressure"])
current = data["wind"]
print("Wind : %d" % current["speed"])
