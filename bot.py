import logging

import requests
import datetime

from random import randint

from aiogram import Bot, Dispatcher, executor, types

import os

API_TOKEN = os.environ.get("API_TOKEN", "")
open_weather_token = os.environ.get("WEATHER_API_TOKEN", "")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply('Привет, я GogikPBot, приятно познакомиться, мои возможности написанны в описании')

@dp.message_handler()
async def get_weather(message: types.Message):
    text = message.text.lower()
    if 'погода' in text:
        text = text.replace('погода', '')
        print(text)
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

            city_r = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={text}&appid={open_weather_token}")
            city_data = city_r.json()

            lat = city_data[0]['lat']
            lon = city_data[0]['lon']

            weather_r = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}&units=metric")
            weather_data = weather_r.json()

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
            length_of_the_day = datetime.datetime.fromtimestamp(
                weather_data['sys']['sunset']) - datetime.datetime.fromtimestamp(weather_data['sys']['sunrise'])

            print(city, temp, humidity, pressure, wind, sunrise_timestamp, sunset_timestamp, length_of_the_day)
            await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                  f"Погода в городе: {city}\n"
                  f"Температура: {temp}°C {wd}\n"
                  f"Влажность: {humidity}%\n"
                  f"Давление: {pressure} мм.рт.ст\n"
                  f"Скорость ветра: {wind} м/с\n"
                  f"Время рассвета: {sunrise_timestamp}\n"
                  f"Время заката: {sunset_timestamp}\n"
                  f"Длина дня: {length_of_the_day}\n"
                  f"**Хорошего дня!**")

        except:
            await message.reply('\U00002620 Проверьте название города \U00002620')

    elif 'красная панда' in text:
        try:
            # making a GET request to the endpoint.
            resp = requests.get(f"https://api.unsplash.com/search/photos?client_id={CLIENT_ID}&query=red-panda&order_by=relevant&page={str(random.randint(1,50))}&per_page=1")
            # checking if resp has a healthy status code.
            content = resp.json()  # We have a dict now.
            photo = content['results'][0]['urls']['regular']
            await bot.send_photo(message.chat.id, photo=photo)
        except:
            resp = requests.get(f"https://api.unsplash.com/search/photos?client_id={CLIENT_ID}&query=red_panda&order_by=relevant&page={str(random.randint(1,100))}&per_page=1")
            # checking if resp has a healthy status code.
            content = resp.json()  # We have a dict now.
            photo = content['results'][0]['urls']['regular']
            await message.reply('Что-то пошло не так')

    elif 'енот' in text:
        try:
            resp = requests.get("https://some-random-api.ml/img/raccoon")
            if 300 > resp.status_code >= 200:
                content = resp.json()  # We have a dict now.
                photo = content['link']
            else:
                content = f"Recieved a bad status code of {resp.status_code}."
            await bot.send_photo(message.chat.id, photo=photo)
        except:
            await message.reply('Что-то пошло не так')

    elif 'лиса' in text:
        try:
            resp = requests.get("https://some-random-api.ml/img/fox")
            if 300 > resp.status_code >= 200:
                content = resp.json()  # We have a dict now.
                photo = content['link']
            else:
                content = f"Recieved a bad status code of {resp.status_code}."
            await bot.send_photo(message.chat.id, photo=photo)
        except:
            await message.reply('Что-то пошло не так')
    elif 'собака' in text:
        try:
            resp = requests.get("https://some-random-api.ml/img/dog")
            if 300 > resp.status_code >= 200:
                content = resp.json()  # We have a dict now.
                photo = content['link']
            else:
                content = f"Recieved a bad status code of {resp.status_code}."
            await bot.send_photo(message.chat.id, photo=photo)
        except:
            await message.reply('Что-то пошло не так')
    elif 'кот' in text or 'кошка' in text:
        try:
            resp = requests.get("https://some-random-api.ml/img/cat")
            if 300 > resp.status_code >= 200:
                content = resp.json()  # We have a dict now.
                photo = content['link']
            else:
                content = f"Recieved a bad status code of {resp.status_code}."
            await bot.send_photo(message.chat.id, photo=photo)
        except:
            await message.reply('Что-то пошло не так')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
