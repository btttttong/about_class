from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# menuItem = MenuItem()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
is_machine_on = True

while is_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ") or 'latte'
    if choice == 'off':
        exit()
    elif choice == 'report':
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        print(f"It's cost: ${drink.cost}")
        if drink:
            if coffeeMaker.is_resource_sufficient(drink):
                if moneyMachine.make_payment(drink.cost):
                    coffeeMaker.make_coffee(drink)