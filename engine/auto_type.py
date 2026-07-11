import pyautogui
import time

def auto_type(text, delay=0.05):
    """
    Automatically type text in active window
    """
    time.sleep(1)  # small delay before typing
    for char in text:
        pyautogui.write(char)
        time.sleep(delay)
    pyautogui.press("enter")
