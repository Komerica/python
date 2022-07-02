from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
print(menu.get_items())
print(menu.find_drink("espresso"))
print(menu.find_drink("latte"))


money_machine = MoneyMachine()
print(money_machine.money_received) # 0
print(money_machine.profit) # 0
money_machine.report() # Money: $0
# money_machine.process_coins() # Please insert coins.
money_machine.make_payment(2) # Please insert coins.

coffee_maker = CoffeeMaker()
coffee_maker.report() # Water: 300ml....
latte = menu.find_drink("latte")
print(coffee_maker.is_resource_sufficient(latte))
coffee_maker.make_coffee(latte)

# menu_item = MenuItem("hehe", 156, 12 ,13 ,14)
# print(menu_item.ingredients)
# print(menu_item.cost)

# coffee_maker = CoffeeMaker()
# print(coffee_maker.make_coffee("latte"))



