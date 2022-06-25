from random import randint
from guessing_number_art import logo

##################################
## Coded myself without any help #
#### After reading Udemy code ####
##################################

EASY_TURNS = 10
HARD_TURNS = 5


def check_answer(answer, guess):
    if answer > guess:
        return "Too low 😥"
    elif answer < guess:
        return "Too high 😫"
    else:
        return f"You got it! The answer was {answer}"


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_TURNS
    elif difficulty == "hard":
        return HARD_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    is_game_over = False
    while not is_game_over:
        print(f"You have {turns} attempts remaining to guess the number.")
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return

        guess = int(input("Make a guess: "))
        if answer == guess:
            is_game_over = True
        elif answer != guess:
            turns -= 1

        print(check_answer(answer, guess))


game()
