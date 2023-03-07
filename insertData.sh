#sqlite3 /dev/shm/weatherData.db "INSERT INTO weatherData VALUES ($(date +%s), $(cat /sys/class/thermal/thermal_zone2/temp)/1000, 20, 'Fulda');"
#!/bin/bash

while :
do
  sleep 2
  TEMP=$(($(cat /sys/class/thermal/thermal_zone2/temp)/1000))
  HUM=75
  LOC=Fulda
  curl -X POST -d "temperature=$TEMP" -d "humidity=$HUM" -d "location=$LOC" http://127.0.0.1:5000/weather_data
done