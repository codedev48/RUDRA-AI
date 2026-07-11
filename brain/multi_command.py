# brain/multi_command.py

import re


def split_commands(command):
    """
    Splits multi-command input into separate commands.

    Supported separators:
    - and
    - then
    - ,

    Example:
    "open chrome then play music and search google"
    ->
    ["open chrome", "play music", "search google"]
    """

    if not command:
        return []

    command = command.strip()

    # Regex for separators (case insensitive)
    pattern = r"\s+(?:and|then)\s+|,"

    parts = re.split(pattern, command, flags=re.IGNORECASE)

    # Clean results
    final_commands = []

    for part in parts:
        cleaned = part.strip()
        if cleaned:
            final_commands.append(cleaned)

    return final_commands


# For testing only
if __name__ == "__main__":
    test_command = "Open notepad then search Google and play music, check email"
    commands = split_commands(test_command)
    print(commands)