import time
import requests
from pprint import pprint
from config import get_config


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid={0}&zip={1},{2}&units={3}"

while True:
    settings = get_config()
    final_url = BASE_URL.format(settings["api_key"], settings["zip_code"], settings["country_code"], settings["temp_unit"])
    weather_data = requests.get(final_url).json()
    pprint(weather_data)

    pprint(weather_data['main']['temp'])

    time.sleep(20)