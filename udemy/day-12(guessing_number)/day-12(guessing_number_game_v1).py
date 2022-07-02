import random

##################################
## Coded myself without any help #
##################################

print(""" 
██╗░░░██╗███████╗██████╗░░██████╗██╗░█████╗░███╗░░██╗░░░░░███╗░░
██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗░██║░░░░████║░░
╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║██╔██╗██║░░░██╔██║░░
░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██║╚████║░░░╚═╝██║░░
░░╚██╔╝░░███████╗██║░░██║██████╔╝██║╚█████╔╝██║░╚███║██╗███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝╚══════╝ """)
print("Welcome to the Number Guessing Game!")

print("""
_  _ _  _ _  _ ___  ____ ____    ____ _  _ ____ ____ ____ _ _  _ ____    ____ ____ _  _ ____ 
|\ | |  | |\/| |__] |___ |__/    | __ |  | |___ [__  [__  | |\ | | __    | __ |__| |\/| |___ 
| \| |__| |  | |__] |___ |  \    |__] |__| |___ ___] ___] | | \| |__]    |__] |  | |  | |___ 
                                                                                             
""")


def compare(rd_num, make_guess):
    if rd_num == make_guess:
        return f"You got it! The answer was {rd_num}."
    elif rd_num > make_guess:
        return "Too low."
    elif rd_num < make_guess:
        return "Too high."


is_game_over = False

while not is_game_over:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    answer = random.randint(1, 100)

    if difficulty == "easy":
        life = 10
    if difficulty == "hard":
        life = 5
    make_guess = True
    while make_guess:
        print(f"You have {life} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        print(compare(answer, guess))
        if answer == guess:
            is_game_over = True
            make_guess = False
        life -= 1
        if life == 0:
            print("You've run out of guesses, you lose.")
            print(f"Your answer was {answer}")
            is_game_over = True
            make_guess = False
