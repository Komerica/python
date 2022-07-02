from operator import is_
import random
from blackjack_art import logo
import os
def clear(): return os.system('cls')

##################################
## Coded myself without any help #
##################################


print("""
██╗░░░██╗███████╗██████╗░░██████╗██╗░█████╗░███╗░░██╗░░░░░██╗██╗
██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗░██║░░░░██╔╝██║
╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║██╔██╗██║░░░██╔╝░██║
░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██║╚████║░░░███████║
░░╚██╔╝░░███████╗██║░░██║██████╔╝██║╚█████╔╝██║░╚███║██╗╚════██║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░░░░╚═╝""")

def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def cal_sum(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, comp_score):
    if comp_score == user_score:
        return "Draw!"
    elif comp_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win, with a Blackjack 😎"
    elif user_score > 21:
        return "Lose, you went over 😥"
    elif comp_score > 21:
        return "Win, opponent went over 😁"
    elif comp_score < user_score:
        return "You win 😀"
    elif comp_score > user_score:
        return "You lose 😥"


def start_game():
    user_card = []
    comp_card = []
    print(logo)
    is_game_over = False

    for _ in range(2):
        user_card.append(draw_card())
        comp_card.append(draw_card())

    while not is_game_over:
        print(
            f"    Your cards: {user_card}, current score: {cal_sum(user_card)}")
        print(f"    Computer's first card: {comp_card[0]}")
        if cal_sum(user_card) == 0 or cal_sum(comp_card) == 0 or cal_sum(user_card) > 21:
            is_game_over = True
        else:
            if input("Wanna draw another card? Type 'y' to get another card, 'n' to stop: ") == "y":
                user_card.append(draw_card())
            else:
                is_game_over = True

    while cal_sum(comp_card) != 0 and cal_sum(comp_card) < 17:
        comp_card.append(draw_card())

    print(
        f"    Your final hand: {user_card}, final score: {cal_sum(user_card)}")
    print(
        f"    Computer's final hand: {comp_card}, final score: {cal_sum(comp_card)}")
    print(compare(cal_sum(user_card), cal_sum(comp_card)))


while input("Wanna play a game of Blackjack? Type 'y' to play, 'n' to end: ") == "y":
    clear()
    start_game()
