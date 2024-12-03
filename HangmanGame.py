#small project to play Hangman
import random
from HangmanWords import words

#dictionary of key:()
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

#check if these are being displayed correctly
# for line in hangman_art[6]:
#     print(line)

def display_man(wrong_guesses):
    print("*******************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*******************")

def display_hint(hint):
    print(" ".join(hint))

def update_hint(answer, hint, guess):
    for index, char in enumerate(answer):
        if char == guess:
            hint[index] = guess

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_" if char.isalpha() else " " for char in answer]
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        # display_answer(answer)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not (guess.isalpha() or guess.isspace()):
            print("Invalid input, you can only guess 1 letter at a time")
            continue

        if guess in guessed_letters:
            print(f"You have already guessed {guess}")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            update_hint(answer, hint, guess)
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE, WOMP WOMP!")
            is_running = False


if __name__ == "__main__":
    main()