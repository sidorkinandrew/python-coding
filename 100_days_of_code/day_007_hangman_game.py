import random
from day_007_hangman_art import stages, logo
from day_007_hangman_words import word_list
from os import system

game_is_finished = False
lives = len(stages) - 1
fill_char = "_"
alphabet = 'abcdefghijklmnopqrstuvwxyz'

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = [fill_char for _ in range(word_length)]

already_guessed = []
current_status = ""

while not game_is_finished:
    system('cls||clear')
    print(logo)
    print(stages[lives])
    print(f"Guess_word:\n{' '.join(display)}\n")
    print(f"Already guessed: {' '.join(already_guessed )}")
    print(f"{current_status}\n")

    if not "_" in display:
        game_is_finished = True
        print("You win!")
    elif lives <= 0:
        game_is_finished = True
        print("No more lives left! You lose.")
    else:
        guess = input("Guess a letter: ").lower()

    if guess not in alphabet:
        current_status = f"{guess} is not a letter, please re-try."
    elif guess in display or guess in already_guessed or guess == fill_char:
        current_status = f"You've already guessed {guess}"
    else:
        already_guessed.append(guess)

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        if guess in chosen_word:
            current_status = ""
        
        if guess not in chosen_word:
            current_status = f"You guessed {guess}, that's not in the word. You lose a life."
            lives -= 1
