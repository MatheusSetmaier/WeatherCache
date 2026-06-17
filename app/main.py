from fastapi import FastAPI
from app.weatherService import get_weather

app = FastAPI()


@app.get('/')
def home():
    return{'funcionando'}

@app.get('/weather/{cidade}')
def buscarClima(cidade: str):
    return get_weather(cidade)