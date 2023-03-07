import sqlite3 as sql

db = sql.connect("/dev/shm/weatherData.db")
c = db.cursor()
res = c.execute("SELECT temperature, humidity, location FROM weatherData WHERE timestamp = (SELECT max(timestamp) FROM weatherData)")
#res = c.execute("SELECT * FROM weatherData")
r = res.fetchone()
print(r[0])
