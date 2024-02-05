# Based on ChatGPT-generated code

import random

# Function to select a random word from a text file containing 5-letter words
def choose_word():
    with open("5-letter-words.txt", "r") as file:
        words = file.readlines()
    return random.choice(words).strip()  # Remove leading/trailing whitespace

# Function to check the guessed word against the secret word
def check_word(secret_word, guess):
    return secret_word == guess

# Function to provide feedback on the guessed word with color coding
def provide_feedback(secret_word, guess):
    feedback = []
    for i in range(len(secret_word)):
        if secret_word[i] == guess[i]:
            feedback.append(f"\033[92m{guess[i]}\033[0m")  # Correct letter in the correct position (green)
        elif guess[i] in secret_word:
            feedback.append(f"\033[93m{guess[i]}\033[0m")  # Correct letter in the wrong position (yellow)
        else:
            feedback.append(f"\033[91m{guess[i]}\033[0m")  # Incorrect letter (red)
    return " ".join(feedback)

# Main game loop
def play_wordle():
    secret_word = choose_word()
    attempts = 6

    print("Welcome to Wordle! (https://www.nytimes.com/games/wordle)")
    print("Try to guess a 5-letter word. You have 6 attempts.")

    while attempts > 0:
        guess = input(f"Attempt {7 - attempts}: ").lower()
        guess = guess.replace(" ", "")

        if len(guess) != len(secret_word):
            print(f"Invalid guess [{guess}] with a length of {len(guess)}. Please enter a 5-letter word.")
            continue

        if check_word(secret_word, guess):
            print(f"Congratulations! You've guessed the word: {secret_word.capitalize()}")
            break
        else:
            feedback = provide_feedback(secret_word, guess)
            print("Feedback :", feedback)
            attempts -= 1

    if attempts == 0:
        print(f"Out of attempts! The word was: {secret_word.capitalize()}")

if __name__ == "__main__":
    play_wordle()