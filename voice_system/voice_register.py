import sounddevice as sd
import soundfile as sf
import numpy as np
import os

VOICE_FOLDER = "voice_memory"
FS = 16000

# phrases for consistent voice samples
PHRASES = [
    "Hello Rudra",
    "My name is Vedant",
    "Rudra AI activate",
    "I love programming",
    "Today is a great day"
]


def setup_voice_memory():
    """Create voice_memory folder automatically"""
    if not os.path.exists(VOICE_FOLDER):
        os.makedirs(VOICE_FOLDER)
        print("Created voice_memory folder")


def record_voice(duration=3):
    print("Recording...")
    audio = sd.rec(int(duration * FS), samplerate=FS, channels=1)
    sd.wait()
    return np.squeeze(audio)


def register_user(username):

    setup_voice_memory()

    username = username.lower().strip()

    user_folder = os.path.join(VOICE_FOLDER, username)

    os.makedirs(user_folder, exist_ok=True)

    print(f"\nStarting voice registration for {username}\n")

    for i, phrase in enumerate(PHRASES):

        print(f"\nSay this phrase clearly:\n'{phrase}'")

        input("Press Enter to start recording")

        audio = record_voice()

        filename = os.path.join(user_folder, f"sample_{i+1}.wav")

        sf.write(filename, audio, FS)

        print("Saved:", filename)

    print("\nVoice registration completed!")


if __name__ == "__main__":

    name = input("Enter username: ")

    if not name:
        name = "user"

    register_user(name)