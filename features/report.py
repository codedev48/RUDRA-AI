import datetime
import psutil
from engine.speak import speak
from features.news import get_news
from features.todo import show_tasks


def daily_report():
    speak("Here is your daily report")

    # Date
    today = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today's date is {today}")

    # Time
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

    # Battery
    battery = psutil.sensors_battery()
    if battery:
        speak(f"Battery is at {battery.percent} percent")

    # Tasks
    speak("Here are your pending tasks")
    show_tasks()
