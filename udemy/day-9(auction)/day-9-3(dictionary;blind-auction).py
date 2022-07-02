from auction_art import logo
import os
def clear(): return os.system('cls')


print(logo)
print("Welcome to the secret auction program!")

bidders = {}
end_of_game = False


def find_highest_bidder(bidding_record):
    winner_bid_amount = 0
    winner_name = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > winner_bid_amount:
            winner_name = bidder
            winner_bid_amount = bidding_record[bidder]
    print(f"The winner is {winner_name} with a bid of ${winner_bid_amount}")


while not end_of_game:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders == "no":
        end_of_game = True
        find_highest_bidder(bidders)
    elif other_bidders == "yes":
        clear()
