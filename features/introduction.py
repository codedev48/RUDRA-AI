# file: introduction.py
from engine.speak import speak
from config import USER_NAME
import datetime
import sys
import select

def rudra_introduction():
    """
    RUDRA self-introduction with stop functionality.
    Stops immediately if user presses 'Q' or says 'stop'.
    No threading needed. No prompts displayed.
    """
    current_year = datetime.datetime.now().year

    intro_lines = [
        f"Hello Sir.",
        "I am RUDRA, a personal desktop voice assistant.",
        "I was created to make the system smarter, faster, and more powerful.",
        "I can open applications, search Google, read Wikipedia,",
        "check battery status, manage your tasks,",
        "remember important things for you,"
        "give news updates, summarize files,",
        "set reminders, and even play games with you.",
        "I also support",
        "intelligent command processing.",
        "I am continuously evolving.",
        f"Version {current_year} build.",
        f"Developed and trained by Devendra.",
        "I am ready to assist you anytime."
    ]

    speak("Starting introduction.")

    for line in intro_lines:
        # Speak the line
        speak(line)

        # ------------------- Keyboard check ------------------- #
        # Works only on CMD/terminal; non-blocking input check
        try:
            # Check if user pressed Q
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                user_input = sys.stdin.readline().strip().lower()
                if user_input == "q":
                    speak("Introduction stopped as requested.")
                    break
        except Exception:
            # In GUI or environments without stdin, ignore
            pass

        # ------------------- Voice check ------------------- #
        try:
            from engine.listen import listen
            command = listen()
            if command and "stop" in command.lower():
                speak("Introduction stopped as requested.")
                break
        except Exception:
            # If mic fails, continue intro
            pass