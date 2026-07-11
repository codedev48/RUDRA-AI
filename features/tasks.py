# features/tasks.py

import os

tasks_file = "data/tasks.txt"

def add_task(task):
    """Add a new task to tasks.txt"""
    os.makedirs(os.path.dirname(tasks_file), exist_ok=True)
    with open(tasks_file, "a", encoding="utf-8") as f:
        f.write(task + "\n")
    print(f"Task added: {task}")

def show_tasks():
    """Show all saved tasks"""
    try:
        with open(tasks_file, "r", encoding="utf-8") as f:
            tasks = f.readlines()
        if tasks:
            print("Your tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t.strip()}")
        else:
            print("No tasks found.")
    except FileNotFoundError:
        print("No tasks file found. Add a task first.")
