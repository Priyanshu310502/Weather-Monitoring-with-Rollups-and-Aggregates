from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
from weather_service import process_weather_data
import schedule
import time
import threading

load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGODB_URI')
mongo = PyMongo(app)

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather/update', methods=['GET'])
def update_weather():
    process_weather_data()
    return jsonify({"status": "Weather data updated successfully!"})

@app.route('/api/weather/summaries', methods=['GET'])
def get_weather_summaries():
    summaries = mongo.db.weather_summaries.find()
    return jsonify([{
        "date": str(summary['date']),
        "avg_temp": summary['avg_temp'],
        "max_temp": summary['max_temp'],
        "min_temp": summary['min_temp'],
        "dominant_weather": summary['dominant_weather']
    } for summary in summaries])

if __name__ == '__main__':
    schedule.every(5).minutes.do(process_weather_data)
    threading.Thread(target=run_schedule, daemon=True).start()
    app.run(debug=True)
