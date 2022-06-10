import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
# Method1) My answer
var = [rock, scissors, paper]

com_choice = random.randint(0, 2)
computer = var[com_choice]

my_choice = int(input("Rock = 0\nScissors = 1\nPaper = 2\nChoose one? "))

if my_choice < 0 or my_choice > 2:
    print("Please type numers between 0 and 2")
else:
    me = var[my_choice]
    print(f"Computer chose:{computer}\n\n\nYou chose:{me}")
    if com_choice == my_choice:
        print("Try Again")
    elif com_choice == 0 and my_choice == 1:
        print("You lose")
    elif com_choice == 0 and my_choice == 2:
        print("You win")
    elif com_choice == 1 and my_choice == 0:
        print("You win")
    elif com_choice == 1 and my_choice == 2:
        print("You lose")
    elif com_choice == 2 and my_choice == 0:
        print("You lose")
    elif com_choice == 2 and my_choice == 1:
        print("You win")

# Method2) Udemy answer
game_images = [rock, paper, scissors]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
