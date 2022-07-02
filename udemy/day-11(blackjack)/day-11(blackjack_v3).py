########################################
## re-coded (referring to Udemy code) #
########################################

import random
from blackjack_art import logo
import os
def clear(): return os.system('cls')


print(""" 
███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░██████╗░
████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗╚════██╗
██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║░█████╔╝
██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║░╚═══██╗
██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝██████╔╝
╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚═════╝░ """)

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


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
    if comp_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score == comp_score:
        return "Draw! 😉"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Opponent went over. You win 😁 "
    elif user_score > comp_score:
        return "You win! 😀"
    elif user_score < comp_score:
        return "You lose! 😥"


def game_start():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        clear()
        game_switch = True
        user_cards = []
        comp_cards = []

        print(logo)

        for _ in range(2):
            user_cards.append(draw_card())
            comp_cards.append(draw_card())

        while game_switch:
            user_score = cal_sum(user_cards)
            comp_score = cal_sum(comp_cards)
            print(
                f"    Your cards: {user_cards}, current score: {user_score}")
            print(f"    Computer's first card: {comp_cards[0]}")
            if user_score == 0 or comp_score == 0 or user_score > 21:
                game_switch = False
                print(compare(user_score, comp_score))
            else:
                if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                    user_cards.append(draw_card())
                else:
                    game_switch = False
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(draw_card())
        comp_score = cal_sum(comp_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"    Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))


game_start()
