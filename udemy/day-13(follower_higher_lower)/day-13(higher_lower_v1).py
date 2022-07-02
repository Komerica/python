from random import choice
from game_data import data
from higher_lower_art import logo, vs
import os
def clear(): return os.system("cls")

######################################
#### Coded myself without any help ###
## After reading a bit of Udemy code #
######################################


print(""" 
██╗░░░██╗███████╗██████╗░░██████╗██╗░█████╗░███╗░░██╗░░░░░███╗░░
██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗░██║░░░░████║░░
╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║██╔██╗██║░░░██╔██║░░
░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██║╚████║░░░╚═╝██║░░
░░╚██╔╝░░███████╗██║░░██║██████╔╝██║╚█████╔╝██║░╚███║██╗███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝╚══════╝ """)


def get_random_account():
    return choice(data)


def compare(guess, compare_a, compare_b):
    follower_num_a = compare_a['follower_count']
    follower_num_b = compare_b['follower_count']
    if follower_num_a > follower_num_b:
        return guess == "a"
    else:
        return guess == "b"


def game():
    score = 0
    is_game_over = False
    is_correct = True
    while not is_game_over:
        compare_a = get_random_account()
        compare_b = get_random_account()

        while is_correct:
            clear()
            print(f"A: {compare_a['follower_count']}")  # A's follower_count
            print(f"B: {compare_b['follower_count']}")  # B's follower_count
            print(logo)
            if score > 0:
                print(f"You're right! Current score: {score}.")
            print(
                f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
            print(vs)
            print(
                f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")

            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            if compare(guess, compare_a, compare_b):
                score += 1
                compare_a = compare_b
                compare_b = get_random_account()
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                is_game_over = True
                is_correct = False


game()
