class WeatherData():
    def __init__(self):
        self._temperature = 0
        self._humidity = 0
        self._location = ""

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
