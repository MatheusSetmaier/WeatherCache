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
        f'https://weather.visualcrossing.com/'
        f'VisualCrossingWebServices/rest/services/timeline/'
        f'{cidade}?key={API_KEY}'
    )

    response = requests.get(url)

    dados = response.json()

    traducao = {
    'Overcast': 'Nublado',
    'Clear': 'Céu limpo',
    'Partially cloudy': 'Parcialmente nublado',
    'Rain': 'Chuva',
    'Snow': 'Neve'
}
    
    resultado = {
    'cidade': dados['resolvedAddress'],
    'temperatura': dados['currentConditions']['temp'],
    'sensacao_termica': dados['currentConditions']['feelslike'],
    'umidade': dados['currentConditions']['humidity'],
    'condicao': traducao.get(
        dados['currentConditions']['conditions'],
        dados['currentConditions']['conditions']
    )
}

    redis_client.set(
        cidade,
        json.dumps(resultado),
        ex = 43200
    )

    return resultado