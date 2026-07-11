import requests
from engine.speak import speak

# Your OpenWeatherMap API key
API_KEY = "25ca250b9aac0b19b966251aaa60f8fd"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city="Pune"):
    """
    Fetch weather information for a given city.
    Default city is Pune if no city is specified.
    """

    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()

        if data["cod"] != 200:
            speak("Sorry, I could not find weather information for that city.")
            return

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        weather_report = (
            f"The weather in {city} is {condition}. "
            f"Temperature is {temperature} degree Celsius. "
            f"Humidity is {humidity} percent. "
            f"Wind speed is {wind_speed} meters per second."
        )

        print(weather_report)
        speak(weather_report)

    except requests.exceptions.RequestException:
        speak("Unable to fetch weather information. Please check your internet connection.")

    except Exception as e:
        print("Weather Error:", e)
        speak("Something went wrong while fetching weather information.")