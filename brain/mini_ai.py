# brain/mini_ai.py

import random

def mini_ai_response(cmd):

    greetings = ["hello", "hi", "hey"]
    how_are_you = ["how are you", "kasa ahes", "kashi ahes"]

    if any(greet in cmd for greet in greetings):
        return random.choice([
            "Hello Vedant!",
            "Hey there!",
            "Hi, how can I assist you?"
        ])

    if any(q in cmd for q in how_are_you):
        return random.choice([
            "I am functioning perfectly.",
            "All systems operational.",
            "Running smoothly!"
        ])

    return None