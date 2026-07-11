# features/daily_intelligence.py

import random
import datetime
from engine.speak import speak
from features.todo import show_tasks
from features.system_monitor import cpu_usage, ram_usage
from features.system import battery_status


# ---------------- MOTIVATION ---------------- #

def motivational_quote():
    quotes = [
        "Success starts with self discipline.",
        "Push yourself. No one else will do it for you.",
        "Consistency beats motivation.",
        "Small progress is still progress.",
        "Focus on your goal, not distractions.",
        "Every day is a second chance.",
        "Do something today that your future self will thank you for.",
        "Dream big. Start small. Act now.",
        "You are capable of amazing things.",
        "Stay positive, work hard, make it happen."
    ]
    return random.choice(quotes)


# ---------------- GREETING ---------------- #

def get_time_based_greeting(user_name):
    hour = datetime.datetime.now().hour

    if hour < 12:
        return f"Good Morning {user_name}"
    elif hour < 18:
        return f"Good Afternoon {user_name}"
    else:
        return f"Good Evening {user_name}"


# ---------------- DAILY BRIEFING ---------------- #

def daily_briefing(user_name="User"):

    try:

        # Greeting
        greeting = get_time_based_greeting(user_name)
        speak(f"{greeting}. Here is your daily intelligence report.")

        now = datetime.datetime.now()

        # Date and Day
        day_name = now.strftime("%A")
        date_today = now.strftime("%d %B %Y")
        current_time = now.strftime("%I:%M %p")

        speak(f"Today is {day_name}, {date_today}.")
        speak(f"The current time is {current_time}.")

        # Tasks
        speak("Now checking your pending tasks.")
        show_tasks()

        # System Status
        speak("Checking your system health status.")

        cpu_usage()
        ram_usage()
        battery_status()

        # Motivation
        speak("Finally, here is your motivational quote for today.")
        speak(motivational_quote())

        speak("That concludes your daily intelligence report. Have a productive day.")

    except Exception as e:
        print("Daily briefing error:", e)
        speak("Sorry, I encountered an error while preparing your daily report.")