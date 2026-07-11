import time
import threading
from engine.speak import speak


def set_alarm(alarm_time):
    try:
        # Fix time format (7:30 -> 07:30)
        if len(alarm_time) == 4:
            alarm_time = "0" + alarm_time

        speak(f"Alarm set for {alarm_time}")

        def alarm_thread():
            while True:
                current_time = time.strftime("%H:%M")

                if current_time == alarm_time:
                    speak("Alarm ringing")
                    print("ALARM! Time reached.")
                    break

                time.sleep(20)

        thread = threading.Thread(target=alarm_thread)
        thread.daemon = True
        thread.start()

    except Exception as e:
        print("Alarm error:", e)
        speak("Sorry, I could not set the alarm.")