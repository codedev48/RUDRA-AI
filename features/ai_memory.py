import json
import os
from engine.speak import speak

MEMORY_FILE = "data/memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump({}, f)

    try:
     with open(MEMORY_FILE, "r") as f:
        return json.load(f)
    except:
     return {}


def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)


def remember(command):

    try:
        memory = load_memory()

        text = command.replace("remember that", "").replace("remember", "").strip()

        if " is " in text:
            key, value = text.split(" is ", 1)

            key = key.strip()
            value = value.strip()

            memory[key] = value

            save_memory(memory)

            speak(f"Okay Vedant, I will remember that {key} is {value}")

        else:
            speak("Please say it in format like remember that something is something")

    except Exception as e:
        print("Memory error:", e)
        speak("Sorry, I could not save that memory.")


def recall(command):

    try:
        memory = load_memory()

        for key in memory:

            if key in command:
                speak(f"{key} is {memory[key]}")
                return

        if "what did i ask you to remember" in command:
            if memory:
                for key, value in memory.items():
                    speak(f"{key} is {value}")
            else:
                speak("You have not asked me to remember anything yet.")
            return

        speak("I could not find that in my memory.")

    except Exception as e:
        print("Recall error:", e)
        speak("Sorry, I could not access memory.")