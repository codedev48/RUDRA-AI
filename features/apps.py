import os
import webbrowser
import subprocess
from engine.speak import speak


# ---------------- OPEN APPS ---------------- #

def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")


def open_chrome():
    speak("Opening Chrome")
    try:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    except:
        webbrowser.open("https://www.google.com")


def open_edge():
    speak("Opening Microsoft Edge")
    subprocess.Popen("start msedge", shell=True)


def open_copilot():
    speak("Opening Microsoft Copilot")
    subprocess.Popen("start ms-copilot:", shell=True)


def open_instagram():
    speak("Opening Instagram")
    webbrowser.open("https://www.instagram.com")


def open_maps():
    speak("Opening Google Maps")
    webbrowser.open("https://www.google.com/maps")


def open_notepad():
    speak("Opening Notepad")
    subprocess.Popen("notepad", shell=True)


def open_firefox():
    speak("Opening Firefox")
    subprocess.Popen("start firefox", shell=True)


def open_camera():
    speak("Opening Camera")
    subprocess.Popen("start microsoft.windows.camera:", shell=True)


def open_vscode():
    speak("Opening Visual Studio Code")
    subprocess.Popen("code", shell=True)


def open_adobe():
    speak("Opening Adobe Reader")
    subprocess.Popen("start acrord32", shell=True)


def open_discord():
    speak("Opening Discord")
    subprocess.Popen("start discord", shell=True)


def open_recycle_bin():
    speak("Opening Recycle Bin")
    subprocess.Popen("start shell:RecycleBinFolder", shell=True)


def open_word():
    speak("Opening Microsoft Word")
    subprocess.Popen("start winword", shell=True)


def open_excel():
    speak("Opening Microsoft Excel")
    subprocess.Popen("start excel", shell=True)


def open_powerpoint():
    speak("Opening Microsoft PowerPoint")
    subprocess.Popen("start powerpnt", shell=True)


def open_calculator():
    speak("Opening Calculator")
    subprocess.Popen("calc", shell=True)


# ---------------- CLOSE APPS ---------------- #

def close_app(process_name, friendly_name):
    speak(f"Closing {friendly_name}")
    os.system(f"taskkill /f /im {process_name} >nul 2>&1")


def close_chrome():
    close_app("chrome.exe", "Chrome")



def close_edge():
    close_app("msedge.exe", "Microsoft Edge")


def close_firefox():
    close_app("firefox.exe", "Firefox")


def close_notepad():
    close_app("notepad.exe", "Notepad")


def close_calculator():
    close_app("CalculatorApp.exe", "Calculator")


def close_vscode():
    close_app("Code.exe", "Visual Studio Code")


def close_discord():
    close_app("Discord.exe", "Discord")


def close_word():
    close_app("WINWORD.EXE", "Word")


def close_excel():
    close_app("EXCEL.EXE", "Excel")


def close_powerpoint():
    close_app("POWERPNT.EXE", "PowerPoint")


def close_adobe():
    close_app("AcroRd32.exe", "Adobe Reader")


def close_camera():
    close_app("WindowsCamera.exe", "Camera")


def close_recycle_bin():
    speak("Recycle Bin window cannot be safely closed directly.")


def close_youtube():
    close_chrome()  # assuming opened in Chrome


def close_maps():
    close_chrome()


def close_instagram():
    close_chrome()


def close_copilot():
    close_app("msedge.exe", "Copilot")