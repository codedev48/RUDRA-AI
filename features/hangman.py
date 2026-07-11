import random
from engine.speak import speak  # optional for voice feedback

def hangman_game():
    word_list = ["python", "rudra", "ai", "programming", "assistant", "voice", "computer"]
    word = random.choice(word_list).lower()
    guessed_letters = set()
    attempts = 6

    print("=== Welcome to Hangman ===")
    speak("Welcome to Hangman!")
    
    while attempts > 0:
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print("Word:", " ".join(display_word))
        speak(f"Current word: {' '.join(display_word)}")

        if "_" not in display_word:
            print("🎉 Congratulations! You guessed the word:", word)
            speak(f"Congratulations! You guessed the word {word}")
            return

        guess = input("Guess a letter: ").lower().strip()
        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Enter a single letter only.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print(f"✅ Good guess! {guess} is in the word.")
        else:
            attempts -= 1
            print(f"❌ Wrong guess! {guess} is not in the word. Attempts left: {attempts}")

    print("💀 Game Over! The word was:", word)
    speak(f"Game Over! The word was {word}")
    

if __name__ == "__main__":
    hangman_game()