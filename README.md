# Real-Time Data Processing System for Weather Monitoring

## Overview
The Real-Time Data Processing System is designed to monitor weather conditions in key Indian metros, providing summarized insights through daily rollups and aggregates. This application retrieves weather data from the OpenWeatherMap API, processes it in real-time, and generates alerts based on user-defined thresholds.

## Table of Contents
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Non-Functional Requirements](#non-functional-requirements)
- [Test Cases](#test-cases)
- [Future Enhancements](#future-enhancements)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features
- **Real-Time Weather Updates**: Continuously retrieves weather data for Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.
- **Daily Weather Summary**: Calculates daily aggregates like average, maximum, and minimum temperatures, and identifies the dominant weather condition.
- **Alerting Mechanism**: User-configurable thresholds for temperature and weather conditions trigger alerts.
- **Visualizations**: Displays weather summaries and historical trends using charts.
- **User-Friendly Interface**: Developed with React.js for an interactive experience.

## Technology Stack
- **Frontend**: React.js, Axios, Chart.js, Material-UI
- **Backend**: Flask (Python)
- **Database**: MongoDB
- **Scheduler**: Python schedule library
- **Notifications**: SMTP-based email alerts
- **API**: OpenWeatherMap API

## Getting Started
### Prerequisites
- Node.js (v12 or higher)
- Python (v3.7 or higher)
- MongoDB (Local or Atlas)
- An OpenWeatherMap API Key (Sign up at [OpenWeatherMap](https://openweathermap.org/))

### Installation
#### Clone the Repository:
```bash
git clone https://github.com/yourusername/weather_monitoring.git
cd weather_monitoring

```
### Setup Backend:
1. Navigate to the backend directory:
    ```bash
    cd backend
    ```
2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows
    ```
3. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
4. Configure Environment Variables: Create a `.env` file in the backend directory and add:
    ```bash
    OPENWEATHER_API_KEY=your_api_key
    MONGO_URI=mongodb://localhost:27017/weatherDB
    ```
5. Run the Backend:
    ```bash
    python app.py
    ```

### Setup Frontend:
1. Navigate to the frontend directory:
    ```bash
    cd frontend
    ```
2. Install dependencies:
    ```bash
    npm install
    ```
3. Run the Frontend:
    ```bash
    npm start
    ```



## Usage
### Access the Application
Open your web browser and navigate to [http://localhost:3000](http://localhost:3000).

### Set Alert Thresholds
Go to the settings section to define temperature thresholds or specific weather conditions for alerts.

### View Real-Time Data
The dashboard will display real-time weather updates for the selected metros.

### Historical Data
Access visualizations to see daily weather summaries and trends over time.

### Receive Alerts
If the weather conditions exceed the defined thresholds, alerts will be triggered, which can be viewed on the console or through email notifications.

## Non-Functional Requirements
### Security
- **API Security**: The backend uses environment variables to secure sensitive API keys.
- **Data Validation**: All inputs are validated on the server-side to prevent injection attacks.
- **CORS Configuration**: Configured to allow only trusted origins in production.

### Performance
- **Efficient Data Retrieval**: Implemented caching for frequently accessed weather data to minimize API calls and improve response times.
- **Scalability**: The system is designed to handle multiple users and can be scaled horizontally by deploying more instances of the backend server.
- **Optimized Database Queries**: MongoDB is used to store daily summaries, ensuring quick access to historical data.

### Maintainability
- **Modular Code Structure**: The application is structured into clear modules (frontend, backend) with well-defined responsibilities.
- **Documentation**: Comprehensive inline documentation and this README guide enhance maintainability.

## Test Cases
- **System Setup**: Verify system startup and API connection.
- **Data Retrieval**: Ensure weather data is retrieved and parsed correctly.
- **Temperature Conversion**: Validate accuracy in temperature conversions.
- **Daily Summary Calculation**: Confirm correct calculation of daily summaries.
- **Alert Triggering**: Test alert mechanisms when thresholds are breached.

## Future Enhancements
- **Additional Weather Parameters**: Extend to include humidity, wind speed, and pressure data.
- **Forecast Retrieval**: Add features to display weather forecasts.
- **User Authentication**: Implement user sign-in and preferences saving.
- **Mobile Responsiveness**: Ensure the application is mobile-friendly.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- **OpenWeatherMap**: For providing real-time weather data through their API.
- **MongoDB**: For efficient data storage and retrieval.
- **React.js**: For a robust frontend framework.

