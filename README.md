# Weather Alert System

This project is a simple weather alert system that sends email notifications to specified recipients when there is a chance of rain in their area. It utilizes the WeatherAPI to retrieve weather forecast data and Gmail API to send email alerts.


![Logo](https://img.freepik.com/premium-vector/weather-icons-set-glassmorpism-effect_776789-85.jpg?size=338&ext=jpg&ga=GA1.1.1395880969.1710115200&semt=ais)


## Features

- Retrieves weather forecast data using the WeatherAPI.
- Sends email alerts to specified recipients when there is a chance of rain in their area.
- Configurable to monitor multiple locations simultaneously.
- Utilizes threading for concurrent email alerts.
- Uses the Schedule library to schedule periodic checks for weather updates.

## Requirements

- Python 3.x
- Requests library (can be installed via `pip install requests`)
- Schedule library (can be installed via `pip install schedule`)
- Gmail library (custom implementation required, not available via pip)
- dotenv library (can be installed via `pip install python-dotenv`)



