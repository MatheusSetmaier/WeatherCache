from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.weatherService import get_weather

app = FastAPI()

app.mount('/static', StaticFiles(directory = 'static'), name = 'static')

@app.get('/')
def home():
    return FileResponse('static/index.html')

@app.get('/weather/{cidade}')
def buscarClima(cidade: str):
    return get_weather(cidade)