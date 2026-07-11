import psutil
from engine.speak import speak
from features.system_control import set_volume, set_brightness

current_mode = "normal"

SAFE_PROCESSES = [
    "explorer",
    "system",
    "winlogon",
    "cmd",
    "python"
]

SOCIAL_APPS = [
    "discord",
    "spotify",
    "telegram",
    "teams"
]

GAME_APPS = [
    "valorant",
    "steam",
    "epicgames",
    "launcher"
]


# ---------------- WORK MODE ---------------- #

def enable_work_mode():
    global current_mode

    if current_mode == "work":
        speak("Work mode is already active")
        return

    speak("Activating work mode")

    set_volume(30)
    set_brightness(70)

    close_apps(GAME_APPS + SOCIAL_APPS)

    current_mode = "work"
    speak("Work mode activated. Stay focused.")


# ---------------- SILENT MODE ---------------- #

def enable_silent_mode():
    global current_mode

    if current_mode == "silent":
        speak("Silent mode is already active")
        return

    speak("Activating silent mode")

    set_volume(5)

    current_mode = "silent"
    speak("Silent mode enabled")


# ---------------- NORMAL MODE ---------------- #

def enable_normal_mode():
    global current_mode

    speak("Restoring normal mode")

    set_volume(50)
    set_brightness(70)

    current_mode = "normal"
    speak("System back to normal mode")


# ---------------- CLOSE APPS FUNCTION ---------------- #

def close_apps(app_list):
    for proc in psutil.process_iter(['name']):
        try:
            name = proc.info['name'].lower()

            if any(safe in name for safe in SAFE_PROCESSES):
                continue

            if any(app in name for app in app_list):
                proc.kill()

        except:
            pass