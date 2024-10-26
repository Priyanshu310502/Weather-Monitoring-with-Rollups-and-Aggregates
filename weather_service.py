import requests
from datetime import datetime
from models import WeatherSummary
from notifications import send_alert
from flask_pymongo import PyMongo
import os

mongo = PyMongo()

cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

def get_weather_data():
    api_key = os.getenv('OPENWEATHER_API_KEY')
    results = []
    
    for city in cities:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
        if response.status_code == 200:
            results.append(response.json())
    
    return results

def process_weather_data():
    weather_data = get_weather_data()
    daily_summary = {}

    for data in weather_data:
        date = datetime.fromtimestamp(data['dt']).date()
        temp = data['main']['temp']
        condition = data['weather'][0]['main']

        if date not in daily_summary:
            daily_summary[date] = {
                'total_temp': 0,
                'count': 0,
                'max_temp': temp,
                'min_temp': temp,
                'conditions': {}
            }

        daily_summary[date]['total_temp'] += temp
        daily_summary[date]['count'] += 1
        daily_summary[date]['max_temp'] = max(daily_summary[date]['max_temp'], temp)
        daily_summary[date]['min_temp'] = min(daily_summary[date]['min_temp'], temp)
        daily_summary[date]['conditions'][condition] = daily_summary[date]['conditions'].get(condition, 0) + 1

        # Check for alerts
        if temp > 35:
            send_alert(f"High Temperature Alert for {data['name']}", f"Current temperature is {temp}°C in {data['name']}.")

    for date, summary in daily_summary.items():
        dominant_weather = max(summary['conditions'], key=summary['conditions'].get)
        avg_temp = summary['total_temp'] / summary['count']

        weather_summary = WeatherSummary(date, avg_temp, summary['max_temp'], summary['min_temp'], dominant_weather)
        weather_summary.save()
