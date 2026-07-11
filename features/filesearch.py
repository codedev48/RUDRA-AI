import os
import time
import string
from engine.speak import speak
from engine.listen import listen_command


def get_all_drives():
    drives = []
    for letter in string.ascii_uppercase:
        if os.path.exists(f"{letter}:\\"):
            drives.append(f"{letter}:\\")
    return drives


def get_file_properties(path):
    size = os.path.getsize(path)
    size_kb = round(size / 1024, 2)

    creation_time = time.ctime(os.path.getctime(path))
    modified_time = time.ctime(os.path.getmtime(path))

    return size_kb, creation_time, modified_time


def search_in_path(base_path, filename):
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if filename.lower() in file.lower():
                return os.path.join(root, file)
    return None


def find_file(filename):

    speak(f"Searching for {filename}")

    user_home = os.path.expanduser("~")

    priority_paths = [
        os.path.join(user_home, "Desktop"),
        os.path.join(user_home, "Documents"),
        os.path.join(user_home, "Downloads"),
    ]

    # Search priority folders
    for path in priority_paths:
        if os.path.exists(path):
            speak(f"Checking {os.path.basename(path)}")
            time.sleep(1)

            result = search_in_path(path, filename)
            if result:
                return handle_found_file(result)

    # Search drives
    drives = get_all_drives()

    for drive in drives:
        speak(f"Scanning drive {drive}")
        time.sleep(1)

        result = search_in_path(drive, filename)
        if result:
            return handle_found_file(result)

    speak("File not found")


def handle_found_file(full_path):

    speak("File found")
    print("Found at:", full_path)

    size_kb, created, modified = get_file_properties(full_path)

    speak(f"The file size is {size_kb} kilo bytes")
    speak(f"It was created on {created}")
    speak(f"It was last modified on {modified}")

    speak("Do you want me to open it? You can say yes or no.")

    import time
    time.sleep(2)

    # 🔥 Try voice once
    response = listen_command()

    if response and "yes" in response.lower():
        speak("Opening file")
        os.startfile(full_path)
        return

    if response and "no" in response.lower():
        speak("Okay, not opening the file.")
        return

    # 🔥 If voice fails, fallback to typing
    speak("I did not hear clearly. Please type yes or no.")

    user_input = input("Open file? (yes/no): ")

    if user_input.lower() == "yes":
        speak("Opening file")
        os.startfile(full_path)
    else:
        speak("Okay, not opening the file.")