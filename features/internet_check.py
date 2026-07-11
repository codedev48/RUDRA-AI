import requests
from engine.speak import speak

def check_internet_connection():
    try:
        requests.get("https://www.google.com", timeout=5)
        speak("Internet connection is active.")
        print("Internet connection is active.")

    except:
        speak("No internet connection detected.")
        print("No internet connection detected.")