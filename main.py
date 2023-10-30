import requests
import datetime
from pprint import pprint

import os
open_weather_token = os.environ.get("WEATHER_API_TOKEN", "")

def Get_Weather():

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001E328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        lat = 0
        lon = 0
        city = input("Укажите город: ")

        city_r = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={open_weather_token}")
        city_data = city_r.json()
        #pprint(city_data)

        lat = city_data[0]['lat']
        lon = city_data[0]['lon']

        weather_r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}&units=metric")
        weather_data = weather_r.json()
        pprint(weather_data)

        weather_description = weather_data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "На улице что-то непонятное"

        city = city_data[0]['local_names']['ru']
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        pressure = weather_data['main']['pressure']
        wind = weather_data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(weather_data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(weather_data['sys']['sunset'])
        length_of_the_day = datetime.datetime.fromtimestamp(weather_data['sys']['sunset']) - datetime.datetime.fromtimestamp(weather_data['sys']['sunrise'])

        print(city, temp, humidity, pressure, wind, sunrise_timestamp, sunset_timestamp, length_of_the_day)
        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе: {city}\n"
              f"Температура: {temp}°C {wd}\n"
              f"Влажность: {humidity}%\n"
              f"Давление: {pressure} мм.рт.ст\n"
              f"Скорость ветра: {wind} м/с\n"
              f"Время рассвета: {sunrise_timestamp}\n"
              f"Время заката: {sunset_timestamp}\n"
              f"Длина дня: {length_of_the_day}\n")

    except Exception as ex:
        print(ex)
        print('Проверьте название города')

Get_Weather()


