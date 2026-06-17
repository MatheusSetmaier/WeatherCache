import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY')

def get_weather(cidade: str):
    url = (
        f"https://weather.visualcrossing.com/"
        f"VisualCrossingWebServices/rest/services/timeline/"
        f"{cidade}?key={API_KEY}"
    )

    response = requests.get(url)
    return response.json()
