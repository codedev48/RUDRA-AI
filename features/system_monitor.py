import psutil
import threading
import time
from engine.speak import speak

monitoring_active = True


# ---------------- CPU ---------------- #

def cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    speak(f"CPU usage is {usage} percent")


# ---------------- RAM ---------------- #

def ram_usage():
    ram = psutil.virtual_memory()
    speak(f"RAM usage is {ram.percent} percent")


# ---------------- DISK ---------------- #

def disk_usage():
    disk = psutil.disk_usage('/')
    speak(f"Disk usage is {disk.percent} percent")


# ---------------- BATTERY ---------------- #

def battery_status():
    battery = psutil.sensors_battery()
    if battery:
        speak(f"Battery is at {battery.percent} percent")
    else:
        speak("Battery information not available")


# ---------------- BACKGROUND MONITOR ---------------- #

def background_monitor():
    global monitoring_active

    while monitoring_active:
        battery = psutil.sensors_battery()
        cpu = psutil.cpu_percent(interval=1)

        # Low Battery Alert
        if battery and battery.percent <= 20 and not battery.power_plugged:
            speak("Warning. Battery is low.")

        # High CPU Alert
        if cpu >= 90:
            speak("Warning. CPU usage is very high.")

        time.sleep(60)  # check every 1 minute


def start_monitoring():
    thread = threading.Thread(target=background_monitor, daemon=True)
    thread.start()