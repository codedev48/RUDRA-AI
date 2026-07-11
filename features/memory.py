from engine.speak import speak


def remember(data):
    with open("data/memory.txt", "a") as file:
        file.write(data + "\n")
    speak("I will remember that")


def recall_memory():
    try:
        with open("data/memory.txt", "r") as file:
            memories = file.readlines()

        if memories:
            speak("Here is what I remember")
            for memory in memories:
                speak(memory.strip())
                print(memory.strip())
        else:
            speak("I do not remember anything yet")
    except:
        speak("Memory file not found")
