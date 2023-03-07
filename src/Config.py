import sqlite3 as sql
import time
from pathlib import Path
from WeatherData import WeatherData
class Config:
    def __str__(self):
        return f"{self.show_temperature}, {self.show_humidity}, {self.show_location}, {self.show_datetime}"

    def __init__(self):
        self.show_temperature=True
        self.show_humidity=True
        self.show_location=True
        self.show_datetime=True
        self.db_path="/dev/shm/weatherData.db"
        with sql.connect(self.db_path) as con: # creates db if it does not exist
            cursor = con.cursor()
            res = cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='config';")
            data = cursor.fetchone()
            if data is None:
                cursor.execute(f"CREATE TABLE config (show_temperature INTEGER, show_humidity INTEGER, show_location INTEGER, show_datetime INTEGER);")
                con.commit()

    def fetch_config(self):
        with sql.connect(self.db_path) as con:
            cursor = con.cursor()
            res = cursor.execute(f"SELECT * FROM config;")
            conf_data = res.fetchone()
            print(res)
            print(conf_data)
            if conf_data is not None:
                if conf_data[0] == 1:
                    self.show_temperature = True
                else:
                    self.show_temperature = False

                if conf_data[1] == 1:
                    self.show_humidity = True
                else:
                    self.show_humidity = False

                if conf_data[2] == 1:
                    self.show_location = True
                else:
                    self.show_location = False

                if conf_data[3] == 1:
                    self.show_datetime = True
                else:
                    self.show_datetime = False
            
