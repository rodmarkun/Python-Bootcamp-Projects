from tabnanny import check


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

def main():
    money = 0.0
    cafe_menu = ['espresso', 'latte', 'cappuccino']
    print('Welcome to Rodmar\'s Coffee Machine! What would you like to drink?')
    while True:
        choice = input('Espresso: 1.5$ / Latte: 2.5$ / Cappuccino: 3.0$ :').lower()
        if choice in cafe_menu:
            if check_resources(choice):
                money += make_coffee(choice)
        elif choice == 'report':
            report(money)
        else:
            print('I think you mispelled something...')

def make_coffee(coffee_choice):
    price = MENU[coffee_choice]['cost']
    money_entered = insert_coins()
    if price == money_entered:
        deplete_resources(coffee_choice)
        print(f'Here is your {coffee_choice} ☕. Enjoy!')
        return price
    elif price < money_entered:
        deplete_resources(coffee_choice)
        print(f'Here is ${round(money_entered - price, 3)} in change.')
        print(f'Here is your {coffee_choice} ☕. Enjoy!')
        return price
    else:
        print('Sorry that\'s not enough money. Money refunded.')
        return 0

def deplete_resources(coffee_choice):
    for ingredient in MENU[coffee_choice]['ingredients']:
            resources[ingredient] -= MENU[coffee_choice]['ingredients'][ingredient]

def check_resources(coffee_choice):
    for ingredient in MENU[coffee_choice]['ingredients']:
        if resources[ingredient] < MENU[coffee_choice]['ingredients'][ingredient]:
            print(f'Sorry, there is not enough {ingredient} currently.')
            return False
    return True

def insert_coins():
    print('Please insert coins.')
    quarters =  int(input('How many quarters? '))
    dimes =     int(input('How many dimes? '))
    nickles =   int(input('How many nickles? '))
    pennies =   int(input('How many pennies? '))

    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

def report(money):
    for r_key in resources:
        print(f'{r_key.capitalize()}: {resources[r_key]}ml')
    print(f'Money: {money}$')

main()