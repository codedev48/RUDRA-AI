import requests
from engine.speak import speak

def get_ip_address():
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=10)
        data = response.json()

        ip = data["ip"]

        result = f"Your public IP address is {ip}"

        print(result)
        speak(result)

    except Exception as e:
        print("IP error:", e)
        speak("Sorry, I could not fetch your IP address.")