import cv2 as cv
import numpy as np
import subprocess
import time
from StreamWriter import StreamWriter
from StreamReader import StreamReader
from WeatherData import WeatherData
from Config import Config
import sqlite3 as sql

db = sql.connect("/dev/shm/weatherData.db")
c = db.cursor()

weather_data = WeatherData()
config = Config()

print("Start")
rtmp_endpoint = "rtmp://127.0.0.1:1935/raw"
target_endpoint = "rtsp://127.0.0.1:8554/live"

stream_reader = StreamReader(rtmp_endpoint)
stream_writer = StreamWriter(target_endpoint, "h264", "yuv420p", stream_reader.getWidth(), stream_reader.getHeight(), stream_reader.getFPS())

streamAvailable = False

while not streamAvailable:
    ret, frame = stream_reader.read()
    if ret:
        streamAvailable=True
    print("Cannot open Stream")

print("Opened RTMP endpoint")

def addTextToFrame(frame, width, height, pos, text):
    #overlay = cv.cvtColor(frame, )

    font_face = cv.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    font_color = (255,255,255,255)
    font_thickness = 1
    text_size, _ = cv.getTextSize(text, font_face, font_scale, font_thickness)
    text_w, text_h = text_size

    if pos == "location" and config.show_location:
        x,y = (0, text_h)
    elif pos == "datetime" and config.show_datetime:
        x,y = (width - text_w, text_h)
    elif pos == "temperature" and config.show_temperature:
        x,y = (0, height - 2 * text_h)
    elif pos == "humidity" and config.show_humidity:
        x,y = (width - text_w, height - 2 * text_h)
    else:
        print("Wrong pos type")
        return
        

    cv.rectangle(frame, (x,y), (x+text_w, y+text_h), (0,0,0,0.5),-1)
    return cv.putText(
        frame,
        text,
        (x,y+text_h+font_scale-1),
        font_face, #font family
        font_scale,
        font_color,
        font_thickness)

while stream_reader.isOpened():
    width = stream_reader.getWidth()
    height = stream_reader.getHeight()

    ret, frame = stream_reader.read()
    if not ret:
        print("Could not read frame")
    
    weather_data.fetch_data()

    overlay_data = []

    if config.show_temperature:
        overlay_data.append(("temperature", f"Temp: {weather_data.getTemperature()} deg."))
    if config.show_humidity:
        overlay_data.append(("humidity", f"{weather_data.getHumidity()}"))
    if config.show_location:
        overlay_data.append(("location", f"{weather_data.getLocation()}"))
    if config.show_datetime:
        overlay_data.append(("datetime", f"{time.asctime()}"))

    print(overlay_data)
        
    for entry in overlay_data:
        dtype, text = entry
        print(entry)
        frame = addTextToFrame(frame, width, height, dtype, text)
    cv.waitKey(1)
    ret, img = cv.imencode('.png',frame)

    stream_writer.writeToStream(img.tobytes())
stream_reader.release()
    
cv.destroyAllWindows()

if __name__ == " __main__":
    print("Creating Overlay Stream")
