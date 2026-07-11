import requests
import xml.etree.ElementTree as ET
from engine.speak import speak

INDIAN_STATES = [
    "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh",
    "Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka",
    "Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram",
    "Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana",
    "Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Delhi","Jammu & Kashmir","Ladakh"
]

def get_news(scope="global"):
    """
    Fetch latest news based on scope:
    scope: "global", "india", or name of a specific state
    """
    try:
        # Determine URL based on scope
        if scope.lower() == "global":
            url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
            speak("Fetching top global news headlines")
        elif scope.lower() == "india":
            url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:IN"
            speak("Fetching top Indian news headlines")
        elif scope in INDIAN_STATES:
            # State-specific Indian news
            query = f"{scope} India"
            url = f"https://news.google.com/rss/search?q={requests.utils.quote(query)}&hl=en-IN&gl=IN&ceid=IN:IN"
            speak(f"Fetching top news for {scope}")
        else:
            speak("Scope not recognized. Fetching global news instead.")
            url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"

        response = requests.get(url)
        root = ET.fromstring(response.content)

        count = 0
        for item in root.iter("item"):
            title = item.find("title").text
            if title:
                speak(title)
                print(title)
                count += 1
            if count == 5:  # Only top 5 headlines
                break

    except Exception as e:
        speak("Unable to fetch news right now.")
        print("Error:", e)