import platform
import psutil
from engine.speak import speak


def get_system_info():
    try:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        os_name = platform.system()
        processor = platform.processor()

        info = (
            f"Operating system is {os_name}. "
            f"Processor is {processor}. "
            f"CPU usage is {cpu} percent. "
            f"RAM usage is {ram} percent."
        )

        print(info)
        speak(info)

    except Exception as e:
        print("System info error:", e)
        speak("Sorry, I could not fetch system information.")