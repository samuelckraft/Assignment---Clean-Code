#Task 1
class Weather:
    def __init__(self, city, temperature, condition, humidity):
        self.city = city
        self.temperature = temperature
        self.condition = condition
        self.humidity = humidity

    def parse_weather_data(self):
        return f"Weather in {self.city}: {self.temperature} degrees, {self.condition}, Humidity: {self.humidity}%"

    def display_weather(self):
        print(weather_data[self.city])





weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
    }

NY_weather = Weather('New York', weather_data["New York"]['temperature'], weather_data["New York"]['condition'], weather_data["New York"]['humidity'])
London_weather = Weather('London', weather_data["London"]['temperature'], weather_data["London"]['condition'], weather_data["London"]['humidity'])
Tokyo_weather = Weather('Tokyo', weather_data["Tokyo"]['temperature'], weather_data["Tokyo"]['condition'], weather_data["Tokyo"]['humidity'])

NY_weather.parse_weather_data()
NY_weather.display_weather()