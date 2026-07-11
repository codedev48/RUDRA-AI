import pyautogui
import os
from datetime import datetime
from engine.speak import speak


def take_screenshot():
    try:

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join("screenshots", filename)

        screenshot = pyautogui.screenshot()
        screenshot.save(filepath)

        speak("Screenshot taken")
        print("Saved:", filepath)

    except Exception as e:
        print("Screenshot error:", e)
        speak("Sorry, I could not take the screenshot.")