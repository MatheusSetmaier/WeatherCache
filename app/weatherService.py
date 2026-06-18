import os
import json
import requests
from dotenv import load_dotenv
from app.redisClient import redis_client

load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY')

def get_weather(cidade: str):

    cache = redis_client.get(cidade)

    if cache:
        print('Dados retirados do cache')
        return json.loads(cache)
    print('Dados retirados da API')

    url = (
        f"https://weather.visualcrossing.com/"
        f"VisualCrossingWebServices/rest/services/timeline/"
        f"{cidade}?key={API_KEY}"
    )

    response = requests.get(url)

    dados = response.json()

    redis_client.set(
        cidade,json.dumps(dados),
        ex = 43200
    )

    return dados