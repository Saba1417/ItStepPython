import random

def main():
    words = ["apple", "banana", "cherry", "pineapple"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    wrong = 0
    guessed_letters = set()

    while wrong < attempts and "".join(guessed) != word:
        print("\nWord:", " ".join(guessed))
        print(f"Attempts left: {attempts - wrong}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "None")
        guess = input("Guess a letter: ").strip().lower()

        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, ch in enumerate(word):
                if ch == guess:
                    guessed[i] = guess
        else:
            wrong += 1

    if "".join(guessed) == word:
        print(f"\nCongratulations! You guessed the word: {word} with {wrong} wrong guesses.")
    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    main()