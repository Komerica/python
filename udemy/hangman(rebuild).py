import random
from hangman_words import word_list
from hangman_art import stages, logo
import os
def clear(): return os.system('cls')


# Start game
print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

blank = []
for _ in chosen_word:
    blank.append("_")

lives = 6
end_of_game = False

guessed_letters = []
while not end_of_game:
    guess = input("Guess a letter in the word! ")
    clear()
    guessed_letters.append(guess)
    print("👇You have already tried these letters👇")
    print(f"{guessed_letters}")
    if guess in blank:
        print(f"You've already guessed {guess}! Try other letter!")

    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        if letter == guess:
            blank[index] = guess
    print(' '.join(blank))

    if "_" not in blank:
        print("You win!")
        end_of_game = True

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word!")
        print(f"You have {lives} lives left!")

        if lives == 0:
            end_of_game = True
            print("Game Over")
            print(f"The answer is {chosen_word}!")
    print(stages[lives])
