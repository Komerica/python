from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#################################
# OOP version of Coffee machine #
# Udemy Code ####################
#################################

print("""
██╗░░░██╗███████╗██████╗░░██████╗██╗░█████╗░███╗░░██╗░░░██████╗░
██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗░██║░░░╚════██╗
╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║██╔██╗██║░░░░█████╔╝
░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██║╚████║░░░░╚═══██╗
░░╚██╔╝░░███████╗██║░░██║██████╔╝██║╚█████╔╝██║░╚███║██╗██████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝╚═════╝░""")

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)
        # is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        # is_payment_successful = money_machine.make_payment(drink.cost) # 이게 실행되면서 망함!!
        # if is_enough_ingredients and is_payment_successful:
        #     coffee_maker.make_coffee(drink)
        # 👆 재료가 부족해도 돈달라고 한다!
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)