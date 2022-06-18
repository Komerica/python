from calculator_art import logo
import os
def clear(): return os.system('cls')


# Method2) Udemy Answer (Using function + while loop)
print(""" 
███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░██████╗░
████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗╚════██╗
██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║░░███╔═╝
██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║██╔══╝░░
██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝███████╗
╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝ """)
print(logo)

# Add


def add2(n1, n2):
    return n1 + n2


# Subtract


def subtract2(n1, n2):
    return n1 - n2


# Multioply


def multiply2(n1, n2):
    return n1 * n2


# Devide


def devide2(n1, n2):
    return n1 / n2


operations2 = {
    "+": add2,
    "-": subtract2,
    "*": multiply2,
    "/": devide2
}

# function = operations2["+"]
# function(2, 3)


should_continue2 = True


def calculator():
    num1 = int(input("What's the first number?: "))
    for symbol in operations2:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = operations2[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1:.1f} {operation_symbol} {num2:.1f} = {answer:.1f}")

        if input(f"Type 'y' to continue calculating with {answer:.1f}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            clear()
            should_continue = False
            calculator()


calculator()
