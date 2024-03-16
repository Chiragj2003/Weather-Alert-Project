import requests
import schedule
import time
from gmail import WeatherAlert
from threading import Thread
from dotenv import dotenv_values

api_key_dict = dotenv_values(".env")
api_key = api_key_dict.get('API_KEY')


def getRainPossibility(latitude: str, longitude: str):
    try:
        url = "http://api.weatherapi.com/v1/forecast.json"
        parameter = {
            "key": api_key,
            "q": f"{latitude}, {longitude}"
        }
        response = requests.get(url=url, params=parameter).json()
        rain_possibility = response['forecast']['forecastday'][0]['day']
        return rain_possibility

    except Exception as e:
        print(e)
        return {'daily_will_it_rain': 0}


class DataHandler:
    def __init__(self, clients: list) -> None:
        self.clients = clients

    def main(self) -> None:
        for client in self.clients:
            rain_chance = getRainPossibility(client['latitude'], client["longitude"])
            if rain_chance['daily_will_it_rain'] == 1:
                thread = Thread(target=WeatherAlert(rain_chance['daily_chance_of_rain'], client['mail']).alertMail)
                thread.start()

#enter your mail and longitude and latitude of your area 
clients = [
    {"mail": "yourmail@gmail.com",
     "latitude": "29.9457",
     "longitude": "78.1642"},
    {"mail": "your mail@gmail.com",
     "latitude": "9.9921",
     "longitude": "76.3019"},
    {"mail": "yoir mail@gmail.com",
     "latitude": "29.5829",
     "longitude": "80.2182"},
]

# To Run in every 2 Minutes for demonstration of project
schedule.every(1).minutes.do(job_func=DataHandler(clients).main)

# To Run each day for working Project
# schedule.every().day.at("03:00").do(job_func=DataHandler(clients).main)

if __name__ == "__main__":
    DataHandler(clients).main()
    while True:
        n = schedule.idle_seconds()
        if n is None:
            break
        else:
            print(n)
            time.sleep(n)
        schedule.run_pending()

