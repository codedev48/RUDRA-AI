from engine.speak import speak


def add_task(task):
    with open("data/todo.txt", "a") as file:
        file.write(task + "\n")
    speak("Task added successfully")


def show_tasks():
    try:
        with open("data/todo.txt", "r") as file:
            tasks = file.readlines()

        if len(tasks) == 0:
            speak("Your to do list is empty")
        else:
            speak("Here are your tasks")
            for task in tasks:
                speak(task.strip())
                print(task.strip())
    except:
        speak("No tasks found")
