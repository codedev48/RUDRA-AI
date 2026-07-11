import pyperclip
from engine.speak import speak


def read_clipboard():
    try:
        text = pyperclip.paste()

        if text.strip() == "":
            speak("Clipboard is empty.")
            return

        print("Clipboard Content:", text)

        speak("Reading clipboard content.")
        speak(text)

    except Exception as e:
        print("Clipboard error:", e)
        speak("Sorry, I could not read the clipboard.")