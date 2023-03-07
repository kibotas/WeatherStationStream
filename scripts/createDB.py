import sqlite3 as sql

db = sql.connect("/dev/shm/weatherData.db")
c = db.cursor()

c.execute("CREATE TABLE weatherData(timestamp INTEGER, temperature REAL, humidity REAL, location VARCHAR(80))")
#c.execute("INSERT INTO weatherData VALUES()
