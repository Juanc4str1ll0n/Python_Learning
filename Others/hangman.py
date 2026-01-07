import random


palabras = ("apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "nectarine")

hangman_art = {
    0: ("",
        "",
        ""),
    1: ("",
        "  O",
        ""),
    2: ("",
        "  O",
        "  |"),
    3: ("",
        "  O",
        " /|"),
    4: ("", 
        "  O",
        " /|\\"),
    5: ("",
        "  O",
        " /|\\",
        " /"),
    6: ("", 
        "  O",
        " /|\\",
        " / \\"),
}

def display_man(wrong_guesses):
    print("----------------")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("----------------")

def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(palabras)
    hint = ["_"] * len(answer)
    print(answer,  hint)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1
            print(f"{guess} is not in the word")

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You win!")
            is_running = False 

        elif wrong_guesses == 6:
            display_man(wrong_guesses)
            print("Answer : ")
            display_answer(answer)
            print("You lose :(")
            is_running = False

if __name__ == "__main__":
    main()
 