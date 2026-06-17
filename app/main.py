from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return{'mensagem': 'WeatherCache API funcionando'}

@app.get('/weather/{cidade}')
def buscarClima(cidade: str):
    return{'cidade': cidade}