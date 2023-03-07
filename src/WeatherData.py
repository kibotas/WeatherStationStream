import sqlite3 as sql

class WeatherData():
    def __init__(self):
        self._temperature = 0
        self._humidity = 0
        self._location = ""
        self.db_path="/dev/shm/weatherData.db"

    def setTemperature(self, temp):
        self._temperature=temp

    def getTemperature(self):
        return self._temperature
        
    def setHumidity(self,humidity):
        self._humidity=humidity

    def getHumidity(self):
        return self._humidity
        
    def setLocation(self,location):
        self._location=location

    def getLocation(self):
        return self._location

    def fetch_data(self):
        with sql.connect(self.db_path) as con:
            res = con.execute("SELECT temperature, humidity, location FROM weatherData WHERE timestamp = (SELECT max(timestamp) FROM weatherData)")
            query_data = res.fetchone()

            if query_data is not None:
                self.setTemperature(query_data[0])
                self.setHumidity(query_data[1])
                self.setLocation(query_data[2])
