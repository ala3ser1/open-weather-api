import os
import requests
from dotenv import load_dotenv
load_dotenv()

class WeatherData:

    def __init__(self, data):
        self.city = data["name"]
        self.temperature = data["main"]["temp"]
        self.feels_like = data["main"]["feels_like"]
        self.humidity = data["main"]["humidity"]
        self.weather = data["weather"][0]["description"]
        self.wind_speed = data["wind"]["speed"]

    def display(self):
        print("\n===== Weather Information =====")
        print(f"City: {self.city}")
        print(f"Temperature: {self.temperature} °C")
        print(f"Feels Like: {self.feels_like} °C")
        print(f"Humidity: {self.humidity}%")
        print(f"Weather: {self.weather}")
        print(f"Wind Speed: {self.wind_speed} m/s")
        print("================================")


def get_weather(city):
    API_KEY = os.getenv("API_KEY")
    if not API_KEY:
        print("API Key is missing!")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url , params=params , timeout=10)

        response.raise_for_status()

        data = response.json()

        weather_info = WeatherData(data)

        return weather_info

    except requests.exceptions.Timeout:
        print("Request timed out!")

    except requests.exceptions.ConnectionError:
        print("Connection failed!")

    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

    except (KeyError, IndexError, ValueError) as e:
        print("Invalid API response:", e)

    return None

#--------------------------------- Main Program-----------------------

def main():
    while True:
        city = input("\nEnter city name (or 'exit' to quit): ")

        if city.lower() == "exit":
            print("Goodbye!")
            break

        result = get_weather(city)

        if result:
            result.display()

if __name__ == "__main__":
    main()













