from flask_pymongo import PyMongo
from datetime import datetime

mongo = PyMongo()

class WeatherSummary:
    def __init__(self, date, avg_temp, max_temp, min_temp, dominant_weather):
        self.date = date
        self.avg_temp = avg_temp
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.dominant_weather = dominant_weather

    def save(self):
        mongo.db.weather_summaries.update_one(
            {"date": self.date},
            {
                "$set": {
                    "avg_temp": self.avg_temp,
                    "max_temp": self.max_temp,
                    "min_temp": self.min_temp,
                    "dominant_weather": self.dominant_weather,
                }
            },
            upsert=True,
        )
