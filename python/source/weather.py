import requests
from config import get_config

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid={0}&zip={1},{2}&units={3}"


def fetch_weather(zip_code):
    settings = get_config()
    final_url = BASE_URL.format(settings["api_key"], zip_code, settings["country_code"],
                                settings["temp_unit"])
    weather_data = requests.get(final_url).json()
    return weather_data
