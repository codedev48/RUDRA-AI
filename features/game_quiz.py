import random
import time
from engine.speak import speak


# ---------------- SAFE OPTION GENERATOR ---------------- #

def generate_math_question():
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    answer = a + b

    options = {answer}

    while len(options) < 4:
        options.add(answer + random.randint(-20, 20))

    options = list(options)

    return f"What is {a} plus {b}?", answer, options


def generate_capital_question():
    capitals = {
        "India": "New Delhi",
        "Japan": "Tokyo",
        "France": "Paris",
        "Germany": "Berlin",
        "Australia": "Canberra",
        "Canada": "Ottawa",
        "Brazil": "Brasilia"
    }

    country = random.choice(list(capitals.keys()))
    correct = capitals[country]

    wrong = random.sample(
        [v for v in capitals.values() if v != correct], 3
    )

    options = [correct] + wrong
    return f"What is the capital of {country}?", correct, options


def generate_science_question():
    bank = [
        ("Which planet is known as the Red Planet?", "Mars",
         ["Earth", "Jupiter", "Venus"]),
        ("Which gas do plants absorb?", "Carbon Dioxide",
         ["Oxygen", "Nitrogen", "Hydrogen"]),
        ("How many bones are there in adult human body?", "206",
         ["201", "210", "250"]),
        ("What is the boiling point of water in Celsius?", "100",
         ["90", "80", "120"])
    ]

    q = random.choice(bank)
    question, correct, wrong = q
    options = [correct] + wrong
    return question, correct, options


def get_question_pool():
    return [
        generate_math_question(),
        generate_capital_question(),
        generate_science_question()
    ]


# ---------------- VOICE PARSER ---------------- #

def parse_answer(text):
    text = text.lower()

    if "one" in text or "1" in text:
        return 1
    if "two" in text or "2" in text:
        return 2
    if "three" in text or "3" in text:
        return 3
    if "four" in text or "4" in text:
        return 4

    return None


# ---------------- MAIN QUIZ ---------------- #

def play_quiz(listen_function):

    speak("Welcome to the Dynamic Quiz Challenge.")
    speak("I will ask you three random questions.")
    speak("Say option one, two, three or four.")

    score = 0
    asked_questions = []

    for i in range(1, 4):

        # Avoid same question repeat
        while True:
            question, correct_answer, options = random.choice(get_question_pool())
            if question not in asked_questions:
                asked_questions.append(question)
                break

        random.shuffle(options)
        correct_index = options.index(correct_answer) + 1

        speak(f"Question {i}")
        speak(question)

        for idx, option in enumerate(options, 1):
            speak(f"Option {idx}. {option}")

        speak("Your answer please.")

        user_answer = listen_function()

        if not user_answer:
            speak("No answer detected.")
            continue

        selected = parse_answer(user_answer)

        speak("Checking your answer.")
        time.sleep(4)

        if selected == correct_index:
            speak("Correct answer!")
            score += 1
        else:
            speak("Wrong answer.")
            speak(f"The correct answer was option {correct_index}. {correct_answer}")

    speak(f"Quiz completed. Your final score is {score} out of 3.")

    if score == 3:
        speak("Outstanding performance.")
    elif score == 2:
        speak("Very good job.")
    else:
        speak("Keep practicing and try again.")