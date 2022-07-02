import random
from blackjack_art import logo
import os
def clear(): return os.system('cls')


##############
## My answer #
##############
print(""" 
███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░░░███╗░░
████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗░████║░░
██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║██╔██║░░
██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║╚═╝██║░░
██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝███████╗
╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝ """)


def blackjack():
    should_continue = True
    start_game = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start_game == "y":
        clear()
        print(logo)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        my_cards = random.sample(cards, 2)
        computer_cards = random.sample(cards, 2)

        print(f"    Your cards: {my_cards}, current score: {sum(my_cards)}")
        print(
            f"    Computer's first card: {computer_cards[0]}")

        if sum(my_cards) == 21:
            print(
                f"    Your final hand: {my_cards}, final score: {sum(my_cards)}")
            print(
                f"    Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            print("Win with a Blackjack 😎")
            blackjack()
        elif sum(computer_cards) == 21:
            print(
                f"    Your final hand: {my_cards}, final score: {sum(my_cards)}")
            print(
                f"    Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            print("Lose, opponent has Blackjack 😱")
            blackjack()
        else:
            while should_continue:
                should_get_card = input(
                    "Type 'y' to get another card, type 'n' to pass: ")
                if sum(computer_cards) <= 16:
                    rd_comp_card = random.sample(cards, 1)
                    computer_cards.extend(rd_comp_card)
                if should_get_card == "y":
                    rd_my_card = random.sample(cards, 1)
                    my_cards.extend(rd_my_card)
                    print(
                        f"    Your cards: {my_cards}, current score: {sum(my_cards)}")
                    print(
                        f"    Computer's first card: {computer_cards[0]}")
                    if sum(my_cards) > 21:
                        should_continue = False
                        print(
                            f"    Your final hand: {my_cards}, final score: {sum(my_cards)}")
                        print(
                            f"    Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
                        print("You lose 😢")
                        blackjack()
                else:
                    should_continue = False
                    print(
                        f"    Your final hand: {my_cards}, final score: {sum(my_cards)}")
                    print(
                        f"    Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
                    if sum(computer_cards) > 21:
                        print("You win 😉")
                    else:
                        if sum(my_cards) > sum(computer_cards):
                            print("You win 😉")
                        elif sum(my_cards) < sum(computer_cards):
                            print("You lose 😢")
                        else:
                            print("You draw 😢")
                    blackjack()


blackjack()
