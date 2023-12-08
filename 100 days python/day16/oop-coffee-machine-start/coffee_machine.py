#making a coffee machine in python
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
print("""
             __  __                             _   _             
   ___ ___  / _|/ _| ___  ___    __ _ _ __   __| | | |_ ___  __ _ 
  / __/ _ \| |_| |_ / _ \/ _ \  / _` | '_ \ / _` | | __/ _ \/ _` |
 | (_| (_) |  _|  _|  __/  __/ | (_| | | | | (_| | | ||  __/ (_| |
  \___\___/|_| |_|  \___|\___|  \__,_|_| |_|\__,_|  \__\___|\__,_|
""")

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
# menu_items = MenuItem()
is_on = True

money_machine.report()
coffee_maker.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)




