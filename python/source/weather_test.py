import time
import requests
from pprint import pprint

settings = {
    'api_key': '***REMOVED***',
    'zip_code': '45128',
    'country_code': 'de',
    'temp_unit': 'metric'} # unit can be metric, imperial, or kelvin

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid={0}&zip={1},{2}&units={3}"

while True:
    final_url = BASE_URL.format(settings["api_key"], settings["zip_code"], settings["country_code"], settings["temp_unit"])
    weather_data = requests.get(final_url).json()
    pprint(weather_data)

    pprint(weather_data['main']['temp'])

    time.sleep(20) # get new data every 20 seconds