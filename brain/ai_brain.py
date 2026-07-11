from features.search import wikipedia_search
from engine.speak import speak
import random

conversation_context = []
full_summary = ""
sentence_pointer = 0
last_trigger_type = None


def process_ai_query(command):

    global conversation_context
    global full_summary
    global sentence_pointer
    global last_trigger_type

    if not command:
        return False

    command = command.lower().strip()

    # ================= FOLLOW-UP =================

    if command in ["tell me more", "more"]:

        if not full_summary:
            speak("There is no previous topic to continue.")
            return True

        sentences = full_summary.split(". ")

        if sentence_pointer >= len(sentences):
            speak("That is all the information I have.")
            return True

        next_part = ". ".join(sentences[sentence_pointer:sentence_pointer+2])
        sentence_pointer += 2

        speak(next_part)
        return True

    # ================= TRIGGERS =================

    trigger_words = [
        "what is",
        "who is",
        "define",
        "explain",
        "information about"
    ]

    detected_trigger = None

    for trigger in trigger_words:
        if command.startswith(trigger):
            detected_trigger = trigger
            break

    # Continue previous trigger
    if not detected_trigger and last_trigger_type:
        detected_trigger = last_trigger_type
        command = f"{detected_trigger} {command}"

    if detected_trigger:

        last_trigger_type = detected_trigger

        topic = command.replace(detected_trigger, "").strip()

        if not topic:
            speak("Please tell me what you want to know.")
            return True

        conversation_context.append(topic)

        if len(conversation_context) > 5:
            conversation_context.pop(0)

        intros = [
            f"Here is what I found about {topic}.",
            f"Let me explain {topic}.",
            f"This is the information about {topic}.",
            f"Alright Vedant, here is something about {topic}."
        ]

        speak(random.choice(intros))

        try:

            summary = wikipedia_search(topic)

            if summary:

                sentences = summary.split(". ")

                # Limit summary size
                sentences = sentences[:8]

                full_summary = ". ".join(sentences)

                sentence_pointer = 2

                first_part = ". ".join(sentences[:2])

                speak(first_part)

            else:
                speak("Sorry, I couldn't find enough information.")

        except Exception:
            speak("Sorry, I couldn't fetch information right now.")

        return True

    return False