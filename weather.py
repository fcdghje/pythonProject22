import requests as r
import json
from datetime import datetime

def get_weather(city):
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {  # параметры для запроса
        'q': city.capitalize(),  # Пишет город с большой буквы
        'appid': '67515cfcb6644c41390aef34605f5f07',
        'units': 'metric',  # градусы в цельсиях
        'lang': 'ru'  # русский язык
    }
    response = r.get(url, params=params)
    if response.status_code == 200:
        data = response.json()

        today = datetime.today()
        forecast = []
        for line in data['list']:

            date = datetime.fromtimestamp(line['dt'])
            if date.day in [today.day + 1,today.day]:
                day ={
                    'date':datetime.strftime(date,'%d.%m,%H:%M'),
                    'temp' :round(line['main']['temp']),
                    'weather' :line['weather'][0]['description']
                }
                forecast.append(day)
        return forecast
    else:
        return None
with open('weather.json') as file:
    data = json.loads(file.read())






print(get_weather('Бебра'))