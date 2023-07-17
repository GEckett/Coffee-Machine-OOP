from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Classes

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

#Loop
off = False
money = 0
while not off:
    options = menu.get_items()
    choice = input(f"What would you like? {options}").lower()
    if choice == "off":
        off = True
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)