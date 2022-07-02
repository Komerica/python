from calculator_art import logo
import os
def clear(): return os.system('cls')


# Method1) My answer (Using 2 while loops)
print(""" 
███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░░░███╗░░
████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗░████║░░
██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║██╔██║░░
██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║╚═╝██║░░
██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝███████╗
╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝ """)

print(logo)

# Add


def add(n1, n2):
    return n1 + n2


# Subtract


def subtract(n1, n2):
    return n1 - n2


# Multioply


def multiply(n1, n2):
    return n1 * n2


# Devide


def devide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": devide
}

# function = operations["+"]
# function(2, 3)

new_calculation = True
should_continue = True

while new_calculation:
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]

        result = calculation_function(num1, num2)
        print(f"{num1:.1f} {operation_symbol} {num2:.1f} = {result:.1f}")

        if input(f"Type 'y' to continue calculating with {result:.1f}, or type 'n' to start a new calculation: ") == "y":
            num1 = result
            should_continue = True
            new_calculation = False
        else:
            clear()
            should_continue = False
            new_calculation = True
