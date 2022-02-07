from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    coffee_menu = Menu()
    coffee_maker = CoffeeMaker()
    coffee_money_machine = MoneyMachine()

    machine_on = True
    print('Welcome to Rodmar\'s Coffee Machine! What would you like to drink?')
    while machine_on:
        choice = input(coffee_menu.get_items()).lower()
        if choice == 'off':
            machine_on = False
        elif choice == 'report':
            coffee_maker.report()
            coffee_money_machine.report()
        else:
            drink = coffee_menu.find_drink(choice)
            if drink != None:
                if coffee_maker.is_resource_sufficient(drink) and coffee_money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
            else:
                print('I think you mispelled something...')

main()