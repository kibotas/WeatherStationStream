#!/usr/bin/env python
# encoding: utf-8
import json

# https://docs.python.org/3/library/sqlite3.html#sqlite3.connect
import sqlite3 as sql
import time
from pathlib import Path
from WeatherData import WeatherData


# https://flask.palletsprojects.com/en/2.2.x/quickstart/#about-responses
from flask import Flask, request, jsonify

data_keys = ["temperature", "humidity", "location"]
weather_data = WeatherData()

db_path = "/dev/shm/weatherData.db"
db = "weatherdata"

if not Path(db_path).exists():
    with sql.connect(db_path) as con:
        con.execute(f"CREATE TABLE {db} (timestamp INTEGER, temperature REAL, humidity REAL, location VARCHAR(80))")
        con.commit()


app = Flask(__name__)

@app.route('/weather_data', methods=['POST'])
def update_record():
    #data = json.loads(request.data)
    data = request.args
    tmp_dict = {}
    #for k,v in request.args:
    print(request.form)
    for k,v in request.form.items():
        print(k,v)
        if k == "temperature":
            # ToDo: Verify that MultiDicts keys are unique
            weather_data.setTemperature(float(v))
        elif k == "humidity":
            weather_data.setHumidity(float(v))
        elif k == "location":
            weather_data.setLocation(str(v))
    #print(data.get('temperature', 0))
    #print(data.keys())
    print(weather_data.getTemperature())
    print(weather_data.getLocation())
    print(weather_data.getHumidity())

    with sql.connect(db_path) as con: # creates db if it does not exist
        cursor = con.cursor()
        cursor.execute(f"INSERT INTO {db} VALUES {time.time(), weather_data.getTemperature(), weather_data.getHumidity(), weather_data.getLocation()}")
        con.commit()

        #f.write(json.dumps(new_records, indent=2))
    #return jsonify(record)

    return "Success"

@app.route('/show_overlay', methods=['POST'])
def show_overlay():
    print(request.data)
    data = json.loads(request.data)

    if data['value'] == 'True':
        show_values = 1
    else:
        show_values = 0

    with sql.connect(db_path) as con:
        cursor = con.cursor()
        cursor.execute(f"UPDATE config SET show_temperature={show_values}, show_humidity={show_values}, show_location = {show_values}, show_datetime = {show_values}")
        con.commit()

        #f.write(json.dumps(new_records, indent=2))
    #return jsonify(record)

    return "Success"
