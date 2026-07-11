
import pyttsx3
from config import ASSISTANT_NAME

def speak(text):
    try:
        print(f"{ASSISTANT_NAME}: {text}")
        
        engine = pyttsx3.init('sapi5')   # 🔥 re-init every call
        engine.setProperty('rate', 170)

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        
        engine.say(text)
        engine.runAndWait()
        engine.stop()
     
    except Exception as e:
        print("Speech Error:", e)
