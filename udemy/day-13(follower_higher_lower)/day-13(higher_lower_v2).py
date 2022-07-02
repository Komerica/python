from game_data import data
from higher_lower_art import logo, vs
import random
import os
def clear(): return os.system('cls')

######################################
#### Coded myself without any help ###
######################################


print(""" 
██╗░░░██╗███████╗██████╗░░██████╗██╗░█████╗░███╗░░██╗░░░██████╗░
██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗░██║░░░╚════██╗
╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║██╔██╗██║░░░░░███╔═╝
░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██║╚████║░░░██╔══╝░░
░░╚██╔╝░░███████╗██║░░██║██████╔╝██║╚█████╔╝██║░╚███║██╗███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝╚══════╝ """)


def get_rd_account():
    return random.choice(data)


def get_account_info(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}."


def compare(guess, followers_a, followers_b):
    if guess == "A":
        if followers_a > followers_b:
            return True
        else:
            return False
    else:
        if followers_a < followers_b:
            return True
        else:
            return False


def game():
    score = 0
    account_a = get_rd_account()
    account_b = get_rd_account()

    while account_a == account_b:
        account_b = get_rd_account()

    is_game_over = False
    while not is_game_over:
        follower_count_a = account_a["follower_count"]
        follower_count_b = account_b["follower_count"]
        print(follower_count_a)
        print(follower_count_b)

        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}")

        print(f"Compare A: {get_account_info(account_a)}")
        print(vs)
        print(f"Against B: {get_account_info(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ")
        clear()
        is_correct = compare(guess, follower_count_a, follower_count_b)

        if is_correct:
            score += 1
            account_a = account_b
            account_b = get_rd_account()
        else:
            is_game_over = True
            print(f"Sorry, that's wrong. Final score: {score}")


game()
