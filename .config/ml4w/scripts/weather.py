#!/usr/bin/env python3
import requests
import json
import sys
from datetime import datetime
from datetime import timedelta
import os

# Конфигурация
API_KEY = "b1c2c261-4144-41a1-a350-cc486531ff24"
LAT = "54.4275"
LON = "45.3296"
CACHE_TTL = 3600  # 30 минут кэширования

CACHE_FILE = "/tmp/yandex_weather_cache.json"  # Общий кэш для всех Waybar

# Иконки погоды (Nerd Fonts)
ICONS = {
    "clear": "", "partly-cloudy": "", "cloudy": "", "overcast": "",
    "light-rain": "", "rain": "", "heavy-rain": "", "showers": "",
    "thunderstorm": "", "snow": "", "wet-snow": "", "hail": "", "fog": ""
}

error = False

def get_weather():
    global error
    data = None
    
    # Проверка кэша
    if os.path.exists(CACHE_FILE):
        file_time = os.path.getmtime(CACHE_FILE)
        if (datetime.now() - datetime.fromtimestamp(file_time)) < timedelta(seconds=CACHE_TTL):
            try:
                with open(CACHE_FILE, 'r') as f:
                    data = json.load(f)
            except json.JSONDecodeError:
                pass  # Если файл поврежден, просто запросим новые данные
    
    if data is None:
        try:
            headers = {"X-Yandex-Weather-Key": API_KEY}
            url = f"https://api.weather.yandex.ru/v2/forecast?lat={LAT}&lon={LON}&extra=true"
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        
            data = response.json()
            
            # Сохраняем в кэш
            with open(CACHE_FILE, 'w') as f:
                json.dump(data, f)  # Сохраняем data, а не response
                
        except Exception as e:
            print(f"Error getting weather: {e}", file=sys.stderr)
            error = True 
            return {
                "text": " --°C",
                "tooltip": "Нет данных о погоде",
                "class": "weather-error"
            }
               
    # Метаданные
    file_time = os.path.getmtime(CACHE_FILE)
    timestamp = data["now"]

    # Текущая погода
    fact = data["fact"]
    info = data["info"]
    current_temp = fact["temp"]
    condition = fact["condition"]
    feels_like = fact["feels_like"]
    humidity = fact["humidity"]
    wind_speed = fact["wind_speed"]
    pressure_mm = info["def_pressure_mm"]
 
    # Прогноз на сегодня
    today = data["forecasts"][0]
    today_parts = today["parts"]
    today_day = today_parts.get("day", {})
    today_night = today_parts.get("night", {})
 
    # Прогноз на завтра
    tomorrow = data["forecasts"][1]
    tomorrow_parts = tomorrow["parts"]
    tomorrow_day = tomorrow_parts.get("day", {})
    tomorrow_night = tomorrow_parts.get("night", {})

    # Форматирование времени
    sunrise = today.get("sunrise", "?")
    sunset = today.get("sunset", "?")

    result = {
        "text": f"{ICONS.get(condition, '')} {current_temp}°C",
        "tooltip": (
            f"<b>Данные обновлены: {datetime.fromtimestamp(file_time).strftime('%H:%M')}</b>\n"
            f"{condition_translate(condition)}, {current_temp}°C (ощущается {feels_like}°C)\n"
            f"  Влажность: {humidity}%\n"
            f"  Ветер: {wind_speed} м/с\n"
            f"  Давление: {pressure_mm} мм рт.ст.\n"
            f"  Восход: {sunrise} |   Закат: {sunset}\n\n"
                
            f"<b>  Сегодня днем</b>\n"
            f"{condition_translate(today_day.get('condition', 'N/A'))}, "
            f"{today_day.get('temp_avg', 'N/A')}°C (макс. {today_day.get('temp_max', 'N/A')}°C)\n"
            f"Ветер: {today_day.get('wind_speed', 'N/A')} м/с\n\n"
                
            f"<b>  Сегодня ночью</b>\n"
            f"{condition_translate(today_night.get('condition', 'N/A'))}, "
            f"{today_night.get('temp_avg', 'N/A')}°C\n\n"
                
            f"<b>  Завтра ({tomorrow['date']})</b>\n"
            f"Днем: {condition_translate(tomorrow_day.get('condition', 'N/A'))}, "
            f"{tomorrow_day.get('temp_avg', 'N/A')}°C\n"
            f"Ночью: {condition_translate(tomorrow_night.get('condition', 'N/A'))}, "
            f"{tomorrow_night.get('temp_avg', 'N/A')}°C"
        ),
        "class": "weather-info"
    }
        
    return result

def condition_translate(condition):
    translations = {
        "clear": "Ясно", "partly-cloudy": "Малооблачно",
        "cloudy": "Облачно", "overcast": "Пасмурно",
        "light-rain": "Небольшой дождь", "rain": "Дождь",
        "heavy-rain": "Сильный дождь", "showers": "Ливень",
        "thunderstorm": "Гроза", "snow": "Снег",
        "wet-snow": "Дождь со снегом", "hail": "Град",
        "fog": "Туман"
    }
    return translations.get(condition, condition)

if __name__ == "__main__":
    weather_data = get_weather()
    print(json.dumps(weather_data, ensure_ascii=False, indent=None))
