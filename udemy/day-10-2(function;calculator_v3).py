from calculator_art import logo
import os
def clear(): return os.system('cls')

# My code by myself


print(""" 
███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░██████╗░
████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗╚════██╗
██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║░█████╔╝
██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║░╚═══██╗
██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝██████╔╝
╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚═════╝░ """)
print(logo)


def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def devide(a, b):
    return a/b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": devide
}

additional_calculation = True


def calculator():
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    while additional_calculation:
        operation = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))

        function = operations[operation]
        result = function(num1, num2)
        print(f"{num1:.1f} {operation} {num2:.1f} = {result:.1f}")

        should_continue = input(
            f"Type 'y' to continue calculating with {result:.1f}, or type 'n' to start a new calculation: ")

        if should_continue == "y":
            num1 = result
        else:
            clear()
            calculator()


calculator()
