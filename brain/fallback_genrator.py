# brain/fallback_generator.py

import random

def generate_fallback(cmd):

    responses = [
        f"I am not fully trained for '{cmd}' yet.",
        "That feature is not implemented right now.",
        "Interesting request. I will improve in future versions.",
        "This command is outside my current capability."
    ]

    return random.choice(responses)