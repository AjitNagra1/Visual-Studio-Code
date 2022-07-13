class Weather:
    def __init__(self, temperature, wind_speed, wind_direction):
        self.temperature=temperature
        self.wind_speed=wind_speed
        self.wind_direction=wind_direction
    
    def weather_in_your_location(self):
        print(f"The weather in your location: {self.temperature} degrees and {self.wind_speed} m/s and {self.wind_direction} direction")
    
class VerbalWeather(Weather):
    def verbal_weather_in_your_location(self):
        if self.temperature > 20:
            self.temperature="warm"
        else:
            self.temperature="cold"
        
        if self.wind_speed > 30:
            self.wind_speed="windy"
        else:
            self.wind_speed="not windy"
        
        print(f"The weather in your location: {self.temperature} and {self.wind_speed} and {self.wind_direction} direction")


w1=Weather(20,10,"north")
w1.weather_in_your_location()

w2=VerbalWeather(10,60,"south")
w2.verbal_weather_in_your_location()
    


