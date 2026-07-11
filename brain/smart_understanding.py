# brain/smart_understanding.py

def normalize_command(command):
    cmd = command.lower().strip()

    intent_map = {

        # TIME / DATE
        "INTENT_TIME": ["time", "current time", "vel"],
        "INTENT_DATE": ["date", "today's date", "tarikh"],
        "INTENT_DAY": ["day", "today"],

        # NEWS
        "INTENT_GLOBAL_NEWS": ["global news"],
        "INTENT_INDIA_NEWS": ["india news", "indian news"],

        # SYSTEM
        "INTENT_CPU": ["cpu usage"],
        "INTENT_RAM": ["ram usage"],
        "INTENT_DISK": ["disk usage"],
        "INTENT_BATTERY": ["battery"],

        # INTRO
        "INTENT_INTRO": ["who are you", "introduce yourself"],

        # EXIT
        "INTENT_EXIT": ["exit", "stop"]
    }

    for intent, patterns in intent_map.items():
        for pattern in patterns:
            if pattern in cmd:
                return intent

    return cmd  # return raw command if no intent matched