# Step 1
import random
from hangman_art import stages, logo
from hangman_words import word_list
import os
def clear(): return os.system('cls')


print(f"{logo}")

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
# print(chosen_word)

lives = 6
guessed_letter = []
blank = []
for _ in chosen_word:  # 변수로 뭐 안하니까 _ 로 대체 해줘도 문제없음!
    # blank.append("_")
    blank += "_"


# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter in the word! ").lower()
    clear()
    guessed_letter.append(guess)
    print(f"Your guessed letters are {guessed_letter}")
    if guess in blank:
        print(f"You've already guessed '{guess}'! Try other letter!")

    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            blank[position] = letter
    print(f"{' '.join(blank)}")

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word.")
        print(f"You have {lives} lives left.")

        if lives == 0:
            end_of_game = True
            print("Game Over")
            print(f"The answer is {chosen_word}!")

    if "_" not in blank:
        end_of_game = True
        print("You win!")

    print(f"{stages[lives]}")
