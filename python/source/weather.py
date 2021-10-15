import requests

settings = {
    'api_key': '***REMOVED***',
    'zip_code': '45128',
    'country_code': 'de',
    'temp_unit': 'metric'}  # unit can be metric, imperial, or kelvin

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid={0}&zip={1},{2}&units={3}"


def fetch_weather(zip_code):
    final_url = BASE_URL.format(settings["api_key"], zip_code, settings["country_code"],
                                settings["temp_unit"])
    weather_data = requests.get(final_url).json()
    return weather_data
