######################################
#### Coded myself without any help ###
#### A few errors need to be fixed ###
######################################
# Error 👇
# when ordered 2 latte, still asking for payment even though out of resources

print("""
██╗░░░██╗███████╗██████╗░░██████╗██╗░█████╗░███╗░░██╗░░░░░███╗░░
██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗░██║░░░░████║░░
╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║██╔██╗██║░░░██╔██║░░
░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██║╚████║░░░╚═╝██║░░
░░╚██╔╝░░███████╗██║░░██║██████╔╝██║╚█████╔╝██║░╚███║██╗███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝╚══════╝""")

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_ingredients(coffee):
    if resources["water"] < MENU[coffee]["ingredients"]["water"]:
        print("Not enough water")
    if "milk" in MENU[coffee]["ingredients"]:
        if resources["milk"] < MENU[coffee]["ingredients"]["milk"]:
            print("Not enough milk")
    if resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
        print("Not enough coffee")


def insert_coins():
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


money = 0


def get_money(money, coffee):
    money += MENU[coffee]["cost"]
    return money


def deduct_ingredients(coffee):
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    if "milk" in MENU[coffee]["ingredients"]:
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]


def give_change(coffee):
    total = insert_coins()
    if not total < MENU[coffee]["cost"]:
        change = total - MENU[coffee]["cost"]
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {coffee} ☕. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")


is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "espresso" or order == "latte" or order == "cappuccino":
        check_ingredients(order)
        give_change(order)
        money = get_money(money, order)
        deduct_ingredients(order)
    elif order == "report":
        report()
    elif order == "off":
        is_on = False
