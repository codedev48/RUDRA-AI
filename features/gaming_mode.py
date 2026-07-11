import os
from engine.speak import speak
from features.system_control import set_volume, set_brightness
from features.process_manager import kill_process_by_name

gaming_active = False


# Safe apps that should NOT be closed
SAFE_PROCESSES = [
    "explorer",
    "system",
    "winlogon",
    "cmd",
    "python"
]


def enable_gaming_mode():
    global gaming_active

    if gaming_active:
        speak("Gaming mode is already enabled")
        return

    speak("Activating gaming mode")

    # Set performance settings
    set_volume(80)
    set_brightness(100)

    # Close background apps
    close_background_apps()

    gaming_active = True
    speak("Gaming mode activated. Enjoy your game.")


def disable_gaming_mode():
    global gaming_active

    if not gaming_active:
        speak("Gaming mode is not active")
        return

    speak("Disabling gaming mode")

    set_volume(40)
    set_brightness(70)

    gaming_active = False
    speak("Gaming mode disabled. System restored.")


def close_background_apps():
    import psutil

    for proc in psutil.process_iter(['name']):
        try:
            name = proc.info['name'].lower()

            if any(safe in name for safe in SAFE_PROCESSES):
                continue

            # Close common background apps
            if any(bg in name for bg in ["discord", "chrome", "spotify", "teams"]):
                proc.kill()

        except:
            pass