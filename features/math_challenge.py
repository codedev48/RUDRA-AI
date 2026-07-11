import random
import time
from engine.speak import speak  # optional for voice feedback

def math_challenge():
    score = 0
    total_questions = 5

    print("=== Welcome to Math Challenge ===")
    speak("Welcome to Math Challenge!")

    for i in range(total_questions):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        operator = random.choice(["+", "-", "*"])
        if operator == "+":
            correct = a + b
        elif operator == "-":
            correct = a - b
        else:
            correct = a * b

        print(f"Question {i+1}: {a} {operator} {b} = ?")
        speak(f"Question {i+1}: {a} {operator} {b} equals what?")
        start_time = time.time()

        try:
            answer = int(input("Your answer: "))
        except ValueError:
            print("⚠️ Invalid input! Counting as wrong.")
            answer = None

        end_time = time.time()
        if answer == correct:
            print("✅ Correct!")
            speak("Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {correct}.")
            speak(f"Wrong! The correct answer was {correct}")

        print(f"Time taken: {round(end_time - start_time, 2)} seconds\n")

    print(f"🏆 Challenge Over! Your score: {score}/{total_questions}")
    speak(f"Challenge Over! Your score is {score} out of {total_questions}")


if __name__ == "__main__":
    math_challenge()