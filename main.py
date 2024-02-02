from ingredients import resources, MENU


def print_report():
    for key in resources:
        print(f"{key}: {resources[key]}")


def check_resource(drink):
    user_choice = MENU[drink]
    for ingredient in user_choice['ingredients']:
        if user_choice['ingredients'][ingredient] > resources[ingredient]:
            return ingredient

    return ''


def check_balance(drink):
    print('Please insert coins.')
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01

    user_choice = MENU[drink]

    if total >= user_choice['cost']:
        resources['money'] += user_choice["cost"]
        print(
            f'Here is your change ${round(total - user_choice["cost"], 2)}')
        return True
    else:
        return False


def serve_drink(drink):
    user_choice = MENU[drink]
    for ingredient in user_choice['ingredients']:
        if resources[ingredient] >= user_choice['ingredients'][ingredient]:
            resources[ingredient] -= user_choice['ingredients'][ingredient]
    print(f'Here is your {drink}')


def start_program():
    resources['money'] = 0
    running = True
    drinks = ['espresso', 'latte', 'cappuccino']

    while running:
        user_request = input("What would you like? ")

        if user_request == 'report':
            print_report()

        if user_request == 'off':
            running = False
            print('Shutting Off...')

        if user_request in drinks:
            enough_resources = check_resource(user_request)
            if enough_resources != '':
                print(f"Sorry there is not enough {enough_resources}")
            else:
                enough_money = check_balance(user_request)
                if not enough_money:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    serve_drink(user_request)


start_program()
