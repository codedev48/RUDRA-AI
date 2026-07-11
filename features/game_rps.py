import random
import time
from engine.speak import speak

choices = ["rock", "paper", "scissors"]


# ---------------- PARSE USER INPUT ---------------- #

def parse_choice(text):
    if not text:
        return None

    text = text.lower()

    for choice in choices:
        if choice in text:
            return choice

    return None


# ---------------- BALANCED AI ---------------- #

def get_balanced_ai_choice(user_choice):
    """
    40% user wins
    40% random
    20% rudra wins
    """

    win_bias = random.random()

    # User wins (AI intentionally loses)
    if win_bias < 0.4:
        if user_choice == "rock":
            return "scissors"
        elif user_choice == "paper":
            return "rock"
        else:
            return "paper"

    # Fully random
    elif win_bias < 0.8:
        return random.choice(choices)

    # Rudra wins
    else:
        if user_choice == "rock":
            return "paper"
        elif user_choice == "paper":
            return "scissors"
        else:
            return "rock"


# ---------------- SINGLE ROUND ---------------- #

def play_single_round(listen_function):

    while True:
        speak("Say rock, paper, or scissors.")
        user_input = listen_function()

        user_choice = parse_choice(user_input)

        if not user_choice:
            speak("That is not a valid choice. Please try again.")
            continue

        break

    # Countdown drama
    speak("Rock...")
    time.sleep(0.5)
    speak("Paper...")
    time.sleep(0.5)
    speak("Scissors...")
    time.sleep(0.5)
    speak("Shoot!")
    time.sleep(1)

    rudra_choice = get_balanced_ai_choice(user_choice)

    speak(f"I chose {rudra_choice}.")
    time.sleep(1.2)

    if user_choice == rudra_choice:
        speak("It's a draw!")
        return "draw"

    elif (
        (user_choice == "rock" and rudra_choice == "scissors") or
        (user_choice == "paper" and rudra_choice == "rock") or
        (user_choice == "scissors" and rudra_choice == "paper")
    ):
        speak("You win this round!")
        return "user"

    else:
        speak("I win this round!")
        return "rudra"


# ---------------- MAIN GAME ---------------- #

def play_rps(listen_function):

    speak("Welcome to Rock Paper Scissors.")
    time.sleep(1)

    speak("Do you want to play single round or best of three?")

    mode_input = listen_function()

    if not mode_input:
        speak("No mode selected. Starting single round.")
        play_single_round(listen_function)
        return

    mode_input = mode_input.lower()

    # ---------------- BEST OF THREE ---------------- #

    if "best" in mode_input or "three" in mode_input:

        speak("Starting Best of Three mode.")

        user_score = 0
        rudra_score = 0
        round_number = 1

        while user_score < 2 and rudra_score < 2:

            speak(f"Round {round_number}")

            result = play_single_round(listen_function)

            if result == "user":
                user_score += 1
            elif result == "rudra":
                rudra_score += 1

            speak(f"Current score. You {user_score}. Rudra {rudra_score}.")
            round_number += 1
            time.sleep(1)

        # Final result
        if user_score > rudra_score:
            speak("Congratulations! You won the Best of Three match!")
        else:
            speak("I won the Best of Three match!")

    # ---------------- SINGLE MODE ---------------- #

    else:
        speak("Starting Single Round mode.")
        play_single_round(listen_function)

    speak("Game finished.")