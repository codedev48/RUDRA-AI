import pvporcupine
import pyaudio
import struct
from voice_system.voice_recognizer import identify_user
from engine.speak import speak


def start_secure_wake_word(callback_function):

    porcupine = pvporcupine.create(keywords=["jarvis"])

    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("Wake word security system active...")

    while True:

        pcm = audio_stream.read(
            porcupine.frame_length,
            exception_on_overflow=False
        )

        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        result = porcupine.process(pcm)

        if result >= 0:

            print("Wake word detected")

            speak("Verifying voice")

            user = identify_user()

            if user:

                speak(f"Voice verified. Welcome {user}")

                callback_function()

            else:

                speak("Unauthorized user detected")