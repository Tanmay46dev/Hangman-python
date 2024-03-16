from random import choice

words: list[str] = ["Java", "Python", "JavaScript", "Swift", "Ruby", "Haskell", "Dart", "Golang", "Mojo"]

WORD: str = choice(words).lower()
display_word: list = ["_" for _ in WORD]
attempts_left: int = 6


def print_display_word() -> None:
    [print(letter, end=" ") for letter in display_word]


def get_guess_unique_index(guess: str) -> int:
    if guess not in display_word:
        return WORD.index(guess)

    for i in range(len(WORD)):
        if WORD[i] == guess:
            if WORD[i] == display_word[i]:
                continue
            return i


def main():
    global attempts_left
    print("Welcome to the game of hangman!.")
    print("A word is hinted on the screen using underscores as its letters.")
    print("Try to guess the letters and uncover it.")
    while attempts_left > 0:
        print_display_word()
        print()
        display_word_string = "".join(display_word)
        if display_word_string == WORD:
            print(f"Congrats. You won the game with {attempts_left} attempts left.")
            break
        guess = input("Enter your guess: ")[0].lower()
        try:
            guess_index = get_guess_unique_index(guess)
            display_word[guess_index] = guess

        except ValueError:
            print("Oops! Wrong guess.")
            attempts_left -= 1
            print(f"You have {attempts_left} attempts left now.")
    else:
        print("Sorry! Better luck next time. You have lost the game.")
        print(f"The word was: {WORD}")


if __name__ == "__main__":
    main()
