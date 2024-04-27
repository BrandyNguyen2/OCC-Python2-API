# PROGRAMMER: Brandy Nguyen
from WeatherReport import WeatherReport

# Test the WeatherReport class
tester = WeatherReport("Costa Mesa, California", "fahrenheit", "mph")
# Returns the city and State
print(tester.getCity())
# Returns the weather conditions
print(tester.currentWeatherConditions())
# Returns the specific weather condition (i.e. clear sky, rain, etc.)
print(tester.convertCurrentWeatherCondition())