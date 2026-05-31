from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

POWER = True

coffee_menu = Menu()
maker = CoffeeMaker()
machine = MoneyMachine()

while POWER:
    select = input(f"What would you like? ({coffee_menu.get_items()}): ").lower()
    
    if select == "off":
        POWER = False
    elif select == "report":
        maker.report()
        machine.report()
    else:
        current_menu = coffee_menu.find_drink(select)
        if maker.is_resource_sufficient(current_menu) and machine.make_payment(current_menu.cost):
            maker.make_coffee(current_menu)