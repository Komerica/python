from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_item = MenuItem("hehe", 50, 51, 52, 10)
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    menu.get_items()
    order = input("What would you like? ")
    if order == "off":
        is_on = False
    elif order == "report":
        coffee_maker.report()
    elif order in menu.menu.MenuItem.name:
        coffee_maker.report()
