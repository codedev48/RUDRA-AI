# auto_type_test.py
import pyautogui
import time
import speech_recognition as sr

def listen_and_type():
    """
    Listen to user's speech and automatically type it in the active window
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("📢 Please start speaking. I am listening...")
        r.adjust_for_ambient_noise(source, duration=1)  # adjust for noise
        audio_data = r.listen(source, phrase_time_limit=10)  # max 10 sec per input

    try:
        text = r.recognize_google(audio_data)
        print(f"📝 You said: {text}")
        # Automatic typing
        time.sleep(1)  # 1 sec to focus window
        for char in text:
            pyautogui.write(char)
            time.sleep(0.03)  # typing delay
        pyautogui.press("enter")
    except sr.UnknownValueError:
        print("❌ Sorry, I could not understand audio")
    except sr.RequestError as e:
        print(f"❌ Could not request results; {e}")

if __name__ == "__main__":
    print("🚀 Place your cursor in Word/Notepad/WhatsApp before speaking...")
    while True:
        listen_and_type()
        cont = input("Do you want to continue? (y/n): ").lower()
        if cont != "y":
            break
