import psutil
from engine.speak import speak


def battery_status():
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        speak(f"Battery is at {percent} percent")
        print(f"Battery: {percent}%")

        if percent < 20:
            speak("Battery is low. Please charge the system.")
    else:
        speak("Battery information not available.")
